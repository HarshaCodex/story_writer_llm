import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
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



