import PySimpleGUI as sg
from threading import Thread
from queue import Queue
from dotenv import load_dotenv
import os
from source.messages.message_system import MESSAGE_SYSTEM_GUI

load_dotenv()

def start_gui():
    from source.system.run_logins import run_logins_with_queue

    default_logins = os.getenv("CONCURRENT_LOGINS", "5")
    min_logins = int(os.getenv("MIN_LOGINS", "1"))
    max_logins = int(os.getenv("MAX_LOGINS", "1000"))
    layout = [
        [sg.Text(MESSAGE_SYSTEM_GUI["input_label_text"]), sg.InputText(default_logins, key="-N-")],
        [sg.Button(MESSAGE_SYSTEM_GUI["button_execute_text"]), sg.Button(MESSAGE_SYSTEM_GUI["button_exit_text"])],
        [sg.Output(size=(80, 20), key=MESSAGE_SYSTEM_GUI["output_key_text"])]
    ]
    window = sg.Window(MESSAGE_SYSTEM_GUI["window_title_text"], layout)
    thread = None
    queue = Queue()

    while True:
        event, values = window.read(timeout=100)
        if event in (sg.WINDOW_CLOSED, MESSAGE_SYSTEM_GUI["button_exit_text"]):
            break
        if event == MESSAGE_SYSTEM_GUI["button_execute_text"] and not thread:
            try:
                n_logins = int(values["-N-"])
                if n_logins < min_logins or n_logins > max_logins:
                    raise ValueError
            except Exception:
                window[MESSAGE_SYSTEM_GUI["output_key_text"]].update(
                    ERROR_MESSAGES_GUI["invalid_login_count"].format(min_logins=min_logins, max_logins=max_logins)
                )
                continue
            window[MESSAGE_SYSTEM_GUI["output_key_text"]].update("")
            print(MESSAGE_SYSTEM_GUI["executing_logins_text"].format(n_logins=n_logins))
            thread = Thread(target=run_logins_with_queue, args=(n_logins, queue), daemon=True)
            thread.start()
        while not queue.empty():
            msg = queue.get()
            print(msg)
    window.close()