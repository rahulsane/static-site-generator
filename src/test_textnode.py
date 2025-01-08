import sys
import unittest
sys.path.insert(0, "/home/rahul/workspace/github.com/rahulsane/static-site-generator")
from public.textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_texttype_exc(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a text node", TextType.BOGUS)

    def test_textnode_numastext(self):
        node = TextNode(123, TextType.BOLD)
        self.assertIsInstance(node, TextNode)
    
    def test_textnode_noneurl(self):
        node = TextNode("yeehaw", TextType.ITALIC, url=None)
        self.assertIsInstance(node, TextNode)

if __name__ == "__main__":
    unittest.main()