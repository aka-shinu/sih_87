"use client";

import { motion } from 'framer-motion';
import { AnimatedIconProps } from '@/types/components';

export function AnimatedIcon({ children, isActive, size = 22 }: AnimatedIconProps) {
  return (
    <motion.div
      className="flex-shrink-0"
      animate={{
        scale: isActive ? 1.05 : 1,
        rotate: isActive ? 3 : 0,
      }}
      transition={{
        type: "spring",
        stiffness: 400,
        damping: 25,
        mass: 0.8,
      }}
      whileHover={{
        scale: 1.1,
        rotate: 5,
        transition: {
          type: "spring",
          stiffness: 400,
          damping: 25,
        }
      }}
      whileTap={{
        scale: 0.95,
        transition: {
          type: "spring",
          stiffness: 600,
          damping: 40,
        }
      }}
    >
      <motion.div
        animate={{
          opacity: isActive ? 1 : 0.7,
        }}
        transition={{
          duration: 0.3,
          ease: "easeInOut",
        }}
      >
        {children}
      </motion.div>
    </motion.div>
  );
}
