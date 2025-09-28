import requests
from mcp_helpers import create_session, get_signed_transaction_func, get_wallet_info_func
import asyncio

async def signed_tx(**kwargs):
        """Builds and signs a partial transaction to be completed by backend fee payer."""
        session, exit_stack = await create_session()
        return await get_signed_transaction_func(session, **kwargs)

  
async def use_tool(arg: str,amount=0,seller_wallet="") -> dict:
    SELLER_WALLET = seller_wallet
    FACILITATOR_URL = "https://facilitator.latinum.ai/api/facilitator"
    MINT_ADDRESS = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v" # USDC
    NETWORK = "mainnet"
    PRICE_ATOMIC_AMOUNT = amount 
    kwargs = {
        "targetWallet": seller_wallet,  
        "amountAtomic": PRICE_ATOMIC_AMOUNT,
        "network": NETWORK,
        "mint": MINT_ADDRESS
    }
    signed_transaction = await signed_tx(**kwargs)
    signed_b64 = signed_transaction.content[0].text.split("signedTransactionB64: ")[1]
    res = requests.post(FACILITATOR_URL, json={
            "chain": "solana",
            "signedTransactionB64": signed_b64,
            "expectedRecipient": SELLER_WALLET,
            "expectedAmountAtomic": PRICE_ATOMIC_AMOUNT,
            "network": NETWORK,
            "mint": MINT_ADDRESS,
    })
    data = res.json() 
  
    return data
  
    




async def main():
   


    result = await use_tool("transfer_funds",amount=10000,seller_wallet="axyCcXAKRGwTgYqyJYLEyGcY7YtVHnACyxxJ1WY8MLH")

    print("use_tool result:", result)

if __name__ == "__main__":
    asyncio.run(main())

