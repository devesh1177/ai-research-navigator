from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)


def chunk_sections(sections):
    chunks = []

    for section_index, section in enumerate(sections):
        section_chunks = splitter.split_text(section["content"])

        for chunk_index, chunk in enumerate(section_chunks):
            chunks.append(
                {
                    "section_title": section["section_title"],
                    "section_index": section_index,
                    "chunk_index": chunk_index,
                    "content": chunk,
                }
            )

    return chunks
