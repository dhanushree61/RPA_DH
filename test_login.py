def test_valid_login():
    username = "testuser"
    password = "correctpassword"
    assert login(username, password) == "Dashboard"

def test_invalid_login():
    username = "testuser"
    password = "wrongpassword"
    assert login(username, password) == "Invalid username or password"
