MESSAGE_SYSTEM_SUCESS_MAIN = {
    "auto_text_info_text": "Automação de logins simultâneos",
    "info_num_sum_text": "Número de logins simultâneos",
    "exe_interface_gui_text": "Executar com interface gráfica",
    "logins_started_text": "Processo iniciado: {n_logins} logins simultâneos.",
    "logins_completed_text": "Todos os logins foram executados. Tempo total: {total_time}s.",
    "results_exported_json_text": "Resultados exportados para {json_path}.",
    "results_exported_csv_text": "Resultados exportados para {csv_path}.",
    "summary_saved_text": "Resumo salvo em {summary_path}.",
    "gui_started_text": "Interface gráfica iniciada com sucesso.",
    "login_sucess_text": "Login realizado com sucesso para ID {login_id}."
}


MESSAGE_SYSTEM_LOGIN_WORKER = {
    "driver_initialized_text": "WebDriver inicializado para login ID {login_id}.",
    "driver_quit_text": "WebDriver finalizado para login ID {login_id}.",
    "screenshot_saved_text": "Screenshot salvo em {screenshot_path}.",
    "html_saved_text": "HTML salvo em {html_path}.",
    "status_failed_text":"Failed",
    "status_success_text_page": "SUCCESS",
    "status_success_text_page_condition": "You logged into a secure area!"
}

MESSAGE_SYSTEM_RUN_LOGINS = {
    "start_logins_text": "\nIniciando {n_logins} logins simultâneos...",
    "login_status_text": "[{index}] ID: {login_id} | Status: {status} | Tempo: {time_seconds}s",
    "total_time_text": "\nTempo total de execução: {total_time}s",
    "results_exported_json_text": "Resultados exportados para {json_path}",
    "results_exported_csv_text": "Resultados exportados para {csv_path}",
    "summary_header_text": "Total de logins: {n_logins}\nTempo total: {total_time}s\n",
    "summary_entry_text": "[{index}] ID: {login_id} | {status} - {time_seconds}s\n",
    "summary_saved_text": "Resumo salvo em {summary_path}"
}

MESSAGE_SYSTEM_DRIVERCONFIG = {
    "driver_init_local": "Inicializando WebDriver local...",
    "driver_init_remote": "Inicializando WebDriver remoto (Grid)...",
    "driver_headless_mode": "Modo headless ativado.",
    "driver_non_headless_mode": "Modo headless desativado.",
    "driver_config_complete": "Configuração do WebDriver concluída.",
    "driver_config_start": "Iniciando configuração do WebDriver...",
    "driver_config_env_loaded": "Variáveis de ambiente carregadas para configuração do driver.",
    "driver_timeout_set": "Timeout de carregamento de página definido para {timeout}s.",
    "driver_options_applied": "Opções do Chrome aplicadas ao WebDriver.",
    "driver_started_ok": "WebDriver iniciado com sucesso.",
    "driver_shutdown_ok": "WebDriver finalizado corretamente.",
    "driver_shutdown_failed": "Falha ao finalizar o WebDriver: {details}",
    "selenium_mode_info": "Modo Selenium: {selenium_mode}"
}