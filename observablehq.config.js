import {readdirSync, statSync} from "node:fs";
import {join} from "node:path";

function recordEvents() {
  const root = "src/data/records";
  const list = [];
  const paths = [];
  for (const year of readdirSync(root).sort()) {
    const yearPath = join(root, year);
    if (!statSync(yearPath).isDirectory()) continue;
    for (const file of readdirSync(yearPath).sort()) {
      if (!file.endsWith(".csv")) continue;
      const country = file.replace(/\.csv$/, "");
      const path = `/records/${year}/${country}`;
      list.push({name: `${year} — ${country}`, path});
      paths.push(path);
    }
  }
  return {list, paths};
}

function atr() {
  const root = "src/data/atr";
  const list = [];
  const paths = [];
  for (const file of readdirSync(root).sort()) {
    if (!file.endsWith(".csv")) continue;
    const country = file.replace(/\.csv$/, "");
    const path = `/atr/${country}`;
    list.push({name: country, path});
    paths.push(path);
  }
  return {list, paths};
}

const re = recordEvents();
const at = atr();

export default {
  title: "Weather Commons",
  root: "src",
  output: "dist",
  theme: "air",
  pages: [
    {
      name: "Record Events",
      pages: [{name: "Overview", path: "/"}, ...re.list]
    },
    {
      name: "All-Time Records",
      pages: [{name: "Overview", path: "/atr"}, ...at.list]
    },
    {name: "Data Sources", path: "/sources"},
    {name: "Credits", path: "/credits"}
  ],
  dynamicPaths: [...re.paths, ...at.paths],
  footer: `Maintained by <a href="https://github.com/WeatherCommons">Weather Commons</a> · <a href="/credits">Credits</a>`
};
