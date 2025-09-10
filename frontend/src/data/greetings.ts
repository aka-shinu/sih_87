export const getGreeting = () => {
  const hour = new Date().getHours();
  if (hour < 12) return "Good Morning!";
  if (hour < 17) return "Good Afternoon!";
  return "Good Evening!";
};

export const motivationalQuotes = [
  "Every expert was once a beginner.",
  "The only way to do great work is to love what you do.",
  "Success is not final, failure is not fatal.",
  "Believe you can and you're halfway there.",
  "The future belongs to those who believe in their dreams.",
  "Don't watch the clock; do what it does. Keep going.",
  "The way to get started is to quit talking and begin doing.",
  "Innovation distinguishes between a leader and a follower."
];

export const getRandomQuote = () => {
  return motivationalQuotes[Math.floor(Math.random() * motivationalQuotes.length)];
};

// Generate a stable quote that doesn't change on every render
const stableQuote = getRandomQuote();

export const welcomeMessage = {
  getTitle: () => getGreeting(),
  getSubtitle: () => `"${stableQuote}"`,
  getDescription: () => "Start a conversation by typing your message below"
};
