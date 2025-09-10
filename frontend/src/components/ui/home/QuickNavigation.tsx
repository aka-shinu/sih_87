"use client";

import { Card } from "@/components/ui/Card";
import { Moon, Headphones, PlayCircle, Search, Users, BookOpen } from "lucide-react";
import { QuickNavigationProps } from "@/types/home";

const iconMap = {
  Moon,
  Headphones,
  PlayCircle,
  Search,
  Users,
  BookOpen
};

export function QuickNavigation({ quickNavigation }: QuickNavigationProps) {
  return (
    <div className="mb-6">
      <h2 className="text-xl font-bold text-white mb-3">Quick Navigation</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
        {quickNavigation.map((item) => {
          const IconComponent = iconMap[item.icon as keyof typeof iconMap];
          return (
            <Card key={item.id} className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors cursor-pointer group">
              <div className="p-4">
                <div className="flex items-start gap-3">
                  <div className={`w-10 h-10 ${item.color} rounded-lg flex items-center justify-center group-hover:scale-105 transition-transform`}>
                    <IconComponent className="w-5 h-5 text-white" />
                  </div>
                  <div className="flex-1">
                    <h3 className="font-semibold text-white mb-1">{item.title}</h3>
                    <p className="text-sm text-gray-400 mb-2">{item.description}</p>
                    <p className="text-xs text-gray-500">{item.stats}</p>
                  </div>
                </div>
              </div>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
