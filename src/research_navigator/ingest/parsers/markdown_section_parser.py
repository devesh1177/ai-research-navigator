import re


def extract_markdown_sections(text: str) -> list[dict]:
    pattern = r"^#\s+(.+)$"

    matches = list(
        re.finditer(
            pattern,
            text,
            flags=re.MULTILINE
        )
    )

    sections = []

    for i, match in enumerate(matches):

        title = match.group(1).strip()

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        sections.append(
            {
                "section_title": title,
                "content": content
            }
        )

    return sections