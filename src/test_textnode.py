import sys
import unittest
sys.path.insert(0, "/home/rahul/workspace/github.com/rahulsane/static-site-generator")
from public.textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()