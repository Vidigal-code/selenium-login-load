import os
from dotenv import load_dotenv

print("Carregando .env...")
load_dotenv()
print("Lido .env!")

GRID_NODES = int(os.getenv("GRID_NODES", "1"))
print(f"GRID_NODES lido: {GRID_NODES}")

compose_file = 'docker-compose.yml'

if os.path.exists(compose_file):
    print("Excluindo docker-compose.yml existente...")
    os.remove(compose_file)

base_node = """
  node-chrome-{i}:
    image: selenium/node-chrome:4.35.0
    depends_on:
      selenium-hub:
        condition: service_healthy
    environment:
      SE_EVENT_BUS_HOST: selenium-hub
      SE_EVENT_BUS_PUBLISH_PORT: 4442
      SE_EVENT_BUS_SUBSCRIBE_PORT: 4443
      SE_NODE_MAX_SESSIONS: 2
    networks:
      - selenium-grid
"""

with open(compose_file, 'w') as f:
    print("Gerando docker-compose.yml...")
    f.write("services:\n")
    f.write("  selenium-hub:\n")
    f.write("    image: selenium/hub:latest\n")
    f.write("    container_name: selenium-hub\n")
    f.write('    ports:\n      - "4444:4444"\n')
    f.write("    environment:\n      GRID_MAX_SESSION: 50\n      GRID_BROWSER_TIMEOUT: 300\n      GRID_TIMEOUT: 300\n")
    f.write("    healthcheck:\n      test: [\"CMD\", \"curl\", \"-f\", \"http://localhost:4444/status || exit 1\"]\n      interval: 10s\n      timeout: 5s\n      retries: 12\n")
    f.write("    networks:\n      - selenium-grid\n")
    for i in range(1, GRID_NODES+1):
        print(f"Adicionando node-chrome-{i}")
        f.write(base_node.format(i=i))
    f.write("""
  app:
    build: .
    container_name: selenium-login-load
    depends_on:
      - selenium-hub
    env_file:
      - .env
    volumes:
      - ./results:/app/results
    stdin_open: true
    tty: true
    networks:
      - selenium-grid

networks:
  selenium-grid:
    driver: bridge
""")
print("docker-compose.yml gerado com sucesso!")

print("Executando: docker compose up --build")
os.system("docker compose up --build")