from View.ControllScreen.control_screen import ControlScreenView


class ControlScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model
        self.view = ControlScreenView(controller=self, model=self.model)

    def get_view(self) -> ControlScreenView:
        return self.view
