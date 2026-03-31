import argparse
import platform
import os


def parse_args():
    """
    Розбирає аргументи командного рядка.

    Підтримуються такі опції:
    -o, --os - назва операційної системи
    -v, --version - версія ядра ОС
    -p, --processor - архітектура процесора
    -k, --kernels - кількість логічних ядер процесора
    -f, --file - ім'я файлу для збереження результату
    """
    parser = argparse.ArgumentParser(
        description="Збирає інформацію про параметри системи."
    )

    parser.add_argument(
        "-o",
        "--os",
        action="store_true",
        help="Показати назву операційної системи"
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Показати версію ядра ОС"
    )
    parser.add_argument(
        "-p",
        "--processor",
        action="store_true",
        help="Показати архітектуру процесора"
    )
    parser.add_argument(
        "-k",
        "--kernels",
        action="store_true",
        help="Показати кількість логічних ядер процесора"
    )
    parser.add_argument(
        "-f",
        "--file",
        help="Ім'я файлу для збереження результату"
    )

    return parser.parse_args()


def get_all_system_info():
    """
    Збирає повну інформацію про систему.

    Повертає:
        dict: словник з усіма параметрами системи
    """
    return {
        "os": platform.system(),
        "version": platform.release(),
        "processor": platform.machine(),
        "kernels": os.cpu_count()
    }


def select_system_info(args):
    """
    Формує словник з інформацією про систему залежно від обраних опцій.

    Якщо користувач не вказав жодної з опцій:
    --os, --version, --processor, --kernels,
    тоді повертається повна інформація.

    Параметри:
        args - об'єкт з аргументами командного рядка

    Повертає:
        dict: словник лише з потрібними користувачу даними
    """
    all_info = get_all_system_info()

    # Якщо жодна інформаційна опція не вказана,
    # повертаємо повний словник.
    if not (args.os or args.version or args.processor or args.kernels):
        return all_info

    selected_info = {}

    # Додаємо в словник тільки ті значення,
    # які були запитані користувачем.
    if args.os:
        selected_info["os"] = all_info["os"]

    if args.version:
        selected_info["version"] = all_info["version"]

    if args.processor:
        selected_info["processor"] = all_info["processor"]

    if args.kernels:
        selected_info["kernels"] = all_info["kernels"]

    return selected_info


def save_to_file(file_name, data):
    """
    Зберігає словник у файл у вигляді тексту.

    Параметри:
        file_name (str): ім'я файлу
        data (dict): словник з даними
    """
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(str(data))


def main():
    """
    Основна функція програми.

    Якщо вказано опцію --file, результат записується у файл.
    Якщо опція --file не вказана, результат виводиться на екран.
    """
    args = parse_args()
    result = select_system_info(args)

    if args.file:
        save_to_file(args.file, result)
    else:
        print(result)


if __name__ == "__main__":
    main()
