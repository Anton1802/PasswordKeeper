from Model.base_model import BaseScreenModel
from kivy.properties import DictProperty
import Utility.json_writer_reader as json_wr


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    user = DictProperty

    def add_user(self, username, password):
        self.user = {
            "username": username,
            "password": password,
            "data_user": {}
        }
        json_wr.json_write(f'assets/data/{username}.json', self.user)
