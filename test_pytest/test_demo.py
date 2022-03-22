import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('../env.yml')))
    def test_demo(self, env):
        if 'test' in env:
            print("test")
            print(env)
        elif 'dev' in env:
            print('dev')
