from threading import Semaphore
import scanner_lib
from functools import partial


def my_print_status(i):
    print(str(i))

sem = Semaphore(0)
manager = scanner_lib.ScannerManager("localhost", "admin", "admin")
task = manager.launch_scan('my_pc',
                        profile="Full and fast",
                        callback_end=partial(lambda x: x.release(), sem),
                        callback_progress=my_print_status)
sem.acquire()
manager.get_results(task)
manager.display_result(task)