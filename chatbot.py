# step 2. import the chat model ->
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# using temperature values ->
# 0 : most probable answers
# 1 : most creative answers