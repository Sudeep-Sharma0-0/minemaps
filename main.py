import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from extract_zip import extract_zip
from extract_rar import extract_rar
from analyze_dir import analyze_dir


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            analyze_dir(event.src_path)
            return
        if event.src_path.endswith(".crdownload"):
            return
        if event.src_path.endswith(".zip"):
            extract_zip(event.src_path)
        elif event.src_path.endswith(".rar"):
            extract_rar(event.src_path)
        print(f"File {event.src_path} has been modified")

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".zip"):
            extract_zip(event.src_path)
        elif event.src_path.endswith(".rar"):
            extract_rar(event.src_path)
        print(f"File {event.src_path} has been created")

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f"File {event.src_path} has been deleted")


def main():
    folder_to_watch = os.path.join("~", "Downloads", "minemaps", "downloads")
    folder_to_watch = os.path.expanduser(folder_to_watch)
    os.makedirs(folder_to_watch, exist_ok=True)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
