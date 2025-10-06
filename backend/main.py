from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import asyncio
from langchain_core.messages import HumanMessage
from langgraph_flow import buildGraph
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],  # frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatRequest(BaseModel):
    messages: List[Dict[str, Any]]

class ChatResponse(BaseModel):
    messages: List[Dict[str, Any]]


graph = None 
conversation_history = [] 
@app.on_event("startup")
async def startup_event():
    global graph
    graph = await buildGraph()
@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    global conversation_history
    # Add new messages to history
    new_messages = [HumanMessage(content=msg["content"]) for msg in request.messages]
    conversation_history.extend(new_messages)

    # Feed the full history into the graph
    initial_state = {"messages": conversation_history}

    final_state = await graph.ainvoke(initial_state)

    response_messages = [
        {
            "type": msg.type,
            "content": msg.content,
            "additional_kwargs": msg.additional_kwargs,
        }
        for msg in final_state["messages"]
    ]

    # Also extend history with AI responses
    for msg in final_state["messages"]:
        if msg.type == "ai":
            conversation_history.append(msg)

    return ChatResponse(messages=response_messages)

@app.get("/")
async def root():
    return {"message": "Coffee ordering assistant API"}

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)