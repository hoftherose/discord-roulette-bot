import asyncio
import pytest
from unittest.mock import patch

from tests.conftest import noop
from tests.services.mock_user import *

from src.services.users import (
    get_all_users,
    get_user_by_id,
    create_user,
    change_user_name,
    remove_user,
    Users,
)


@pytest.mark.asyncio
async def test_get_all_users(monkeypatch):
    monkeypatch.setattr(Users, "get_all", mock_get_all)
    users = await get_all_users()
    assert len(users) == 4


@pytest.mark.asyncio
async def test_get_user_by_id(monkeypatch):
    monkeypatch.setattr(Users, "get_by_id", mock_get_by_id)
    users = await get_user_by_id("2")
    assert users.id == "2"
    assert users.name == USERS[1].name


@pytest.mark.asyncio
@patch.object(Users, "create")
async def test_create_user(mocked):
    mocked.side_effect = noop
    await create_user("5", "TestUser")
    mocked.assert_called_once()


@pytest.mark.asyncio
@patch.object(Users, "change_name")
async def test_change_user_name(mocked, monkeypatch):
    monkeypatch.setattr(Users, "get_by_id", mock_get_by_id)
    mocked.side_effect = noop

    await change_user_name("1", "TestUser")
    mocked.assert_called_with(name="TestUser")


@pytest.mark.asyncio
@patch.object(Users, "delete")
async def test_remove_user(mocked, monkeypatch):
    monkeypatch.setattr(Users, "get_by_id", mock_get_by_id)
    mocked.side_effect = noop

    await remove_user("1")
    expected_user = await get_user_by_id("1")
    mocked.assert_called_with(expected_user)
