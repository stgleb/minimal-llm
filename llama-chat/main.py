import sys
from llama_cpp import Llama

# Load the model
model_path = "/home/stgleb/GolandProjects/minimal-llm/llama-chat/models/Mixtral-8x7B-Instruct-v0.1.IQ3_M.gguf"  # Update this path as needed
try:
    llama = Llama(model_path=model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

def main():
    print("Model loaded. Enter your text input (type 'exit' to quit):")

    while True:
        # Read user input
        user_input = input(">>> ")

        # Exit the REPL if the user types 'exit'
        if user_input.lower() == 'exit':
            print("Exiting the REPL.")
            break

        # Generate a response from the model
        response = llama(user_input)

        # Print the model's response
        print(response['choices'][0]['text'])

if __name__ == "__main__":
    main()