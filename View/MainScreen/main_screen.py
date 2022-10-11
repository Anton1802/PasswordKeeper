from View.base_screen import BaseScreenView
from kivymd.uix.dialog.dialog import MDDialog
from kivymd.uix.button.button import MDRaisedButton



class MainScreenView(BaseScreenView):

    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """

    def go_login_screen(self):
        self.manager_screens.current = "auth screen"

    def show_message(self, message):
        dialog = MDDialog(
            title="Message",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_press=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

