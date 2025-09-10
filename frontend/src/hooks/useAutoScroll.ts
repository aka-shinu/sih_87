import { useState, useCallback, useRef, RefObject } from 'react';

export function useAutoScroll(containerRef: RefObject<HTMLDivElement | null>) {
  const [isTriggerEnabled, setIsTriggerEnabled] = useState(true);
  const isProgrammaticScroll = useRef(false);

  const scrollToBottom = useCallback(() => {
    if (containerRef.current && isTriggerEnabled) {
      containerRef.current.scrollTo({
        top: containerRef.current.scrollHeight,
        behavior: 'smooth'
      });
    }
  }, [containerRef, isTriggerEnabled]);

  const scrollToBottomNow = useCallback(() => {
    if (containerRef.current) {
      setIsTriggerEnabled(true);
      containerRef.current.scrollTo({
        top: containerRef.current.scrollHeight,
        behavior: 'instant'
      });
    }
  }, [containerRef]);

  const disableTrigger = useCallback(() => {
    setIsTriggerEnabled(false);
  }, []);

  const isProgrammaticScrolling = useCallback(() => {
    return isProgrammaticScroll.current;
  }, []);

  return { 
    scrollToBottom,
    scrollToBottomNow,
    disableTrigger,
    isProgrammaticScrolling,
    isTriggerEnabled
  };
}
