from factories.ui_factory import UIFactory
from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory
from factories.linux_factory import LinuxFactory

def get_factory(os_type: str) -> UIFactory:
    factories = {
        "Windows": WindowsFactory(),
        "Mac": MacFactory(),
        "Linux": LinuxFactory(),
    }
    return factories.get(os_type, None)

os_type = input("Ingrese el sistema operativo (Windows/Mac/Linux): ")
factory = get_factory(os_type)

if factory:
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())
else:
    print("Sistema operativo no soportado")