export interface CarouselProps {
  items: JSX.Element[];
  initialScroll?: number;
}

export type Card = {
  src: string;
  title: string;
  category: string;
  content: React.ReactNode;
};

export interface CarouselContextType {
  onCardClose: (index: number) => void;
  currentIndex: number;
}

export interface CardProps {
  card: Card;
  index: number;
  layout?: boolean;
  cardWidth?: string;
  cardHeight?: string;
}

export interface AppleCardsCarouselProps {
  data: Card[];
  title?: string;
  className?: string;
  headingClassName?: string;
  cardWidth?: string;
  cardHeight?: string;
}
