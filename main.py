import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.responses import Response

load_dotenv()

def generate_story(model: str, prompt: str, temperature: float) -> Response:
    """

    :param temperature:
    :param prompt:
    :type model: object
    """
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OpenAI key is missing!")

    client = OpenAI(
        api_key=key
    )

    response = client.responses.create(
        model=model,
        instructions="You are a story writer who writes short stories for magazines",
        input=prompt,
        temperature=temperature
    )

    return response

if __name__=="__main__":
    try:
        model = "gpt-4o"
        prompt = """Can you write a story that is witty and funny that is no more than 5 sentences?
        And output should look like \"Story Title\": \"Actual Story\"
        Story should be understandable by readers of all ages with simple words yet funny to read.
        
        #Also explain at the end whats the context of the funny thing in the story
        """
        temperature = 0.0
        llm_response = generate_story(model, prompt, temperature)
        print(llm_response.output_text)
    except Exception as e:
        print(f"Something went while sending request to OpenAI: {e}")




