from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI


load_dotenv()

def main() -> None:
    print("Hello from langchain-langgraph!")

if __name__ == "__main__":
    main()
