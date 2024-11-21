from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv() 
api_key = os.getenv('OPENAI_API_KEY')
project_id = os.getenv('PROJECT_ID')

client = OpenAI(project = project_id )

    

def generatePrompt(contentUserInput):
    try:
        if not isinstance(contentUserInput, str):
            raise ValueError("Both contentSystemInput and contentUserInput must be strings")
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": contentUserInput
                }
            ],
            max_tokens=100,
            top_p=1,
        )
        response = completion.choices[0].message.content
        return response
    except ValueError as ve:
        return str
    
