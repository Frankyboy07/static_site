import unittest
from htmlnode import LeafNode
class TestLeafNode(unittest.TestCase):
    def test_rendering_with_tag_and_props(self):
        # Arrange
        node = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        
        # Act
        result = node.to_html()
        
        # Assert
        self.assertEqual(result, '<a href="https://www.google.com">Click me!</a>')

    def test_rendering_without_tag(self):
        # Arrange
        node = LeafNode(tag=None, value="This is just text.")
        
        # Act
        result = node.to_html()
        
        # Assert
        self.assertEqual(result, "This is just text.")
        
    def test_error_on_missing_value(self):
        # Arrange / Act / Assert
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value=None)