from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv() 
api_key = os.getenv('OPENAI_API_KEY')
project_id = os.getenv('PROJECT_ID')

client = OpenAI(project = project_id )


def generatePrompt(contentSystemInput, contentUserInput):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": contentSystemInput
            },
            {
                "role": "user",
                "content": contentUserInput
            }
        ],
        max_tokens=50,
        top_p=1
    )
    return completion.choices[0].message.content