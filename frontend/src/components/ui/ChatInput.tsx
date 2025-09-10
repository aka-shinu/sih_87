"use client";

import { useState } from 'react';
import { Send, Image, HelpCircle } from 'lucide-react';

export function ChatInput() {
  const [inputValue, setInputValue] = useState('');

  return (
    <div className="absolute bottom-0 left-0 right-0 bg-slate-900/20 backdrop-blur-2xl p-4">
      <div className="max-w-4xl mx-auto">
        <div className="flex items-center gap-3 bg-white/3 backdrop-blur-lg rounded-2xl px-6 py-4 border border-white">
          <input
            type="text"
            placeholder="How can I help you today?"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            className="flex-1 bg-transparent text-white placeholder-white/60 outline-none text-sm"
          />
          
          <div className="flex items-center gap-2">
            <button className="p-2 hover:bg-white/10 rounded-lg transition-colors">
              <HelpCircle size={16} className="text-white/70" />
            </button>
            
            <button className="p-2 bg-white/20 hover:bg-white/30 rounded-lg transition-colors">
              <Send size={16} className="text-white/90" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
