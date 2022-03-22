import os

import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '--lf'])
    os.system('allure generate ./temp -o ./report --clean')
