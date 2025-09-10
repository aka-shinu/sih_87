import { forwardRef } from 'react';
import { cn } from '@/lib/utils';
import { ButtonProps } from '@/types/components';

const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = 'primary', size = 'md', loading, asChild, children, ...props }, ref) => {
    const baseStyles = 'inline-flex items-center justify-center rounded-md font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:opacity-50 disabled:pointer-events-none';
    
    const variantStyles = {
      primary: 'bg-blue-600 text-white hover:bg-blue-700',
      secondary: 'bg-blue-900 text-blue-100 hover:bg-blue-800',
      outline: 'border border-blue-800 hover:bg-blue-600 hover:text-white',
      ghost: 'hover:bg-blue-600 hover:text-white',
      destructive: 'bg-red-600 text-white hover:bg-red-700',
      link: 'text-blue-600 underline-offset-4 hover:underline',
    };
    
    const sizeStyles = {
      sm: 'h-9 px-3 text-sm',
      md: 'h-10 px-4 py-2',
      lg: 'h-11 px-8 text-lg',
    };

    if (asChild) {
      return (
        <span
          className={cn(
            baseStyles,
            variantStyles[variant],
            sizeStyles[size],
            className
          )}
        >
          {children}
        </span>
      );
    }

    return (
      <button
        className={cn(
          baseStyles,
          variantStyles[variant],
          sizeStyles[size],
          className
        )}
        ref={ref}
        disabled={loading || props.disabled}
        {...props}
      >
        {loading && <div className="mr-2 h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent" />}
        {children}
      </button>
    );
  }
);

Button.displayName = 'Button';

export { Button };
