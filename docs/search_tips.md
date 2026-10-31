# Search Tips

- Queries are lowercased and common words such as "the" and "how" are ignored, so short keyword queries work best.
- Words are stemmed, so "passwords" also matches "password".
- Results are ranked with BM25: documents that contain rarer query terms more often score higher.
- Use `--top N` (or `:top N` in interactive mode) to change how many results are shown.
- A query made only of ignored words returns no results.
