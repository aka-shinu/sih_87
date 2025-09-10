import { ReactNode } from 'react';

export interface Card {
  description: string;
  title: string;
  src: string;
  ctaText: string;
  ctaLink: string;
  content: () => ReactNode;
}

export interface ExpandableCardDemoProps {
  cards: Card[];
}
