from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture
def client():
    return TestClient(app_module.app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Keep each test isolated from in-memory mutations.
    initial_state = deepcopy(app_module.activities)
    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_state))

    yield

    app_module.activities.clear()
    app_module.activities.update(deepcopy(initial_state))
