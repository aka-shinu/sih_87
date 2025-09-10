"use client";

import { Card } from "@/components/ui/Card";
import { PlayCircle, Clock, Heart } from "lucide-react";

export function RelaxContent() {
  return (
    <div className="flex w-full h-full bg-[#22273433] backdrop-blur-sm relative p-6 overflow-y-auto">
      <div className="w-full">
        <h1 className="text-3xl font-bold text-white mb-8">Relax & Meditate</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <PlayCircle className="w-8 h-8 text-purple-400" />
                <h3 className="text-xl font-semibold text-white">Guided Meditation</h3>
              </div>
              <p className="text-gray-400 mb-4">10-minute breathing exercise</p>
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <Clock className="w-4 h-4" />
                <span>10 min</span>
              </div>
            </div>
          </Card>
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <Heart className="w-8 h-8 text-red-400" />
                <h3 className="text-xl font-semibold text-white">Stress Relief</h3>
              </div>
              <p className="text-gray-400 mb-4">Progressive muscle relaxation</p>
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <Clock className="w-4 h-4" />
                <span>15 min</span>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
