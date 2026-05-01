# Contributing

We welcome contributions of new station records! Here's how:

## Adding or updating data

1. **Fork** this repository
2. **Edit** `src/data/records.csv` — add or correct rows
   - GitHub renders CSVs as tables, so you can edit directly in the browser
   - Keep columns: `station,region,date,temp_max,temp_min`
   - Use ISO dates (`YYYY-MM-DD`), temperatures in Celsius
   - Leave a field blank if unknown
3. **Open a pull request** against `main`
4. A maintainer will review the diff and merge

Once merged, the site rebuilds and deploys automatically via GitHub Pages.

## Running locally

```bash
npm install
npm run dev
```

This starts a local preview server at `http://localhost:3000`.
