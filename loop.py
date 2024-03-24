from multiprocessing import Process
from components import run_loop

class Loop:
    def __init__(self):
        self.loop = None
    
    def new_loop(self, prompt):
        self.end_loop()
        self.loop = Process(target=run_loop, args=(prompt,))
        self.loop.start()
    
    def end_loop(self):
        if self.loop != None:
            self.loop.terminate()
            self.loop.join()