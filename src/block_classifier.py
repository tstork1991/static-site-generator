from block_type import BlockType

def block_to_block_type(block):
    lines = block.split("\n")

    # Code block: starts and ends with triple backticks
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading: 1-6 '#' followed by a space
    if lines[0].startswith("#"):
        if 1 <= len(lines[0].split(" ")[0]) <= 6 and lines[0][len(lines[0].split(" ")[0])] == " ":
            return BlockType.HEADING

    # Quote: every line starts with '>'
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list: every line starts with '- '
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list: 1. item, 2. item, etc.
    if all(
        line.split(". ")[0].isdigit() and
        line.startswith(f"{i + 1}. ") for i, line in enumerate(lines)
    ):
        return BlockType.ORDERED_LIST

    # Default
    return BlockType.PARAGRAPH
