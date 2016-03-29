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
        self.root = root
        if self.root is not None:
            correct_type(root, Tag)

    def get_tags(self, root, tags=None, recursive=True):
        """
        Gets all child tags from a Tag object.
        :param root: Tag object, from where children are searched.
        :param tags: tags list where found children are added
        :param recursive: boolean determining whether the search is recursive
        :return: list of tags
        """
        if tags is None:
            tags = []
        for child in root.children:
            tags.append(child)
            print "got here"
            print len(tags)
            if recursive:
                self.get_tags(child, tags)
        return tags
