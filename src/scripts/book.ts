const storageKey = 'algorithm-notes';
function read<T>(key: string, fallback: T): T {
  try { return JSON.parse(sessionStorage.getItem(`${storageKey}:${key}`) || 'null') ?? fallback; } catch { return fallback; }
}
function save(key: string, value: unknown) {
  try { sessionStorage.setItem(`${storageKey}:${key}`, JSON.stringify(value)); } catch { /* Current-page interactions remain available. */ }
}
const sidebar = document.querySelector<HTMLElement>('.sidebar');
const menus = document.querySelectorAll<HTMLDetailsElement>('details[data-menu]');
const expanded = read<Record<string, boolean>>('expanded', {});
menus.forEach(menu => {
  const key = menu.dataset.menu!;
  if (key in expanded) menu.open = expanded[key];
  if (menu.querySelector('[aria-current="page"]')) menu.open = true;
  expanded[key] = menu.open;
  menu.addEventListener('toggle', () => { expanded[key] = menu.open; save('expanded', expanded); });
});
save('expanded', expanded);
if (sidebar) {
  sidebar.scrollTop = read<number>('sidebar-scroll', 0);
  const active = sidebar.querySelector<HTMLElement>('[aria-current="page"]');
  if (active) {
    const box = active.getBoundingClientRect();
    if (box.top < 0 || box.bottom > innerHeight) active.scrollIntoView({ block: 'nearest' });
  }
  sidebar.addEventListener('scroll', () => save('sidebar-scroll', sidebar.scrollTop), { passive: true });
}
document.querySelectorAll<HTMLElement>('[data-code-tabs]').forEach(shell => {
  const tabs = [...shell.querySelectorAll<HTMLButtonElement>('[data-language]')];
  const panels = [...shell.querySelectorAll<HTMLElement>('[data-code-panel]')];
  const timers = new Map<HTMLElement, ReturnType<typeof setTimeout>>();
  function resetCopy(panel: HTMLElement) {
    clearTimeout(timers.get(panel));
    timers.delete(panel);
    const button = panel.querySelector<HTMLButtonElement>('[data-copy]')!;
    button.textContent = '코드 복사';
    delete button.dataset.result;
    panel.querySelector<HTMLElement>('.copy-status')!.textContent = '';
  }
  function select(language: string) {
    tabs.forEach(tab => { const active = tab.dataset.language === language; tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1; });
    panels.forEach(panel => { panel.hidden = panel.dataset.codePanel !== language; resetCopy(panel); });
  }
  const saved = read<string>('language', 'cpp');
  select(tabs.some(tab => tab.dataset.language === saved) ? saved : 'cpp');
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => { select(tab.dataset.language!); save('language', tab.dataset.language); });
    tab.addEventListener('keydown', event => {
      const next = event.key === 'ArrowRight' ? (index + 1) % tabs.length : event.key === 'ArrowLeft' ? (index + tabs.length - 1) % tabs.length : event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length - 1 : -1;
      if (next < 0) return;
      event.preventDefault(); tabs[next].focus(); tabs[next].click();
    });
  });
  panels.forEach(panel => {
    const button = panel.querySelector<HTMLButtonElement>('[data-copy]')!;
    button.addEventListener('click', async () => {
      const code = panel.querySelector('code')!;
      const status = panel.querySelector<HTMLElement>('.copy-status')!;
      resetCopy(panel);
      button.disabled = true;
      try {
        await navigator.clipboard.writeText(code.textContent || '');
        if (panel.hidden) return;
        button.textContent = '✓ 복사 완료';
        button.dataset.result = 'success';
        status.textContent = '복사 완료';
      } catch {
        if (panel.hidden) return;
        const range = document.createRange();
        range.selectNodeContents(code);
        const selection = getSelection();
        selection?.removeAllRanges();
        selection?.addRange(range);
        button.textContent = 'Ctrl+C로 복사';
        status.textContent = '코드가 선택되었습니다. Ctrl+C로 복사하세요.';
      } finally {
        button.disabled = false;
      }
      timers.set(panel, setTimeout(() => resetCopy(panel), 2000));
    });
  });
});
