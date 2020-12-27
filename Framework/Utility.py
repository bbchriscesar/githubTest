from appium import webdriver
import os.path
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

xpath = By.XPATH
id = By.ID
css = By.CSS_SELECTOR
name = By.NAME
className = By.CLASS_NAME

def setupDriver(appPackage, appActivity, udid, systemPort):
    global driver
    capabilities = {
        'platformName': 'Android',
        'deviceName': 'Pixel 2',
        'appPackage': appPackage,
        'appActivity': appActivity,
        'udid': udid,
        'systemPort': systemPort,
        'automationName': 'UiAutomator2',
        'noReset': True,
        'orientation': 'PORTRAIT',
        'uiautomator2ServerLaunchTimeout': '5000'
    }
    url = 'http://localhost:4723/wd/hub'
    driver = webdriver.Remote(url, capabilities)
    return driver

def takeScreenshot(filename):
    time.sleep(1)
    driver.save_screenshot(filename + '.png')
    b = os.path.split(filename)[1]
    print('Take screenshot for ' + b)

def findAndClick(locator, value):
    driver.find_element(locator, value).click()
    time.sleep(1)

def findAndClickElements(locator, value, index):
    driver.find_elements(locator, value)[index].click()
    time.sleep(1)

def changeLocale(udid, lang):
    adb = 'adb -s ' + udid + ' shell am broadcast -a com.google.android.testing.i18n.localeswitcher.CHANGE_LOCALE -e LANGUAGE_TAG ' + lang
    os.system(adb)
    time.sleep(1)

def startApp(udid, appPackageappActivity):
    adb = 'adb -s ' + udid + ' shell am start -n ' + appPackageappActivity
    os.system(adb)
    time.sleep(2)

def stopApp(udid, appPackage):
    adb = 'adb -s ' + udid + ' shell am force-stop ' + appPackage
    os.system(adb)
    time.sleep(1)

def tearDown(udid):
    adb = 'adb -s ' + udid + ' shell am broadcast -a com.google.android.testing.i18n.localeswitcher.CHANGE_LOCALE -e LANGUAGE_TAG en-US'
    os.system(adb)
    driver.quit()

def moveBack():
    driver.back()
    time.sleep(2)

def swipeUp(x1, y1, x2, y2, delay):
    driver.swipe(x1, y1, x2, y2, delay)
    time.sleep(2)

def swipeDown(x2, y2, x1, y1, delay):
    driver.swipe(x2, y2, x1, y1, delay)
    time.sleep(2)

def clickElement(x_coordinates, y_coordinates):
    TouchAction(driver).tap(x=x_coordinates, y=y_coordinates).perform()
    time.sleep(2)

def waitForElement(locator, value):
    wait = WebDriverWait(driver, 60)
    try:
        element = wait.until(EC.element_to_be_clickable((locator, value)))
        print('Waiting for the element to be clickable')
    except Exception as ex:
        print(ex)

def customDelay(secondsToDelay):
    time.sleep(secondsToDelay)
    print('Added ' + str(secondsToDelay) + ' seconds to delay')

def swipeLeft(udid):
    adb = 'adb -s ' + udid + ' shell input swipe 944 1687 118 1697 2000'
    os.system(adb)
    time.sleep(2)

def expandNotificationBar(udid):
    adb = 'adb -s ' + udid + ' shell cmd statusbar expand-notifications'
    os.system(adb)
    time.sleep(2)

def collapseNotificationBar(udid):
    adb = 'adb -s ' + udid + ' shell cmd statusbar collapse'
    os.system(adb)
    time.sleep(2)

def homeScreen(udid):
    adb = 'adb -s ' + udid + ' shell input keyevent KEYCODE_HOME'
    os.system(adb)
    time.sleep(1)