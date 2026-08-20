#Found from https://gist.github.com/igniteflow/1253276
import datetime

class Timer(object):
    """A simple timer class"""
    
    def __init__(self): #doesn't need attributes
        pass
    
    def start(self): #starts defining methods
        """Starts the timer"""
        self.start = datetime.datetime.now() #module, class, method
        return self.start #prints out the object's current datetime
    
    def stop(self, message="Total: "):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = datetime.datetime.now()
        return message + str(self.stop - self.start) #gets difference from the two method calls
    
    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        return message + str(datetime.datetime.now() - self.start) #gets difference from current time to past method call

test = Timer() 
test.start()