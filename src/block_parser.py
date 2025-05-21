def markdown_to_blocks(markdown):
    # Split by two or more newlines, clean up whitespace, and remove blanks
    raw_blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]
    return blocks
