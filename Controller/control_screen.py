from View.ControlScreen.control_screen import ControlScreenView


class ControlScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model
        self.view = ControlScreenView(controller=self, model=self.model)

    def get_view(self) -> ControlScreenView:
        return self.view


    def add_account(self, name, username, password, url):
        if len(name) != 0 and len(username) != 0 and len(password) != 0 and len(url) != 0:
            self.model.add_account(name, username, password, url)
            self.view.dialogue.dismiss()
            self.view.show_message("Add Successful!")
        else:
            self.view.dialogue.dismiss()
            self.view.show_message("Error: One field or all fields are empty!")
