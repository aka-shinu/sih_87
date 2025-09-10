import { forwardRef } from 'react';
import { cn } from '@/lib/utils';
import { InputProps } from '@/types/components';

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ className, label, error, helperText, variant = 'default', ...props }, ref) => {
    const variantStyles = {
      default: 'border-blue-800 bg-blue-950/50',
      filled: 'border-transparent bg-blue-900/30',
      outlined: 'border-2 border-blue-800 bg-transparent',
    };

    return (
      <div className="space-y-2">
        {label && (
          <label className="text-sm font-medium text-blue-100">
            {label}
          </label>
        )}
        <input
          className={cn(
            'flex h-10 w-full rounded-md px-3 py-2 text-sm text-blue-100 file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-blue-400 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50',
            variantStyles[variant],
            error && 'border-red-500 focus-visible:ring-red-500',
            className
          )}
          ref={ref}
          {...props}
        />
        {error && (
          <p className="text-sm text-red-400">{error}</p>
        )}
        {helperText && !error && (
          <p className="text-sm text-blue-400">{helperText}</p>
        )}
      </div>
    );
  }
);

Input.displayName = 'Input';

export { Input };
