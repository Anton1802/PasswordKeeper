from Model.base_model import BaseScreenModel
from kivy.properties import StringProperty
from kivy.properties import ListProperty
import os
import libs.json_writer_reader as json_wr


class AuthScreenModel(BaseScreenModel):

    path = StringProperty
    file_list = ListProperty
    username_file = StringProperty
    user = ListProperty

    def get_user(self, username: str, password: str) -> dict:

        self.path = 'assets/data/users'
        self.file_list = os.listdir(self.path)
        self.username_file = username + '.json'

        for el in self.file_list:
            if el == self.username_file:
                self.user = json_wr.json_read(self.path + '/' + self.username_file)

        return self.user


