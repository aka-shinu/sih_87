"use client";

import { useState, useEffect, useRef } from 'react';
import { ChatInputField, ChatMessage } from '@/components/ui';
import { ThinkingDots } from '@/components/animations';
import { useChat } from '@/hooks/useChat';
import { useAutoScroll } from '@/hooks/useAutoScroll';
import { useResizableSidebar } from '@/hooks/useAnimation';
import { welcomeMessage } from '@/data/greetings';

export function RightSidebar() {
  const [isMounted, setIsMounted] = useState(false);
  const messagesContainerRef = useRef<HTMLDivElement>(null);
  const { scrollToBottom, scrollToBottomNow, disableTrigger } = useAutoScroll(messagesContainerRef);
  const { inputValue, setInputValue, messages, isInputAtTop, isLoading, isStreaming, handleKeyPress, handleSend } = useChat(5);
  const [firstCalculatedHeight, setFirstCalculatedHeight] = useState(120);
  const { width, isResizing, handleMouseDown } = useResizableSidebar();

  useEffect(() => {
    setIsMounted(true);
  }, []);

  // Scroll immediately when user sends message
  useEffect(() => {
    if (messages.length > 0) {
      const userMessages = messages.filter(msg => msg.role === 'user');
      if (userMessages.length > 0) {
        const lastUserMessage = userMessages[userMessages.length - 1];
        const timeSinceUserMessage = Date.now() - lastUserMessage.timestamp.getTime();
        if (timeSinceUserMessage < 1000) {
          scrollToBottomNow();
        }
      }
    }
  }, [messages, scrollToBottomNow]);

  // Scroll during streaming
  useEffect(() => {
    if (messages.length > 0) {
      const lastMessage = messages[messages.length - 1];
      if (lastMessage?.isStreaming) {
        scrollToBottom();
      }
    }
  }, [messages, scrollToBottom]);

  const lastScrollTop = useRef(0);
  
  const handleScroll = () => {
    if (messagesContainerRef.current) {
      const { scrollTop, scrollHeight, clientHeight } = messagesContainerRef.current;
      const isAtBottom = scrollTop + clientHeight >= scrollHeight - 10;
      
      // Only disable if user scrolled up and not at bottom
      if (scrollTop < lastScrollTop.current && !isAtBottom) {
        disableTrigger();
      }
      
      lastScrollTop.current = scrollTop;
    }
  };


  if (!isMounted) {
    return (
      <div className="w-130 bg-gray-800/30 backdrop-blur-sm border border-white/5 relative flex flex-col">
        <div className="flex-1 relative">
          <div className="absolute top-4 left-4 right-4">
            <ChatInputField
              inputValue=""
              setInputValue={() => {}}
              onKeyPress={() => {}}
              onSend={() => {}}
            />
          </div>
        </div>
      </div>
    );
  }

  return (
    <div 
      className="border-l border-white/10 bg-black/30 backdrop-blur-sm flex flex-col h-screen relative"
      style={{ width: `${width}%` }}
    >
      {/* Resize Handle */}
      <div
        className="absolute left-0 top-0 bottom-0 w-1 cursor-col-resize hover:bg-white/20 transition-colors duration-200 z-10"
        onMouseDown={handleMouseDown}
      />
      <div className="flex-1 relative flex flex-col min-h-0">
        {messages.length > 0 ? (
          <div className="flex-1 flex flex-col min-h-0">
            <div 
              className="flex-1 overflow-y-auto min-h-0 messages-scrollbar" 
              ref={messagesContainerRef}
              onScroll={handleScroll}
              style={{
                scrollbarWidth: 'thin',
                scrollbarColor: 'rgba(255, 255, 255, 0.2) transparent'
              }}
            >
              <div className="p-4 pb-0 w-full  space-y-6 min-h-[60vh]">
                {messages
                  .sort((a, b) => a.timestamp.getTime() - b.timestamp.getTime())
                  .map((message) => (
                    <ChatMessage 
                      key={message.id} 
                      message={message}
                      isStreaming={message.isStreaming}
                      containerRef={messagesContainerRef}
                      firstCalculatedHeight={firstCalculatedHeight}
                      setFirstCalculatedHeight={setFirstCalculatedHeight}
                    />
                  ))}
              </div>
            </div>
          </div>
        ) : (
          <div className="flex-1 flex flex-col justify-between min-h-0">
            <div className="flex-1 flex items-center justify-center">
              <div className="text-center space-y-4">
                <div className="text-2xl font-semibold text-white/90">
                  {welcomeMessage.getTitle()}
                </div>
                <div className="text-xs text-white/50 max-w-xs">
                  {welcomeMessage.getDescription()}
                </div>
              </div>
            </div>
            <div className="p-4 text-center">
              <div className="text-sm text-white/70 italic">
                {welcomeMessage.getSubtitle()}
              </div>
            </div>
          </div>
        )}
        
        <div className={`${isInputAtTop ? 'absolute top-4 left-4 right-4' : 'p-4'}`}>
          <ChatInputField
            inputValue={inputValue}
            setInputValue={setInputValue}
            onKeyPress={handleKeyPress}
            onSend={handleSend}
          />
        </div>
      </div>
    </div>
  );
}
