from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

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

button_open_tiktok = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Predicted app: TikTok")
button_open_tiktok.click()

button_profile = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(6)")
button_profile.click()

button_close_auth = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Fechar")
button_close_auth.click()

button_open_menu = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Menu")
button_open_menu.click()

button_set_language = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.view.View\").instance(17)")
button_set_language.click()

button_select_language = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App language, Select your default app language")
button_select_language.click()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(741, 2768)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(752, 937)
actions.w3c_actions.pointer_action.release()
actions.perform()

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(872, 2717)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.move_to_location(915, 752)
actions.w3c_actions.pointer_action.release()
actions.perform()

radio_button_languague_portugues = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.RadioButton\").instance(7)")
radio_button_languague_portugues.click()

button_save_language = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Done")
button_save_language.click()

driver.quit()