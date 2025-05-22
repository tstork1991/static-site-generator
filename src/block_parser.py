def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]
    return blocks

