from argparse import Namespace

from src.system_info import get_all_system_info
from src.system_info import save_to_file
from src.system_info import select_system_info


def test_get_all_system_info_keys():
    """
    Перевіряє, що функція повертає словник
    з усіма потрібними ключами.
    """
    result = get_all_system_info()

    assert isinstance(result, dict)
    assert "os" in result
    assert "version" in result
    assert "processor" in result
    assert "kernels" in result


def test_select_system_info_all_when_no_flags():
    """
    Якщо жодної інформаційної опції не передано,
    повинна повертатися повна інформація.
    """
    args = Namespace(
        os=False,
        version=False,
        processor=False,
        kernels=False,
        file=None
    )

    result = select_system_info(args)

    assert "os" in result
    assert "version" in result
    assert "processor" in result
    assert "kernels" in result


def test_select_system_info_only_os():
    """
    Перевіряє, що при виборі лише --os
    повертається словник тільки з ключем os.
    """
    args = Namespace(
        os=True,
        version=False,
        processor=False,
        kernels=False,
        file=None
    )

    result = select_system_info(args)

    assert list(result.keys()) == ["os"]


def test_select_system_info_os_and_version():
    """
    Перевіряє, що при виборі --os і --version
    повертаються лише ці два поля.
    """
    args = Namespace(
        os=True,
        version=True,
        processor=False,
        kernels=False,
        file=None
    )

    result = select_system_info(args)

    assert "os" in result
    assert "version" in result
    assert "processor" not in result
    assert "kernels" not in result


def test_select_system_info_processor_and_kernels():
    """
    Перевіряє, що при виборі --processor і --kernels
    повертаються лише ці два поля.
    """
    args = Namespace(
        os=False,
        version=False,
        processor=True,
        kernels=True,
        file=None
    )

    result = select_system_info(args)

    assert "processor" in result
    assert "kernels" in result
    assert "os" not in result
    assert "version" not in result


def test_save_to_file(tmp_path):
    """
    Перевіряє, що словник коректно записується у файл.
    """
    test_data = {
        "os": "Linux",
        "version": "6.8.0",
        "processor": "x86_64",
        "kernels": 8
    }

    file_path = tmp_path / "result.txt"

    save_to_file(file_path, test_data)

    content = file_path.read_text(encoding="utf-8")

    assert content == str(test_data)
