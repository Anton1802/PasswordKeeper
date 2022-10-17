from View.ControlScreen.control_screen import ControlScreenView
from cerberus.validator import Validator


class ControlScreenController:

    def __init__(self, model):
        self.model = model
        self.view = ControlScreenView(controller=self, model=self.model)

    def get_view(self) -> ControlScreenView:
        return self.view


    def add_account(self, name: str, username: str, password: str, url: str) -> None:
        v = Validator()
        regex_url = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
        schema = {"name": {'type': 'string', 'maxlength': 80, 'required': True},
                  "username": {'type': 'string', 'maxlength': 80, 'required': True},
                  "password": {'type': 'string', 'maxlength': 80, 'required': True},
                  "url": {'type': 'string', 'required': True, 'regex': regex_url},
                  }
        document = {
            "name": name,
            "username": username,
            "password": password,
            "url": url,
        }
        if v.validate(document, schema):
            self.model.add_account(name, username, password, url)
            self.view.dialogue.dismiss()
            self.view.show_message("Add Successful!")
        else:
            self.view.dialogue.dismiss()
            self.view.show_message("Error: Some of the fields are entered incorrectly!")

    def remove_accounts(self):
        for child in self.view.ids.container_accounts.children:
            if child.checkbox_state:
                self.model.remove_account(child.key_object)

        self.model.notify_observers('control screen')



