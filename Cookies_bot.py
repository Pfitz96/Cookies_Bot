from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from Selenium_config import (
    URL,
    get_chrome_web_driver,
    get_chrome_options,
    set_chrome_incognito,
)


class CookieAPI:
    def __init__(self, page_url):
        self.page_url = page_url
        options = get_chrome_options()
        set_chrome_incognito(options)
        self.driver = get_chrome_web_driver(options)
        self.number = 2

    def run(self):
        self.driver.get(self.page_url)
        self.driver.implicitly_wait(5)
        bigCookie = self.driver.find_element_by_id("bigCookie")
        cookie_count = self.driver.find_element_by_id("cookies")
        actions = ActionChains(self.driver)
        actions.click(bigCookie)
        while True:
            actions.perform()
            counter = (cookie_count.text.split(" ")[0]).replace(",", "")
            count = int(counter)
            print(count)
            if count > 1000 and self.number > 9:
                self.number += 1
            else:
                for product_price in self.productPrice():
                    val = (product_price.text).replace(",", "")
                    value = int(val)
                    if count >= value:
                        buy_actions = ActionChains(self.driver)
                        buy_actions.move_to_element(product_price)
                        num = self.productPrice().index(product_price)
                        buy_actions.click()
                        buy_actions.perform()
                        product_name = self.driver.find_element_by_id("productName" + str(num))
                        print(product_name.text + " upgraded!")


    def productPrice(self):
        try:
            products_price = [self.driver.find_element_by_id("productPrice" + str(i)) for i in range(self.number)]
            return products_price

        except NoSuchElementException:
            print("Can't get the prices!")


if __name__ == '__main__':
    api = CookieAPI(URL)
    api.run()

