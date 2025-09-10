"use client";

import { Card } from "@/components/ui/Card";
import { TrendingUp, Calendar, BarChart3 } from "lucide-react";
import { PersonalizedFeedProps } from "@/types/home";

const iconMap = {
  progress: BarChart3,
  trending: TrendingUp,
  events: Calendar
};

export function PersonalizedFeed({ personalizedFeed }: PersonalizedFeedProps) {
  return (
    <div className="mb-6">
      <h2 className="text-xl font-bold text-white mb-3">Personalized Feed</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
        {personalizedFeed.map((item) => {
          const IconComponent = iconMap[item.type as keyof typeof iconMap];
          return (
            <Card key={item.id} className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors">
              <div className="p-3">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-8 h-8 bg-blue-500 rounded-lg flex items-center justify-center">
                    <IconComponent className="w-4 h-4 text-white" />
                  </div>
                  <h3 className="font-semibold text-white">{item.title}</h3>
                </div>
                {item.type === 'progress' && item.data && (
                  <div className="space-y-2">
                    {Object.entries(item.data).map(([key, value]) => (
                      <div key={key} className="flex justify-between items-center">
                        <span className="text-sm text-gray-400 capitalize">{key}</span>
                        <span className="text-sm text-white font-medium">{String(value)}</span>
                      </div>
                    ))}
                  </div>
                )}
                {item.items && (
                  <div className="space-y-2">
                    {item.items.map((listItem, index) => (
                      <div key={index} className="text-sm text-gray-300 flex items-center gap-2">
                        <div className="w-1.5 h-1.5 bg-blue-400 rounded-full" />
                        {listItem}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
