"""Решение домашнего задания №7 - Тест-файл с тест кейсами"""
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage



def test_check_footer_text(driver) -> None:
    """2. в файле test_check_text.py реализуйте таст кейс:
    a. перейти на страницу 'https://demoqa.com/'
    b. проверить что текст в подвале == ‘© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’"""
    demo_qa_page = DemoQa(driver)
    demo_qa_page.visit()
    assert (
        demo_qa_page.text_footer.get_text()
        == "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."
    ) 

def test_elements_text(driver):
    """3. в файле test_check_text.py реализуйте таст кейс:
    a. перейти на страницу 'https://demoqa.com/'
    b. через кнопку перейти на страницу 'https://demoqa.com/elements'
    c. проверить что текст по центру == 'Please select an item from left to start practice.'"""
    demo_qa_page = DemoQa(driver)
    elements_page = ElementsPage(driver)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    assert (demo_qa_page.btn_elements.exist())
    demo_qa_page.btn_elements.click()

    assert elements_page.equal_url()

    assert (elements_page.text_center.get_text()
        == "Please select an item from left to start practice.")