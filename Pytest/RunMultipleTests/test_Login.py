import pytest

@pytest.yield_fixture()
def setup():
    print("Open URL to login")
    yield
    print("Close browser after login")

def testEmail(setup):
    print("This is login test by email")

def testFacebook(setup):
    print("This is login test by facebook")

