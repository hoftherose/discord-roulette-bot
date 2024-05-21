"""Response utility functions"""

from datetime import date


def orm_as_dict(orm):
    """Get dictionary format from sqlalchemy ORM object"""

    return {field: serialize(orm, field) for field in orm.__dict__ if field[0] != "_"}


def serialize(orm, field: str):
    """Serialize the various sql fields for json prep"""

    field_data = getattr(orm, field)
    if isinstance(field_data, date):
        return field_data.strftime("%d/%m/%Y")
    return field_data
