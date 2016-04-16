"""
Modules containing objects nessecary for parsing
"""

from dom import Dom
from tag import Tag

class Parser(object):
    """
    Parser class. Responsible for parsing the HTML into a dom
    """
    def __init__(self, html=None):
        """
        Initializer. Sets the html we will be parsing
        :param html: The HTML to be parsed
        :return: None
        """
        self.html = html
        self.current_tag = None

    def parse_html(self):
        dom = Dom()
        index = 0
        while index <= len(self.html) - 1:
            char = self.html[index]
            if char == "<":
                if self.html[index + 1] == "/": # Ending a tag
                    self.current_tag.set_closed(True)
                    index = self.html.find(">", index) # Skip over to the end
                    self.current_tag = self.current_tag.parent

                else:  # It's just a normal tag guys, calm down
                    index += 1
                    char = self.html[index]
                    tag_name = ""
                    while char != ">":  # Fill up the name of the tag
                        tag_name += char
                        index += 1
                        char = self.html[index]
                    if self.current_tag is None:  # It's our first tag
                        self.current_tag = Tag(tag_name)
                        dom.set_root(self.current_tag)
                    else:  # It's not our first tag
                        self.current_tag = Tag(tag_name, self.current_tag)
            index += 1
        return dom
