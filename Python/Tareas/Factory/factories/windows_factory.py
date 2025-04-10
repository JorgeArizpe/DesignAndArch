from factories.ui_factory import UIFactory
from models.button import Button, WindowsButton
from models.checkbox import Checkbox, WindowsCheckbox

class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()