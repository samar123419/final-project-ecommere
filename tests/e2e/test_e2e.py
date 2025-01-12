import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class TestDefaultSuite():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.get("http://127.0.0.1:8000/#/")
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

  def test_search_button(self):
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("booties")
    time.sleep(2)
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    assert True

  def test_search_accourding_category(self):
    self.driver.find_element(By.NAME, "q")
    self.driver.find_element(By.NAME, "q").send_keys("toys")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(3)
    div = self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div")
    div_content = div.get_attribute("innerHTML").strip()

    assert div_content != ""

    print(self.driver.page_source) 

  def test_buy_items(self):
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR,"#navbarScroll > div > a:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR,"#email").click()
    self.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("samar1@mail.com")
    self.driver.find_element(By.CSS_SELECTOR,"#password").click()
    self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Keys.ENTER)
    time.sleep(1)
    self.driver.find_element(By.NAME, "q").click()
    self.driver.find_element(By.NAME, "q").send_keys("booties")
    self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div:nth-child(4) > div > a").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    time.sleep(2)

    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div.col-md-4 > div > div.list-group-item > button").click()
    time.sleep(2)

    self.driver.find_element(By.ID, "address").click()
    self.driver.find_element(By.ID, "address").send_keys("Israel")

    time.sleep(2)
    self.driver.find_element(By.ID, "city").click()
    self.driver.find_element(By.ID, "city").send_keys("Rahat")

    time.sleep(1)

    self.driver.find_element(By.ID, "postalCode").click()
    self.driver.find_element(By.ID, "postalCode").send_keys("123456")
    time.sleep(2)
    self.driver.find_element(By.ID, "country").click()
    self.driver.find_element(By.ID, "country").send_keys("israel")

    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    time.sleep(3)
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div.row > div.col-md-4 > div > div > div:nth-child(7) > button").click()
    time.sleep(5)
    assert "Order:" in self.driver.page_source
    assert True

  def test_login(self):
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR,"#navbarScroll > div > a:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR,"#email").click()
    self.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("samar1@mail.com")
    self.driver.find_element(By.CSS_SELECTOR,"#password").click()
    self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
    self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Keys.ENTER)
    time.sleep(1)
    assert True

  def test_add_items_to_card(self):
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(4) .card-img").click()
    time.sleep(1)
    # self.driver.execute_script("window.scrollTo(0,432.79998779296875)")
    self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".active > img").click()
    time.sleep(1)
    self.driver.execute_script("window.scrollTo(0, 1100)")
    time.sleep(2)
    self.driver.find_element(By.LINK_TEXT, "2").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(8) .card-img").click()
    time.sleep(2)
    self.driver.execute_script("window.scrollTo(0, 100)")
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    time.sleep(2)
    # self.driver.find_element(By.CSS_SELECTOR,"#root > header > nav > div > a").click()
    # time.sleep(2)
    # self.driver.execute_script("window.scrollTo(0, 1100)")
    # time.sleep(2)
    # self.driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    # time.sleep(2)
    assert "Shopping Cart" in self.driver.page_source

  def test_add_delete_items_from_card(self):
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, "#root > header > nav > div > a").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".col-xl-3:nth-child(1) .card-img").click()
    time.sleep(2)
    self.driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(4)
    self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div.col-md-8 > div > div > div > div.col-md-1 > button").click()
    WebDriverWait(self.driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".list-group-item:nth-child(2) .fas"))
    )
    assert True


# def test_add_item_to_card(self):
#     # time.sleep(3)
#     self.driver.find_element(By.NAME, "q")
#     self.driver.find_element(By.NAME, "q").send_keys("gloves")
#     self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
#     time.sleep(2)
#     self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div:nth-child(4) > div > div > a > div > strong").click()
#     time.sleep(2)
#     self.driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
#     time.sleep(2)
#     assert "Shopping Cart" in self.driver.page_source

 # def test_addreview(self):
  #   self.driver.find_element(By.NAME, "q").click()
  #   self.driver.find_element(By.NAME, "q").send_keys("WHITE SWEATER")
  #   self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
  #   time.sleep(2)
  #   self.driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a > img").click()
  #   time.sleep(3)
  #   self.driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(2) > div > div > div:nth-child(2) > div > a").click()
  #   time.sleep(3)
  #   self.driver.find_element(By.CSS_SELECTOR,"#email").click()
  #   self.driver.find_element(By.CSS_SELECTOR, "#email").send_keys("samar1@mail.com")
  #   self.driver.find_element(By.CSS_SELECTOR,"#password").click()
  #   self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123456")
  #   self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(Keys.ENTER)

  #   time.sleep(2)
  #   self.driver.execute_script("window.scrollTo(0,702.4000244140625)")

  #   time.sleep(60)

  #   self.driver.find_element(By.ID, "rating").click()

  #   dropdown = self.driver.find_element(By.ID, "rating")
  #   dropdown.find_element(By.XPATH, "//option[. = '4 - Very Good']").click()
  #   time.sleep(5)

  #   self.driver.find_element(By.ID, "comment").click()
  #   self.driver.find_element(By.ID, "comment").send_keys("beautiful sweater ")
  #   self.driver.find_element(By.CSS_SELECTOR, ".my-3:nth-child(3)").click()

  #   time.sleep(10)
