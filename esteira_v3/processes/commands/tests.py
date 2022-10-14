from processes.commands.abstractprocess import AbstractProcess

class Tests(AbstractProcess):
    def __init__(self,void_list) -> None:
        pass
    
    def execute(self):
        print(f'Televisor testado...')
