from kivymd.uix.list.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty


class AccountItem(OneLineIconListItem):
    path_icon = StringProperty()
    key_object = StringProperty()
    checkbox_state = BooleanProperty(False)
    function_button = ObjectProperty()

    def check_box_active(self, checkbox, value):
        self.checkbox_state = value




