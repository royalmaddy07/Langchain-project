# app.py file : is responsible for storing the application logic

# step 1. to load enviroument variables -> 
from dotenv import load_dotenv
from chatbot import llm

load_dotenv()

# step 3 : llm.invoke() function : used to ask the model
# this sends request via the internet to Google server -> Gemini -> sends back -> Response object
# object : is not a string, rather an AIMessage object with its own methods and properties

question = input("Ask: ")
response = llm.invoke(question)

print(response.content)