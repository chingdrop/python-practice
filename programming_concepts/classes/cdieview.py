# cdieview.py
#   Implementation of a DieView with changeable forground color
#   Illustrates inheritance

from programming_concepts.classes.dieview import DieView


class ColorDieView(DieView):

    def set_value(self, value):
        self.value = value  # remember this value
        DieView.set_value(self, value)  # call setValue from parent class

    def set_color(self, color):
        self.foreground = color
        self.set_value(self.value)
