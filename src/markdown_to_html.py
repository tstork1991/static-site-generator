from block_parser import markdown_to_blocks
from block_type import BlockType
from block_classifier import block_to_block_type
from markdown_parser import text_to_textnodes
from converter import text_node_to_html_node
from htmlnode import ParentNode, LeafNode


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = [block_to_html_node(block) for block in blocks]
    return ParentNode("div", children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == BlockType.PARAGRAPH:
        flat = block.replace("\n", " ")
        return ParentNode("p", text_to_children(flat))

    elif block_type == BlockType.HEADING:
        heading_level = len(block.split(" ")[0])  # count the #s
        text = block[heading_level+1:].strip()
        return LeafNode(f"h{heading_level}", text)

    elif block_type == BlockType.QUOTE:
        stripped = "\n".join([line[1:].strip() for line in block.split("\n")])
        return ParentNode("blockquote", text_to_children(stripped))

    elif block_type == BlockType.UNORDERED_LIST:
        items = [line[2:].strip() for line in block.split("\n")]
        return ParentNode("ul", [ParentNode("li", text_to_children(item)) for item in items])

    elif block_type == BlockType.ORDERED_LIST:
        items = [line.split(". ", 1)[1] for line in block.split("\n")]
        return ParentNode("ol", [ParentNode("li", text_to_children(item)) for item in items])

    elif block_type == BlockType.CODE:
        inner = block.strip()[3:-3]
        if not inner.endswith("\n"):
            inner += "\n"
        return ParentNode("pre", [ParentNode("code", [LeafNode(None, inner)])])

    else:
        raise Exception(f"Unknown block type: {block_type}")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(n) for n in text_nodes]
