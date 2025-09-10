import { ButtonHTMLAttributes, HTMLAttributes, ReactNode } from 'react';

export interface BaseComponentProps {
  className?: string;
  children?: ReactNode;
}

export interface ButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'outline' | 'ghost' | 'destructive' | 'link';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  asChild?: boolean;
}

export interface CardProps extends HTMLAttributes<HTMLDivElement> {
  variant?: 'default' | 'outlined' | 'elevated';
}

export interface HeaderProps extends BaseComponentProps {
  title?: string;
  showNav?: boolean;
  showAuth?: boolean;
}

export interface FooterProps extends BaseComponentProps {
  showSocial?: boolean;
  showCopyright?: boolean;
}

export interface InputProps extends React.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
  variant?: 'default' | 'filled' | 'outlined';
}

export interface BadgeProps extends BaseComponentProps {
  variant?: 'default' | 'secondary' | 'destructive' | 'outline';
  size?: 'sm' | 'md';
}

export interface AvatarProps extends BaseComponentProps {
  src?: string;
  alt?: string;
  size?: 'sm' | 'md' | 'lg' | 'xl';
  fallback?: string;
}

export interface AnimatedIconProps {
  children: ReactNode;
  isActive: boolean;
  size?: number;
}

export interface AnimatedButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode;
  onClick: () => void;
  className: string;
  isActive: boolean;
}

export interface ChatInputFieldProps {
  inputValue: string;
  setInputValue: (value: string) => void;
  onKeyPress: (e: React.KeyboardEvent) => void;
  onSend: () => void;
}

export interface ChatMessage {
  id: string;
  content: string;
  role: 'user' | 'assistant';
  timestamp: Date;
  isPinned?: boolean;
  isStreaming?: boolean;
  parentId?: string;
}

export interface ChatMessageProps {
  message: ChatMessage;
  isStreaming?: boolean;
  containerRef?: React.RefObject<HTMLDivElement | null>;
  firstCalculatedHeight?: number;
  setFirstCalculatedHeight?: (height: number) => void;
}

export interface PinnedMessageProps {
  message: string;
}

export interface StreamingResponseProps {
  content: string;
  isComplete: boolean;
}
