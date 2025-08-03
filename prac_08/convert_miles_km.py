"""
CP1404 Week 11 Workshop - GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """
    output_km = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.output_km = "0.0"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


    def handle_convert(self, text):
        self.output_km = str(self.convert_to_km(text))

    def handle_increment(self, text, change):
        try:
            value = float(text)
        except ValueError:
            value = 0.0
        value += change
        self.root.ids.input_miles.text = str(value)
        self.handle_convert(str(value))

    def convert_to_km(self, text):
        try:
            miles = float(text)
            return miles * MILES_TO_KM
        except ValueError:
            return 0.0


MilesConverterApp().run()