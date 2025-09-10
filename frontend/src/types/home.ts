export interface Recommendation {
  id: string;
  title: string;
  type: string;
  duration: string;
  description: string;
  image: string;
  rating: number;
}

export interface RecommendationsSectionProps {
  recommendations: Recommendation[];
}

export interface ContinueItem {
  id: string;
  title: string;
  channel: string;
  progress: number;
  duration: string;
  type: string;
  lastAccessed: string;
  thumbnail: string;
  views: string;
}

export interface ContinueSectionProps {
  continueItems: ContinueItem[];
}

export interface QuickAction {
  id: string;
  title: string;
  icon: string;
  color: string;
  action: string;
}

export interface QuickActionsProps {
  quickActions: QuickAction[];
}

export interface SocialPost {
  id: string;
  user: {
    name: string;
    username: string;
    avatar: string;
  };
  content: string;
  time: string;
  likes: number;
  comments: number;
  type: string;
  image?: string;
  location?: string;
}

export interface SocialFeedProps {
  socialFeed: SocialPost[];
}

export interface PersonalizedFeedItem {
  id: string;
  title: string;
  type: string;
  data?: any;
  items?: string[];
}

export interface PersonalizedFeedProps {
  personalizedFeed: PersonalizedFeedItem[];
}

export interface QuickNavItem {
  id: string;
  title: string;
  description: string;
  icon: string;
  color: string;
  stats: string;
}

export interface QuickNavigationProps {
  quickNavigation: QuickNavItem[];
}

export interface WellnessSession {
  id: string;
  title: string;
  instructor: string;
  thumbnail: string;
  duration: string;
  type: string;
}

export interface WellnessSessionsProps {
  sessions: WellnessSession[];
}
