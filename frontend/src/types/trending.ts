import { ReactNode } from "react";

export interface TrendingFeature {
  Icon: React.ComponentType<any>;
  name: string;
  description: string;
  href: string;
  cta: string;
  className: string;
  background: ReactNode;
}


