import { FooterProps } from '@/types/components';

export function Footer({ 
  showSocial = true, 
  showCopyright = true,
  className 
}: FooterProps) {
  const socialLinks = [
    { name: 'Twitter', href: '#' },
    { name: 'GitHub', href: '#' },
    { name: 'LinkedIn', href: '#' },
  ];

  const footerLinks = [
    { label: 'Privacy Policy', href: '#' },
    { label: 'Terms of Service', href: '#' },
    { label: 'Contact', href: '#' },
  ];

  return (
    <footer className={`border-t border-slate-700 bg-slate-800/80 ${className}`}>
      <div className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div>
            <h3 className="text-lg font-semibold text-gradient mb-4">Modular App</h3>
            <p className="text-blue-300 text-sm">
              A modern, modular Next.js application with beautiful components and dark blue theme.
            </p>
          </div>
          
          <div>
            <h4 className="font-medium mb-4 text-blue-100">Quick Links</h4>
            <ul className="space-y-2">
              {footerLinks.map((link) => (
                <li key={link.label}>
                  <a
                    href={link.href}
                    className="text-blue-300 hover:text-blue-100 transition-colors text-sm"
                  >
                    {link.label}
                  </a>
                </li>
              ))}
            </ul>
          </div>
          
          {showSocial && (
            <div>
              <h4 className="font-medium mb-4 text-blue-100">Follow Us</h4>
              <div className="flex space-x-4">
                {socialLinks.map((social) => (
                  <a
                    key={social.name}
                    href={social.href}
                    className="text-blue-300 hover:text-blue-100 transition-colors"
                  >
                    {social.name}
                  </a>
                ))}
              </div>
            </div>
          )}
        </div>
        
        {showCopyright && (
          <div className="mt-8 pt-8 border-t border-blue-800 text-center text-sm text-blue-300">
            © 2024 Modular App. All rights reserved.
          </div>
        )}
      </div>
    </footer>
  );
}
