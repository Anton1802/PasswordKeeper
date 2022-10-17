from Model.base_model import BaseScreenModel
from kivy.properties import StringProperty, ListProperty
import libs.json_writer_reader as json_wr
import os


class ControlScreenModel(BaseScreenModel):

    path = StringProperty
    file_list = ListProperty
    username_file = StringProperty
    user = ListProperty

    def get_current_user(self) -> dict:
        current_user = json_wr.json_read('assets/data/users/current_user.json')

        self.path = 'assets/data/users'
        self.file_list = os.listdir(self.path)
        self.username_file = current_user[0] + '.json'

        for el in self.file_list:
            if el == self.username_file:
                self.user = json_wr.json_read(self.path + '/' + self.username_file)

        return self.user

    def add_account(self, name: str, username: str, password: str, url: str) -> None:
        path = 'assets/data/users/' + self.user['username'] + '.json'
        count = len(self.user['data_user'])

        self.user['data_user'][f'account{count}'] = [name, username, password, url]
        json_wr.json_write(path, self.user)

        self.notify_observers('control screen')

    def remove_account(self, key):
        path = 'assets/data/users/' + self.user['username'] + '.json'
        self.user['data_user'].pop(key)
        json_wr.json_write(path, self.user)






