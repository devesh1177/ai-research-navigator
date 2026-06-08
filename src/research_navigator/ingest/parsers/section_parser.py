import re


def extract_sections(text: str) -> list[dict]:
    pattern = r"\n\d+\n([A-Z][A-Za-z\s\-]+)\n"

    matches = list(re.finditer(pattern, text))

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
                "content": content,
            }
        )

    return sections