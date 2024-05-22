"""Response models for client endpoint"""

from typing import List
from pydantic import BaseModel

from .systemcodes import SystemCodes
from src.routers.responses.base import BaseResponse


class UserSchema(BaseModel):
    """Schema for returning users"""

    name: str


class UserResponse(BaseResponse):
    """Response to return next payment dates in specified range."""

    message: str = "Returned due date in specified range"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        root: UserSchema


class UserListResponse(BaseResponse):
    """Response to return next payment dates in specified range."""

    message: str = "Returned due date in specified range"
    code: int = SystemCodes.SUCCESSFUL_QUERY

    class Schema(BaseModel):
        """Data Schema"""

        root: List[UserSchema]
