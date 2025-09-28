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
    args = parser.parse_args()

    CONCURRENT_LOGINS = int(os.getenv("CONCURRENT_LOGINS", 5))
    n_logins = args.num or CONCURRENT_LOGINS
    if n_logins <= 0 or n_logins > 1000:
        print(ERROR_MESSAGES_MAIN["invalid_arg_login_count"])
        exit(1)
    print(MESSAGE_SYSTEM_SUCESS_MAIN["logins_started_text"].format(n_logins=n_logins))
    run_logins(n_logins)