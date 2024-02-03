from autogen.autogen import Autogen  # Import Autogen from the correct module



def generate_ideas(subject):
    # Initialize the Autogen model
    model = Autogen()

    # Generate ideas for teaching the subject
    ideas = model.generate(
        prompt=f"Teach me about {subject}",
        max_tokens=200,  # Adjust based on desired length
        num_return_sequences=1,
    )

    # Extract key concepts, explanations, and teaching points
    key_points = ideas[0]['text']

    return key_points

if __name__ == "__main__":
    # Replace 'your_subject' with the actual subject you want to teach
    subject = 'your_subject'
    result = generate_ideas(subject)

    # Print or save the key points
    print(result)
