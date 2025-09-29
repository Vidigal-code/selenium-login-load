import os
from dotenv import load_dotenv

print("Loading .env file...")
load_dotenv()
print(".env file loaded!")

compose_file = 'docker-compose.yml'

if os.path.exists(compose_file):
    print("Deleting existing docker-compose.yml...")
    os.remove(compose_file)

with open(compose_file, 'w') as f:
    print("Generating docker-compose.yml (CLI only)...")
    f.write("services:\n")
    f.write("""  app:
    build: .
    container_name: selenium-login-load
    env_file:
      - .env
    volumes:
      - ./results:/app/results
    stdin_open: true
    tty: true
    command: >
      python -m source.main

networks:
  selenium-grid:
    driver: bridge
""")
print("docker-compose.yml generated successfully!")

print("Running: docker compose up --build app")
os.system("docker compose up --build app")