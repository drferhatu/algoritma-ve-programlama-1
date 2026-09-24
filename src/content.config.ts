import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const weeks = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './content/weeks' }),
  schema: z.object({
    week: z.number().int().min(1),
    title: z.string(),
    topic: z.string(),
    description: z.string(),
    module: z.string(),
    // Algo-I tek yarıyıllık bir derstir; alan uyumluluk için korunur, her zaman 1'dir
    semester: z.union([z.literal(1), z.literal(2)]).default(1),
    exam: z.boolean().default(false),
    // taslak: iskelet var, notlar eksik | hazir: ders notları tamam
    status: z.enum(['taslak', 'hazir']).default('taslak'),
    // Konu/tarih değişikliği olduğunda sayfada uyarı kutusu olarak gösterilir
    changeNote: z.string().default(''),
    tags: z.array(z.string()).default([]),
    objectives: z.array(z.string()).default([]),
    tools: z.array(z.string()).default([]),
    // Portfolyo kilometre taşı (course.json → portfolio.milestones[].id), ör. "KT1"
    milestone: z.string().optional(),
    // Haftanın Java defteri (Jupyter + IJava): notebooks/hafta-XX.ipynb → sitede gömülü görünüm
    notebook: z
      .object({
        file: z.string(),            // depo içi yol, ör. notebooks/hafta-01.ipynb
        title: z.string().optional(),
        embed: z.boolean().default(true), // public/notebooks/hafta-XX.html gömülsün mü
        // auto: sayfa defteri notların altına kendisi yerleştirir
        // inline: yazar .mdx gövdesinde <NotebookEmbed .../> ile istediği yere koyar
        placement: z.enum(['auto', 'inline']).default('auto'),
      })
      .optional(),
    resources: z
      .array(z.object({ title: z.string(), url: z.string().url(), note: z.string().optional() }))
      .default([]),
  }),
});

/** Laboratuvar oturumları: content/labs/lab-XX.md — aynı haftanın teorisinden bir hafta sonra yapılır. */
const labs = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './content/labs' }),
  schema: z.object({
    week: z.number().int().min(1),
    title: z.string(),
    description: z.string(),
    status: z.enum(['taslak', 'hazir']).default('taslak'),
    objectives: z.array(z.string()).default([]),
    tools: z.array(z.string()).default([]),
    // Teslim edilecek ürün ve kuralı (ör. "Portfolyoya Hesap.java dosyasını ekleyin")
    deliverable: z.string().optional(),
    // Bu labda teslim edilen portfolyo kilometre taşı, ör. "KT1"
    milestone: z.string().optional(),
  }),
});

const announcements = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './content/announcements' }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    pinned: z.boolean().default(false),
    // bilgi | onemli | sinav
    kind: z.enum(['bilgi', 'onemli', 'sinav']).default('bilgi'),
  }),
});

const guides = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './content/guides' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(99),
    icon: z.string().optional(),
  }),
});

export const collections = { weeks, labs, announcements, guides };
