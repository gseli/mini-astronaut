from selenium import webdriver

#set up a remote chrome driver options for automated testing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('enable-automation')

#set up chromedriver thats remote
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=chrome_options)