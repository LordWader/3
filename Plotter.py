import psutil
import matplotlib.pyplot as plt


def graph():
        s = [psutil.cpu_percent(), psutil.virtual_memory().percent]
        x = range(2)
        ax = plt.gca()
        ax.bar(x, s)
        ax.set_xticks(x)
        ax.set_xticklabels(('CPU', 'Memory'))
        plt.draw()
        plt.savefig('foo.png')
        plt.close()

if __name__ == "__main__":
    graph()
        
        
