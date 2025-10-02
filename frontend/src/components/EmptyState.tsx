import { Coffee } from "lucide-react";

export const EmptyState = () => {
  return (
    <div className="flex flex-col items-center justify-center h-full text-center px-6">
      <div className="bg-gradient-to-br from-accent/20 to-primary/20 p-8 rounded-full mb-6">
        <Coffee className="w-16 h-16 text-accent" />
      </div>
      
      <h2 className="text-2xl font-bold mb-3 text-foreground">
        Welcome to Brew Haven Coffee Shop
      </h2>
      
      <p className="text-muted-foreground max-w-md text-sm leading-relaxed">
        The first coffee shop running entirely on blockchain payments. Ask me about coffee, 
        and pay seamlessly with USDC.
      </p>

      <div className="mt-8 grid grid-cols-2 gap-4 text-left max-w-md">
        <div className="bg-card p-4 rounded-lg border border-border">
          <p className="text-xs font-medium text-accent mb-1">Try asking:</p>
          <p className="text-sm text-muted-foreground">"How much is an espresso?"</p>
        </div>
        <div className="bg-card p-4 rounded-lg border border-border">
          <p className="text-xs font-medium text-accent mb-1">Or simply:</p>
          <p className="text-sm text-muted-foreground">"I'd like a cappuccino"</p>
        </div>
      </div>
    </div>
  );
};
