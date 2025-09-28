ERROR_MESSAGES_LOGIN_WORKER = {
    "timeout_login_elements_text": "Timeout ao buscar elementos de login. Possível lentidão ou problema de conexão.",
    "login_element_not_found_text": "Elemento de login não encontrado na página.",
    "redirect_no_success_message_text": "Redirecionado, mas mensagem de sucesso não encontrada.",
    "redirect_timeout_success_message_text": "Redirecionamento, mas mensagem de sucesso não encontrada (timeout).",
    "redirect_element_no_success_message_text": "Redirecionamento, mas mensagem de sucesso não encontrada.",
    "redirect_or_element_not_found_text": "Redirecionamento ou elemento de sucesso não encontrado.",
    "webdriver_timeout_text": "Timeout geral do WebDriver. Verifique conexão ou recursos do sistema.",
    "element_not_found_text": "Elemento não encontrado na página.",
    "webdriver_exception_text": "WebDriverException: {details}",
    "unexpected_error_text": "Erro inesperado: {details}",
    "save_html_failed_text": "Falha ao salvar HTML: {details}",
    "save_screenshot_failed_text": "Falha ao salvar screenshot: {details}",
    "driver_quit_failed_text": "Falha ao finalizar driver: {details}"
}

ERROR_MESSAGES_MAIN = {
    "invalid_arg_login_count": "Erro: Número de logins simultâneos deve ser entre 1 e 1000.",
    "missing_required_argument": "Argumento obrigatório ausente.",
    "environment_variable_error": "Erro ao carregar variável de ambiente."
}

ERROR_MESSAGES_DRIVERCONFIG = {
    "invalid_chromedriver_path": "Caminho do ChromeDriver inválido ou não encontrado. Verifique a variável CHROMEDRIVER_PATH.",
    "webdriver_start_failed": "Falha ao iniciar o WebDriver. Verifique se o ChromeDriver está instalado e compatível.",
    "webdriver_remote_failed": "Falha ao conectar ao Selenium Grid remoto. Verifique o endereço e conectividade.",
    "missing_chromedriver_env": "CHROMEDRIVER_PATH não definido no ambiente para execução local.",
    "unsupported_selenium_mode": "Modo Selenium não suportado: {mode}. Use 'local' ou 'grid'.",
    "driver_not_initialized": "WebDriver não foi inicializado corretamente.",
    "grid_connect_attempt": "Tentando conectar ao Selenium Grid: {selenium_remote_url}"
}