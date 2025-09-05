import React from 'react';
import { createRoot } from 'react-dom/client';
import AITestDashboard from './components/AITestDashboard';
import './styles/main.css';

const container = document.getElementById('ai-test-root');
const root = createRoot(container);
root.render(<AITestDashboard />);
