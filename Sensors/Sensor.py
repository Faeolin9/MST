from threading import Thread
from multiprocessing import Queue
import random
import time

class Sensor():
    
    @staticmethod
    def __creator_thread(seed, n_min, n_max, queue_out: Queue):
        random.seed(seed) 
        while True:
            data = random.uniform(n_min, n_max)
            queue_out.put(data)
            time.sleep(1)



    def __init__(self, name, n_min, n_max, seed, sfreq=1) -> None:
        
        self.seed = seed
        self.name = name
        self.sfreq = sfreq

        self.queue = Queue()

        crea_thread = Thread(target=self.__creator_thread, name=f'DataGenerator{name}', args=(seed, n_min, n_max, self.queue))

        crea_thread.start()


    
    
    def get_data(self):
        output = []

        while not self.queue.empty():
            output.append(self.queue.get())

        return output
