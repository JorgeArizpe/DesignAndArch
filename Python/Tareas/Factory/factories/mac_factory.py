from factories.ui_factory import UIFactory
from models.button import Button, MacButton
from models.checkbox import Checkbox, MacCheckbox

class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()