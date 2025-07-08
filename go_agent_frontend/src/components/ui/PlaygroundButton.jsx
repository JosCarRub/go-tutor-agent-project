import { h } from 'preact';

export default function PlaygroundButton() {
  return (
    <>
      <style>{`
        .playground-btn-unified {
          position: relative;
          width: 30px; /* w-12 */
          height: 30px; /* h-12 */
          background-color: var(--bg-primary);
          border: 0.5px solid var(--go-color); 
          border-radius: 0.92rem; /* rounded-xl */
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
          transition: all 0.3s ease-in-out;

          box-shadow: 0 2px 8px rgba(0,0,0,0.1), inset 0 1px 2px rgba(0,0,0,0.05);
          /* Animación de pulso sutil */
          animation: subtle-pulse 3s ease-in-out infinite;
        }

        .dark .playground-btn-unified {
          box-shadow: 0 2px 8px rgba(0,0,0,0.3), inset 0 1px 2px rgba(0,0,0,0.2);
        }

        /* Animación de pulso sutil */
        @keyframes subtle-pulse {
          0%, 100% { 
            transform: scale(1);
            box-shadow: 0 2px 8px rgba(0,0,0,0.1), inset 0 1px 2px rgba(0,0,0,0.05);
          }
          50% { 
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15), inset 0 1px 2px rgba(0,0,0,0.05);
          }
        }

        .dark .playground-btn-unified {
          animation: subtle-pulse-dark 3s ease-in-out infinite;
        }

        @keyframes subtle-pulse-dark {
          0%, 100% { 
            transform: scale(1);
            box-shadow: 0 2px 8px rgba(0,0,0,0.3), inset 0 1px 2px rgba(0,0,0,0.2);
          }
          50% { 
            transform: scale(1.02);
            box-shadow: 0 4px 12px rgba(0,0,0,0.4), inset 0 1px 2px rgba(0,0,0,0.2);
          }
        }

        /* Brillo sutil en el borde */
        .playground-btn-unified::before {
          content: '';
          position: absolute;
          inset: -1px;
          border-radius: 0.75rem;
          padding: 1px;
          background: linear-gradient(135deg, var(--go-color), transparent, var(--go-color));
          mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
          mask-composite: exclude;
          opacity: 0.3;
          transition: opacity 0.3s ease;
        }

        .playground-btn-unified:hover {
          border-color: var(--go-color);

          box-shadow: 0 6px 16px rgba(0,0,0,0.15), inset 0 1px 2px rgba(0,0,0,0.05);
          animation: none; /* Pausa la animación en hover */
        }

        .playground-btn-unified:hover::before {
          opacity: 0.6;
        }

        .playground-btn-unified:active {
          transform: translateY(-1px) scale(1.02);
        }

        .playground-btn-unified svg {
          width: 18px; 
          height: 18px; 
          color: var(--text-secondary);
          transition: all 0.3s ease-in-out;
          filter: drop-shadow(0 1px 2px rgba(0,0,0,0.1));
        }

        .playground-btn-unified:hover svg {
          color: var(--go-color);
          transform: scale(1.15);
          filter: drop-shadow(0 2px 4px rgba(0,0,0,0.15));
        }

        .playground-btn-unified:hover::after {
          animation: none;
          opacity: 0.8;
          transform: scale(1.2);
        }
      `}</style>
      
      <div class="flex-shrink-0">
        <button 
          id="open-playground-btn" 
          class="playground-btn-unified" 
          title="Abrir Playground"
        >
          <svg fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path>
          </svg>
        </button>
      </div>
    </>
  );
}