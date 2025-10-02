import { Bot, Database, DollarSign } from "lucide-react";

export default function About() {
  return (
    <div className="h-screen overflow-y-auto">
      <div className="max-w-3xl mx-auto py-12 px-6">
        <div className="mb-12">
          <h1 className="text-4xl font-bold mb-4 bg-gradient-to-r from-accent to-primary bg-clip-text text-transparent">
            About Brew Haven
          </h1>
          <p className="text-lg text-muted-foreground">
            Where AI meets blockchain to revolutionize your coffee experience
          </p>
        </div>

        <div className="space-y-8">
          {/* RAG Pipeline Section */}
          <div className="bg-card rounded-xl p-6 border border-border coffee-glow">
            <div className="flex items-start gap-4 mb-4">
              <div className="bg-accent/20 p-3 rounded-lg">
                <Bot className="w-6 h-6 text-accent" />
              </div>
              <div>
                <h2 className="text-xl font-semibold mb-2">Advanced RAG Pipeline</h2>
                <p className="text-muted-foreground leading-relaxed">
                  Brew Haven Coffee Shop runs on an advanced RAG (Retrieval-Augmented Generation) pipeline. 
                  The knowledge base is converted into vectors and injected as context into the LLM, ensuring 
                  accurate menu queries and coffee information.
                </p>
              </div>
            </div>
          </div>

          {/* Payments Section */}
          <div className="bg-card rounded-xl p-6 border border-border coffee-glow">
            <div className="flex items-start gap-4 mb-4">
              <div className="bg-primary/20 p-3 rounded-lg">
                <DollarSign className="w-6 h-6 text-primary-foreground" />
              </div>
              <div>
                <h2 className="text-xl font-semibold mb-2">Blockchain Payments with Latinum.ai</h2>
                <p className="text-muted-foreground leading-relaxed">
                  Payments are processed directly on-chain using Latinum.ai's agent, letting customers order 
                  coffee with simple prompts like "Buy me an espresso". Every transaction is secure, 
                  transparent, and instant.
                </p>
              </div>
            </div>
          </div>

          {/* USDC Section */}
          <div className="bg-card rounded-xl p-6 border border-border coffee-glow">
            <div className="flex items-start gap-4 mb-4">
              <div className="bg-secondary/20 p-3 rounded-lg">
                <Database className="w-6 h-6 text-secondary-foreground" />
              </div>
              <div>
                <h2 className="text-xl font-semibold mb-2">USDC-Only Operations</h2>
                <p className="text-muted-foreground leading-relaxed">
                  By operating only on USDC, Brew Haven redefines how people think about payments: 
                  instant, reliable, and built into everyday chat. No credit cards, no cash—just 
                  seamless blockchain transactions.
                </p>
              </div>
            </div>
          </div>

          {/* Tech Stack */}
          <div className="bg-gradient-to-br from-accent/10 to-primary/10 rounded-xl p-6 border border-accent/20">
            <h3 className="text-lg font-semibold mb-3">Technology Stack</h3>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <span className="text-accent font-medium">Frontend:</span>
                <span className="text-muted-foreground ml-2">React + TypeScript</span>
              </div>
              <div>
                <span className="text-accent font-medium">AI:</span>
                <span className="text-muted-foreground ml-2">RAG Pipeline + LLM</span>
              </div>
              <div>
                <span className="text-accent font-medium">Blockchain:</span>
                <span className="text-muted-foreground ml-2">Solana + USDC</span>
              </div>
              <div>
                <span className="text-accent font-medium">Agent:</span>
                <span className="text-muted-foreground ml-2">Latinum.ai</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
