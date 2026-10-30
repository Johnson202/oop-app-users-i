# your User class goes here
class User:
    def __init__(self, name, email, driver_license_num, phone_number, dob):
        self.name = name
        self.email = email
        self.driver_license_num = driver_license_num
        self.phone_number = phone_number
        self.dob = dob
        
    def __str__(self):
        # represent the class as a readable string
        return f"User(name={self.name}, email={self.email}, driver_license_num={self.driver_license_num}, phone_number={self.phone_number}, dob={self.dob})"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value.strip()

    @property
    def email(self):
        return self._email

    # just simple data validation checks for practice (would use email-validator library in real-world application)
    @email.setter
    def email(self, value):
        if not isinstance(value, str):
            raise ValueError("Email must be a string.")
        
        stripped_email = value.strip()
        
        # check for @ symbol
        if not "@" in stripped_email or stripped_email.count('@') != 1:
            raise ValueError("Email must contain exactly 1 @ symbol.")
        
        # check left and right parts of email exist
        local_part, domain_part = stripped_email.split("@")
        if not local_part or not domain_part:
            raise ValueError("Email must have a local part (left of @) and a domain part (right of @).")
    
        # check domain part
        if not "." in domain_part:
            raise ValueError("Email domain part must contain at least one dot.")
        
        if domain_part[0] == "." or domain_part[-1] == ".":
            raise ValueError("Email domain part cannot start or end with a dot.")
            
        self._email = stripped_email

    @property
    def driver_license_num(self):
        return self._driver_license_num

    @driver_license_num.setter
    def driver_license_num(self, value):
        if not isinstance(value, str):
            raise ValueError("Driver license number must be a string.")
        self._driver_license_num = value.strip()

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not isinstance(value, str):
            raise ValueError("Phone number must be a string.")
        self._phone_number = value.strip()

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, value):
        if not isinstance(value, str):
            raise ValueError("Date of birth must be a string.")
        self._dob = value.strip()