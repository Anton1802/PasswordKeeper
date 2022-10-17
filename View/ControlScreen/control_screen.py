from View.base_screen import BaseScreenView
from View.ControlScreen.components.AccountItem.account_item import AccountItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty
from View.ControlScreen.components.ContentDialogueAddAccount.content_dialogue_add_account \
    import ContentDialogueAddAccount
from kivymd.uix.button.button import MDRaisedButton



class ControlScreenView(BaseScreenView):

    dialogue = ObjectProperty()
    dialog_message = ObjectProperty()

    def model_is_changed(self) -> None:
        self.ids.container_accounts.clear_widgets()
        self.generate_items()

    def on_enter(self) -> None:
        self.generate_items()

    def show_message(self, message: str):
        self.dialog_message = MDDialog(
            title="Message",
            text=message,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_press=lambda x: self.dialog_message.dismiss()
                )
            ]
        )
        self.dialog_message.open()

    def generate_items(self) -> None:
        user = self.model.get_current_user()
        keys = list()

        path_icon = "assets/images/icon.png"

        for key in user['data_user']:
            keys.append(key)

        for key in keys:
            account_item = AccountItem(
                key_object=key,
                text=user['data_user'][key][0],
                path_icon=path_icon,
            )
            self.ids.container_accounts.add_widget(account_item)

    def show_dialogue_add_account(self) -> None:
        self.dialogue = MDDialog(
            title="Add Account",
            type="custom",
            content_cls=ContentDialogueAddAccount(),
            buttons=[
                MDFlatButton(
                    text="Add",
                ),
                MDFlatButton(
                    text="Cancel",
                    on_press=lambda x: self.dialogue.dismiss(),
                ),
            ],
        )
        self.dialogue.open()

        self.dialogue.buttons[0].bind(on_press=lambda x: self.controller.add_account(
            self.dialogue.content_cls.ids.dialogue_name_field.text,
            self.dialogue.content_cls.ids.dialogue_username_field.text,
            self.dialogue.content_cls.ids.dialogue_password_field.text,
            self.dialogue.content_cls.ids.dialogue_url_field.text
        ))



