export interface Message {
    id: string;
    type: 'user' | 'assistant' | 'system';
    content: string;
    timestamp: string;
    isCode?: boolean;
    language?: string;
  }