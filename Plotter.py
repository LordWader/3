import psutil
import time
import matplotlib.pyplot as plt
import sys


def graph():
        s = [psutil.cpu_percent(), psutil.virtual_memory().percent]
        x = range(2)
        ax = plt.gca()
        plt.ion()
        plt.show()
        ax.bar(x, s)
        ax.set_xticks(x)
        ax.set_xticklabels(('CPU', 'Memory'))
        plt.draw()
        plt.pause(0.001)
        time.sleep(5)
        plt.close()
        return

if __name__ == "__main__":    
    while True:
        graph()
        select = input('Press q to exit or any other key to continue: ')
        if select.lower() == 'q':
            sys.exit()
        else:
            continue
        
        
