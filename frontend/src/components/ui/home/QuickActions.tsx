"use client";

import { Card } from "@/components/ui/Card";
import { Moon, Search, Users, BookOpen } from "lucide-react";
import { QuickActionsProps } from "@/types/home";

const iconMap = {
  Moon,
  Search,
  Users,
  BookOpen
};

export function QuickActions({ quickActions }: QuickActionsProps) {
  return (
    <div className="mb-6">
      <h2 className="text-xl font-bold text-white mb-3">Quick Actions</h2>
      <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
        {quickActions.map((action) => {
          const IconComponent = iconMap[action.icon as keyof typeof iconMap];
          return (
            <Card key={action.id} className="bg-gray-800/50 border-gray-700 hover:bg-gray-800/70 transition-colors cursor-pointer">
              <div className="p-3 text-center">
                <div className={`w-10 h-10 ${action.color} rounded-lg flex items-center justify-center mx-auto mb-2`}>
                  <IconComponent className="w-5 h-5 text-white" />
                </div>
                <h3 className="font-medium text-white text-xs">{action.title}</h3>
              </div>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
