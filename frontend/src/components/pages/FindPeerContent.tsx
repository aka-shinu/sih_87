"use client";

import { Card } from "@/components/ui/Card";
import { Search, Users, MessageCircle } from "lucide-react";

export function FindPeerContent() {
  return (
    <div className="flex w-full h-full bg-[#22273433] backdrop-blur-sm relative p-6 overflow-y-auto">
      <div className="w-full">
        <h1 className="text-3xl font-bold text-white mb-8">Find Peer</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <Search className="w-8 h-8 text-green-400" />
                <h3 className="text-xl font-semibold text-white">Search Peers</h3>
              </div>
              <p className="text-gray-400 mb-4">Find someone with similar interests</p>
            </div>
          </Card>
          <Card className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
            <div className="p-6">
              <div className="flex items-center gap-3 mb-4">
                <Users className="w-8 h-8 text-blue-400" />
                <h3 className="text-xl font-semibold text-white">Active Peers</h3>
              </div>
              <p className="text-gray-400 mb-4">12 people online now</p>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
