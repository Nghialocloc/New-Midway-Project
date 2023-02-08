import concretegui

def get_timer(time_y):
    # Returns timer
    s, ms = divmod(int(time_y), 1000)
    m, s = divmod(s, 60)
    return '{:02d}m:{:02d}s'.format(m, s)

class Timer:
    """
    Controls the timers for the game, including fischer based incrementation format.
    """
    def __init__(self):
        self.base = 5 * 60 * 1000             # 5 minutes in ms
        
        
        self.inc = 10000                      # increment time in ms (10 sec)
        self.elapsed = 0
        self.run_out = False

    def update_base(self):                    # Update base time after every move
        self.base -= self.elapsed             # add 10 seconds minus elapsed time
        self.base = max(0, self.base)
        self.elapsed = 0
        if self.base == 0 :
            self.run_out = True
        
    
