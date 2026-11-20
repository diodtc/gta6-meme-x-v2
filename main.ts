// Entrypoint for the gta6-meme-x-01 v2 entry (Node 22, standard library only).
//
// The entry is the post, not this program. The agent took the user's receipt
// meme, added the real make.fun ghost mark to its picture, and the post went
// out from a public X account with make.fun (a link or written out) and/or a
// tag of @makefunai plus the account's play code in its text. POST.json at
// this repository's root holds that post's address; this program's only job
// is to carry the address to the grader by writing it to /output/POST.json,
// where the gate picks it up. The house then fetches the post from X and the
// judge looks at its first picture and its text. Nothing this file writes
// about the post is judged.
//
// Local check, the way the grader runs it:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });

try {
  const post = readFileSync(join(botDir, "POST.json"));
  writeFileSync(join(outputDir, "POST.json"), post);
} catch (err) {
  console.error(`POST.json could not be handed over from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
