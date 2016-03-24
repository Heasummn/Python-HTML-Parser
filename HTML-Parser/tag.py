"""
Module contaning the Tag class.
"""

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
        if self.parent is not None:
            parent.add_child(self)


    def add_child(self, child):
        """Adds child tag to children list

        :param child: child Tag object
        :return: None
        """
        if not isinstance(child, Tag):
            raise TypeError("Expected Tag object, got {0} of type {1}"
                             .format(child, type(child)))
        child.set_parent(self)
        self.children.append(child)

    def set_parent(self, parent):
        """Sets parent tag.

        :param parent: parent Tag object
        :return: None
        """
        if not isinstance(parent, Tag):
            raise TypeError("Expected Tag object, got {0} of type {1}"
                             .format(parent, type(parent)))
        self.parent = parent
