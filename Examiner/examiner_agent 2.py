import os
import logging
from autogen import Autogen

def generate_test_questions(explanation):
    try:
        # Initialize the Autogen model
        model = Autogen()

        # Generate test questions based on the explanation
        questions = model.generate(
            prompt=f"Create test questions based on the following explanation: {explanation}",
            max_tokens=500,  # Adjust based on desired length
            num_return_sequences=3,  # Adjust based on the number of questions desired
        )

        # Extract questions and correct answers
        test_questions = [question['text'] for question in questions]

        return test_questions

    except Exception as e:
        logging.error(f"Error in generating test questions: {e}")
        return None

if __name__ == "__main__":
    with open('writer_output.txt', 'r') as file:
        explanation = file.read()

    result = generate_test_questions(explanation)

    if result:
        for i, question in enumerate(result, start=1):
            print(f"Question {i}: {question}")
            # You may need to manually provide correct answers based on the generated questions
            # For simplicity, let's assume answers are 'A', 'B', 'C', etc.
            print(f"Correct Answer: {chr(ord('A') + i - 1)}")
            print()
    else:
        print("Failed to generate test questions.")
