import { useEffect, useRef, useState } from 'react';
import { useOutsideClick } from './useOutsideClick';
import { useExpandableCardContext } from '@/contexts/ExpandableCardContext';
import { Card } from '@/types/expandableCard';

export function useExpandableCardWithContext() {
  const [active, setActive] = useState<Card | boolean | null>(null);
  const { setIsExpanded } = useExpandableCardContext();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setIsExpanded(active !== null && typeof active === 'object');
  }, [active, setIsExpanded]);

  useEffect(() => {
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setActive(false);
      }
    }

    if (active && typeof active === "object") {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "auto";
    }

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, [active]);

  useOutsideClick(ref, () => setActive(null));

  return { active, setActive, ref };
}

