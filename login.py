def login(username, password):
    correct_username = "admin"
    correct_password = "1234"

    if username == correct_username and password == correct_password:
        return "Login Successful"
    else:
        return "Invalid Username or Password"


print(login("admin", "1234"))
def logout():
    return "Logout Successful"
