import { h } from 'preact';
import { useSignal } from '@preact/signals';

export default function ChatInput({ disabled, loading, maxLength = 2000, onSendMessage }) {
  const inputValue = useSignal('');

  const handleInput = (e) => {
    inputValue.value = e.currentTarget.value;
  };

  const handleSend = () => {
    if (inputValue.value.trim()) {
      onSendMessage({ detail: { message: inputValue.value.trim() } });
      inputValue.value = '';
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  return (
    <div class="p-4 sm:p-6 border-t border-[var(--border)] bg-[var(--bg-secondary)]">
      <div class="flex items-end gap-3">
        <div class="flex-1 relative">
          <textarea
            value={inputValue.value}
            onInput={handleInput}
            onKeyDown={handleKeyDown}
            placeholder="Escribe tu pregunta sobre Go..."
            maxLength={maxLength}
            disabled={disabled || loading}
            rows="1"
            class="w-full resize-none bg-[var(--bg-primary)] border border-[var(--border)] rounded-xl px-4 py-3 pr-14 text-sm focus:outline-none focus:ring-2 focus:ring-[var(--go-color)]/50 focus:border-[var(--go-color)] transition-all duration-200 min-h-[48px] max-h-36 disabled:opacity-50 disabled:cursor-not-allowed"
            style={{ fieldSizing: 'content' }}
          ></textarea>
        </div>
        <div class="flex-shrink-0">
          <button
            onClick={handleSend}
            disabled={disabled || loading || !inputValue.value.trim()}
            class="w-12 h-12 bg-[var(--go-color)] text-white rounded-xl flex items-center justify-center hover:bg-[var(--go-color)]/90 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-[var(--bg-secondary)] focus:ring-[var(--go-color)]/50 disabled:opacity-50 disabled:cursor-not-allowed"
            title="Enviar mensaje"
          >
            {loading ? (
              <svg class="w-6 h-6 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="m4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            ) : (
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M12 5l7 7-7 7"></path></svg>
            )}
          </button>
        </div>
      </div>
    </div>
  );
}