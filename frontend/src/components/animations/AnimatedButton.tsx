"use client";

import { motion } from 'framer-motion';
import { AnimatedButtonProps } from '@/types/components';

export function AnimatedButton({ children, onClick, className, isActive }: AnimatedButtonProps) {
  return (
    <motion.button
      onClick={onClick}
      className={`${className} flex items-center`}
      animate={{
        scale: isActive ? 1.01 : 1,
      }}
      transition={{
        type: "spring",
        stiffness: 300,
        damping: 25,
        mass: 0.8,
      }}
      whileHover={{
        scale: 1.02,
        transition: {
          type: "spring",
          stiffness: 300,
          damping: 20,
        }
      }}
      whileTap={{
        scale: 0.98,
        transition: {
          type: "spring",
          stiffness: 600,
          damping: 40,
        }
      }}
    >
      <motion.div
        className="flex items-center gap-3"
        animate={{
          x: isActive ? 2 : 0,
        }}
        transition={{
          type: "spring",
          stiffness: 400,
          damping: 25,
        }}
      >
        {children}
      </motion.div>
    </motion.button>
  );
}
