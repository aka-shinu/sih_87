"use client";

import { useTypewriter } from '@/hooks/useTypewriter';

interface TypewriterTextProps {
  text: string;
  speed?: number;
  className?: string;
  children?: React.ReactNode;
}

export function TypewriterText({ text, speed = 50, className = '', children }: TypewriterTextProps) {
  const { displayedText, isTyping } = useTypewriter(text, speed);

  return (
    <span className={className}>
      {displayedText}
      {isTyping && <span className="animate-pulse">|</span>}
      {children}
    </span>
  );
}
