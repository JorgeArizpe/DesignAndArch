from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Renderizando botón en Windows"

class MacButton(Button):
    def render(self):
        return "Renderizando botón en Mac"

class LinuxButton(Button):
    def render(self):
        return "Renderizando botón en Linux"