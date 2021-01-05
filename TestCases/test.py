import time

from PageObject.Registration import Registration


class Test_001_Registration:

    def test_registration_l01(self,setup):
        self.driver = setup
        self.rP = Registration(self.driver)
        self.rP.clickSkip()
        self.rP.clickRegitration()
        self.rP.setEmailaddress("hamza@gmail.com")
        self.rP.clickSignup()
        self.rP.setFirstname("hamza")
        self.rP.setLastname("shafiq")
        self.rP.setPassowrd("Admin@123")
        self.rP.setConfirmpassword("Admin@123")
        self.rP.clickCheckboxterm()
        self.rP.clickSignupregister()
        self.rP.clickRegisOK()


    # for future use
    def test_registration_l02(self,setup):






