import { readFileSync } from 'node:fs';

const diagrams = new URL('../assets/diagrams/', import.meta.url);

// Embed repository SVGs and number figures in reading order within each document.
export default function rehypeFigures() {
  return function transform(tree) {
    let number = 0;
    function visit(node) {
      if (!node.children) return;
      for (let i = 0; i < node.children.length; i++) {
        const child = node.children[i];
        const meaningful = child.children?.filter(part => part.type !== 'text' || part.value.trim());
        const img = meaningful?.[0];
        if (child.type === 'element' && child.tagName === 'p' && meaningful?.length === 1 && img.type === 'element' && img.tagName === 'img') {
          number++;
          const caption = img.properties.title || img.properties.alt || '';
          delete img.properties.title;
          const match = String(img.properties.src).match(/^\.\.\/\.\.\/\.\.\/assets\/diagrams\/([a-z0-9-]+\.svg)$/);
          let graphic = img;
          if (match) {
            const svg = readFileSync(new URL(match[1], diagrams), 'utf8');
            graphic = { type: 'raw', value: svg.replace('<svg ', '<svg class="note-diagram" ') };
          }
          node.children[i] = {
            type: 'element', tagName: 'figure', properties: { className: ['note-figure'] },
            children: [graphic, {
              type: 'element', tagName: 'figcaption', properties: {},
              children: [{ type: 'text', value: `▲ [그림 ${number}] ${caption}` }],
            }],
          };
        } else visit(child);
      }
    }
    visit(tree);
  };
}
