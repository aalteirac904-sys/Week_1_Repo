from abc import ABC, abstractmethod



class ConservationLaw(ABC):
    
    @abstractmethod
    def flux(self):
        pass
    
    @abstractmethod
    def max_wave_speed(self):
        pass
    
    