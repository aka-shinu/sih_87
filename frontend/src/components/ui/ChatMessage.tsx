"use client";

import { useEffect, useRef, useState } from 'react';
import { useInView } from 'react-intersection-observer';
import { ChatMessageProps } from '@/types/components';
import { ThinkingDots, TypewriterText } from '@/components/animations';

export function ChatMessage({ message, isStreaming = false, containerRef, firstCalculatedHeight = 120, setFirstCalculatedHeight }: ChatMessageProps) {
  const [aiMessageHeight, setAiMessageHeight] = useState('120px');
  const [isPinned, setIsPinned] = useState(false);
  const conRef = useRef<HTMLDivElement>(null);
  
  const { ref: userMessageRef, inView: userMessageInView } = useInView({
    threshold: 0.1,
    triggerOnce: false
  });
  
  const { ref: aiMessageRef, inView: aiMessageInView } = useInView({
    threshold: 0.1,
    triggerOnce: false
  });
  useEffect(() => {
    const calculateHeight = () => {
      if (containerRef?.current && message.role === 'assistant' && message.parentId) {
        const containerHeight = containerRef.current.offsetHeight;
        const userMessageId = `user-message-${message.parentId}`;
        const userMessageElement = document.getElementById(userMessageId);
        const rectm = conRef.current?.getBoundingClientRect();
        
        if (userMessageElement) {
          const rect= userMessageElement?.getBoundingClientRect()
          const yNet = rect.height + rect.y;
          const spacing = (rectm?.y || 0) - (yNet || 0);
          const userMessageHeight = rect?.height;
          const calculatedHeight = containerHeight - userMessageHeight - rect?.y - (spacing) ; // 32px for padding/margins
          
          // Store the first successful calculation in RightSidebar
          if (firstCalculatedHeight === 120 && setFirstCalculatedHeight) {
            setFirstCalculatedHeight(Math.max(calculatedHeight, 120));
          }
          
          setAiMessageHeight(`${Math.max(calculatedHeight, firstCalculatedHeight)}px`);
        }
      }
    };

    calculateHeight();
    window.addEventListener('resize', calculateHeight);
    return () => window.removeEventListener('resize', calculateHeight);
  }, [containerRef, message.parentId, message.role,conRef]);

  useEffect(() => {
    if (message.role === 'user') {
      setIsPinned(userMessageInView);
    } else {
      setIsPinned(aiMessageInView);
    }
  }, [userMessageInView, aiMessageInView, message.role]);

  useEffect(() => {
    if (message.role === 'user') {
      const isNewMessage = Date.now() - message.timestamp.getTime() < 5000;
      if (isNewMessage) {
        setIsPinned(true);
      }
    }
  }, [message.timestamp, message.role]);

  const isUser = message.role === 'user';
  
  if (isUser) {
    return (
      <div 
        ref={userMessageRef}
        className={`text-start ${isPinned ? 'sticky top-0 z-10  p-4 -mx-4 -mt-4 mb-4' : ''}`}
        id={`user-message-${message.id}`}
      >
        <div className="bg-gray-800/30 rounded-2xl px-6 py-3 border border-white/10 w-full text-sm text-white/90 whitespace-pre-wrap break-words">
          {message.content}
        </div>
      </div>
    );
  }
  return (
    <div className="flex gap-3" ref={aiMessageRef}>   
      <div className="flex-1 w-full text-left">
        <div 
        ref={conRef}
          className="rounded-lg p-2 pb-0 pt-0 text-sm text-white/90 whitespace-pre-wrap break-words"
          style={{ minHeight: aiMessageHeight }}
        >
          {isStreaming && message.content === '' ? (
            <ThinkingDots />
          ) : (
            message.content
          )}
        </div>
      </div>
    </div>
  );
}
