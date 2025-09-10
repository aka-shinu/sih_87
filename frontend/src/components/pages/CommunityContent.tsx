"use client";

import { Card } from "@/components/ui/Card";
import { Users, MessageCircle, Heart } from "lucide-react";

export function CommunityContent() {
  return (
    <div className="flex w-full h-full bg-[#22273433] backdrop-blur-sm relative p-6 overflow-y-auto">
      <div className="w-full">
        <h1 className="text-3xl font-bold text-white mb-8">Community</h1>
        <div className="space-y-4">
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-start gap-4">
                <div className="w-10 h-10 bg-blue-500 rounded-full flex items-center justify-center">
                  <Users className="w-5 h-5 text-white" />
                </div>
                <div className="flex-1">
                  <h3 className="font-semibold text-white mb-2">Daily Check-in</h3>
                  <p className="text-gray-400 mb-3">How are you feeling today?</p>
                  <div className="flex items-center gap-4">
                    <button className="flex items-center gap-2 text-gray-400 hover:text-red-400 transition-colors">
                      <Heart className="w-4 h-4" />
                      <span className="text-sm">24</span>
                    </button>
                    <button className="flex items-center gap-2 text-gray-400 hover:text-blue-400 transition-colors">
                      <MessageCircle className="w-4 h-4" />
                      <span className="text-sm">8</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
