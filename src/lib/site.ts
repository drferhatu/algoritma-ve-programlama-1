import courseRaw from '@content/data/course.json';
import modulesRaw from '@content/data/modules.json';
import scheduleRaw from '@content/data/schedule.json';
import { getCollection, type CollectionEntry } from 'astro:content';

/* ------------------------------------------------------------------
   Veri sözleşmesi (content/data/*.json)
   JSON dosyaları içerik ekibi tarafından yazılır; burada açık tipler
   tanımlanır ve eksik alanlar için güvenli varsayılanlar üretilir.
------------------------------------------------------------------- */

export type SectionId = 'A' | 'B';

export interface Section { id: SectionId; theory: string; lab: string }
export interface Assistant { name: string; role?: string; email?: string }
export interface AiPolicyLevel { id: 'kirmizi' | 'sari' | 'yesil'; label: string; where: string; rule: string; why: string }
export interface AiPolicy { intro: string; levels: AiPolicyLevel[] }
export interface Milestone { id: string; week: number; title: string; desc: string }
export interface Portfolio { intro: string; milestones: Milestone[]; rules: string[] }

export interface Course {
  title: string;
  titleEn?: string;
  shortTitle: string;
  code?: string;
  university: string;
  faculty: string;
  department?: string;
  program?: string;
  audience?: string;
  level?: string;
  semesters: string[];
  academicYear: string;
  language: string;
  credits: { theory: number; practice: number; lab: number; local: number; ects: number };
  prerequisites: string;
  instructor: { name: string; email: string; title?: string };
  assistant?: Assistant;
  sections?: Section[];
  classTime?: string;
  methods: string[];
  purpose: string;
  justification: string;
  outcomes: { id: string; text: string; weeks: number[] }[];
  assessment: {
    components: { name: string; weight: number; note?: string }[];
    activities: { name: string; count: number; hours: number; total: number }[];
    totalWorkload: number;
    ectsRule: string;
  };
  textbooks: { author: string; title: string; edition?: string; publisher?: string; year?: number; url?: string; note?: string }[];
  software: { name: string; url: string; desc: string }[];
  resources: { group: string; items: { name: string; url: string; desc: string }[] }[];
  tagline: string;
  codingPhilosophy: string;
  channels: { id: string; name: string; desc: string; url: string; cta: string }[];
  aiTools: {
    intro: string; tip: string; student: string; studentUrl: string;
    items: { id: string; name: string; by: string; url: string; desc: string; free: string; highlight: string }[];
  };
  aiPolicy?: AiPolicy;
  portfolio?: Portfolio;
}

export interface Module { id: string; slug: string; semester: number; title: string; short: string; weeks: number[]; color: string; summary: string }

export type ScheduleStatus = 'normal' | 'tatil' | 'ertelendi' | 'sinav';
export interface ScheduleRow {
  week: number;
  theory: Partial<Record<SectionId, string>>;
  lab: Partial<Record<SectionId, string>>;
  status: ScheduleStatus;
  note: string;
}

export const course = courseRaw as unknown as Course;
export const modules = modulesRaw as unknown as Module[];

/** Varsayılan şubeler: course.json'da sections yoksa kullanılır. */
export const DEFAULT_SECTIONS: Section[] = [
  { id: 'A', theory: 'Cuma 09.15', lab: 'Çarşamba 13.15' },
  { id: 'B', theory: 'Cuma 13.15', lab: 'Perşembe 15.15' },
];
export const sections: Section[] = course.sections?.length ? course.sections : DEFAULT_SECTIONS;
export const sectionOf = (id: SectionId): Section => sections.find((s) => s.id === id) ?? DEFAULT_SECTIONS.find((s) => s.id === id)!;

export const assistant: Assistant = course.assistant ?? { name: 'Arş. Gör. Ömer Miraç Kökçam', role: 'Laboratuvar' };

export const aiPolicy: AiPolicy = course.aiPolicy ?? { intro: '', levels: [] };
export const portfolio: Portfolio = course.portfolio ?? { intro: '', milestones: [], rules: [] };
export const milestoneOf = (id: string | undefined): Milestone | undefined =>
  id ? portfolio.milestones.find((m) => m.id === id) : undefined;

/** Ders süresi (hafta) — schedule.json satır sayısı, yoksa 14 */
export const TOTAL_WEEKS = 14;

/** classTime yoksa sections'tan "A Cuma 09.15 · B Cuma 13.15" üretir */
export const classTimeLabel = (): string =>
  course.classTime || sections.map((s) => `${s.id} ${s.theory}`).join(' · ');

/* ------------------------------------------------------------------
   Takvim: schedule.json → {week, theory:{A,B}, lab:{A,B}, status, note}
   Eski şemadaki tek "date" alanı varsa geriye dönük uyumluluk için
   teori tarihine (her iki şube) çevrilir.
------------------------------------------------------------------- */
type RawRow = { week: number; date?: string; theory?: Partial<Record<SectionId, string>>; lab?: Partial<Record<SectionId, string>>; status?: string; note?: string };
const STATUSES: ScheduleStatus[] = ['normal', 'tatil', 'ertelendi', 'sinav'];

function normalizeRow(r: RawRow): ScheduleRow {
  const theory = r.theory ?? (r.date ? { A: r.date, B: r.date } : {});
  const status = STATUSES.includes(r.status as ScheduleStatus) ? (r.status as ScheduleStatus) : 'normal';
  return { week: r.week, theory, lab: r.lab ?? {}, status, note: r.note ?? '' };
}

const scheduleRows: ScheduleRow[] = (((scheduleRaw as unknown as { weeks?: RawRow[] }).weeks) ?? []).map(normalizeRow);
export const schedule = { weeks: scheduleRows };

export function scheduleOf(n: number): ScheduleRow | undefined {
  return scheduleRows.find((r) => r.week === n);
}

/** Haftanın teori tarihi (ISO); şube verilmezse A. */
export function getTheoryDate(week: number, section: SectionId = 'A'): string | undefined {
  return scheduleOf(week)?.theory[section] || undefined;
}

/** Haftanın lab tarihleri: her şube için ISO tarih (varsa). Lab, teoriden bir hafta SONRA yapılır. */
export function getLabDates(week: number): Partial<Record<SectionId, string>> {
  return scheduleOf(week)?.lab ?? {};
}

/** A ve B teori aynı günse tek tarih, değilse her şube ayrı. */
export function theorySameDay(week: number): boolean {
  const s = scheduleOf(week);
  if (!s) return true;
  const a = s.theory.A, b = s.theory.B;
  return !a || !b || a === b;
}

/* ------------------------------------------------------------------
   Tarih biçimleme (yerel saat dilimine bağımlı olmadan)
------------------------------------------------------------------- */
const MONTHS = ['Oca', 'Şub', 'Mar', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Kas', 'Ara'];
const MONTHS_LONG = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
const DAYS = ['Paz', 'Pzt', 'Sal', 'Çar', 'Per', 'Cum', 'Cmt'];
const DAYS_LONG = ['Pazar', 'Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi'];

function parseIso(iso: string | undefined): { y: number; m: number; d: number; dow: number } | null {
  if (!iso) return null;
  const [y, m, d] = iso.split('-').map(Number);
  if (!y || !m || !d) return null;
  const dow = new Date(Date.UTC(y, m - 1, d)).getUTCDay();
  return { y, m, d, dow };
}

/** "25 Eyl" | long: "25 Eylül 2026" */
export function formatDate(iso: string | undefined, long = false): string {
  const p = parseIso(iso);
  if (!p) return '';
  return long ? `${p.d} ${MONTHS_LONG[p.m - 1]} ${p.y}` : `${p.d} ${MONTHS[p.m - 1]}`;
}

/** Gün adıyla: "Cum 25 Eyl" | long: "Cuma 25 Eylül" */
export function formatDayDate(iso: string | undefined, long = false): string {
  const p = parseIso(iso);
  if (!p) return '';
  return long ? `${DAYS_LONG[p.dow]} ${p.d} ${MONTHS_LONG[p.m - 1]}` : `${DAYS[p.dow]} ${p.d} ${MONTHS[p.m - 1]}`;
}

export function formatDateObj(d: Date): string {
  return `${d.getDate()} ${MONTHS_LONG[d.getMonth()]} ${d.getFullYear()}`;
}

/**
 * Teori satırı: A ve B aynı günse "Cuma 25 Eylül · A 09.15 / B 13.15",
 * değilse "A Cuma 25 Eylül 09.15 · B Cuma 2 Ekim 13.15". Tarih yoksa "".
 */
export function theoryLine(week: number, long = true): string {
  const s = scheduleOf(week);
  if (!s) return '';
  const a = s.theory.A, b = s.theory.B;
  const timeOf = (id: SectionId) => sectionOf(id).theory.replace(/^\S+\s*/, ''); // "Cuma 09.15" → "09.15"
  if (a && b && a === b) return `${formatDayDate(a, long)} · A ${timeOf('A')} / B ${timeOf('B')}`;
  const parts: string[] = [];
  if (a) parts.push(`A ${formatDayDate(a, long)} ${timeOf('A')}`);
  if (b) parts.push(`B ${formatDayDate(b, long)} ${timeOf('B')}`);
  return parts.join(' · ');
}

/** Lab satırı: "A Çar 30 Eyl · B Per 1 Eki" (long: gün ve ay adları uzun, saat eklenir). */
export function labLine(week: number, long = false): string {
  const lab = getLabDates(week);
  const parts: string[] = [];
  (['A', 'B'] as SectionId[]).forEach((id) => {
    const d = lab[id];
    if (!d) return;
    const time = long ? ' ' + sectionOf(id).lab.replace(/^\S+\s*/, '') : '';
    parts.push(`${id} ${formatDayDate(d, long)}${time}`);
  });
  return parts.join(' · ');
}

export const STATUS_LABEL: Record<string, string> = {
  normal: '',
  tatil: 'Tatil — ders yok',
  ertelendi: 'Ertelendi',
  sinav: 'Sınav haftası',
};

/* ------------------------------------------------------------------
   Rotalar ve koleksiyonlar
------------------------------------------------------------------- */
export type Week = CollectionEntry<'weeks'>;
export type Lab = CollectionEntry<'labs'>;

/** base path'e duyarlı bağlantı üretir: href('/haftalar') → '/depo/haftalar' */
export function href(path: string): string {
  const base = import.meta.env.BASE_URL.replace(/\/$/, '');
  if (path === '/') return base + '/';
  return base + (path.startsWith('/') ? path : '/' + path);
}

export const weekSlug = (n: number) => `hafta-${String(n).padStart(2, '0')}`;
export const weekHref = (n: number) => href(`/haftalar/${weekSlug(n)}`);
export const labHref = (n: number) => `${weekHref(n)}#lab`;

export const JAVA_PLAYGROUND = 'https://dev.java/playground/';
export const REPO = 'drferhatu/algoritma-ve-programlama-1';

export function moduleOf(id: string): Module {
  const m = modules.find((x) => x.id === id);
  if (!m) throw new Error(`Modül bulunamadı: ${id}`);
  return m;
}

export async function getWeeksSorted(): Promise<Week[]> {
  const all = await getCollection('weeks');
  return all.sort((a, b) => a.data.week - b.data.week);
}

export async function getLabsSorted(): Promise<Lab[]> {
  const all = await getCollection('labs');
  return all.sort((a, b) => a.data.week - b.data.week);
}

export async function getLabOfWeek(n: number): Promise<Lab | undefined> {
  const all = await getCollection('labs');
  return all.find((l) => l.data.week === n);
}

/** Modül rengi için CSS değişken adı */
export const moduleColorVar = (m: Module) => `var(--mod-${m.color})`;
