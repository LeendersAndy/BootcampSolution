import textwrap


class StringFormat:
    """Contains utilities used to format Strings"""

    def __init__(self, modify_text):
        self.modify_text = modify_text

    def create_paragraph(self):
        return textwrap.fill(self.modify_text, 85)

    def create_author_format(self):
        return '{0:>85}'.format('-'+self.modify_text)