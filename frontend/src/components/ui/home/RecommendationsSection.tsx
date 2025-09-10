"use client";

import { ExpandableCardWrapper } from "@/components/ui/ExpandableCardWrapper";
import { recommendations } from "@/data/homeData";

export function RecommendationsSection() {
  const expandableCards = recommendations.map(item => ({
    description: item.type,
    title: item.title,
    src: item.image,
    ctaText: "Start",
    ctaLink: "#",
    content: () => (
      <div>
        <div className="flex items-center gap-2 mb-4">
          <span className="text-yellow-400">★</span>
          <span className="text-sm text-gray-300">{item.rating}</span>
        </div>
        <p className="text-gray-300 mb-4">{item.description}</p>
        <div className="text-sm text-gray-400">
          Duration: {item.duration}
        </div>
      </div>
    )
  }));

  return (
    <div className="pl-4 mb-8 ">
      <h2 className="text-2xl font-bold text-white mb-8">Recommended for You</h2>
      <div className="scale-90 origin-top-left">
        <ExpandableCardWrapper cards={expandableCards} />
      </div>
    </div>
  );
}
