import asyncio
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

SERVER_PATH = "/Users/imaadthouheed/.local/bin/latinum-wallet-mcp"

async def create_session():
    """Setup MCP session and return the session object"""
    exit_stack = AsyncExitStack()
    await exit_stack.__aenter__()

    server_params = StdioServerParameters(command="python", args=[SERVER_PATH], env=None)
    stdio_transport = await exit_stack.enter_async_context(stdio_client(server_params))
    stdio, write = stdio_transport
    session = await exit_stack.enter_async_context(ClientSession(stdio, write))
    await session.initialize()
    return session, exit_stack

async def get_signed_transaction_func(session, **kwargs):
    """Builds and signs a partial transaction to be completed by backend fee payer."""
    return await session.call_tool("get_signed_transaction", kwargs)

async def get_wallet_info_func(session, **kwargs):
    """Return wallet address, balances, and recent transactions."""
    return await session.call_tool("get_wallet_info", kwargs)