# Support Knowledge Base + Local Search

A small collection of support knowledge-base articles (markdown files) and
`search_engine.py`, a local BM25 keyword search over them. No AI and no network
access are needed.

## Usage

```bash
python search_engine.py                                   # interactive mode
python search_engine.py --folder ./docs                   # index another folder
python search_engine.py --query "password reset" --top 3  # single query
python search_engine.py --no-recursive                    # do not enter sub-folders
python search_engine.py --no-color                        # plain output
```

Interactive commands: `:help`, `:files`, `:stats`, `:reload`, `:top N`, `:quit`.

## Optional dependencies

- `colorama` for coloured terminal output
- `PyPDF2` to index PDF files

```bash
pip install colorama PyPDF2
```

## Knowledge base

The numbered `.md` files cover login, billing, refunds, API keys, security,
passwords, account deletion, prompt injection, technical issues and escalation.
