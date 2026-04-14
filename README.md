# Design Patterns

A personal collection of design pattern implementations written while practicing Low-Level Design (LLD) in Python. Each folder contains a self-contained example of a classic Gang of Four pattern, built from scratch to internalize the structure, intent, and trade-offs of each one.

## Why this repo?

Design patterns are the vocabulary of software architecture. Reading about them is one thing — implementing them, breaking them, and extending them is how they actually stick. This repo is my working notebook: messy in places, refined in others, but always hands-on.

## Patterns covered

- **Memento** — snapshot-based undo/redo for a text editor
- _More to come as I work through them_

## Structure

Each pattern lives in its own directory with:
- The core classes (originator, memento, caretaker, etc.)
- A `main.py` demonstrating the pattern in action

## Running

```bash
uv venv .venv
source .venv/bin/activate
uv run python memento/main.py
```

## Goal

Work through the full catalog of creational, structural, and behavioral patterns — one implementation at a time — and build the intuition to recognize when (and when not) to reach for them in real code.
