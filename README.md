# weather-extremes

A community-maintained catalog of verified weather record events, published as
an [Observable Framework](https://observablehq.com/framework/) site to GitHub
Pages on every merge to `main`.

- **Live site:** https://WeatherCommons.github.io/weather-extremes/
- **Adding records:** see [CONTRIBUTING.md](CONTRIBUTING.md)
- **Schema reference:** see [DATASETS.md](DATASETS.md)

## Running locally

Requires Node.js ≥ 18.

If your local Node is older (check with `node -v`), upgrade it. With Homebrew:

```bash
brew upgrade node
```

Then install dependencies and start the dev server:

```bash
npm ci
npm run dev
```

The dev server prints a local URL (typically `http://127.0.0.1:3000/`). It
watches the file tree — edits to CSVs under `src/data/records/` and to
`src/index.md` reload the page automatically.

## How it deploys

`.github/workflows/deploy.yml` runs on every push to `main`:

1. `npm ci`
2. `npm run build` — Observable compiles `src/` (markdown pages + data loaders)
   into static HTML/JS in `dist/`.
3. `dist/` is uploaded as a GitHub Pages artifact and published.

Direct pushes to `main` are blocked — all changes go through pull requests.
