# ThinkTalk

A local, single-user app for turning a daily spoken reading entry into Anki cards,
tracked predictions, and a reviewable video record.

The daily habit is a 1-2 minute spoken entry — either a summary of that day's reading,
or a stance plus counter-stance on a live issue, with a prediction when there is one.
ThinkTalk captures it at the desk, transcribes it locally, extracts cards and predictions,
and keeps the takes browsable.

Shaped pitch (problem, appetite, rabbit holes, no-gos):
https://claude.ai/code/artifact/d5e149c9-dbca-4e71-99a0-21299a3441d6

## Status

Pre-M1. Nothing is built yet.

## Stack

React + Vite + TypeScript · FastAPI · Postgres · arq/Redis · ffmpeg · local whisper.cpp · genanki

Runs locally on the Mac: `docker compose up`, then `localhost:8000`.
