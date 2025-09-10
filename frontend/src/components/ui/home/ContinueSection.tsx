"use client";

import { ContinueSectionProps } from "@/types/home";

export function ContinueSection({ continueItems }: ContinueSectionProps) {
  return (
    <div className="pl-4 mb-8">
      <div className="flex items-center justify-between mb-8">
        <h2 className="text-2xl font-bold text-white">Continue Where You Left Off</h2>
        <button className="text-blue-400 hover:text-blue-300 text-sm font-medium transition-colors">
          View all
        </button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {continueItems.map((item) => (
          <div key={item.id} className="group cursor-pointer h-full">
            <div className="relative bg-gray-800/30 rounded-xl overflow-hidden hover:bg-gray-800/50 transition-all duration-300 transform hover:scale-[1.02] hover:shadow-xl h-full flex flex-col">
              <div className="relative flex-shrink-0">
                <img 
                  src={item.thumbnail} 
                  alt={item.title}
                  className="w-full h-48 object-cover transition-transform duration-300 group-hover:scale-105"
                />
                <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-all duration-300 flex items-center justify-center">
                  <div className="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <div className="w-12 h-12 bg-white/90 rounded-full flex items-center justify-center shadow-lg">
                      <div className="w-0 h-0 border-l-[8px] border-l-black border-y-[6px] border-y-transparent ml-1"></div>
                    </div>
                  </div>
                </div>
                <div className="absolute bottom-3 right-3 bg-black/90 text-white text-xs font-medium px-2 py-1 rounded">
                  {item.duration}
                </div>
                <div className="absolute bottom-0 left-0 right-0 h-1.5 bg-gray-700/50">
                  <div 
                    className="h-full bg-red-500 transition-all duration-500 ease-out"
                    style={{ width: `${item.progress}%` }}
                  />
                </div>
                <div className="absolute bottom-0 left-0 right-0 h-1.5 bg-gradient-to-r from-red-500/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
              </div>
              <div className="p-4 flex-1 flex flex-col">
                <h3 className="font-semibold text-white text-sm leading-tight line-clamp-2 mb-3 group-hover:text-blue-300 transition-colors min-h-[2.5rem]">
                  {item.title}
                </h3>
                <div className="flex items-center gap-2 mb-3">
                  <div className="w-6 h-6 bg-gradient-to-br from-blue-400 to-purple-500 rounded-full flex items-center justify-center flex-shrink-0">
                    <span className="text-white text-xs font-bold">
                      {item.channel.charAt(0)}
                    </span>
                  </div>
                  <p className="text-gray-400 text-xs font-medium truncate">{item.channel}</p>
                </div>
                <div className="flex space-x-1 text-xs text-gray-500 mt-auto">
                  <span className="truncate">{item.views}</span>
                  <span className="text-[90%]">•</span>
                  <span className="truncate">{item.lastAccessed}</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}