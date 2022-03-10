import pytest

@pytest.yield_fixture()
def setup():
    print("Open URL to signup")
    yield
    print("Close the browser after signup")

def testEmail(setup):
    print("This is signup test by email")

def testFacebook(setup):
    print("This is signup test by facebook")