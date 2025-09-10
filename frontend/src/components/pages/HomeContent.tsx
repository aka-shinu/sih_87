"use client";

import { AppleCardsCarousel } from "@/components/ui/AppleCardsCarousel";
import { SlidingContainer } from "@/components/ui/SlidingContainer";
import { carouselData } from "@/data/carouselData";
import { 
  RecommendationsSection, 
  ContinueSection, 
  QuickActions, 
  SocialFeed, 
  QuickNavigation, 
  PersonalizedFeed,
  WellnessSessions
} from "@/components/ui/home";
import { 
  continueItems, 
  quickActions, 
  socialFeed, 
  quickNavigation, 
  personalizedFeed,
  wellnessSessions
} from "@/data/homeData";

export function HomeContent() {
  return (
    <div className="flex w-full h-screen bg-[#22273433] backdrop-blur-sm relative p-4 overflow-y-auto middle-content-scrollbar">
      <div className="pl-4 w-full space-y-6" id="home-content">
        <SlidingContainer>
          <AppleCardsCarousel
            data={carouselData}
            title="Discover Life, Share Happiness."
            headingClassName="text-blue-600 md:text-2xl"
            cardWidth="w-64 md:w-50"
            cardHeight="h-72 md:h-55"
            className="py-2 mb-0"
          />
        </SlidingContainer>
        <RecommendationsSection />
        <SlidingContainer>
          <ContinueSection continueItems={continueItems} />
        </SlidingContainer>
        <SlidingContainer>
          <WellnessSessions sessions={wellnessSessions} />
        </SlidingContainer>
        <SlidingContainer>
          <SocialFeed socialFeed={socialFeed} />
        </SlidingContainer>
      </div>
    </div>
  );
}
