"""Configuration for automated test suite, allows you to automatically
skip tests marked as slow unless you provide the --slow option
on the commandline when invoking pytest
"""

import pytest

def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true", help="run slow tests")

def pytest_runtest_setup(item):
    """
    Skip tests if they are marked as slow, unless the
    test run is explicitly specified to run the slow tests.
    """

    if 'slow' in item.keywords and not item.config.getoption("--slow"):
        pytest.skip("need --slow option to run")