"use client";

import { Send, HelpCircle } from 'lucide-react';
import { ChatInputFieldProps } from '@/types/components';

export function ChatInputField({ inputValue, setInputValue, onKeyPress, onSend }: ChatInputFieldProps) {
  return (
    <div className="flex items-center gap-3 bg-gray-800/30 backdrop-blur-lg rounded-2xl px-6 py-4 border border-white/10">
      <input
        type="text"
        placeholder="How can I help you today?"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={onKeyPress}
        className="flex-1 bg-transparent text-white placeholder-white/60 outline-none text-sm"
      />
      
      <div className="flex items-center gap-2">
        <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
          <HelpCircle size={16} className="text-white/70" />
        </button>
        
        <button onClick={onSend} className="p-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors">
          <Send size={16} className="text-white/90" />
        </button>
      </div>
    </div>
  );
}
