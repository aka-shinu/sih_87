"use client";

import { motion } from 'framer-motion';
import { navigationItems } from '@/data/navigation';
import { AnimatedButton } from '@/components/animations/AnimatedButton';
import { AnimatedIcon } from '@/components/animations/AnimatedIcon';
import { useSidebarLabelAnimation } from '@/hooks/useAnimation';
import { useNavigation } from '@/contexts/NavigationContext';

export function Sidebar() {
  const { activeItem, setActiveItem } = useNavigation();
  const { controls, showLabel, hideLabel } = useSidebarLabelAnimation();

  return (
    <div 
      className="w-[5%] bg-black h-screen flex flex-col border-r border-white/10 group/sidebar hover:w-56 transition-all duration-300"
      onMouseEnter={showLabel}
      onMouseLeave={hideLabel}
    >
      <nav className="flex-1 px-2 py-6">
        <ul className="space-y-1">
          {navigationItems.map((item) => {
            const IconComponent = item.icon;
            return (
              <li key={item.id}>
                <AnimatedButton
                  onClick={() => setActiveItem(item.id)}
                  isActive={activeItem === item.id}
                  className={`w-full text-left px-3 py-3 rounded-lg transition-all duration-200 flex items-center gap-5 group ${
                    activeItem === item.id
                      ? 'text-white font-medium'
                      : 'text-white/60 hover:text-white hover:font-normal'
                  }`}
                >
                  <AnimatedIcon isActive={activeItem === item.id}>
                    <motion.div
                      animate={{
                        strokeWidth: activeItem === item.id ? 2.5 : 1.5,
                      }}
                      transition={{
                        type: "spring",
                        stiffness: 400,
                        damping: 25,
                      }}
                    >
                      <IconComponent 
                        size={18} 
                        strokeWidth={activeItem === item.id ? 2.5 : 1.5}
                        className={activeItem === item.id ? 'fill-current' : 'stroke-current fill-none'}
                      />
                    </motion.div>
                  </AnimatedIcon>
                  <motion.span 
                    className="font-normal text-sm tracking-wide whitespace-nowrap"
                    animate={controls}
                    initial={{ opacity: 0, x: -20 }}
                  >
                    {item.label}
                  </motion.span>
                </AnimatedButton>
              </li>
            );
          })}
        </ul>
      </nav>
    </div>
  );
}
