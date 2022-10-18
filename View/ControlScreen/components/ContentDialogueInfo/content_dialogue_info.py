from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class ContentDialogueInfo(BoxLayout):
    name = StringProperty()
    username = StringProperty()
    password = StringProperty()
    url = StringProperty()
