export interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
}

export interface Theme {
  mode: 'light' | 'dark';
  primary: string;
  secondary: string;
}

export interface ComponentProps {
  className?: string;
  children?: React.ReactNode;
}

export * from './image';