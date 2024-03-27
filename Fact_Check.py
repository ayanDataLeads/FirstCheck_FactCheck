from openai import OpenAI

# Define the fact-checking function
def check_fact(text, client):
    prompt = text + "\nbased on the above message, give a fact-checking response in one paragraph.\
             \nthe Fact check must be backed by scientific evidence, research, and studies. Look for information published by WHO and other reputed medical organisations.\
             \nStart the response with 'The claim...'\
             \nIn a new paragraph starting with 'Always remember', emphasize the importance of obtaining medical advice from certified health professionals rather than relying on social media or unverified sources. Stress that misleading information can be harmful to public health and it's crucial to ensure the accuracy of health-related information before sharing it with others."

    prompt = str(prompt)
    
    try:
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant named Dr. Eagle."},
                {"role": "user", "content": prompt},
            ]
        )
        response_data = response.choices[0].message.content
        return response_data

    except Exception as e:
        return f"Error during fact-checking: {e}"
