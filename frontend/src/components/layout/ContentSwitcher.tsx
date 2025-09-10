"use client";

import { useNavigation } from "@/contexts/NavigationContext";
import { HomeContent } from "@/components/pages/HomeContent";
import { RelaxContent } from "@/components/pages/RelaxContent";
import { PodcastsContent } from "@/components/pages/PodcastsContent";
import { VideosContent } from "@/components/pages/VideosContent";
import { FindPeerContent } from "@/components/pages/FindPeerContent";
import { CommunityContent } from "@/components/pages/CommunityContent";
import { ResourcesContent } from "@/components/pages/ResourcesContent";

export function ContentSwitcher() {
  const { activeItem } = useNavigation();

  switch (activeItem) {
    case 'home':
      return <HomeContent />;
    case 'relax':
      return <RelaxContent />;
    case 'podcasts':
      return <PodcastsContent />;
    case 'videos':
      return <VideosContent />;
    case 'find-peer':
      return <FindPeerContent />;
    case 'community':
      return <CommunityContent />;
    case 'resources':
      return <ResourcesContent />;
    default:
      return <HomeContent />;
  }
}
