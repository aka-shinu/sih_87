import { motion } from 'framer-motion';

export const useThinkingAnimation = () => {
  const dotVariants = {
    animate: {
      y: [-1, 1, -1],
    }
  };

  const dotTransition = (index: number) => ({
    duration: 0.9,
    repeat: Infinity,
    delay: index * 0.15,
    ease: "easeInOut" as const
  });

  return {
    dotVariants,
    dotTransition,
    motion
  };
};
