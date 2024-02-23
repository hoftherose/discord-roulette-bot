from src.services.users import Users

USERS = [
    Users(id="1", name="John"),
    Users(id="2", name="Tom"),
    Users(id="3", name="Brad"),
    Users(id="4", name="Alice"),
]


async def mock_get_all():
    return USERS


async def mock_get_by_id(user_id):
    users = [user for user in USERS if user.id==user_id]
    if len(users) != 1:
        raise ValueError("User lookup not found or not unique")
    return users[0]


async def mock_create(user_id):
    users = [user for user in USERS if user.id==user_id]
    if len(users) != 1:
        raise ValueError("User lookup not found or not unique")
    return users[0]
