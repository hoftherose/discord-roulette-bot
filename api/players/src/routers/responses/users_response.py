"""Response models for client endpoint"""

from typing import List

from .systemcodes import SystemCodes
from src.routers.responses.base import BaseResponse, BaseSchema, RootSchema


class UserSchema(BaseSchema):
    """Schema for returning users"""

    id: int
    name: str


class UserResponse(BaseResponse):
    """Response to return next payment dates in specified range."""

    message: str = "Returned due date in specified range"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(RootSchema):
        """Data Schema"""

        root: UserSchema


class UserListResponse(BaseResponse):
    """Response to return next payment dates in specified range."""

    message: str = "Returned due date in specified range"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(RootSchema):
        """Data Schema"""

        root: List[UserSchema]
