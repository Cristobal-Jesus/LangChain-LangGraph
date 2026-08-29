from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from tavily import TavilyClient
from typing import Any, cast


load_dotenv()

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """
    Tool that searches over internet

    Args:
        query (str): The query to search for

    Returns:
        str: The search results
    """
    print(f"Searching for: {query}")
    return tavily.search(query=query)

llm = ChatOllama(model="qwen3:4b", temperature=0) 
tools = [search]
agent: Any = cast(Any, create_agent(model=llm, tools=tools))

def main() -> None:
    print("Hello from langchain-langgraph!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]}) 
    print(result) 

if __name__ == "__main__": 
    main() 
