from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from multiprocessing import Pool
import time

"""Change UserAgent in Chrome"""
options = webdriver.ChromeOptions()             # Add option var to transfer to driver
options.add_argument("user-agent=HelloWorld")   # Changing user agent.
                                                # List of UserAgents: https://developers.whatismybrowser.com/useragents/explore/
driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

"""Change UserAgent in Firefox"""
options = webdriver.FirefoxOptions()
options.set_preference("general.useragent.override", "HelloWorld")
driver = webdriver.Firefox(executable_path="./geckodriver.exe", options=options)

"""Use proxy server without authorization"""
from selenium.webdriver.chrome.service import Service
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=199.19.224.3:80")  # Proxy without authorization
driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)

"""Proxy using login and password"""
from seleniumwire import webdriver
proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@199.19.224.3:80"  # protocol: "login: password @ IP : port"
    }
}
driver = webdriver.Chrome(service=Service("./chromedriver.exe"), seleniumwire_optoins=proxy_options)

driver = webdriver.Chrome(service=Service("./chromedriver.exe"))  # Creating driver with default options

"""Disable WebDriver mode to look like real user"""
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(service=Service("./chromedriver.exe"), options=options)

"""Headless mode (фоновый режим)"""
options.add_argument("--headless")

"""Using cookies (user data)"""
import pickle
pickle.dump(driver.get_cookies(), open(f"{login}_cookies", "wb"))  # Save cookies

driver.get("https://vk.com/")                                      # "GET" method
for cookie in pickle.load(open(f"{login}_cookies", "rb")):         # Load cookies
    driver.add_cookie(cookie)

"""Locators and elements"""
search_field = driver.find_element_by_xpath("//input[@name='text']")
element1 = driver.find_elements_by_css_selector("$$('#uniq16365599061801')") #=id, .=class, [name='text']
element2 = driver.find_element(By.XPATH, "//input[@name='text']")

"""Switching frames"""
frame = driver.find_element_by_xpath("//iframe[@class='demo-frame']")  # If an element is in IFRAME, switch_to.frame() needed
driver.switch_to.frame(frame)
driver.switch_to.default_content()  # Come back to the def frame, once we are done with working on frames
driver.switch_to.parent_frame()     # Come back to the parent frame, once we are done with working on frames
driver.switch_to.window()            # Switch to one of the open tabs

"""Switching window tabs"""
window1 = driver.window_handles[0]
element1 = driver.find_element_by_xpath("//a[@data-id='images']").click()
window2 = driver.window_handles[1]
driver.switch_to.window(window1)
driver.switch_to.window(window2)

"""Expected conditions"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)  # waits 10 secs, then returns TimeOut exception
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-id='images']")))
                    EC.title_is()
                    EC.title_contains()
                    EC.presence_of_element_located()
                    EC.visibility_of_element_located()
                    EC.text_to_be_present_in_element()
                    EC.frame_to_be_available_and_switch_to_it()
                    EC.alert_is_present()

"""Implicit Waits"""
driver.implicitly_wait(10)  # Waits 10 secs if element(s) is unavailable, then returns NoSuchElementException
driver.get(url)
element2 = driver.find_element_by_xpath("//Something")

"""Actions"""
from selenium.webdriver.common.action_chains import ActionChains
draggable = driver.find_element_by_xpath("//div[@id='draggable']")
droppable = driver.find_element_by_xpath("//div[@id='droppable']")

driver.save_screenshot("file_name.png")  # Save a screenshot
search_field.send_keys('XPath for beginners')  # Input text
search_field.send_keys(Keys.ENTER)             # Input Key from keyboard
action1 = ActionChains(driver)
action1.click_and_hold(draggable).move_by_offset(50, 50).release().perform()  # release() - to release the button
action1.drag_and_drop_by_offset(draggable, 50, 50).perform()                  # perform() - to perform the action
action1.double_click().perform()
action1.context_click().perform()  # rightClick
action1.click_and_hold(draggable).pause(3).move_to_element(droppable).release().perform()  # pause() - in seconds
action1.drag_and_drop(draggable, droppable).perform()

"""Working with drop-down list <select>"""
from selenium.webdriver.support.ui import Select
driver.get("http://htmlbook.ru/html/select")
select1 = Select(driver.find_element_by_xpath("//select[@name='select2']"))
select1.deselect_all()        # (For multi-select - список множественного выбора) deselect all selected options
select1.deselect_by_index(0)  # deselect the option with index '0'
select1.select_by_index(1)
select1.select_by_visible_text("Крыса Лариса")

"""Popup dialogs (alerts)"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)            # waits 10 secs, then returns TimeOut exception
alert = wait.until(EC.alert_is_present())
alert.accept()      # OK
alert.dismiss()     # Cancel
alert.send_keys("text")

"""Navigating"""
driver.refresh()
driver.back()       # Back in browser's history
driver.forward()
driver.execute_script("window.scrollTo(X, Y)")  # Scroll a page to Y pixels down, X pixels right
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom of the page

"""Scroll a page with infinite loading"""
SCROLL_PAUSE_TIME = 0.5
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll to the bottom of the page
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

"""Multiprocessing (open multiple browsers)"""
from selenium import webdriver
from multiprocessing import Pool
from selenium.webdriver.chrome.service import Service
import time

def get_data(url):
    try:
        driver = webdriver.Chrome(service=Service("./chromedriver.exe"))
        driver.get(url=url)
        print(url)
        time.sleep(10)
    except Exception as ex:
        print("---------Exception-------")
        print(ex)
        print("------------------------")
    finally:
        driver.close()  # Closes one tab, but if just one tab was open, by default most browser will exit entirely
        driver.quit()  # Exits entire browser

if __name__ == '__main__':
    url = input("Enter url: ")
    processes = int(input("How many browsers at the same time needed? "))
    p = Pool(processes=processes)
    url_list = [url] * processes
    print(url_list)
    p.map(get_data, url_list)


