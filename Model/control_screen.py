from Model.base_model import BaseScreenModel
from kivy.properties import StringProperty, ListProperty
from Utility.sync import Sync
import libs.json_writer_reader as json_wr
import os
import json


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

    def add_account(self, name: str, username: str, password: str, url: str, icon_path: str) -> None:
        path = 'assets/data/users/' + self.user['username'] + '.json'
        count = len(self.user['data_user'])

        self.user['data_user'][f'account{count}'] = [name, username, password, url, icon_path]
        json_wr.json_write(path, self.user)

        self.notify_observers('control screen')

    def remove_account(self, key):
        path = 'assets/data/users/' + self.user['username'] + '.json'
        self.user['data_user'].pop(key)
        json_wr.json_write(path, self.user)

    def sync_accounts(self) -> bool:

        sync = Sync('localhost', 3035)
        sync.connect()
        try:
            message = json.dumps(self.user)
            sync.request_message(message)

            json_wr.json_write(self.path + '/' + self.username_file,
                               json.loads("".join(sync.response_message())))

            self.notify_observers("control screen")

        except json.decoder.JSONDecodeError:
            return False
        else:
            return True
















