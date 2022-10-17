from View.MainScreen.main_screen import MainScreenView
from kivy.properties import StringProperty
import os



class MainScreenController:

    path = StringProperty

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_view(self) -> MainScreenView:
        return self.view

    def register_user(self) -> None:
        self.path = "assets/data/users/"
        username = self.view.ids.register_username_textfield.text
        password = self.view.ids.register_password_textfield.text
        if username == "" or password == "":
            self.view.show_message("Error: username and password fields are empty!")
        elif len(username) < 5 or len(password) < 8:
            self.view.show_message("Error: not enough characters in username, password fields!")
            self.view.ids.register_username_textfield.text = ""
            self.view.ids.register_password_textfield.text = ""
        else:
            if not username + ".json" in os.listdir(self.path):
                self.model.add_user(username, password)
                self.view.show_message("You have registered!")
                self.view.manager_screens.current = 'auth screen'
            else:
                self.view.show_message("User already exists!")
                self.view.ids.register_username_textfield.text = ""
                self.view.ids.register_password_textfield.text = ""






