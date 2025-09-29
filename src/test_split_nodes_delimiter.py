import unittest

from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is some text with a **bolded phrase** in the middle", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[0].text, "This is some text with a ")
        self.assertEqual(new_nodes[2].text, " in the middle")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_italic(self):
        node = TextNode("This is text with _italicised text_ in it", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[0].text, "This is text with ")
        self.assertEqual(new_nodes[2].text, " in it")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_bad_code(self):
        node = TextNode("This is text with a `code block word", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], TextType.CODE)


if __name__ == "__main__":
    unittest.main()
