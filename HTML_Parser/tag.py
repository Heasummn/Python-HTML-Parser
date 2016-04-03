"""
Module contaning the Tag class.
"""

from utils import correct_type


class Tag(object):
    """
    A HTML tag object. Contains tag name, parent tag and child tags.
    """

    def __init__(self, name, parent=None):
        """Initializer, sets <tag> name and parent tag.

        :param name: tag name
        :param parent: parent tag object
        :return:
        """
        self.name = name
        self.children = []
        self.parent = parent
        self.is_closed = False
        if self.parent is not None:
            parent.add_child(self)

    def add_child(self, child):
        """Adds child tag to children list

        :param child: child Tag object
        :return: None
        """
        correct_type(child, Tag)
        child.set_parent(self)
        self.children.append(child)

    def set_parent(self, parent):
        """Sets parent tag.

        :param parent: parent Tag object
        :return: None
        """
        correct_type(parent, Tag)
        self.parent = parent

    def set_closed(self, closed):
        """
        Set's whether or not the Tag has been closed
        :param closed: Whether or not the tag is closed
        :return: None
        """
        self.is_closed = closed
