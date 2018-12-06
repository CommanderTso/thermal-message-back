def parse_login_error(errors):
    # example WTForm validation error dict:
    # {'username': ['Invalid email address.'], 'password': ['This field is required.']}
    if errors is None:
        return None
    elif 'username' in errors and errors['username'][0] == "Invalid email address.":
        return "Please enter a valid email address."
    elif 'password' in errors and errors['password'][0] == "This field is required.":
        return "You need to enter a password!"
    else:
        return errors[next(iter(errors))][0] # grab whatever key we can find and print that
