from langchain_core.prompts import ChatPromptTemplate

# note : {topic} -> placeholder managed by langchain, note that it only generates the prompt and does not invoke
# the brain/llm being used
programming_prompt = ChatPromptTemplate.from_template(
    """
You are an expert programming tutor.

Explain the following topic in simple language.

Topic:
{topic}

Give:
1. Definition
2. Working
3. Time Complexity (if applicable)
4. Example
"""
)