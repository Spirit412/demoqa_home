Запуск в терминале по команде docker-compose up --build

В терминале должен быть ответ вида

```
========================= 5 passed in 62.10s (0:01:02) =========================
============================= test session starts ==============================
platform linux -- Python 3.8.11, pytest-8.3.2, pluggy-1.5.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
collecting ... collected 5 items

tests/test_check_swag.py::test_check_icon PASSED
tests/test_check_swag.py::test_check_username_field PASSED
tests/test_check_swag.py::test_check_password_field PASSED
tests/tests_hw/test_check_text.py::test_check_footer_text PASSED
tests/tests_hw/test_check_text.py::test_elements_text PASSED

========================= 5 passed in 62.17s (0:01:02) =========================
```
