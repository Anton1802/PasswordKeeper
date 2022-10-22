from View.ControlScreen.control_screen import ControlScreenView


class ControlScreenController:

    def __init__(self, model):
        self.model = model
        self.view = ControlScreenView(controller=self, model=self.model)

    def get_view(self) -> ControlScreenView:
        return self.view

    def add_account(self, name: str, username: str, password: str, url: str) -> None:
        if (len(name) <= 80
                and len(username) <= 80
                and len(password) <= 80
                and len(name) != 0
                and len(username) != 0
                and len(password) != 0
                and len(url) != 0):
            self.model.add_account(name, username, password, url)
            self.view.dialogue.dismiss()
            self.view.show_message("Add Successful!")
        else:
            self.view.dialogue.dismiss()
            self.view.show_message("Error: Some of the fields are empty!")

    def remove_accounts(self):
        state = False
        for child in self.view.ids.container_accounts.children:
            if child.checkbox_state:
                self.model.remove_account(child.key_object)
                state = True

        self.model.notify_observers('control screen')

        if state:
            self.view.snackbar_show("Successfully removed!")
        else:
            self.view.snackbar_show("Select accounts to delete!")


