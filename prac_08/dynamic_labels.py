from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Caitlyn", "Susan", "Cam", "Alex", "Bailey"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.create_label(name)
        return self.root

    def create_label(self, name):
        """Create widgets from data and add them to the GUI."""
        label = Label(text=name)
        self.root.ids.main.add_widget(label)


DynamicWidgetsApp().run()
