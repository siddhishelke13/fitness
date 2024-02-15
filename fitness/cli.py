# from personalization import ask_question
from chatbot_logic import get_chatbot_response

def main():
    print("Welcome to Fitness Chatbot!")
    print("Ask me anything related to fitness and nutrition.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = get_chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
