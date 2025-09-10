"use client";

import { useThinkingAnimation } from '@/hooks/useThinkingAnimation';

export function ThinkingDots() {
  const { dotVariants, dotTransition, motion } = useThinkingAnimation();

  return (
    <div className="flex gap-1">
      {[0, 1, 2].map((index) => (
        <motion.div
          key={index}
          className="w-1 h-1 bg-white/60 rounded-full"
          variants={dotVariants}
          animate="animate"
          transition={dotTransition(index)}
        />
      ))}
    </div>
  );
}
