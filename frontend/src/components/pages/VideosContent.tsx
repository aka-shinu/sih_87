"use client";

import { Card } from "@/components/ui/Card";
import { PlayCircle, Clock, Video } from "lucide-react";

export function VideosContent() {
  return (
    <div className="flex w-full h-full bg-[#22273433] backdrop-blur-sm relative p-6 overflow-y-auto">
      <div className="w-full">
        <h1 className="text-3xl font-bold text-white mb-8">Videos</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <Video className="w-8 h-8 text-red-400" />
                <h3 className="text-xl font-semibold text-white">Yoga Flow</h3>
              </div>
              <p className="text-gray-400 mb-4">Beginner-friendly yoga session</p>
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <Clock className="w-4 h-4" />
                <span>30 min</span>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
