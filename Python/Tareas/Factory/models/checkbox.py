from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsCheckbox(Checkbox):
    def render(self):
        return "Renderizando checkbox en Windows"

class MacCheckbox(Checkbox):
    def render(self):
        return "Renderizando checkbox en Mac"

class LinuxCheckbox(Checkbox):
    def render(self):
        return "Renderizando checkbox en Linux"