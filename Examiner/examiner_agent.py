from autogen import Autogen

def generate_test_questions(explanation):
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

if __name__ == "__main__":
    # Replace 'writer_output' with the actual output from the Writer Agent
    writer_output = 'writer_output'
    result = generate_test_questions(writer_output)

    # Print or save the test questions
    for i, question in enumerate(result, start=1):
        print(f"Question {i}: {question}")
        # You may need to manually provide correct answers based on the generated questions
        # For simplicity, let's assume answers are 'A', 'B', 'C', etc.
        print(f"Correct Answer: {chr(ord('A') + i - 1)}")
        print()
