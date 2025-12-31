from appium.options.common import AppiumOptions
from selenium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:deviceName": "Pixel 6",
	"appium:automationName": "UiAutomator2",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True
})

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

button_open_tiktok = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Predicted app: TikTok")
button_open_tiktok.click()

button_open_shop = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().text(\"Loja\")")
button_open_shop.click()

header_screen_shop = driver.find_element(by=AppiumBy.ID,value="com.zhiliaoapp.musically:id/tqr")
text_screen_shop = "Não há mais produtos"

assert header_screen_shop.text == text_screen_shop

driver.quit()