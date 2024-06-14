import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import  FileSystemEventHandler

from_dir = "C:/Users/Hp/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Hey {event.src_path} has been created!')
    def on_deleted(self, event):
        print(f'Oops! somebody deleted {event.src_path}!')
    def on_modified(self, event):
       print(f'{event.src_path} has been modified')
    def on_moved(self, event):
       print(f'{event.src_path} has been moved')

event_handler=FileEventHandler()
observer=Observer()
observer.schedule(event_handler,from_dir,recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped ...") 
    observer.stop()       