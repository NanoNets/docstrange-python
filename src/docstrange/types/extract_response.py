# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExtractResponse"]


class ExtractResponse(BaseModel):
    record_id: str

    status: str

    success: bool

    message: Optional[str] = None
