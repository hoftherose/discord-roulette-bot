"""Error response outlines"""

from src.routers.responses.base import BaseErrors, BaseResponse
from .systemcodes import StatusCodes, SystemCodes


class ErrorResponses(BaseErrors):
    """Class to store all generic error responses"""

    class NotFound(BaseResponse):
        """Item not found in database"""

        status_code: int = StatusCodes.NOT_FOUND
        description: str = "Not Found"
        message: str = "Object was not found"
        code: int = SystemCodes.TEST_NOT_FOUND

    class InvalidRequest(BaseResponse):
        """Request Invalid"""

        status_code: int = StatusCodes.BAD_REQUEST
        description: str = "Bad Request"
        message: str = "Incorrect request format"
        code: int = SystemCodes.TEST_BAD_REQUEST

    class UnauthAccess(BaseResponse):
        """Unauthorized access"""

        status_code: int = StatusCodes.UNAUTHORIZED
        description: str = "Unauthorized Access"
        message: str = "User does not have access to item"
        code: int = SystemCodes.TEST_UNAUTH_ACCESS
