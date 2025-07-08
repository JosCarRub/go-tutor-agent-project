import { h } from 'preact';

export default function ChatMessage({ type, content, timestamp, isCode, language, isTyping = false }) {
  const baseBubbleClasses = "relative px-3 py-2 sm:px-4 sm:py-3 rounded-2xl shadow-sm";
  const typeClasses = {
    user: `bg-[var(--go-color-dark)] text-white rounded-br-lg`,
    assistant: `bg-[var(--bg-primary)] text-[var(--text-primary)] rounded-bl-lg border border-[var(--border)]`,
    system: `bg-transparent text-[var(--text-secondary)] text-center text-xs w-full`
  };
  const messageClasses = `${baseBubbleClasses} ${typeClasses[type]}`;

  return (
    <div class={`flex gap-2 sm:gap-3 w-full ${type === 'user' ? 'justify-end' : 'justify-start'} ${type === 'system' ? 'justify-center' : ''}`}>
      {type === 'assistant' && (
        <div class="flex-shrink-0 order-first self-end">
          <div class="w-8 h-8 bg-[var(--go-color)]/10 rounded-full flex items-center justify-center border border-[var(--go-color)]/20">
            <img src="/gopher.svg" alt="Gopher" class="w-5 h-5" />
          </div>
        </div>
      )}
      <div class={`flex flex-col max-w-[85%] sm:max-w-md md:max-w-lg ${type === 'user' ? 'items-end' : 'items-start'}`}>
        <div class={messageClasses}>
          {isTyping ? (
            <div class="flex items-center gap-1 p-2">
              <div class="w-2 h-2 bg-[var(--text-secondary)] rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
              <div class="w-2 h-2 bg-[var(--text-secondary)] rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
              <div class="w-2 h-2 bg-[var(--text-secondary)] rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
            </div>
          ) : isCode ? (
            <div class="bg-black/80 dark:bg-black/50 rounded-lg overflow-hidden my-1 text-left">
              <div class="flex items-center justify-between px-3 py-1.5 bg-white/10">
                <span class="text-xs font-medium text-gray-300 uppercase">{language}</span>
              </div>
              <pre class="p-3 text-sm overflow-x-auto"><code class={`language-${language}`}>{content}</code></pre>
            </div>
          ) : (
            <div class="text-sm leading-relaxed whitespace-pre-wrap" dangerouslySetInnerHTML={{ __html: content }}></div>
          )}
        </div>
        {type !== 'system' && !isTyping && (
          <div class="text-xs text-[var(--text-secondary)] mt-1.5 px-1">{timestamp}</div>
        )}
      </div>
    </div>
  );
}