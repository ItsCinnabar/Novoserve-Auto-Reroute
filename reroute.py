from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyderman

#Install chrome driver
driver_path = pyderman.install(browser=pyderman.chrome,overwrite=True,verbose=False)

options=Options()
options.headless=True
with webdriver.Chrome(executable_path=driver_path, options=options) as driver:
    url = "http://lg.novoserve.com/rerouteintel.php"
    driver.get(url)
    passed=False
    for _ in range(15):
        if b"The results are in!" in driver.page_source.encode("utf-8"):
            passed = True
            break
        else:
            time.sleep(60)
    if not passed:
        raise StopIteration("Failed to set routes")
        
