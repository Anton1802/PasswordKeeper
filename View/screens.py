# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.main_screen import MainScreenModel
from Model.auth_screen import AuthScreenModel
from Controller.main_screen import MainScreenController
from Controller.auth_screen import AuthScreenController


screens = {
    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },
    "auth screen": {
        "model": AuthScreenModel,
        "controller": AuthScreenController
    }
}
