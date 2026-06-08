setup:
	uv sync

lint:
	uv run ruff check src
	uv run mypy src

test:
	uv run pytest