import { useState, useEffect, useRef } from 'react';
import { useOutsideClick } from '@/hooks/useOutsideClick';

export function useCardModal() {
  const [open, setOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        handleClose();
      }
    }

    if (typeof window !== 'undefined') {
      if (open) {
        document.body.style.overflow = "hidden";
      } else {
        document.body.style.overflow = "auto";
      }

      window.addEventListener("keydown", onKeyDown);
      return () => window.removeEventListener("keydown", onKeyDown);
    }
  }, [open]);

  useOutsideClick(containerRef, () => handleClose());

  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return { open, containerRef, handleOpen, handleClose };
}

export function useImageLoading() {
  const [isLoading, setLoading] = useState(true);
  
  const handleLoad = () => setLoading(false);
  
  return { isLoading, handleLoad };
}
