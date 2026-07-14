import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile"
role="user"



# customer ticket
from pydantic import BaseModel
class ticket(BaseModel):
    name: str
    product: str
    email: str
    issue: str
    phone_number: str

schema = ticket.model_json_schema()

response_format={
        "type": "json_object"
    }

system_prompt = f"""You are a helpful assistant. You will be given a customer ticket. Please extract the personal information from the ticket and return it in the following JSON format: {schema}"""
Text = "My name is PiYush. I have purchased an iPhone. My email is ABC@123. The issue is that it stops working after 2 daysMy phone number is 1234567. "
prompt=f""" This is a customer ticket. Please extract Personal information from this.{Text} """

message_system={
    "role": "system",
    "content": system_prompt   
}
# message me role and content
message={
    "role": role,
    "content": prompt
}

messages=[message_system,message]
# Temperature by default is 0 meaning safe. range is [0,2]
response=client.chat.completions.create(model=model, messages=messages, response_format=response_format )
# print(response)



answer=response.choices[0].message.content
print(answer)
#to read the json data from the response we can use pydantic model to parse the data
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=ticket(**data_file)
print(ticket.name)
print(ticket.email)
print(ticket.phone_number)
print(ticket.issue)
