import streamlit as st
from transformers import BartForConditionalGeneration, BartTokenizer
from safetensors.torch import load_file
import torch

# Load the trained model and tokenizer
safetensors_file = r"C:/Users/HP/OneDrive/Bureau/summerization_text/bart_finetuned/model.safetensors"
state_dict = load_file(safetensors_file)

# Save the model weights as a PyTorch model
torch.save(state_dict, r"C:/Users/HP/OneDrive/Bureau/summerization_text/bart_finetuned/pytorch_model.bin")

model_directory = "/app/model"

# Load the model from the safetensors file
model = BartForConditionalGeneration.from_pretrained(model_directory)

# Load the tokenizer from the same directory
tokenizer = BartTokenizer.from_pretrained(model_directory)

# Move the model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Streamlit App Interface
st.title("Text Summarization App")
st.write("This app uses a fine-tuned BART model to summarize your text.")

# Text input from the user
user_input = st.text_area("Enter your text here:", "")

# Button to generate summary
if st.button("Generate Summary"):
    if user_input:
        # Tokenize the input text
        inputs = tokenizer(user_input, return_tensors="pt", max_length=512, truncation=True)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        # Generate the summary
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=50,
            num_beams=4,
            length_penalty=2.0,
            early_stopping=True
        )

        # Decode and display the summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        st.write("**Summary:**")
        st.write(summary)
    else:
        st.write("Please enter some text.")
