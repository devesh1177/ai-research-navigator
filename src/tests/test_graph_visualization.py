from research_navigator.agents.graph import (
    research_graph,
)

png_data = research_graph.get_graph().draw_mermaid_png()

with open(
    "graph.png",
    "wb",
) as file:
    file.write(png_data)

print("graph.png created")
