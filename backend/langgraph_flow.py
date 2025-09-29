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
from mcp_helpers import create_session, get_signed_transaction_func, get_wallet_info_func, send_money_to_wallet_func, get_credit_func
from test_payment import use_tool
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
async def main():
    
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
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.5,
        api_key=OPENAI_API_KEY
    )
    async def wallet_info(**kwargs):
        """Return wallet address, balances, and recent transactions."""
        return await get_wallet_info_func(session, **kwargs)

    async def signed_tx(**kwargs):
        """Builds and signs a partial transaction to be completed by backend fee payer."""
        return await get_signed_transaction_func(session, **kwargs)
    
    async def credit(**kwargs):
        """Get your credit balance."""
        return await get_credit_func(session, **kwargs)

    async def send_money_to_wallet(amount_usdc: str, target_wallet: str):
        """Send money to a wallet.
            
        """
        amount_usdc = int(amount_usdc)
        target_wallet = str(target_wallet)
        print("Seedhe Maut", amount_usdc, target_wallet)
        params = {"amount_usdc": amount_usdc, "target_wallet": target_wallet}
        return await use_tool("transfer_funds",amount=amount_usdc,seller_wallet=target_wallet)


    def should_continue(state: State) -> State:
        print("STATE SHOULD CONTINUE: ", state)
        messages = state["messages"]
        last_message = messages[-1]
        print("LAST MESSAGE: ", last_message)
        if last_message.tool_calls:
            return "tools"
        return END
    
    llm_with_tools=llm.bind_tools([wallet_info, signed_tx,credit,send_money_to_wallet])
    session, exit_stack = await create_session()
    builder = StateGraph(State)
    builder.add_node("get_response", get_response)
    tool_node = ToolNode([wallet_info,signed_tx,credit,send_money_to_wallet])
    builder.add_node("tools", tool_node)
    builder.add_edge(START, "get_response")
    builder.add_conditional_edges("get_response",should_continue)
    builder.add_edge("tools", "get_response")
    builder.add_edge("get_response", END)
    graph = builder.compile()
    initial_state = {
        "messages": [HumanMessage(content="send 1000 atomic amount  to wallet axyCcXAKRGwTgYqyJYLEyGcY7YtVHnACyxxJ1WY8MLH using the appropraite function. If theres an error show entire error stack.")]
    }

    # Run the graph
    final_state = await graph.ainvoke(initial_state)
    messages=final_state['messages']
    for m in messages:
        m.pretty_print()
    
    await exit_stack.aclose()
    

if __name__ == "__main__":
    asyncio.run(main())