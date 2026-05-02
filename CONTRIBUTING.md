# Contributing

We welcome contributions of new station records! Here's how:

## Adding or updating data

Records are organized by year and country:

```
src/data/records/<YYYY>/<COUNTRY>.csv
```

For example, an Indian record set in 2026 lives at `src/data/records/2026/India.csv`.

1. **Fork** this repository.
2. **Find the right file** for the year and country of the record. If it doesn't
   exist yet, create it with the schema header below.
3. **Add a row** following the Record Events schema (see [DATASETS.md](DATASETS.md)
   for the authoritative spec):

   ```
   Date,City,Lat,Lon,Country,Metric,Type,Value,Prev,Prev Date,Scope,Since
   ```

   - `Date`, `Prev Date`: ISO format `YYYY-MM-DD`.
   - `Lat`, `Lon`: decimal degrees.
   - `Metric`: e.g. `Rain`, `Max Temp`.
   - `Type`: e.g. `24hrs`, `High`.
   - `Value`, `Prev`: temperature in °C, rainfall in mm.
   - `Scope`: e.g. `Month`, `Year`.
   - `Since`: the year the prior record series begins.
4. **Open a pull request** against `main`. GitHub renders CSVs as tables so the
   diff is easy to review.
5. A maintainer will review and merge.

Once merged, the site rebuilds and deploys automatically via GitHub Pages.

## Running locally

```bash
npm install
npm run dev
```

This starts a local preview server at `http://localhost:3000`.
