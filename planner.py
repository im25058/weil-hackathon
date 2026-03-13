from langchain_openai import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

def plan_query(query):

    prompt = f"""
Break the research question into steps.

Question:
{query}

Return each step on a new line.
"""

    response = llm.invoke(prompt)

    tasks = response.content.split("\n")

    return tasks