import { forwardRef } from 'react';
import { cn } from '@/lib/utils';
import { BadgeProps } from '@/types/components';

const Badge = forwardRef<HTMLDivElement, BadgeProps>(
  ({ className, variant = 'default', size = 'md', children, ...props }, ref) => {
    const variantStyles = {
      default: 'bg-blue-600 text-white',
      secondary: 'bg-blue-900 text-blue-100',
      destructive: 'bg-red-600 text-white',
      outline: 'border border-blue-800 text-blue-100',
    };

    const sizeStyles = {
      sm: 'px-2 py-1 text-xs',
      md: 'px-2.5 py-0.5 text-sm',
    };

    return (
      <div
        ref={ref}
        className={cn(
          'inline-flex items-center rounded-full font-medium transition-colors',
          variantStyles[variant],
          sizeStyles[size],
          className
        )}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Badge.displayName = 'Badge';

export { Badge };
