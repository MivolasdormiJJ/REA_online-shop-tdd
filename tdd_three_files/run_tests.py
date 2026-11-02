"""Запуск тестов без установки дополнительных библиотек.

В терминале из любой папки:
    python tdd_three_files/run_tests.py

Для демонстрации TDD:
- коммит RED: большинство тестов красные (ошибки);
- следующий коммит GREEN: все тесты зелёные.
"""
import pathlib
import sys
import unittest


folder = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(folder))

# Находим все тесты из файла test_shop.py.
tests = unittest.defaultTestLoader.discover(
    start_dir=str(folder),
    pattern="test_shop.py",
)

# verbosity=2 выводит название и результат каждого теста.
result = unittest.TextTestRunner(verbosity=2).run(tests)

# Код выхода 1 позволяет GitHub/терминалу заметить ошибки.
sys.exit(0 if result.wasSuccessful() else 1)
