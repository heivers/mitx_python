from ast import Sub


class info_hiding():
    def __init__(self):
        self.visible = "Look at me"
        self.__also_visible__ = "Look at me too"
        self.__invisible = "Don't look at me directly"

    def print_visible(self):
        print(self.visible)

    def print_invisible(self):
        print(self.__invisible)

    def __print_invisible(self):
        print(self.__invisible)

    def __print_invisible__(self):
        print(self.__invisible)

class Sub_class(info_hiding):
    def new_print_invisible(self):
        print(self.__invisible)


test = Sub_class()
test.new_print_invisible()

test = info_hiding()

test.print_invisible()
test.__print_invisible__()
test.__print_invisible()
#print(test.__invisible)

