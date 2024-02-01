import os
from researcher_agent import generate_ideas
from writer_agent import generate_explanation
from examiner_agent import generate_test_questions

def main():
    # Researcher Agent
    subject = 'your_subject'
    researcher_output = generate_ideas(subject)

    if researcher_output:
        print("Researcher Agent Output:")
        print(researcher_output)
        print("-" * 50)

        # Save researcher output to a file
        with open('researcher_output.txt', 'w') as file:
            file.write(researcher_output)

        # Writer Agent
        writer_output = generate_explanation(researcher_output)

        if writer_output:
            print("Writer Agent Output:")
            print(writer_output)
            print("-" * 50)

            # Save writer output to a file
            with open('writer_output.txt', 'w') as file:
                file.write(writer_output)

            # Examiner Agent
            examiner_output = generate_test_questions(writer_output)

            if examiner_output:
                print("Examiner Agent Output:")
                for i, question in enumerate(examiner_output, start=1):
                    print(f"Question {i}: {question}")
                    # You may need to manually provide correct answers based on the generated questions
                    print(f"Correct Answer: {chr(ord('A') + i - 1)}")
                    print("-" * 50)
            else:
                print("Examiner Agent failed.")
        else:
            print("Writer Agent failed.")
    else:
        print("Researcher Agent failed.")

if __name__ == "__main__":
    main()
