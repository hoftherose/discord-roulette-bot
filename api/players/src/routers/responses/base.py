"""Base response and error objects"""
import json
from typing import Optional

from pydantic import BaseModel
from fastapi.responses import JSONResponse

from src.repo.conn import Base
from .systemcodes import StatusCodes, SystemCodes
from .utils import orm_as_dict


class BaseResponse(BaseModel):
    """All responses must inherit from this class, otherwise the format
    outlined in the requirement documentation may not be followed correctly.

    Attributes:
        description (str): A short description of what this response represents,
            this will normally be the same as the http status code description
            but could have more descriptive messages like 'User Not Found'.
            This name is used inside of the swagger url page.
        status_code (int): HTTP status code, should follow simple standard and
            correctly represent the response status.
        message (str): Longer description of what the response means, for example
            'Query executed successfully'. Do NOT use default message.
        code (int): System code for consulting documentation, mostly useful for
            error handling. Do NOT use default value (0).
        Schema (pydantic.BaseModel): Response schema, usually outlined in schemas file.
    """

    description: str = "OK"
    status_code: int = StatusCodes.OK
    message: str = "Message goes here"
    code: int = SystemCodes.UNDEFINED

    class Schema(BaseModel):
        """Response content schema, must be defined in each response object.
        Object name must stay the same (Schema). Consult the pydantic
        documentation for more info.
        """

    def model(self):
        """
        Return complete nested model, used for automated documentation. This
        model avoids having to define two response models for nested responses.
        """
        self.Schema.__name__ = self.__repr_name__() + "Schema"

        class Response(BaseModel):
            """Response schema"""

            description: str = self.get("description")
            status_code: int = self.get("status_code")
            message: str = self.get("message")
            code: int = self.get("code")
            schemas: Optional[self.Schema]

        Response.__name__ = self.__repr_name__()

        return Response

    def format(self, content=None):
        """Return input context in the specified dictionary format
        Examples:
            >>> BaseResponse.format({'name': name, 'age': age}
            JSONResponse(
                status_code=200,
                content={
                    'description': 'OK',
                    'status_code': 200,
                    'message': 'Successful query',
                    'code': 1,
                    'schemas': {
                        'name': 'John Smith',
                        'age': 27,
                    },
                },
            )
        Args:
            content (dict, SQLAlchemy.Base): Content of response

        Returns:
            JSONResponse: Resulting response in correct format
        """

        if content is None:
            content = {}
        elif isinstance(content, Base):
            content = orm_as_dict(content)
        if isinstance(content, list):
            inner_schema = self.Schema.model_fields["root"]
            schema_content = self.Schema(
                root=[inner_schema(**cont) for cont in content]
            )
        elif isinstance(content, dict):
            schema_content = self.Schema(**content)
        else:
            pass

        return JSONResponse(
            status_code=self.get("status_code"),
            content={
                "description": self.get("description"),
                "status_code": self.get("status_code"),
                "message": self.get("message"),
                "code": self.get("code"),
                "schemas": json.loads(schema_content.model_dump_json()),
            },
        )

    @classmethod
    def get(cls, field: str):
        """Get the default value assigned"""
        return cls.__fields__[field].default


class BaseErrors:
    """Container class for all errors in a specified route."""

    class ExampleError(BaseResponse):
        """Error content response, must be defined in a case to case basis.
        Object name should follow description value, see BaseResponse for more.
        """

        status_code: int = 500
        description: str = "Example Error"
        message: str = "Example error message"
        code: int = 0

    @classmethod
    def all(cls):
        """Return full error response models, used for documentation"""
        attr_dict = {}
        for attr in cls.__dict__:
            if attr[0] != "_":
                attr_dict = {**attr_dict, **cls.get_model_dict(attr)}
        return attr_dict

    @classmethod
    def get_model_dict(cls, error_name: str):
        """Get the model specification in dictionary form."""
        error = cls.__dict__.get(error_name)
        return {
            error.get("status_code"): {
                "description": error.get("description"),
                "model": error,
            }
        }
