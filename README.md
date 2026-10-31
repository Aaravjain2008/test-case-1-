# Support Knowledge Base Search

A small local search engine over a support knowledge base (the numbered `.md`
files in this folder). It ranks documents with BM25 and needs no AI and no
network access.

## Usage

```bash
python search_engine.py                              # interactive mode
python search_engine.py --query "reset password"     # single query
python search_engine.py --folder ./docs --top 3      # other folder, 3 results
```

Optional extras: `pip install colorama` for coloured output and
`pip install PyPDF2` for PDF support.

## Knowledge base topics

Account login, billing, refunds, API keys, security, passwords, account
deletion, prompt injection, technical issues and escalation.
