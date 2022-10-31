from pytest_bdd import scenarios, given, when, then

scenarios(r'../features/fruits.feature')


@given("I have 5 bananas")
def step_impl(selenium):
    selenium.get('https://google.com')
    print(selenium.title)
    assert selenium.title == 'Google'


@when("I eat 2 bananas")
def step_impl():
    pass


@then("I should have 3 bananas")
def step_impl():
    pass