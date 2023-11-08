from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    """ConvertMilesToKilometresApp is a Kivy App for converting miles to kilometres."""

    def build(self):
        """ build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion_calculation(self):
        """Convert input number into miles (from kilometres)."""
        value = self.get_valid_number()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Make the miles number go up or down by 1."""
        value = self.get_valid_number() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_conversion_calculation()

    def get_valid_number(self):
        """Get a valid number for conversion."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKilometresApp().run()
