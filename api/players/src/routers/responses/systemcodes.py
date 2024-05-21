"""System and Status code definitions"""


# pylint: disable=too-few-public-methods
class SystemCodes:
    """Micro-service system codes, used for reviewing documentation
    Default value is UNDEFINED, which will return 0.
    There are more values that extend UNDEFINED for readibilty only.
    """

    UNDEFINED = 0
    TEST_NOT_FOUND = 1
    TEST_BAD_REQUEST = 2
    TEST_UNAUTH_ACCESS = 3
    TEST_VALIDATION_ERROR = 4
    TEST_SERVER_ERROR = 5

    UNKNOWN_ISSUE = 1000
    SUCCESSFUL_QUERY = 1001


# pylint: disable=too-few-public-methods
class StatusCodes:
    """Status code values for cleaner code management."""

    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    NOT_FOUND = 404
    VALIDATION_ERROR = 422
    SERVER_ERROR = 500
