import { h } from 'preact';
import PlaygroundButton from '../ui/PlaygroundButton';


export default function ChatHeader({ status, onClearChat }) {
  const statusConfig = {
    online: { color: 'bg-green-500', text: 'Listo para ayudarte' },
    typing: { color: 'bg-[var(--go-color)]', text: 'Escribiendo...' }
  };

  return (
    <div class="px-4 py-3 sm:px-6 sm:py-4 border-b border-[var(--border)] bg-[var(--bg-secondary)]">
      <div class="flex items-center gap-3">
        <div class="relative flex-shrink-0">
          <div class="w-10 h-10 bg-[var(--go-color)]/10 rounded-full flex items-center justify-center border border-[var(--go-color)]/20">
            <img src="/gopher.svg" alt="Gopher" class="w-6 h-6" />
          </div>
          <div class={`absolute -bottom-0.5 -right-0.5 w-3 h-3 rounded-full border-2 border-[var(--bg-secondary)] ${statusConfig[status]?.color || 'bg-gray-400'} transition-colors`}></div>
        </div>
        <div class="flex-1 min-w-0">
          <h2 class="font-semibold text-base sm:text-lg text-[var(--text-primary)] truncate">Go Tutor Agent</h2>
          <p class="text-xs sm:text-sm text-[var(--text-secondary)] truncate">{statusConfig[status]?.text || 'Cargando...'}</p>
        </div>
        <div class="flex items-center gap-4">

        <PlaygroundButton />

          <button onClick={onClearChat} class="p-2 hover:bg-red-50 dark:hover:bg-red-950 rounded-lg text-[var(--text-secondary)] hover:text-red-500" title="Limpiar conversación">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path></svg>
          </button>

          

          
        </div>
      </div>
    </div>
  );
}