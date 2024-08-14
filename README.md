Запуск в терминале, из папки home_work\5_hw по команде docker-compose up --build

В терминале должен быть ответ вида

```
demoqa_home-selenium_test-1  | ============================= test session starts ==============================
demoqa_home-selenium_test-1  | platform linux -- Python 3.8.11, pytest-8.3.2, pluggy-1.5.0 -- /usr/local/bin/python
demoqa_home-selenium_test-1  | cachedir: .pytest_cache
demoqa_home-selenium_test-1  | rootdir: /app
demoqa_home-selenium_test-1  | collecting ... collected 3 items
demoqa_home-selenium_test-1  | 
demoqa_home-selenium_test-1  | tests/test_check_swag.py::test_check_icon PASSED
demoqa_home-selenium_test-1  | tests/test_check_swag.py::test_check_username_field PASSED
demoqa_home-selenium_test-1  | tests/test_check_swag.py::test_check_password_field PASSED
demoqa_home-selenium_test-1  | 
demoqa_home-selenium_test-1  | ============================== 3 passed in 3.20s ===============================
```
