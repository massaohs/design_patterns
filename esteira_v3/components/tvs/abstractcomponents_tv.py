from abc import ABC, abstractmethod

class AbstractComponentsTV(ABC):
    
    @abstractmethod
    def get_front_mold(self):
        pass

    @abstractmethod
    def get_back_mold(self):
        pass

    @abstractmethod
    def get_screen(self):
        pass

    def get_wifi(self):
        pass

    @abstractmethod
    def get_board(self):
        pass

    @abstractmethod
    def get_internal_bolts(self):
        pass

    @abstractmethod
    def get_external_bolts(self):
        pass
    
    @abstractmethod
    def get_tests(self):
        pass

    @abstractmethod
    def get_package(self):
        pass