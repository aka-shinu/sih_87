import { useAnimation } from 'framer-motion';
import { useState, useEffect } from 'react';

export function useHoverAnimation() {
  const controls = useAnimation();

  const handleHoverStart = () => {
    controls.start({
      x: 4,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  const handleHoverEnd = () => {
    controls.start({
      x: 0,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  return { controls, handleHoverStart, handleHoverEnd };
}

export function useIconAnimation() {
  const controls = useAnimation();

  const animateIn = () => {
    controls.start({
      scale: 1.1,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  const animateOut = () => {
    controls.start({
      scale: 1,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  return { controls, animateIn, animateOut };
}

export function useSidebarLabelAnimation() {
  const controls = useAnimation();

  const showLabel = () => {
    controls.start({
      opacity: 1,
      x: 0,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  const hideLabel = () => {
    controls.start({
      opacity: 0,
      x: -20,
      transition: { duration: 0.2, ease: "easeOut" }
    });
  };

  return { controls, showLabel, hideLabel };
}

export function useResizableSidebar() {
  const [isResizing, setIsResizing] = useState(false);
  const [width, setWidth] = useState(50); // percentage

  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    setIsResizing(true);
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (!isResizing) return;
    
    const newWidth = ((window.innerWidth - e.clientX) / window.innerWidth) * 100;
    const clampedWidth = Math.min(Math.max(newWidth, 20), 80); // min 20%, max 80%
    setWidth(clampedWidth);
  };

  const handleMouseUp = () => {
    setIsResizing(false);
  };

  useEffect(() => {
    if (isResizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none';
    }

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      document.body.style.cursor = '';
      document.body.style.userSelect = '';
    };
  }, [isResizing]);

  return { width, isResizing, handleMouseDown };
}