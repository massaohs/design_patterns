from processes.commands.backmold import BackMold
from processes.commands.board import Board
from processes.commands.externalbolts import ExternalBolts
from processes.commands.frontmold import FrontMold
from processes.commands.internalbolts import InternalBolts
from processes.commands.label import Label
from processes.commands.package import Package
from processes.commands.tests import Tests
from processes.commands.screen import Screen
from processes.commands.wifi import Wifi

__MAP_PROCESSES_DICT__ = {
    "FrontMold": FrontMold,
    "Screen": Screen,
    "Board": Board, 
    "Wifi": Wifi, 
    "InternalBolts": InternalBolts,
    "BackMold": BackMold,
    "ExternalBolts": ExternalBolts,
    "Label": Label,
    "Tests": Tests,
    "Package": Package
}

class ProcessesUsed:
    def __init__(self, batch, list_processes) -> None:
        self.batch = batch
        self.list_processes = list_processes
        self.list_run = list()

    def add_run_list(self):
            self.list_run.append(__MAP_PROCESSES_DICT__[self.list_processes](self.batch.components[self.list_processes]))

    def get_started(self):
        for command in self.list_run:
            command.execute()
        # self.list_run = list()
        