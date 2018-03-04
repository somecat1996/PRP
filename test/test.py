from __future__ import print_function
# from openvas_lib import report_parser
from threading import Semaphore
from functools import partial
from openvas_lib import VulnscanManager, VulnscanException



def my_print_status(i):
    print(str(i))


def my_launch_scanner():
    sem = Semaphore(0)

    # Configure
    manager = VulnscanManager("localhost", "admin", "admin")

    # Launch
    task, target = manager.launch_scan('10.10.10.130',
                        profile="empty",
                        callback_end=partial(lambda x: x.release(), sem),
                        callback_progress=my_print_status)

    # Wait
    sem.acquire()

    # Finished scan
    print("finished")
    print(task)
    print(target)
    manager.get_results(task_id=task)

# results = report_parser("metasploitable_all.xml")
# for i in results:
#     print(i.id)
#     print(i.host)
#     print(i.threat)
#     print('\n')
