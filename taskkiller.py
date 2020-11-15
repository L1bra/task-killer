import ctypes
import os


def get_tasks():
    with open('tasks.txt') as f:
        return [x.rstrip('\n') for x in f.readlines()]




def is_task_alive(tasks):
    for x in os.popen('tasklist').readlines():
        if len(x) > 1:
            task = x.split()[0]
            if task in tasks:
                return task


def main():
    tasks = get_tasks()

    while True:
        task = is_task_alive(tasks)
        if task:
            os.system(f'taskkill /f /im {task}')
            ctypes.windll.user32.MessageBoxW(0, 'Get back to work!', 'Alert!', 0)



if __name__ == "__main__":
    main()