import unittest
from htmlnode import ParentNode, LeafNode, HTMLNode
class TestParentNode(unittest.TestCase):

    def test_basic_parent_node(self):
        node = ParentNode(
            tag="p",
            children=[
                LeafNode(tag="b", value="Bold text"),
                LeafNode(tag=None, value="Normal text"),
                LeafNode(tag="i", value="italic text"),
                LeafNode(tag=None, value="Normal text"),
            ]
        )
        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_missing_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_missing_children(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None)
    
    def test_nested_parent_node(self):
        child_node = ParentNode(
            tag="div",
            children=[LeafNode(tag="span", value="Nested text")]
        )
        node = ParentNode(
            tag="p",
            children=[child_node]
        )
        expected_html = "<p><div><span>Nested text</span></div></p>"
        self.assertEqual(node.to_html(), expected_html)

if __name__ == '__main__':
    unittest.main()