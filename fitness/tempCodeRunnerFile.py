from transformers import pipeline

# Load the question answering pipeline
qa_pipeline = pipeline("question-answering", model="mrm8488/bert-tiny-finetuned-squadv2")

# Main function for interacting with the chatbot
def main():
    print("Welcome to Fitness Chatbot!")
    print("Ask me anything related to fitness and nutrition.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Define the context for the question (you can customize this based on your needs)
        context = "Fitness and nutrition are important for maintaining a healthy lifestyle."

        # Get the answer from the model
        answer = qa_pipeline(question=user_input, context=context)
        print("Chatbot:", answer['answer'])

if __name__ == "__main__":
    main()
