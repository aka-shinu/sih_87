import { BentoCard, BentoGrid } from "./bento-grid";
import { trendingFeatures } from "@/data/trending";

const TrendingSection = () => (
  <div className="w-full">
    <div className="mb-4">
      <h2 className="text-xl font-semibold text-white font-display tracking-tight mb-1">
        Trending Now
      </h2>
      <p className="text-white/60 text-xs">
        Discover what's popular in wellness this week
      </p>
    </div>
    <BentoGrid>
      {trendingFeatures.map((feature, idx) => (
        <BentoCard 
          key={idx} 
          name={feature.name}
          className={feature.className}
          background={feature.background}
          Icon={feature.Icon}
          description={feature.description}
          href={feature.href}
          cta={feature.cta}
        />
      ))}
    </BentoGrid>
  </div>
);

export { TrendingSection };
