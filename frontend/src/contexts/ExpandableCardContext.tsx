"use client";

import { createContext, useContext, useState, ReactNode } from 'react';

interface ExpandableCardContextType {
  isExpanded: boolean;
  setIsExpanded: (expanded: boolean) => void;
}

const ExpandableCardContext = createContext<ExpandableCardContextType | undefined>(undefined);

export function ExpandableCardProvider({ children }: { children: ReactNode }) {
  const [isExpanded, setIsExpanded] = useState(false);

  return (
    <ExpandableCardContext.Provider value={{ isExpanded, setIsExpanded }}>
      {children}
    </ExpandableCardContext.Provider>
  );
}

export function useExpandableCardContext() {
  const context = useContext(ExpandableCardContext);
  if (!context) {
    throw new Error('useExpandableCardContext must be used within ExpandableCardProvider');
  }
  return context;
}