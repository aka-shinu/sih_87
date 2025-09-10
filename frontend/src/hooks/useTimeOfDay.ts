import { useState, useEffect } from 'react';

export function useTimeOfDay() {
  const [timeOfDay, setTimeOfDay] = useState('morning');

  useEffect(() => {
    const hour = new Date().getHours();
    
    if (hour < 12) {
      setTimeOfDay('morning');
    } else if (hour < 17) {
      setTimeOfDay('afternoon');
    } else {
      setTimeOfDay('evening');
    }
  }, []);

  return timeOfDay;
}
