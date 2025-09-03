import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OpenAI key is missing!")

try:
    client = OpenAI(
        api_key=key
    )

    response = client.responses.create(
        model="gpt-4o",
        instructions="You are a story writer who writes short stories for magazines",
        input="""Can you write a story that is witty and funny that is no more than 5 sentences?
        And output should look like \"Story Title\": \"Actual Story\"
        Story should be understandable by readers of all ages with simple words yet funny to read.
        
        #Also explain at the end whats the context of the funny thing in the story
        """,
        temperature=0
    )

    print(response.output_text)
except Exception as e:
    print(f"Something went while sending request to OpenAI: {e}")



