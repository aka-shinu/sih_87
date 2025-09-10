"use client";

import { WellnessSessionsProps } from "@/types/home";

export function WellnessSessions({ sessions }: WellnessSessionsProps) {
  return (
    <div className="mb-8 pl-4">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-2xl font-bold text-white">Wellness Sessions</h2>
        <button className="text-blue-400 hover:text-blue-300 text-sm font-medium transition-colors">
          View all
        </button>
      </div>
      <div className="space-y-2">
        {sessions.map((session) => (
          <div key={session.id} className="flex items-center gap-4 p-4 rounded-2xl bg-gray-800/30 hover:bg-gray-800/50 transition-all duration-300 group hover:shadow-lg hover:scale-[1.01]">
            <div className="relative flex-shrink-0">
              <img 
                src={session.thumbnail} 
                alt={session.title}
                className="w-16 h-16 rounded-xl object-cover ring-2 ring-gray-700 group-hover:ring-blue-500 transition-all duration-300"
              />
              <div className="absolute inset-0 bg-black/20 rounded-xl flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                <div className="w-10 h-10 bg-white/95 rounded-full flex items-center justify-center shadow-lg">
                  <div className="w-0 h-0 border-l-[8px] border-l-black border-y-[6px] border-y-transparent ml-1"></div>
                </div>
              </div>
              <div className="absolute -top-1 -right-1 w-4 h-4 bg-green-500 rounded-full border-2 border-gray-800"></div>
            </div>
            <div className="flex-1 min-w-0">
              <h3 className="font-bold text-white text-base truncate mb-1 group-hover:text-blue-300 transition-colors">{session.title}</h3>
              <p className="text-gray-400 text-sm truncate mb-2">{session.instructor}</p>
              <div className="flex items-center gap-2">
                <span className="text-xs text-gray-400 font-medium">{session.duration}</span>
                <span className="text-[50%] text-gray-500">•</span>
                <span className="text-xs text-gray-500 capitalize">{session.type}</span>
              </div>
            </div>
            <button className="bg-white text-black px-6 py-2.5 rounded-full text-sm font-semibold hover:bg-gray-200 hover:scale-105 transition-all duration-200 flex-shrink-0 shadow-md">
              Start
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
