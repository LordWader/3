import psutil
import time
import matplotlib.pyplot as plt
import sys

def graph():
        s = [psutil.cpu_percent(), psutil.virtual_memory().percent]
        x = range(2)
        ax = plt.gca()
        ax.bar(x, s)
        ax.set_xticks(x)
        ax.set_xticklabels(('CPU', 'Memory'))
        plt.draw()
        plt.savefig('C:\\Users\\Николай\\Desktop\\1\\images\\foo.png')
        plt.close()
        

if __name__ == "__main__":
    graph()
        
        
