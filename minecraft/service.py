from mctools import QUERYClient


def get_online(server_ip: str, port: int) -> int:
    """Возвращает онлайн сервера

    Args:
        server_ip (str): Ip или хост сервера
        port (int): Порт

    Returns:
        int: Кол-во игроков онлайн
    """
    try:
        client = QUERYClient(server_ip, port, timeout=1)
        online_players = client.get_basic_stats()["numplayers"]
        return online_players
    except Exception as e:
        print(f"Ошибка подключения к серверу {server_ip}:{port} - {str(e)}")
        return 0


def get_online_servers(lst: list[tuple[str, int]]) -> list[int]:
    """
    Возвращает список онлайна серверов

    Args:
        lst (list[tuple[str, int]]): Список кортежей, содержащих ip и порт серверов

    Returns:
        list[int]: Список онлайна серверов. Если сервер недоступен, значение онлайна будет 0.
    """
    onlines = []
    for host, port in lst:
        onlines.append(get_online(host, port))
    return onlines
