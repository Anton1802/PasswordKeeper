from View.ControlScreen.control_screen import ControlScreenView


class ControlScreenController:

    def __init__(self, model):
        self.model = model
        self.view = ControlScreenView(controller=self, model=self.model)

    def get_view(self) -> ControlScreenView:
        return self.view

    def add_account(self, name: str, username: str, password: str, url: str, icon_path: str) -> None:
        if (len(name) <= 80
                and len(username) <= 80
                and len(password) <= 80
                and len(name) != 0
                and len(username) != 0
                and len(password) != 0
                and len(url) != 0):
            self.model.add_account(name, username, password, url, icon_path)
            self.view.dialogue.dismiss()
            self.view.show_message("Add Successful!")
        else:
            self.view.dialogue.dismiss()
            self.view.show_message("Error: Some of the fields are empty!")

    def remove_accounts(self) -> None:
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

    def sync_control_user(self):
        if self.model.sync_accounts():
            self.view.snackbar_show("Synchronization Success!")
        else:
            self.view.snackbar_show("Not connection to the server!")


