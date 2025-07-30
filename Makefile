# ------------------- Makefile -------------------
# Quick commands for day‑to‑day development.
#
# Usage examples:
#   make run             # launch CLI chat
#   make docker-build    # build container
#   make docker-run      # run container interactively
#   make api             # run fastAPI
# ------------------------------------------------

PYTHON = python3
PYPATH = PYTHONPATH=./src
IMG    = faq-rag

.PHONY: help ingest test run run-openai docker-build docker-run

help:
	@echo "Targets:" && \
	echo "  test          – run regression tests (qa_check)" && \
	echo "  run           – CLI chat with OpenAI embeddings" && \
	echo "  docker-build  – build Docker image '$(IMG)'" && \
	echo "  docker-run    – run container interactively" && \
	echo "  api           - run fastAPI"


test:
	$(PYPATH) $(PYTHON) -m tests.qa_check

run:
	$(PYPATH) $(PYTHON) manual_test.py

docker-build:
	docker build -t $(IMG) .

docker-run:
	docker run -it $(IMG)
	
api:
	$(PYPATH) uvicorn src.api:app --reload --host 0.0.0.0 --port 8000

