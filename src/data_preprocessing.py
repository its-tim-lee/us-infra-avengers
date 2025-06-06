import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(normal_path, attack_path):
    normal = pd.read_csv(normal_path)
    attack = pd.read_csv(attack_path, sep=';')
    return normal, attack

def clean_data(df):
    # Drop the stray first row
    df = df.iloc[1:]
    return df

def parse_timestamps(df):
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True, errors='coerce')
    df = df.set_index('Timestamp')
    return df

def select_p1_p4_columns(normal, attack):
    # Select columns for stages 1-4 (ending in 1xx, 2xx, 3xx, 4xx)
    p14_cols = [c for c in normal.columns
                if c != 'Timestamp' and len(c) >= 3 and c[-3] in {'1', '2', '3', '4'}]
    normal = normal[p14_cols]
    attack = attack[p14_cols + ['Normal/Attack']]
    return normal, attack

def interpolate_missing_values(df):
    return df.interpolate(limit_direction='both')

def standard_scale(normal, attack):
    # Get sensor columns (exclude the label column)
    sensor_cols = [col for col in attack.columns if col != 'Normal/Attack']

    # Fit scaler on normal data
    scaler = StandardScaler().fit(normal[sensor_cols])

    # Transform both datasets using only sensor columns
    normal_z = pd.DataFrame(scaler.transform(normal[sensor_cols]),
                           index=normal.index, columns=sensor_cols)
    attack_z = pd.DataFrame(scaler.transform(attack[sensor_cols]),
                           index=attack.index, columns=sensor_cols)

    # Add the label column back to attack_z
    attack_z['Normal/Attack'] = attack['Normal/Attack'].values

    return normal_z, attack_z


def convert_to_numeric(df):
    """Convert European decimal format (comma) to numeric"""
    for col in df.columns:
        if col != 'Normal/Attack':  # Skip the label column
            # Replace comma with dot and convert to numeric
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce')
    return df