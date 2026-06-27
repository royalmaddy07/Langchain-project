# app.py file : is responsible for storing the application logic

# 1. to load enviroument variables -> 
from dotenv import load_dotenv
load_dotenv()

# 2. import the chat model ->
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
# using temperature values ->
# 0 : most probable answers
# 1 : most creative answers

# llm.invoke() function : used to ask the model
# this sends request via the internet to Google server -> Gemini -> sends back -> Response object
# object : is not a string, rather an AIMessage object with its own methods and properties
response = llm.invoke("Explain Binary Search.")

print(response.content)