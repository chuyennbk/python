# from concurrent.futures import thread
import threading
import multiprocessing
import time
import concurrent.futures
def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping ...')
    
def do_something2(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping ...')

def do_something3(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping {seconds} second(s)...'

def unuse_thread_multiprocessing():
    do_something()
    do_something()

def thread_test():
    start=time.perf_counter()
    for i in range(10):
        x=threading.Thread(target=do_something)
        x.start()
    x.join()
    finish=time.perf_counter()
    print(f'Finished in {round(finish-start,4)} second(s)')
    
def multiprocessing_test1():
    start=time.perf_counter()
    p1=multiprocessing.Process(target=do_something)
    p2=multiprocessing.Process(target=do_something)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    finish=time.perf_counter()
    print(f'Finished in {round(finish-start,4)} second(s)')
def multiprocessing_test2():
    start=time.perf_counter()
    processes=[]
    for _ in range(10):
        p=multiprocessing.Process(target=do_something2, args=[1.5])
        p.start()
        processes.append(p)
    # all processes join and wait
    for process in processes:
        process.join()
    finish=time.perf_counter()
    print(f'Finished in {round(finish-start,4)} second(s)')
def concurrent_futures():
    start=time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as excurtor:       
        #Test1-----
        # f1=excurtor.submit(do_something3, 1)
        # f2=excurtor.submit(do_something3, 1)
        # print(f1.result())
        # print(f2.result())
        
        #Test2-----
        # secs=[5,4,3,2,1]
        # results=[excurtor.submit(do_something3, sec) for sec in secs]
        # for i in concurrent.futures.as_completed(results):
        #     print(i.result())
        
        #Test3-----
        secs=[5,4,3,2,1]
        secs2=[1,2,3,4,5]
        results=excurtor.map(do_something3,secs)
        for i in results:
            print(i)
    finish=time.perf_counter()
    print(f'Finished in {round(finish-start,4)} second(s)')
if __name__ == "__main__":
    concurrent_futures()
    

