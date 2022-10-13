from View.MainScreen.main_screen import MainScreenView



class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def register_user(self):
        username = self.view.ids.register_username_textfield.text
        password = self.view.ids.register_password_textfield.text
        if username == "" or password == "":
            self.view.show_message("Error: username and password fields are empty!")
        elif len(username) < 6 or len(password) < 8:
            self.view.show_message("Error: not enough characters in username, password fields!")
        else:
            self.model.add_user(username, password)
            self.view.show_message("You have registered!")
            self.view.manager_screens.current = 'auth screen'






