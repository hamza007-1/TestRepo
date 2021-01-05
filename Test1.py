import pytest
from appium import webdriver



desired_cap = {

  "platformName": "Android",
  "deviceName": "RF8M31XC6CF",
  "app": "C:\\Users\\Hamza\\Desktop\\Appium\\app-debug.apk"

}

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(50)
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView").click()

# email = driver.find_element_by_id("com.km.emotika:id/etEmailAddress")
# email.send_keys("sophia1@mailinator.com")
#
# password = driver.find_element_by_id("com.km.emotika:id/etPassword")
# password.send_keys("admin@1234")
#
# login = driver.find_element_by_id("com.km.emotika:id/btnLogin")
# login.click()


Registration = driver.find_element_by_id("com.km.emotika:id/tvSignup")
Registration.click()

RegistrationEmail = driver.find_element_by_id("com.km.emotika:id/etSignupEmailAddress")
RegistrationEmail.send_keys("hamza+2@mailinator.com")

driver.implicitly_wait(5)

signupClick = driver.find_element_by_id("com.km.emotika:id/btnSignup")
signupClick.click()

firstname = driver.find_element_by_id("com.km.emotika:id/etSignUpFirstname")
firstname.send_keys("Hamza")

Secondname = driver.find_element_by_id("com.km.emotika:id/etSignUpLastName")
Secondname.send_keys("Shafiq")

password = driver.find_element_by_id("com.km.emotika:id/etSignupPassword")
password.send_keys("Admin@1234")

confirmpassword = driver.find_element_by_id("com.km.emotika:id/etConfirmPassword")
confirmpassword.send_keys("Admin@1234")

checkbox = driver.find_element_by_id("com.km.emotika:id/cbTermsAndCondition")
checkbox.click()

SignUp = driver.find_element_by_id("com.km.emotika:id/btnSignUp")
SignUp.click()

driver.implicitly_wait(3)

driver.find_element_by_id("com.km.emotika:id/tvOk").click()



