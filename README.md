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
