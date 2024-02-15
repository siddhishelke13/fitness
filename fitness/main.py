# Import necessary libraries
import random

# Function to collect user input
def get_user_input():
    print("Let's personalize your fitness plan.")
    body_type = input("What is your body type (e.g., ectomorph, mesomorph, endomorph)?: ")
    fitness_goal = input("What is your fitness goal (e.g., lose weight, build muscle)?: ")
    dietary_restrictions = input("Do you have any dietary restrictions? If yes, please specify: ")

    return body_type, fitness_goal, dietary_restrictions

# Function to generate personalized recommendations
def generate_recommendations(body_type, fitness_goal, dietary_restrictions):
    # Example personalized recommendations (replace with actual logic)
    workout_plan = f"For your {body_type} body type, a mix of cardio and strength training exercises is recommended to achieve your goal of {fitness_goal}."
    diet_plan = f"Considering your dietary restrictions ({dietary_restrictions}), a balanced diet with lean proteins, fruits, vegetables, and healthy fats would be beneficial."

    return workout_plan, diet_plan

# Main function for interacting with the chatbot
def main():
    print("Welcome to Fitness Chatbot!")
    print("Ask me anything related to fitness and nutrition.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Check if user wants personalized recommendations
        if "personalize" in user_input.lower():
            body_type, fitness_goal, dietary_restrictions = get_user_input()
            workout_plan, diet_plan = generate_recommendations(body_type, fitness_goal, dietary_restrictions)
            print("Chatbot: Here are your personalized recommendations:")
            print("Chatbot: Workout Plan:", workout_plan)
            print("Chatbot: Diet Plan:", diet_plan)
        else:
            # Default response for non-personalized queries
            responses = ["I'm sorry, I don't understand.", "Could you please provide more details?", "Let's focus on personalized recommendations. Ask me to personalize your plan."]
            print("Chatbot:", random.choice(responses))

if __name__ == "__main__":
    main()
