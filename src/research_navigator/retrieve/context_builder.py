def build_context(results):

    return "\n\n".join(
        result.payload["content"]
        for result in results
    )