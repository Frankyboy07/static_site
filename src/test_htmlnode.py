import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_exception(self):
        node = HTMLNode("p", "test_value", "test_children", {"test": "value", "test2": "value2"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_to_html_empty(self):
        node = HTMLNode("p", "test_value", "test_children", {})
        result = node.props_to_html()
        self.assertEqual(result, "")
    
    def test_to_html_single(self):
        node = HTMLNode("p", "test_value", "test_children", {"Test": "python"})
        result = node.props_to_html()
        self.assertEqual(result, ' Test="python"')

    def test_props_to_html_multiple(self):
        node2 = HTMLNode("p", "test_value", "test_children", {"test": "value", "test2": "value2"})
        result_multiple = node2.props_to_html()
        self.assertEqual(result_multiple, ' test="value" test2="value2"')
    
    def test_to_html_none(self):
        node = HTMLNode("p", "test_value", "test_children")
        result = node.props_to_html()
        self.assertEqual(result, "")    

    

if __name__ == "__main__":
    unittest.main()