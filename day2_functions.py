def add_tax(price, tax_rate):
    return price + (price * tax_rate)

result = add_tax(100, 0.2)
print(result)  # should print 120.0
def print_welcome_message(username):
    print(f"Welcome back, {username}!")

print_welcome_message("banut")
def login_attempt(username, password="wrong_password"):
    print(f"Trying to log in as {username} with password {password}")

login_attempt("standard_user")                      # uses the default password
login_attempt("standard_user", "secret_sauce")      # overrides it