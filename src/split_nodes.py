from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
def split_notes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            delimiter_count = len(node.text.split(delimiter))-1
            if delimiter_count % 2 != 0:
                raise Exception(f"Unpaired delimiter {delimiter}")
            split_text = node.text.split(delimiter)
            for i in range(len(split_text)):
                if i % 2 == 0:
                    result.append(TextNode(split_text[i], TextType.TEXT))
                else:
                    result.append(TextNode(split_text[i], text_type))
        else:
            result.append(node)
    return(result)
        
