import { useState } from "react";
import { ChatMessage } from "@/components/ChatMessage";
import { ChatInput } from "@/components/ChatInput";
import { EmptyState } from "@/components/EmptyState";

interface Message {
  type: "human" | "ai" | "tool";
  content: string;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (content: string) => {
  const userMessage: Message = { type: "human", content };
  setMessages((prev) => [...prev, userMessage]);
  setIsLoading(true);

  try {
    // Prepare request body (all messages including the new one)
    const updatedMessages = [...messages, userMessage];

    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ messages: updatedMessages }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // The backend returns `messages`, we’ll take the last one as the AI’s reply
    const aiMessages = data.messages.filter((msg: any) => msg.type === "ai");

    if (aiMessages.length > 0) {
      const aiMessage: Message = {
        type: "ai",
        content: aiMessages[aiMessages.length - 1].content,
      };
      setMessages((prev) => [...prev, aiMessage]);
    }
  } catch (error) {
    console.error("Error sending message:", error);
  } finally {
    setIsLoading(false);
  }
};


  return (
    <div className="h-screen flex flex-col">
      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto">
        {messages.length === 0 ? (
          <EmptyState />
        ) : (
          <div className="max-w-4xl mx-auto py-8 px-6">
            {messages.map((message, index) => (
              <ChatMessage key={index} type={message.type} content={message.content} />
            ))}
            {isLoading && (
              <div className="flex gap-4 mb-6">
                <div className="w-10 h-10 rounded-full bg-primary/30 flex items-center justify-center">
                  <div className="w-5 h-5 border-2 border-primary-foreground border-t-transparent rounded-full animate-spin" />
                </div>
                <div className="bg-card rounded-2xl px-5 py-3">
                  <p className="text-sm text-muted-foreground">Brewing your response...</p>
                </div>
              </div>
            )}
          </div>
        )}
      </div>

      {/* Input */}
      <ChatInput onSendMessage={handleSendMessage} disabled={isLoading} />
    </div>
  );
}
