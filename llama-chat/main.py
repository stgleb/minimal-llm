import sys
from llama_cpp import Llama

# Load the model
model_path = "models/mixtral-8x7b-instruct-v0.1.Q2_K.gguf"  # Update this path as needed
llama = Llama(model_path=model_path)

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
        print(response['text'])

if __name__ == "__main__":
    main()