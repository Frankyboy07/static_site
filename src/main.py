from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode
def main():
    node1 = LeafNode("p", "This is a paragraph of text.")
    node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(node2.to_html())




if __name__ == '__main__':
    main()