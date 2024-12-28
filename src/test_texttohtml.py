import unittest
from main import text_node_to_html_node
from textnode import TextNode, TextType
from htmlnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text_type_text(self):
        text_node = TextNode(text_type=TextType.TEXT, text="Hello World")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "Hello World")
    
    def test_text_type_bold(self):
        bold_node = TextNode(text_type=TextType.BOLD, text="Bold Text")
        html_node = text_node_to_html_node(bold_node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "Bold Text")

    def test_text_type_italic(self):
        italic_node = TextNode(text_type=TextType.ITALIC, text="Italic Text")
        html_node = text_node_to_html_node(italic_node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "Italic Text")

    def test_text_type_code(self):
        code_node = TextNode(text_type=TextType.CODE, text="Code Text")
        html_node = text_node_to_html_node(code_node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "Code Text")

    def test_text_type_link(self):
        link_node = TextNode(text_type=TextType.LINK, text="link Text", url="google.com")
        html_node = text_node_to_html_node(link_node)
        print(html_node.props_to_html())
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "link Text")
        self.assertEqual(html_node.props, {'href':'google.com'})

    def test_text_type_image(self):
        img_node = TextNode(text_type=TextType.IMAGE, text="alt Text", url="google.com")
        html_node = text_node_to_html_node(img_node)
        print(html_node.props_to_html())
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {'src':'google.com', 'alt':'alt Text'})
    
    def test_invalid_text_type(self):
        invalid_node = TextNode(text_type="INVALID", text="Oops")
        with self.assertRaises(Exception):
            text_node_to_html_node(invalid_node)

    # Add more test methods for other TextTypes...

if __name__ == "__main__":
    unittest.main()