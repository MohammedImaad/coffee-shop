from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio
from langchain_core.messages import HumanMessage
from langgraph_flow import buildGraph

app = FastAPI()

graph=buildGraph()
class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]

class ChatResponse(BaseModel):
    messages: List[Dict[str, Any]]

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    graph=await buildGraph()
    # Convert dict messages to HumanMessage objects
    messages = [HumanMessage(content=msg["content"]) for msg in request.messages]
    
    initial_state = {
        "messages": messages
    }
    
    # Run the graph
    final_state = await graph.ainvoke(initial_state)
    
    # Convert messages back to dict for response
    response_messages = []
    for msg in final_state["messages"]:
        response_messages.append({
            "type": msg.type,
            "content": msg.content,
            "additional_kwargs": msg.additional_kwargs
        })
    
    return ChatResponse(messages=response_messages)

@app.get("/")
async def root():
    return {"message": "Coffee ordering assistant API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)