#!/bin/bash
set -e

REPO_URL="https://github.com/mitansh108/Design_Patterns.git"
MSG="${1:-update}"

if [ ! -d .git ]; then
    git init
    git branch -M main
fi

if ! git remote | grep -q "^origin$"; then
    git remote add origin "$REPO_URL"
fi

if [ ! -f README.md ]; then
    echo "# Design_Patterns" >> README.md
fi

git add -A
git commit -m "$MSG" || echo "nothing to commit"
git push -u origin main
