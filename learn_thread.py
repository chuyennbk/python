import threading
import logging
import time

def thread_func(name):
    logging.info('Thread %s starting', name)
    time.sleep(1)
    logging.info('Thread %s finished!', name)
if __name__ == '__main__':
    format='%(asctime)s: %(message)s' # dinh dang log in ra man hinh
    logging.basicConfig(format=format,level=logging.INFO,datefmt='%H:%M:%S')
    
    #1 thread
    # logging.info('Main   : before creating thread')
    # x=threading.Thread(target=thread_func,args=(1,))
    # logging.info('Main   : before running thread')
    # x.start()
    # logging.info('Main   : waiting for thread finish')
    # x.join() #doi thuc thi xong het cac thread
    # logging.info('Main   : Done!!!')
    
    #multi threads running
    # threads=list()
    # for i in range(3):
    #     logging.info("Main   : creating and start thread %d", i)
    #     x=threading.Thread(target=thread_func,args=(i,))
    #     threads.append(x)
    #     x.start()
    # for i, thread in enumerate(threads):
    #     logging.info("Main   : before joining thread %d", i)
    #     thread.join()
    #     logging.info("Main   : thread %d done!", i)   
    # logging.info("Main   : Done")
    
    #thread pool excutor
    import concurrent.futures as con
    with con.ThreadPoolExecutor(max_workers=100) as excutor:
        excutor.map(thread_func,range(100))
        

        
        
    
    