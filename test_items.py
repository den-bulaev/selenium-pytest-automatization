link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_add_to_basket_button(browser):
    browser.get(link)
    btn = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    assert len(btn) == 1, "button not found" if len(btn) < 1 else "selector is not unique"
#   меньше 1 элемента в списке - кнопки нет; в ином случае - селектор не уникальный
#   если в списке 1 элемент - AssertionError не вызывается

# для проверки добавьте time.sleep(30) сразу после открытия ссылки
