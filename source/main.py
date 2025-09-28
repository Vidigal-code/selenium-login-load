import os
from dotenv import load_dotenv
from source.system.run_logins import run_logins

load_dotenv()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Automação de logins simultâneos")
    parser.add_argument(
        "-n", "--num",
        type=int,
        help="Número de logins simultâneos"
    )
    args = parser.parse_args()

    CONCURRENT_LOGINS = int(os.getenv("CONCURRENT_LOGINS", 5))
    n_logins = args.num or CONCURRENT_LOGINS
    if n_logins <= 0 or n_logins > 1000:
        print("Erro: Número de logins simultâneos deve ser entre 1 e 1000.")
        exit(1)
    print(f"Processo iniciado: {n_logins} logins simultâneos.")
    run_logins(n_logins)