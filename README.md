# AI-Powered Infrastructure Security

## TLDR;
This project showcases an AI-driven approach to significantly boost cybersecurity for U.S. critical infrastructure, starting with Water Treatment Systems (WTS).

The core concept is to harness advanced AI ⎯ including LLMs, machine learning algorithms, and [Agents](https://cookbook.openai.com/topic/agents) employing [RAG](https://platform.openai.com/docs/guides/optimizing-llm-accuracy/retrieval-augmented-generation-rag#retrieval-augmented-generation-rag) with [human-in-the-loop](https://platform.openai.com/docs/guides/safety-best-practices/human-in-the-loop-hitl#human-in-the-loop-hitl) ⎯ to detect and respond to cyber threats in real-time.

## Problem
Cyberattacks on U.S. critical infrastructure are a persistent, evolving threat. Malicious actors, including state-sponsored groups from nations like China and Russia, continuously seek to exploit vulnerabilities, jeopardizing essential services and national security. Traditional security often struggles against these sophisticated and rapid attacks.

## Vision
The US-Infra-Avengers initiative envisions a comprehensive AI-powered safety net for all U.S. critical infrastructure. This system would act as a vigilant guardian, proactively identifying and neutralizing threats before significant harm occurs ⎯ much like a digital ["Avengers"](https://en.wikipedia.org/wiki/The_Avengers_(2012_film)) for national infrastructure.

## Solution
The prototype called "Aquaman" initially for WTS, but should be extendable to other sectors, involves:
> Note: At the hackathon demo, this project was presented with a [slide](https://miro.com/app/board/uXjVOR_KLDo=/?share_link_id=307595755820), the backend (ie., this repository), and an inspirational [frontend](https://us-infra-avengers.web.app).

1.  **Real-time Data Analysis:** Ingesting and analyzing data from industrial control systems (ICS) and sensors.
2.  **AI-Driven Anomaly Detection:** Employing LLMs and ML algorithms to identify unusual patterns and potential threats.
3.  **Intelligent Verification:** Utilizing Agents with RAG. These agents access and process info (maintenance logs, operational manuals, threat intelligence, ...) to contextualize anomalies, distinguishing true threats from benign operational deviations.
4.  **Rapid Alerting & Mitigation Support:** Providing early, accurate warnings of confirmed attacks for swift human intervention and automated responses.

This "Human-in-the-Loop" approach combines AI's analytical power with human expertise for robust security.

## Contact
With over a decade of software engineering experience, I am passionate about leveraging technology to solve critical national challenges. This project demonstrates my commitment to applying AI and machine learning concepts to the vital area of national security, and I am eager to contribute my expertise in software architecture and project realization to this field.

I am highly motivated to see the core concepts of this project explored and developed further. I am actively seeking opportunities to collaborate with government agencies, research institutions, or private sector partners on similar challenges. My goal is to dedicate my engineering skills and leadership to a role where I can help build and deploy innovative AI-driven security solutions for our critical infrastructure. With the right team and resources, I believe we can make a significant difference.

## Acknowledgements
Securing 1st Place in the OpenAI Track (National Security) at the SCSP x AGI House Hackathon 2025 was an incredible honor. This achievement was made possible by the vision and support of:

*   [@scspai](https://github.com/scspai)
*   [@openai](https://github.com/openai)
*   [@agi-house](https://github.com/agi-house)

Thank you for fostering innovation against critical national security challenges through technology.




## Development

#### Prepare the development environment
##### 1. Use .env
  - Rename provided **.env.example** to  **.env**
  - Proivde the API keys in the file

##### 2. Prepare data
  * Create a folder data/raw/ in the project root
  * Download [the data](https://drive.google.com/file/d/15tBLNlnWbzdTLn59sD-XXIabbEhKii9Y/view?usp=sharing)
  * Unzip the data and pull the content to the folder
  * Now you should have the files same as below structure:
    * data/raw/SWaT_Dataset_Attack_v0.csv
    * data/raw/SWaT_Dataset_Normal_v1.csv

##### 3. Run the commands

  ```bash
  conda env create -f environment.yml
  conda activate aquaman
  ```

#### Run each notebook
1. notebooks/01_data_exploration: process the raw data, which will generate the processed data under data/processed/
2. notebooks/02_model_training: use the prcoessed data (ie., data/processed/) to train the model
3. notebooks/03_crewai_scada_triage: use the trained model (ie., models/) to detect anomaly behaviors.

Note:
- When running a notebook, you should "Select Kernel" to choose "aquaman (Python 3.10.18)" on the Jupyter notebook UI, which is the dependent version listed in environment.yml.
- You may simply just run the first and the third notebooks since the model has been trained and prepared in models/