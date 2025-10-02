import { cn } from "@/lib/utils";
import { User, Bot, CheckCircle } from "lucide-react";

interface ChatMessageProps {
  type: "human" | "ai" | "tool";
  content: string;
}

export const ChatMessage = ({ type, content }: ChatMessageProps) => {
  const isUser = type === "human";
  const isPaymentConfirmation = content.includes("✅") || content.includes("Thank you for your order");

  // Parse content for images
  const imageMatch = content.match(/Here is an image:?\s*(https?:\/\/[^\s]+)/i);
  const imageUrl = imageMatch ? imageMatch[1] : null;
  const textContent = imageUrl ? content.replace(/Here is an image:?\s*https?:\/\/[^\s]+/gi, "").trim() : content;

  if (type === "tool") return null; // Don't render tool messages

  return (
    <div className={cn("message-fade-in flex gap-4 mb-6", isUser && "flex-row-reverse")}>
      {/* Avatar */}
      <div
        className={cn(
          "w-10 h-10 rounded-full flex items-center justify-center flex-shrink-0",
          isUser ? "bg-accent/20" : "bg-primary/30"
        )}
      >
        {isUser ? <User className="w-5 h-5 text-accent" /> : <Bot className="w-5 h-5 text-primary-foreground" />}
      </div>

      {/* Message Content */}
      <div className={cn("flex-1 max-w-2xl", isUser && "flex justify-end")}>
        <div
          className={cn(
            "rounded-2xl px-5 py-3",
            isUser ? "bg-accent text-accent-foreground" : "bg-card",
            isPaymentConfirmation && "coffee-glow border border-accent/30"
          )}
        >
          {isPaymentConfirmation && (
            <div className="flex items-center gap-2 mb-2 text-accent">
              <CheckCircle className="w-4 h-4" />
              <span className="text-sm font-medium">Payment Confirmed</span>
            </div>
          )}

          <p className="text-sm leading-relaxed whitespace-pre-wrap">{textContent}</p>

          {imageUrl && (
            <div className="mt-3">
              <img
                src={imageUrl}
                alt="Coffee"
                className="rounded-lg max-w-full h-auto border border-border"
                style={{ maxHeight: "300px" }}
              />
            </div>
          )}
        </div>

        <div className="text-xs text-muted-foreground mt-1 px-2">
          {isUser ? "You" : "Brew Haven AI"}
        </div>
      </div>
    </div>
  );
};
