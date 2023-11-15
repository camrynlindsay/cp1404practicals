from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """Build the Kivy GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Print a greeting with the entered input name."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_fields(self):
        """Clear the text field and output label to blank."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


BoxLayoutDemo().run()
