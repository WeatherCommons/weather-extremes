import {readdir, readFile, stat} from "node:fs/promises";
import {join, dirname} from "node:path";
import {fileURLToPath} from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, "records");

const out = ["Year,Date,City,Lat,Lon,Country,Metric,Type,Value,Prev,Prev Date,Scope,Since"];

for (const year of (await readdir(root)).sort()) {
  const yearPath = join(root, year);
  if (!(await stat(yearPath)).isDirectory()) continue;
  for (const file of (await readdir(yearPath)).sort()) {
    if (!file.endsWith(".csv")) continue;
    const csv = await readFile(join(yearPath, file), "utf-8");
    const lines = csv.trim().split("\n").slice(1);
    for (const row of lines) out.push(`${year},${row}`);
  }
}

process.stdout.write(out.join("\n") + "\n");
