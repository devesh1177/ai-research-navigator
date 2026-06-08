def parse_markdown(markdown_path: str) -> str:

    with open(
        markdown_path,
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()