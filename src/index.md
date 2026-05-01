# Weather Extremes -- Station Records

This table shows verified temperature extremes by region.

```js
const records = await FileAttachment("data/records.csv").csv({typed: true});
```

```js
Plot.plot({
  title: "Verified temperature extremes by region",
  width,
  height: 500,
  x: {type: "utc", label: "Date"},
  y: {label: "Max temperature (C)"},
  color: {legend: true},
  marks: [
    Plot.dot(records, {
      x: "date",
      y: "temp_max",
      fill: "region",
      r: 6,
      tip: true
    }),
    Plot.ruleY([0])
  ]
})
```

## Records table

```js
Inputs.table(records, {
  columns: ["station", "region", "date", "temp_max", "temp_min"],
  header: {
    station: "Station",
    region: "Region",
    date: "Date",
    temp_max: "Max (C)",
    temp_min: "Min (C)"
  }
})
```
