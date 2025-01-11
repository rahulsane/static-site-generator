import sys
import unittest
sys.path.insert(0, "/home/rahul/workspace/github.com/rahulsane/static-site-generator")
from public.htmlnode import *

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_creation(self):
        node = HTMLNode("h1", "this is an h1", children=None, props=None)
        self.assertIsInstance(node, HTMLNode)
        msg = '''
HTMLNode object:
tag: h1
value: this is an h1
props: None
children: None
'''
        self.assertEqual(repr(node), msg)

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

class TestLeafNode(unittest.TestCase):
    def test_leafnode_creation(self):
        node = LeafNode("p","this is a paragraph")
        self.assertIsInstance(node, LeafNode)

        with self.assertRaises(ValueError):
            node2 = LeafNode("p")

    def test_to_html(self):
        node = LeafNode("p","this is a paragraph")
        html_str = "<p>this is a paragraph</p>"
        self.assertEqual(node.to_html(), html_str)

        props = {"href": "https://www.bootdev.com"}
        node2 = LeafNode("a", "this is a link", props)
        html2_str = "<a href=\"https://www.bootdev.com\">this is a link</a>"
        self.assertEqual(node2.to_html(), html2_str)