import { 
  TrendingUp, 
  Heart, 
  Brain, 
  Zap, 
  Users, 
  BookOpen,
  Activity,
  Target
} from 'lucide-react';
import { TrendingFeature } from '@/types/trending';

export const trendingTopics = [
  {
    name: "Mindfulness",
    description: "Daily meditation practices and breathing exercises",
    icon: Brain,
    trend: "+15%",
    color: "text-purple-400"
  },
  {
    name: "Sleep Quality",
    description: "Improving rest and recovery patterns",
    icon: Activity,
    trend: "+23%",
    color: "text-blue-400"
  },
  {
    name: "Stress Management",
    description: "Techniques for handling daily pressures",
    icon: Zap,
    trend: "+18%",
    color: "text-yellow-400"
  },
  {
    name: "Emotional Wellness",
    description: "Building emotional intelligence and resilience",
    icon: Heart,
    trend: "+12%",
    color: "text-pink-400"
  }
];

export const trendingFeatures: TrendingFeature[] = [
  {
    Icon: TrendingUp,
    name: "Trending Topics",
    description: "Discover what's popular in wellness this week",
    href: "#",
    cta: "Explore trends",
    className: "w-1/3 h-80",
    background: (
      <div className="absolute inset-0 p-3">
        <div className="grid grid-cols-2 gap-2 h-full">
          {trendingTopics.map((topic, idx) => (
            <div key={idx} className="bg-gray-50 rounded-lg p-2 border border-gray-200">
              <div className="flex items-center gap-1 mb-1">
                <topic.icon className={`h-3 w-3 ${topic.color}`} />
                <span className="text-xs font-medium text-gray-900">{topic.name}</span>
              </div>
              <div className="text-xs text-gray-600 mb-1 line-clamp-2">{topic.description}</div>
              <div className={`text-xs font-semibold ${topic.color}`}>{topic.trend}</div>
            </div>
          ))}
        </div>
      </div>
    ),
  },
  {
    Icon: Users,
    name: "Community Insights",
    description: "See what others are focusing on",
    href: "#",
    cta: "Join community",
    className: "w-2/3 h-80",
    background: (
      <div className="absolute inset-0 p-3">
        <div className="space-y-2">
          <div className="bg-gray-50 rounded-lg p-2 border border-gray-200">
            <div className="text-xs font-medium text-gray-900 mb-1">Active Users</div>
            <div className="text-lg font-bold text-green-500">2,847</div>
            <div className="text-xs text-gray-600">+12% this week</div>
          </div>
          <div className="bg-gray-50 rounded-lg p-2 border border-gray-200">
            <div className="text-xs font-medium text-gray-900 mb-1">Sessions</div>
            <div className="text-lg font-bold text-blue-500">15,234</div>
            <div className="text-xs text-gray-600">+8% this week</div>
          </div>
        </div>
      </div>
    ),
  },
];
