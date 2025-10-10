import os
from dotenv import load_dotenv
from source.system.run_logins import run_logins
from source.messages.message_errors import ERROR_MESSAGES_MAIN
from source.messages.message_system import MESSAGE_SYSTEM_SUCESS_MAIN

load_dotenv()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=MESSAGE_SYSTEM_SUCESS_MAIN["auto_text_info_text"])
    parser.add_argument(
        "-n", "--num",
        type=int,
        help=MESSAGE_SYSTEM_SUCESS_MAIN["info_num_sum_text"]
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        help="Máximo de workers concorrentes (substitui MAX_CONCURRENT)",
        default=None
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help=MESSAGE_SYSTEM_SUCESS_MAIN["exe_interface_gui_text"]
    )
    args = parser.parse_args()

    min_logins = int(os.getenv("MIN_LOGINS", "1"))
    max_logins = int(os.getenv("MAX_LOGINS", "1000"))

    if args.gui:
        from source.interface.gui import start_gui
        print(MESSAGE_SYSTEM_SUCESS_MAIN["gui_started_text"])
        start_gui()
    else:
        CONCURRENT_LOGINS = int(os.getenv("CONCURRENT_LOGINS", "5"))
    n_logins = args.num or CONCURRENT_LOGINS
    max_workers = args.max_workers
        if n_logins < min_logins or n_logins > max_logins:
            print(f"{ERROR_MESSAGES_MAIN['invalid_arg_login_count']} ({min_logins} e {max_logins})")
            exit(1)
        print(MESSAGE_SYSTEM_SUCESS_MAIN["logins_started_text"].format(n_logins=n_logins))
        if max_workers:
            run_logins(n_logins, max_workers=max_workers)
        else:
            run_logins(n_logins)