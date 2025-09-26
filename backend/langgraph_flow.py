from get_mcp_tools import test_mcp_server_connection
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_core.tools import StructuredTool
import asyncio, os
from dotenv import load_dotenv
import asyncio
from langchain_core.runnables import RunnableLambda
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage, AIMessage, AnyMessage
from langchain_core.tools import tool
from typing import Annotated
from langgraph.prebuilt import ToolNode
from retriever_file import get_answer
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
async def main():
    tools = await test_mcp_server_connection()
    print(tools)
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.5,
        api_key=OPENAI_API_KEY
    )
    llm_with_tools=llm.bind_tools(tools)
    class State(TypedDict):
        messages: Annotated[list[AnyMessage], add_messages]
        
    def get_response(state: State):
        context=get_answer(state["messages"][-1].content)
        prompt=f"""You are assisting people in ordering coffee.Use the following context to answer the question concisely.
            Context:
            {context}

            All the messages: {state["messages"]}

            Answer:"""
        response = llm_with_tools.invoke(prompt)
        return {"messages": [response]}
    
    builder = StateGraph(State)
    builder.add_node("get_response", get_response)
    builder.add_edge(START, "get_response")
    builder.add_edge("get_response", END)
    graph = builder.compile()
    initial_state = {
        "messages": [HumanMessage(content="Whats the balance")]
    }

    # Run the graph
    final_state = await graph.ainvoke(initial_state)
    messages=final_state['messages']
    for m in messages:
        m.pretty_print()
    
    
    

if __name__ == "__main__":
    asyncio.run(main())