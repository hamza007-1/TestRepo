from appium import webdriver
class Registration:
    button_skip_id ="com.km.emotika.staging:id/skipTextView"
    button_registration_id = "com.km.emotika:id/tvSignup"
    textbox_emailaddress_id ="com.km.emotika:id/etSignupEmailAddress"
    button_signup_id = "com.km.emotika:id/btnSignup"
    textbox_firstname_id = "com.km.emotika:id/etSignUpFirstname"
    textbox_lastname_id = "com.km.emotika:id/etSignUpLastName"
    textbox_password_id = "com.km.emotika:id/etSignupPassword"
    textbox_confirmpassword_id = "com.km.emotika:id/etConfirmPassword"
    toggle_notification_id = "com.km.emotika:id/cbNotify"
    checkbox_terms_id = "com.km.emotika:id/cbTermsAndCondition"
    button_signupregister_id = "com.km.emotika:id/btnSignUp"
    button_registok_id = "com.km.emotika:id/tvOk"



    def __init__(self,driver):
        self.driver=driver

    def clickSkip(self):
        self.driver.find_element_by_xpath(self.button_skip_xpath).click()

    def clickRegitration(self):
        self.driver.find_element_by_id(self.button_registration_id).click()

    def setEmailaddress(self, emailaddress):
        self.driver.find_element_by_id(self.textbox_emailaddress_id).clear()
        self.driver.find_element_by_id(self.textbox_emailaddress_id).send_keys(emailaddress)

    def clickSignup(self):
        self.driver.find_element_by_id(self.button_signup_id).click()

    def setFirstname(self, firstname):
        self.driver.find_element_by_id(self.textbox_firstname_id).clear()
        self.driver.find_element_by_id(self.textbox_firstname_id).send_keys(firstname)

    def setLastname(self, lastname):
        self.driver.find_element_by_id(self.textbox_lastname_id).clear()
        self.driver.find_element_by_id(self.textbox_lastname_id).send_keys(lastname)

    def setPassowrd(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def setConfirmpassword(self, confirmpassword):
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).clear()
        self.driver.find_element_by_id(self.textbox_confirmpassword_id).send_keys(confirmpassword)

    def clickToggle(self):
        self.driver.find_element_by_id(self.toggle_notification_id).click()

    def clickCheckboxterm(self):
        self.driver.find_element_by_id(self.checkbox_terms_id).click()

    def clickSignupregister(self):
        self.driver.find_element_by_id(self.button_signupregister_id).click()

    def clickRegisOK(self):
        self.driver.find_element_by_id(self.button_registok_id).click()




