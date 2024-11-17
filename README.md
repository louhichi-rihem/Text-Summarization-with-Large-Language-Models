# Text-Summarization-with-Large-Language-Models

## The Task
The task is to perform text summarization using Large Language Models (LLMs). This process generates a concise version of a document or article while preserving all the key information

## The Dataset
We are going to use the SamSum Dataset, which contains three csv files for training, testing, and validation. All these files are structured into a specific id, a dialogue, and a summary. The SamSum dataset consists of chat texts, which is ideal for the summarization of dialogues.

## The Model
We will leverage the power of a pre-trained model for this task, specifically using the BART architecture. In particular, I will fine-tune a version of BART to enhance its performance for our needs.

## Evaluation Metrics
Evaluating performance for language models can be quite tricky, especially when it comes to text summarization. The goal of our model is to produce a short sentence describing the content of a dialogue, while maintaining all the important information within that dialogue.
One of the quantitative metrics we can employ to evaluate performance is the ROUGE Score. It is considered one of the best metrics for text summarization and it evaluates performance by comparing the quality of a machine-generated summary to a human-generated summary used for reference.



## Example of text summarization using the implemented Streamlit interface
![summ1](https://github.com/user-attachments/assets/f35b85d5-7ad0-44cc-af0a-bf862af4c59b)

The text summarization application is a Streamlit-based project utilizing a fine-tuned BART model for summarizing input text. To enhance portability and ease of deployment, the application was containerized using Docker. The trained model, stored locally with the required files such as config.json, pytorch_model.bin, and tokenizer files, was integrated into the Docker image. A custom Dockerfile was created to set up the container environment, including the installation of dependencies from a requirements.txt file and copying the model files and application script into the container. The model was loaded from the local directory within the container using Hugging Face’s from_pretrained method. The container was configured to expose port 8501, enabling users to access the Streamlit app via a browser. This containerization process ensures that the application, along with the model, can be deployed consistently across different systems without manual setup, making it scalable and efficient for real-world usage.
