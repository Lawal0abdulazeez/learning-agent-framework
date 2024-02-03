from autogen import Autogen

from autogen import Autogen



def generate_explanation(key_points):
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

if __name__ == "__main__":
    # Replace 'researcher_output' with the actual output from the Researcher Agent
    #researcher_output = 'researcher_output'
    researcher_output = 'powerbi'
    result = generate_explanation(researcher_output)

    # Print or save the refined explanation
    print(result)
