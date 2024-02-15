from transformers import pipeline

# Load the question answering pipeline
qa_pipeline = pipeline("question-answering", model="mrm8488/bert-tiny-finetuned-squadv2")

def get_chatbot_response(user_input):
    # Define the context for the question (you can customize this based on your needs)
    context = "Fitness and nutrition are important for maintaining a healthy lifestyle."

    # Get the answer from the model
    answer = qa_pipeline(question=user_input, context=context)
    return answer['answer']
