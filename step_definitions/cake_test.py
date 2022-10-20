from pytest_bdd import scenario, given, when, then
from driver import driver

# add vegan scenario
@scenario(r'../features/cake.feature', "Vegans")
def test_cake():
    pass


@given("some of the cakes can be bought by vegans")
def step_impl(selenium):
    selenium.get('https://google.com')
    print(selenium.title)


@when("I mark the vegan cakes")
def step_impl():
    pass


@then("vegan cakes can only be bought by vegans")
def step_impl():
    pass


@then("I am a vegan")
def step_impl():
    pass
