from abc import ABC, abstractmethod
from models.button import Button
from models.checkbox import Checkbox

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass