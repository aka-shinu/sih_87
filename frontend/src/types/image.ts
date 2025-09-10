// Image-related type definitions for webpack compatibility
export interface ImageProps {
  height?: number;
  width?: number;
  src?: string;
  className?: string;
  alt?: string;
  fill?: boolean;
  blurDataURL?: string;
  [key: string]: any;
}
