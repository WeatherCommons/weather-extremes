# Weather Records

Records are reported in **°C** for temperature and **mm** for rainfall.

```js
const records = await FileAttachment("data/all-records.csv").csv({typed: true});
```

```js
const clear = view(Inputs.button("Clear all filters", {value: 0, reduce: (v) => v + 1}));
```

```js
const yearOptions = ["All", ...Array.from(new Set(records.map(d => d.Year))).sort()];
const cityOptions = ["All", ...Array.from(new Set(records.map(d => d.City))).sort()];
const countryOptions = ["All", ...Array.from(new Set(records.map(d => d.Country))).sort()];
const metricOptions = ["All", ...Array.from(new Set(records.map(d => d.Metric))).sort()];
const typeOptions = ["All", ...Array.from(new Set(records.map(d => d.Type))).sort()];
const scopeOptions = ["All", ...Array.from(new Set(records.map(d => d.Scope))).sort()];
```

```js
const year = (clear, view(Inputs.select(yearOptions, {label: "Year", value: "All"})));
const country = (clear, view(Inputs.select(countryOptions, {label: "Country", value: "All"})));
const city = (clear, view(Inputs.select(cityOptions, {label: "City", value: "All"})));
const metric = (clear, view(Inputs.select(metricOptions, {label: "Metric", value: "All"})));
const type = (clear, view(Inputs.select(typeOptions, {label: "Type", value: "All"})));
const scope = (clear, view(Inputs.select(scopeOptions, {label: "Scope", value: "All"})));
```

```js
const datePrefix = (clear, view(Inputs.text({label: "Date prefix", placeholder: "2026, 2026-04, 2026-04-26"})));
const minValue = (clear, view(Inputs.number({label: "Value ≥", placeholder: "min"})));
const maxValue = (clear, view(Inputs.number({label: "Value ≤", placeholder: "max"})));
```

```js
const filtered = records.filter(d => {
  if (datePrefix && !String(d.Date).startsWith(datePrefix)) return false;
  if (year !== "All" && String(d.Year) !== String(year)) return false;
  if (country !== "All" && d.Country !== country) return false;
  if (city !== "All" && d.City !== city) return false;
  if (metric !== "All" && d.Metric !== metric) return false;
  if (type !== "All" && d.Type !== type) return false;
  if (scope !== "All" && d.Scope !== scope) return false;
  if (minValue != null && d.Value < minValue) return false;
  if (maxValue != null && d.Value > maxValue) return false;
  return true;
});
```

```js
Inputs.table(filtered, {
  columns: ["Year", "Date", "City", "Country", "Metric", "Type", "Value", "Prev", "Prev Date", "Scope", "Since", "Lat", "Lon"]
})
```
