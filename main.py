from User import User

user1 = User("John Doe", "john.doe1@email.com", "1q98y6r43hh3er9087e", "123-456-7890", "1985-05-15")
print(user1)

# test parameters out of order for different user
user2 = User(dob="1990-01-01", name="Greg Jones", email="greg.jones123@example.com", driver_license_num="2255yhg4", phone_number="098-765-4321")
print(user2)

# test bad input for email
# user3 = User("Jane Smith", "jane.smith.email.com", "1q98y6r43hh3er9087e", "123-456-7890", "1985-05-15")
# user3 = User("Jane Smith", "jane.smith@examplecom", "1q98y6r43hh3er9087e", "123-456-7890", "1985-05-15")
# user3 = User("Jane Smith", "jane.smith@.com", "1q98y6r43hh3er9087e", "123-456-7890", "1985-05-15")
# print(user3)

# test putting extra whitespace around inputs
user3 = User("          Jane Smith   ", "   jane.smith@email.com ", " 1q98y6r43hh3er9087e  ", "  123-456-7890    ", " 1985-05-15 ")
print(user3)