import { 
  Home, 
  Moon, 
  BookOpen, 
  Users, 
  Search,
  Headphones,
  PlayCircle
} from 'lucide-react';

export const navigationItems = [
  { id: 'home', label: 'Home', icon: Home },
  { id: 'relax', label: 'Relax', icon: Moon },
  { id: 'podcasts', label: 'Podcasts', icon: Headphones },
  { id: 'videos', label: 'Videos', icon: PlayCircle },
  { id: 'find-peer', label: 'Find Peer', icon: Search },
  { id: 'community', label: 'Community', icon: Users },
  { id: 'resources', label: 'Resources', icon: BookOpen },
];

export const userProfile = {
  name: 'Alex',
  username: '@alex_wellness',
  avatar: '/api/placeholder/40/40'
};
