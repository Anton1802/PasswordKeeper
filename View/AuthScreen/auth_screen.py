from View.base_screen import BaseScreenView
from kivy.properties import ObjectProperty
from kivymd.uix.button.button import MDRaisedButton
from kivymd.uix.dialog.dialog import MDDialog


class AuthScreenView(BaseScreenView):

    dialogue = ObjectProperty()

    def model_is_changed(self) -> None:
        pass

    def show_message(self, message: str) -> None:
        self.dialogue = MDDialog(
            title="Message",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_press=lambda x: self.dialogue.dismiss()
                )
            ]
        )
        self.dialogue.open()
