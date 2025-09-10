import React from "react";
import ReactDOM from "react-dom/client";
import AITestDashboard from "./components/AITestDashboard";
import "./styles/globals.css";
import { NavigationProvider } from "@/contexts/NavigationContext";
import { ExpandableCardProvider } from "@/contexts/ExpandableCardContext";
import { Sidebar, RightSidebar } from "@/components/layout";
import { ContentSwitcher } from "@/components/layout/ContentSwitcher";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <NavigationProvider>
      <ExpandableCardProvider>
        <div className="min-h-screen bg-black flex w-full">
          <Sidebar />
          <ContentSwitcher />
          <RightSidebar />
        </div>
      </ExpandableCardProvider>
    </NavigationProvider>
  </React.StrictMode>
);
