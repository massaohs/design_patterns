from src.loadfiles import LoadFiles
from components.createcomponents import CreateComponents
from processes.processesused import ProcessesUsed

class Orchestrator:

    def __init__(self) -> None:
        self.datasheet = LoadFiles().get_info_datasheet()
        self.setup_map = LoadFiles().setup()
        self.components = list()
        self.list_execution = list()

    def show_batch(self, amount, type_tv):
        print(f"\n------------####### Montagem de {amount} {type_tv} #######------------\n")

    def running_machine(self):

        for assembly in self.datasheet['assembly']:
            tv = CreateComponents(assembly['type'], assembly['amount']).create()
            self.components.append(tv)

        while self.components:
            self.list_execution = list()
            assembly = self.components.pop(0)
            for process in self.setup_map[assembly.type_tv]['processes']:
                instance = ProcessesUsed(assembly, process)
                instance.add_run_list()
                self.list_execution.append(instance)

            self.show_batch(assembly.amount, assembly.type_tv)
            number_tvs = assembly.amount

            while number_tvs > 0:
                for action in self.list_execution:
                    action.get_started()
                number_tvs -=1
                print()
            
            

            

            
            
            
