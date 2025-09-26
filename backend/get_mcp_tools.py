import asyncio
import pytest
import os
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import AIMessage
SERVER_PATH = "/Users/imaadthouheed/.local/bin/latinum-wallet-mcp"
@pytest.mark.asyncio
async def test_mcp_server_connection():
    """Connect to an MCP server and verify the tools"""

    exit_stack = AsyncExitStack()

    server_params = StdioServerParameters(
        command="python", args=[SERVER_PATH], env=None
    )

    stdio_transport = await exit_stack.enter_async_context(
        stdio_client(server_params)
    )
    stdio, write = stdio_transport
    session = await exit_stack.enter_async_context(
        ClientSession(stdio, write)
    )

    await session.initialize()

    response = await session.list_tools()
    tools = response.tools
    print(response.tools)
    tool_names = [tool.name for tool in tools]
    tool_descriptions = [tool.description for tool in tools]
    tools_dict = [{"type": "function", "function": {
    "name": tool.name,
    "description": tool.description or "",
    "parameters": tool.inputSchema
        }} for tool in tools]
    
    await exit_stack.aclose()
    return tools_dict


if __name__ == "__main__":
    tools=asyncio.run(test_mcp_server_connection())
