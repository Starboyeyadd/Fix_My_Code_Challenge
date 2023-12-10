#!/usr/bin/python3

# Editting 1: Make the class Square not square
class Square():
    # Editing 2: Adding Doc
    """ start the class"""

    # Edit 3: We don't need kwargs, we just will use width and height
    def __init__(self, width, height):
    # Edit 4: Adding doc
        """ init the class"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        # Edit 5: adding doc
        """ permmiter of the square"""
        # Edit 6: Exchange the permiter of rectangle by the square
        return 4 * self.width

    def __str__(self):
        # Edit 7: Adding doc
        """ String representation """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
