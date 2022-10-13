from Model.base_model import BaseScreenModel
from kivy.properties import StringProperty
from kivy.properties import ListProperty
import os
import Utility.json_writer_reader as json_wr


class AuthScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """

    path = StringProperty
    file_list = ListProperty
    username_file = StringProperty
    user = ListProperty

    def get_user(self, username, password):

        self.path = 'assets/data/users'
        self.file_list = os.listdir(self.path)
        self.username_file = username + '.json'

        for el in self.file_list:
            if el == self.username_file:
                self.user = json_wr.json_read(self.path + '/' + self.username_file)

        return self.user


