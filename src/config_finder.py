import argparse
import os


def parse_args():
    """
    Розбирає аргументи командного рядка.

    Підтримуються такі опції:
    -c
    --config

    Ці опції дозволяють явно передати шлях до конфігураційного файлу.
    """
    parser = argparse.ArgumentParser(
        description="Повертає шлях до конфігураційного файлу."
    )

    parser.add_argument(
        "-c",
        "--config",
        help="Шлях до конфігураційного файлу"
    )

    return parser.parse_args()


def get_config_path():
    """
    Визначає шлях до конфігураційного файлу за таким пріоритетом:
    1. Опція командного рядка -c / --config
    2. Змінна оточення CONFIG_PATH
    3. Значення за замовчуванням ~/.config.yaml

    Повертає:
        str: шлях до конфігураційного файлу
    """
    args = parse_args()

    # Якщо користувач передав шлях через аргумент командного рядка,
    # то використовуємо саме його.
    if args.config:
        return args.config

    # Якщо аргумент не був переданий, перевіряємо змінну оточення.
    env_config = os.environ.get("CONFIG_PATH")
    if env_config:
        return env_config

    # Якщо немає ні аргументу, ні змінної оточення,
    # повертаємо значення за замовчуванням.
    return "~/.config.yaml"


def main():
    """
    Основна функція програми.
    Виводить знайдений шлях до конфігураційного файлу.
    """
    config_path = get_config_path()
    print(config_path)


if __name__ == "__main__":
    main()
