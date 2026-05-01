# weather-extremes

Observable Framework site published to GitHub Pages on merge to `main`.

## Git workflow

Direct pushes to `main` are blocked by branch protection. All changes go through a PR.

### Preferred: branch first, then commit

Cleanest flow — local `main` never diverges, so post-merge sync is a fast-forward `git pull`.

```bash
git checkout -b my-feature-branch
# ...edit files...
git commit -m "first commit..."
git push -u origin my-feature-branch
# <open + merge PR on GitHub>
git checkout main
git pull                               # fast-forward, no conflicts
git branch -D my-feature-branch        # cleanup local branch
git push origin --delete my-feature-branch  # cleanup remote branch (optional)
```

### Recovery: if you committed on local main first

If you committed on local `main` before pushing to a feature branch, local `main`
will be ahead of `origin/main` with the same content that just got merged. Reset it:

```bash
git checkout main
git fetch origin
git reset --hard origin/main          # local main was ahead with the same content; safe to discard
git branch -d <feature-branch>         # cleanup local branch
git push origin --delete <feature-branch>  # cleanup remote branch (optional)
```

The `reset --hard` is destructive — only safe because the PR merge captures the same change.
