from factories.ui_factory import UIFactory
from models.button import Button, LinuxButton
from models.checkbox import Checkbox, LinuxCheckbox

class LinuxFactory(UIFactory):
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()