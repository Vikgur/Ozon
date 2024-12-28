# Класс разных видов скролла.


class Scrolls:

    def __init__(self, driver, action):
        self.driver = driver
        self.action = action

    # Скролл по x и y
    def scroll_by(self, x, y):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")

    # Скролл в самый низ страницы
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # Скролл на самый верх страницы
    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0)")

    # Скролл к элементу с раскрытием контента под ним
    def scroll_to_element(self, element):
        self.action.scroll_to_element(element).perform()
        self.driver.execute_script(
            """
        window.scrollTo({
            top: window.scrollY + 500,
        });
        """
        )

    # Скролл к элементу в центре страницы
    def scroll_to_center(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({ block: 'center' });", element
        )
