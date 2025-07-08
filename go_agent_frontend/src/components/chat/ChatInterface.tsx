
import { useSignal, useSignalEffect } from "@preact/signals";
import { h } from 'preact';
import type { FunctionComponent } from 'preact';

import ChatHeader from './ChatHeader.jsx';
import ChatMessage from './ChatMessage.jsx';
import ChatInput from './ChatInput.jsx';
import type { Message } from '../../lib/types';

interface ChatInterfaceProps {
  apiEndpoint: string;
}

const ChatInterface: FunctionComponent<ChatInterfaceProps> = ({ apiEndpoint }) => {
  const messages = useSignal<Message[]>([
    {
      id: 'welcome-1',
      type: 'assistant',
      content: '¡Hola! Soy <strong>Go Tutor Agent</strong><span class="text-[var(--go-color)]">.</span> <br><br>Estoy equipado con un conjunto de herramientas inteligentes que me permiten adaptarme a lo que necesites.<br><br>¡Si quieres escribir código para que lo ejecute puedes utilizar nuestro editor de código embebido!<br><br>',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    }
  ]);
  const isAssistantTyping = useSignal(false);
  const currentTypewriterRef = useSignal<NodeJS.Timeout | null>(null);

  // Función para limpiar el typewriter activo
  const clearCurrentTypewriter = () => {
    if (currentTypewriterRef.value) {
      clearInterval(currentTypewriterRef.value);
      currentTypewriterRef.value = null;
    }
  };

  const simulateTyping = (fullText: string, messageId: string) => {

    clearCurrentTypewriter();

    // streaming
    const CHARS_PER_CHUNK = 1; // Caracteres por "chunk"
    const BASE_DELAY = 30; // Delay base en ms
    const PUNCTUATION_DELAY = 150; // Delay extra para puntuación
    const WORD_DELAY = 80; // Delay extra entre palabras

    let currentIndex = 0;
    const totalLength = fullText.length;

    const typeNextChunk = () => {
      if (currentIndex >= totalLength) {

        clearCurrentTypewriter();
        isAssistantTyping.value = false;
        return;
      }

      const endIndex = Math.min(currentIndex + CHARS_PER_CHUNK, totalLength);
      const nextChunk = fullText.slice(0, endIndex);
      
      messages.value = messages.value.map(msg => 
        msg.id === messageId 
          ? { ...msg, content: nextChunk }
          : msg
      );

      // Calcular el delay dinámico basado en el carácter actual
      let delay = BASE_DELAY;
      const currentChar = fullText[currentIndex];
      
      if (['.', '!', '?', ';'].includes(currentChar)) {
        delay += PUNCTUATION_DELAY;
      } else if ([',', ':'].includes(currentChar)) {
        delay += PUNCTUATION_DELAY / 2;
      } else if (currentChar === ' ') {
        delay += WORD_DELAY;
      }

      delay += Math.random() * 20 - 10; // ±10ms de variación
      
      currentIndex = endIndex;
      
      // Programar el siguiente chunk
      currentTypewriterRef.value = setTimeout(typeNextChunk, Math.max(delay, 10));
    };

    // Iniciar el streaming
    typeNextChunk();
  };

  const handleSendMessage = async (event: CustomEvent) => {
    const userMessageText = event.detail.message;
    if (!userMessageText || isAssistantTyping.value) return;

    clearCurrentTypewriter();

    const userMessage: Message = {
      id: crypto.randomUUID(),
      type: 'user',
      content: userMessageText,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    };
    messages.value = [...messages.value, userMessage];
    isAssistantTyping.value = true;

    const assistantMessageId = crypto.randomUUID();

    try {

      const response = await fetch(apiEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ userPrompt: userMessageText }),
      });

      if (!response.ok) {
        throw new Error(`Error del servidor: ${response.status}`);
      }

      const data = await response.json();
      let fullText = data.agentResponse || 'No se recibió una respuesta válida.';

     
      fullText = fullText.trim();

      await new Promise(resolve => setTimeout(resolve, 300 + Math.random() * 500));

     
      const assistantMessage: Message = {
        id: assistantMessageId,
        type: 'assistant',
        content: '',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      messages.value = [...messages.value, assistantMessage];

      
      simulateTyping(fullText, assistantMessageId);

    } catch (error) {
      console.error("Error al conectar con el backend:", error);
      clearCurrentTypewriter();
      
      
      const errorMessage: Message = {
        id: assistantMessageId,
        type: 'system',
        content: 'No se pudo conectar con el tutor. Por favor, inténtalo de nuevo más tarde.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
      };
      messages.value = [...messages.value, errorMessage];
      isAssistantTyping.value = false;
    }
  };

  const handleClearChat = () => {
    if (messages.value.length > 1 && confirm('¿Estás seguro de que quieres limpiar la conversación?')) {
      
      clearCurrentTypewriter();
      isAssistantTyping.value = false;
      messages.value = [messages.value[0]];
    }
  };

  
  useSignalEffect(() => {
    const container = document.querySelector('#messages-container-id');
    if (container) {
      
      container.scrollTo({
        top: container.scrollHeight,
        behavior: isAssistantTyping.value ? 'smooth' : 'auto'
      });
    }
  });

  
  useSignalEffect(() => {
    return () => {
      clearCurrentTypewriter();
    };
  });

  return (
    <div class="w-full max-w-3xl mx-auto">
      <div class="bg-[var(--bg-secondary)] rounded-xl shadow-lg border border-[var(--border)] overflow-hidden flex flex-col h-[70vh] max-h-[700px]">
        <ChatHeader 
          status={isAssistantTyping.value ? 'typing' : 'online'}
          onClearChat={handleClearChat}
        />
        <div id="messages-container-id" class="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
          {messages.value.map((msg) => (
            <ChatMessage {...msg} key={msg.id} />
          ))}
          
          {isAssistantTyping.value && 
           messages.value[messages.value.length - 1]?.type !== 'assistant' && (
            <ChatMessage type="assistant" isTyping={true} />
          )}
        </div>
        <ChatInput 
          disabled={isAssistantTyping.value}
          loading={isAssistantTyping.value}
          onSendMessage={handleSendMessage}
        />
      </div>
    </div>
  );
}

export default ChatInterface;