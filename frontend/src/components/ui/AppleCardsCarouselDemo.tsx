"use client";

import React from "react";
import { AppleCardsCarousel } from "./AppleCardsCarousel";
import { carouselData } from "@/data/carouselData";

export function AppleCardsCarouselDemo() {
  return (
    <AppleCardsCarousel 
      data={carouselData} 
      title="Get to know your iSad."
      headingClassName="text-center text-blue-600"
      cardWidth="w-64 md:w-80"
      cardHeight="h-72 md:h-96"
    />
  );
}
