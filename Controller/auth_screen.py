from View.AuthScreen.auth_screen import AuthScreenView
import Utility.json_writer_reader as json_wr



class AuthScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = AuthScreenView(controller=self, model=self.model)

    def get_view(self) -> AuthScreenView:
        return self.view

    def login_user(self):
        username = self.view.ids.login_username_textfield.text
        password = self.view.ids.login_password_textfield.text

        user = self.model.get_user(username, password)

        try:
            if user['username'] == username and user['password'] == password:
                self.view.show_message("Login Successful!")
                self.view.manager_screens.current = "control screen"
                path = "assets/data/users/current_user.json"
                current_user = [user['username'], user['password']]
                json_wr.json_write(path, current_user)
            else:
                self.view.show_message("User is not found!")
        except TypeError:
            self.view.show_message("User is not found!")







