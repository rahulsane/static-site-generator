import sys
import unittest
sys.path.insert(0, "/home/rahul/workspace/github.com/rahulsane/static-site-generator")
from public.htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_creation(self):
        node = HTMLNode("h1", "this is an h1", children=None, props=None)
        self.assertIsInstance(node, HTMLNode)

    def test_to_html(self):
        node = HTMLNode("h1", "this is an h1", children=None, props=None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        propsdict = {
            "prop1": "lol",
            "prop2": "lmao, even"
        }
        propstring = f" prop1=\"lol\" prop2=\"lmao, even\""
        node = HTMLNode("h1", "this is an h1", children=None, props=propsdict)
        self.assertEqual(node.props_to_html(), propstring)