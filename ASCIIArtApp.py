from kivy.app import app
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyfiglet

class ASCIIArtApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10,spacing=10)

        self.input = TextInput (text='Enter text', multiline=False)
        self.layout.add_widget(self.input)

        self.button = Button(text='Generate')
        self.button.bind(on_press=self.generate_ascii)
        self.layout.add_widget(self.button)

        self.output = Label(text='Result appears here', font_name='Courier')
        self.layout.add_widget(self.output)

        return self.layout

    def generate_ascii(self, instance):
        text = self.input.textascii_art = pyfiglet.figlet_format(text)
        self.output.text = ascii_art

if _name_== '_main_':
    ASCIIArtApp().run()