import { Button } from '@/components/ui/Button';
import { HeaderProps } from '@/types/components';

export function Header({ 
  title = "Modular App", 
  showNav = true, 
  showAuth = true,
  className 
}: HeaderProps) {
  const navItems = [
    { label: 'Home', href: '#' },
    { label: 'About', href: '#' },
    { label: 'Contact', href: '#' },
  ];

  return (
    <header className={`border-b border-slate-700 bg-slate-800/80 backdrop-blur-sm ${className}`}>
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <h1 className="text-2xl font-bold text-gradient">{title}</h1>
          </div>
          
          {showNav && (
            <nav className="hidden md:flex items-center space-x-6">
              {navItems.map((item) => (
                <a
                  key={item.label}
                  href={item.href}
                  className="text-slate-300 hover:text-white transition-colors"
                >
                  {item.label}
                </a>
              ))}
            </nav>
          )}
          
          {showAuth && (
            <div className="flex items-center space-x-2">
              <Button variant="ghost" size="sm">
                Sign In
              </Button>
              <Button size="sm">
                Get Started
              </Button>
            </div>
          )}
        </div>
      </div>
    </header>
  );
}
