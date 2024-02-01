import os
import logging
from autogen import Autogen

def generate_explanation(key_points):
    try:
        # Initialize the Autogen model
        model = Autogen()

        # Generate a coherent piece of text explaining the topic
        explanation = model.generate(
            prompt=f"Explain the following key points: {key_points}",
            max_tokens=300,  # Adjust based on desired length
            num_return_sequences=1,
        )

        # Refine the output for readability and coherence
        refined_explanation = explanation[0]['text']

        return refined_explanation

    except Exception as e:
        logging.error(f"Error in generating explanation: {e}")
        return None

if __name__ == "__main__":
    with open('researcher_output.txt', 'r') as file:
        key_points = file.read()

    result = generate_explanation(key_points)

    if result:
        print(result)
        # Save the result to a file for later use
        with open('writer_output.txt', 'w') as file:
            file.write(result)
    else:
        print("Failed to generate explanation.")
