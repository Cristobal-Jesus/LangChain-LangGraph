from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch
from typing import Any, cast, List
from pydantic import BaseModel, Field


load_dotenv()


class Source(BaseModel):
    """Scheme for a source used by the agent."""
    
    url: str = Field(description="The URL of the source.")
    
    
class AgentResponse(BaseModel):
    """Scheme for the agent's response with answer and sources."""
    
    answer: str = Field(description="The agent's answer to the query.")
    sources: List[Source] = Field(default_factory=list, description="The list of sources used to generate the answer.")


llm = ChatOllama(model="qwen3:4b", temperature=0) 
tools = [TavilySearch()]
agent: Any = cast(Any, create_agent(model=llm, tools=tools, response_format=AgentResponse))

def main() -> None:
    print("Hello from langchain-langgraph!")
    result = agent.invoke(
        {
            "messages": [HumanMessage(
                content="What is the weather in Tokyo?")]
            }
        ) 
    print(result) 

if __name__ == "__main__": 
    main() 
