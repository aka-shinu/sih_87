export const generateAIResponse = async (userMessage: string): Promise<string> => {
  const responses = [
    "I understand you're asking about that. Let me help you with that.",
    "That's a great question! Here's what I think about it.",
    "I can help you with that. Let me break it down for you.",
    "Interesting point! Here's my perspective on this topic.",
    "I'd be happy to assist you with that. Let me provide some insights.",
    "That's a common concern. Here's how I would approach it.",
    "Great question! Let me share some thoughts on this.",
    "I can definitely help you understand this better."
  ];
  
  const randomResponse = responses[Math.floor(Math.random() * responses.length)];
  
  await new Promise(resolve => setTimeout(resolve, 1000 + Math.random() * 2000));
  
  return `${randomResponse} Regarding "${userMessage}", here's what I can tell you: This is a simulated AI response. In a real implementation, this would connect to an actual AI service like OpenAI's API. Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200Lorem200
  `;
};
