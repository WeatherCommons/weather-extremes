# Credits

```js
const contributors = await FileAttachment("data/contributors.json").json();
display(html`<ul>${contributors.map(c => html`<li>${c.name}${
  c.X ? html` — X: <a href=${`https://x.com/${c.X.replace(/^@/, "")}`}>${c.X}</a>` : ""
}${
  c.github ? html` — GitHub: <a href=${`https://github.com/${c.github}`}>@${c.github}</a>` : ""
}</li>`)}</ul>`);
```
