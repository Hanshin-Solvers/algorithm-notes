import groups from '../data/navigation.json';
import algorithmGroups from '../data/navigation-algorithms.json';
import utilityGroups from '../data/navigation-utilities.json';
import languageConfig from '../data/example-languages.json';
import relatedConfig from '../data/related-algorithms.json';
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';

type Topic = { id: string; title: string };
type NavigationGroup = { title: string; id?: string; items?: Topic[] };
function makeNavigation(groups: NavigationGroup[], category: string, categoryTitle: string, prefix: number) {
  return groups.map((group, i) => {
  const number = `${prefix}.${i + 1}`;
  const direct = Boolean(group.id);
  const topics = direct ? [{ id: group.id!, title: group.title }] : group.items!;
  return {
    title: group.title, number, direct,
    items: topics.map((item, j) => ({ ...item, category, categoryTitle, number: direct ? number : `${number}.${j + 1}`, group: direct ? '' : group.title })),
  };
});
}
export const navigation = makeNavigation(groups, 'data-structures', 'Data Structures', 1);
export const algorithmNavigation = makeNavigation(algorithmGroups, 'algorithms', 'Algorithms', 2);
export const utilityNavigation = makeNavigation(utilityGroups, 'utilities', 'Utilities', 3);
export const categories = [
  { id: 'data-structures', title: '1 Data Structures', groups: navigation },
  { id: 'algorithms', title: '2 Algorithms', groups: algorithmNavigation },
  { id: 'utilities', title: '3 Utilities', groups: utilityNavigation },
];
export const entries = categories.flatMap(category => category.groups.flatMap(group => group.items));
const relatedIds = new Map(entries.map(entry => [entry.id, new Set<string>()]));
for (const [source, targets] of Object.entries(relatedConfig)) {
  const sourceIds = relatedIds.get(source);
  if (!sourceIds) throw new Error(`Unknown related topic: ${source}`);
  for (const target of targets) {
    const targetIds = relatedIds.get(target);
    if (!targetIds || source === target) throw new Error(`Invalid related topics: ${source}, ${target}`);
    sourceIds.add(target);
    targetIds.add(source);
  }
}
export const relatedEntries = (topic: string) => entries.filter(entry => relatedIds.get(topic)?.has(entry.id));
export const url = (path = '') => `${import.meta.env.BASE_URL.replace(/\/$/, '')}/${path}`;
export const noteUrl = (id: string) => {
  const entry = entries.find(entry => entry.id === id);
  if (!entry) throw new Error(`Unknown topic: ${id}`);
  return url(`notes/${entry.category}/${id}/`);
};
export const languages = [
  { id: 'cpp', label: 'C++', version: 'C++20', syntax: 'cpp', file: 'main.cpp' },
  { id: 'java', label: 'JAVA', version: 'Java 17', syntax: 'java', file: 'Main.java' },
  { id: 'python', label: 'python', version: 'Python 3', syntax: 'python', file: 'main.py' },
] as const;
export const hasExample = (topic: string) => ((languageConfig as Record<string, string[]>)[topic] ?? languages).length > 0;
export async function loadExample(topic: string) {
  const entry = entries.find(entry => entry.id === topic);
  if (!entry) throw new Error(`Unknown topic: ${topic}`);
  const enabled = (languageConfig as Record<string, string[]>)[topic] ?? languages.map(language => language.id);
  const codes = await Promise.all(languages.filter(language => enabled.includes(language.id)).map(async language => ({
    ...language,
    source: await readFile(resolve(`codes/${language.id}/${entry.category}/${topic}/${language.file}`), 'utf8'),
  })));
  const casePath = entry.category === 'data-structures' ? topic : `${entry.category}/${topic}`;
  const sample = JSON.parse(await readFile(resolve(`tests/cases/${casePath}.json`), 'utf8'))[0] as { input: string; output: string };
  return { codes, sample };
}
