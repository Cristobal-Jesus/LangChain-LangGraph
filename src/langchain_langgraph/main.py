from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from typing import Any, cast


load_dotenv()

llm = ChatOllama(model="qwen3:4b", temperature=0) 
tools = [TavilySearch()]
agent: Any = cast(Any, create_agent(model=llm, tools=tools))

def main() -> None:
    print("Hello from langchain-langgraph!")
    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]}) 
    print(result) 

if __name__ == "__main__": 
    main() 
