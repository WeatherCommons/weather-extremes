# Record Events

Records are reported in **°C** for temperature and **mm** for rainfall.

```js
const records = await FileAttachment("data/records/2026/India.csv").csv({typed: true});
```

```js
const country = view(Inputs.select(["All", ...new Set(records.map(d => d.Country))], {label: "Country", value: "All"}));
```

```js
const city = view(Inputs.select(["All", ...new Set(records.map(d => d.City))], {label: "City", value: "All"}));
```

```js
const metric = view(Inputs.select(["All", ...new Set(records.map(d => d.Metric))], {label: "Metric", value: "All"}));
```

```js
const recordType = view(Inputs.select(["All", ...new Set(records.map(d => d.Type))], {label: "Type", value: "All"}));
```

```js
const scope = view(Inputs.select(["All", ...new Set(records.map(d => d.Scope))], {label: "Scope", value: "All"}));
```

```js
const datePrefix = view(Inputs.text({label: "Date prefix", placeholder: "2026, 2026-04, 2026-04-26"}));
```

```js
const filtered = records.filter(d => {
  if (datePrefix && !(d.Date instanceof Date ? d.Date.toISOString().slice(0, 10) : String(d.Date)).startsWith(datePrefix)) return false;
  if (country !== "All" && d.Country !== country) return false;
  if (city !== "All" && d.City !== city) return false;
  if (metric !== "All" && d.Metric !== metric) return false;
  if (recordType !== "All" && d.Type !== recordType) return false;
  if (scope !== "All" && d.Scope !== scope) return false;
  return true;
});
```

```js
import {recordsTable} from "./components/recordsTable.js";
display(recordsTable(filtered, ["Date", "City", "Country", "Metric", "Type", "Value", "Prev", "Prev Date", "Scope", "Since", "Elevation", "WMO"]));
```
