def is_valid_login(username, password):
    return username == "standard_user" and password == "secret_sauce"

print(is_valid_login("standard_user", "secret_sauce"))   # expect True
print(is_valid_login("standard_user", "wrong_password"))  # expect False