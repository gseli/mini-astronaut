import pytest
from driver import driver

@pytest.fixture(scope='session', autouse=True)
def selenium():
    local_driver=driver
    yield local_driver
    driver.quit()