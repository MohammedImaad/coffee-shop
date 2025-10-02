import { Coffee, Info } from "lucide-react";
import { NavLink } from "react-router-dom";
import { cn } from "@/lib/utils";

export const Sidebar = () => {
  return (
    <aside className="w-64 h-screen bg-sidebar border-r border-sidebar-border flex flex-col">
      {/* Header */}
      <div className="p-6 border-b border-sidebar-border">
        <div className="flex items-center gap-3">
          <Coffee className="w-8 h-8 text-accent" />
          <div>
            <h1 className="text-xl font-bold text-sidebar-foreground">Brew Haven</h1>
            <p className="text-xs text-muted-foreground">Web3 Coffee Shop</p>
          </div>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 p-4">
        <div className="space-y-2">
          <NavLink
            to="/"
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 px-4 py-3 rounded-lg transition-all",
                "hover:bg-sidebar-accent",
                isActive && "bg-sidebar-accent text-sidebar-accent-foreground font-medium"
              )
            }
          >
            <Coffee className="w-5 h-5" />
            <span>Get Coffee</span>
          </NavLink>

          <NavLink
            to="/about"
            className={({ isActive }) =>
              cn(
                "flex items-center gap-3 px-4 py-3 rounded-lg transition-all",
                "hover:bg-sidebar-accent",
                isActive && "bg-sidebar-accent text-sidebar-accent-foreground font-medium"
              )
            }
          >
            <Info className="w-5 h-5" />
            <span>About</span>
          </NavLink>
        </div>
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-sidebar-border">
        <div className="text-xs text-muted-foreground text-center">
          <p>Powered by USDC</p>
          <p className="text-accent">Blockchain Coffee ☕</p>
        </div>
      </div>
    </aside>
  );
};
