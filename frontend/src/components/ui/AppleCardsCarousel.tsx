"use client";

import React from "react";
import { Carousel, Card } from "./apple_carousel";
import { AppleCardsCarouselProps } from "@/types/carousel";

export function AppleCardsCarousel({ 
  data, 
  title, 
  className, 
  headingClassName, 
  cardWidth, 
  cardHeight 
}: AppleCardsCarouselProps) {
  const cards = data.map((card, index) => (
    <Card 
      key={card.src} 
      card={card} 
      index={index} 
      layout={true} 
      cardWidth={cardWidth}
      cardHeight={cardHeight}
    />
  ));

  return (
    <div className={`w-full pl-4 h-fit py-5 ${className || ""}`}>
      {title && (
        <h2 className={`max-w-7xl    text-xl md:text-5xl font-bold text-neutral-800 dark:text-neutral-200 font-sans ${headingClassName || ""}`}>
          {title}
        </h2>
      )}
      <Carousel items={cards} />
    </div>
  );
}
