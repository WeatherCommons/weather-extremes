import {html} from "npm:htl";

const metricSlug = (m) => String(m).toLowerCase().replace(/\s+/g, "-");

const fmt = (v) => v instanceof Date ? v.toISOString().slice(0, 10) : v;

const styles = html`<style>
  table.records {
    border-collapse: collapse;
    margin: 0;
    width: max-content;
    max-width: 100%;
    font-variant-numeric: tabular-nums;
  }
  table.records th,
  table.records td {
    padding: 6px 12px;
    text-align: left;
    vertical-align: top;
    white-space: nowrap;
  }
  table.records th:first-child,
  table.records td:first-child {
    padding-left: 0;
  }
  table.records thead th {
    border-bottom: 2px solid #888;
    font-weight: 600;
  }
  table.records tbody tr:nth-child(even) {
    background: #f3f3f3;
  }
  table.records tbody tr.metric-max-temp td   { color: #d62728; }
  table.records tbody tr.metric-min-temp td   { color: #f08080; }
  table.records tbody tr.metric-rain td       { color: #006400; }
  table.records tbody tr.metric-snow td       { color: #1f77b4; }
  table.records tbody tr.metric-dew-point td  { color: #800080; }
  table.records tbody tr.metric-max-wind td   { color: #000000; }
  table.records tbody tr.metric-wet-bulb td   { color: #800080; }
</style>`;

export function recordsTable(rows, columns) {
  return html`${styles}<table class="records"><thead><tr>${
    columns.map(c => html`<th>${c}</th>`)
  }</tr></thead><tbody>${
    rows.map(row => html`<tr class="metric-${metricSlug(row.Metric)}">${
      columns.map(c => html`<td>${fmt(row[c])}</td>`)
    }</tr>`)
  }</tbody></table>`;
}
