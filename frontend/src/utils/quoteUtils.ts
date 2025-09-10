export function getRandomQuote(quotes: string[]): string {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  return quotes[randomIndex];
}

export function getGreeting(timeOfDay: string): string {
  const greetingMap = {
    morning: 'Good morning',
    afternoon: 'Good afternoon',
    evening: 'Good evening'
  };
  
  return greetingMap[timeOfDay as keyof typeof greetingMap] || 'Hello there';
}
