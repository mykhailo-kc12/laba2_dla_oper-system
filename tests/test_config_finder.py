from src.config_finder import get_config_path


def test_get_config_path_from_command_line(monkeypatch):
    """
    Перевіряє, що шлях береться з аргументів командного рядка,
    якщо передано опцію --config.
    """
    monkeypatch.setattr(
        "sys.argv",
        ["program_name", "--config", "/tmp/my_config.yaml"]
    )
    monkeypatch.delenv("CONFIG_PATH", raising=False)

    result = get_config_path()

    assert result == "/tmp/my_config.yaml"


def test_get_config_path_from_short_option(monkeypatch):
    """
    Перевіряє, що шлях береться з короткої опції -c.
    """
    monkeypatch.setattr(
        "sys.argv",
        ["program_name", "-c", "/etc/test.yaml"]
    )
    monkeypatch.delenv("CONFIG_PATH", raising=False)

    result = get_config_path()

    assert result == "/etc/test.yaml"


def test_get_config_path_from_environment(monkeypatch):
    """
    Перевіряє, що шлях береться зі змінної оточення CONFIG_PATH,
    якщо аргумент командного рядка не передано.
    """
    monkeypatch.setattr("sys.argv", ["program_name"])
    monkeypatch.setenv("CONFIG_PATH", "/home/user/config.yaml")

    result = get_config_path()

    assert result == "/home/user/config.yaml"


def test_get_config_path_default_value(monkeypatch):
    """
    Перевіряє, що повертається значення за замовчуванням,
    якщо немає ні аргументу командного рядка, ні змінної оточення.
    """
    monkeypatch.setattr("sys.argv", ["program_name"])
    monkeypatch.delenv("CONFIG_PATH", raising=False)

    result = get_config_path()

    assert result == "~/.config.yaml"


def test_command_line_has_priority_over_environment(monkeypatch):
    """
    Перевіряє, що аргумент командного рядка має вищий пріоритет,
    ніж змінна оточення.
    """
    monkeypatch.setattr(
        "sys.argv",
        ["program_name", "--config", "/priority/config.yaml"]
    )
    monkeypatch.setenv("CONFIG_PATH", "/env/config.yaml")

    result = get_config_path()

    assert result == "/priority/config.yaml"
