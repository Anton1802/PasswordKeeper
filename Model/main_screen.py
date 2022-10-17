from Model.base_model import BaseScreenModel
from kivy.properties import DictProperty
import libs.json_writer_reader as json_wr


class MainScreenModel(BaseScreenModel):

    user = DictProperty

    def add_user(self, username: str, password: str) -> None:
        self.user = {
            "username": username,
            "password": password,
            "data_user": {}
        }
        json_wr.json_write(f'assets/data/users/{username}.json', self.user)
