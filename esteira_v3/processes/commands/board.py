from processes.commands.abstractprocess import AbstractProcess

class Board(AbstractProcess):
    def __init__(self, list_components) -> None:
        self.list_components = list_components

    def execute(self):
        component = self.list_components.pop(0)
        print(f'compomente {component} add...')
