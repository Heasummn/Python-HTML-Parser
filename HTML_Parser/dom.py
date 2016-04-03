"""
Module containing the Dom class.
"""

from utils import correct_type
from tag import Tag


class Dom(object):
    """
    Document Object Model class. Contains root of the HTML tag tree.
    """

    def __init__(self, root=None):
        """
        Initializer. Sets the root atrribute.
        :param root: Root Tag of the HTML tag tree. Usually the <html> element.
        :return: None
        """
        self.set_root(root)

    def get_tags(self, root, recursive=True):
        """
        Gets all child tags from a Tag object.
        :param root: Tag object, from where children are searched.
        :param recursive: boolean determining whether the search is recursive
        :return: list of tags
        """
        tags = []
        for child in root.children:
            tags.append(child)
            print("got here")
            print(len(tags))
            if recursive:
                tags += self.get_tags(child)
        return tags

    def set_root(self, root):
        """
        Sets the root of the Dom
        :param root: Root Tag of the HTML tag tree. Usually the <html> element.
        :return: None
        """
        self.root = root
        if self.root is not None:
            correct_type(root, Tag)
