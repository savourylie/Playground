from multiprocessing import Process

def print_func(cont='Asia'):
    print("The name of the continent is: {}".format(cont))

if __name__ == '__main__':
    names = ['Asia', 'Africa', 'America']
    procs = []

    for name in names:
        proc = Process(target=print_func, args=(name, ))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()




