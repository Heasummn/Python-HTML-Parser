"""
A module containing classes used for testing purposes
"""

import unittest
from tag import Tag
from parser import Parser
from dom import Dom


class TestParser(unittest.TestCase):

    def test_html_string_parsing(self):
        html = """
                <html>
                    <body>
                        <p>This is a p tag</p>
                    </body>
                </html>
               """
        root = Tag("html")
        body = Tag("body")
        body.add_child(Tag("p"))
        root.add_child(body)
        test_dom = Dom(root=root)

        parser = Parser(html)
        parsed_dom = parser.parse_html()
        parsed_tags = parsed_dom.get_tags(parsed_dom.root)
        expected_tags = test_dom.get_tags(test_dom.root)
        self.assertEquals(len(expected_tags), len(parsed_tags))
        for i, tag in enumerate(expected_tags):
            self.assertEquals(tag.name, parsed_tags[i].name)

if __name__ == '__main__':
    unittest.main()
