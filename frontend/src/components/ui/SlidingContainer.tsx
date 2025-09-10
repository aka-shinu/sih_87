"use client";

import { motion } from 'framer-motion';
import { useExpandableCardContext } from '@/contexts/ExpandableCardContext';

interface SlidingContainerProps {
  children: React.ReactNode;
  className?: string;
  excludeFromSliding?: boolean;
}

export function SlidingContainer({ children, className = "", excludeFromSliding = false }: SlidingContainerProps) {
  const { isExpanded } = useExpandableCardContext();

  if (excludeFromSliding) {
    return <div className={className}>{children}</div>;
  }

  return (
    <motion.div
      animate={{
        scale: isExpanded ? 0.95 : 1,
        opacity: isExpanded ? 0.3 : 1,
        y: isExpanded ? -20 : 0,
      }}
      style={{
        zIndex: isExpanded ? -1 : "auto",
        position:  "relative",
      }}
      transition={{ duration: 0.3, ease: "easeInOut" }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
