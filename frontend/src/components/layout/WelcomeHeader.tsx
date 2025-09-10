"use client";

import { useState, useEffect } from 'react';
import { motivationalQuotes, greetings } from '@/data/quotes';
import { getRandomQuote, getGreeting } from '@/utils/quoteUtils';
import { useTimeOfDay } from '@/hooks/useTimeOfDay';

export function WelcomeHeader() {
  const [quote, setQuote] = useState('');
  const timeOfDay = useTimeOfDay();

  useEffect(() => {
    setQuote(getRandomQuote(motivationalQuotes));
  }, []);

  const greeting = getGreeting(timeOfDay);

  return (
    <header className="bg-gradient-to-r from-blue-600 to-purple-600 py-4 px-4">
      <div className="max-w-6xl mx-auto">
        <div className="flex items-center justify-between">
          <h1 className="text-xl font-semibold text-white">
            {greeting}! How are you feeling today?
          </h1>
          <div className="bg-white/20 rounded-lg p-3 max-w-md">
            <p className="text-white text-sm italic">
              "{quote}"
            </p>
          </div>
        </div>
      </div>
    </header>
  );
}
