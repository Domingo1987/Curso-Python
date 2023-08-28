
import threading

class Tenedor:
    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()
        
    def levantar(self):
        return self.lock.acquire(blocking=False)
    
    def dejar(self):
        self.lock.release()
        
    def get_id(self):
        return self.id
