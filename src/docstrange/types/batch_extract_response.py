# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BatchExtractResponse"]


class BatchExtractResponse(BaseModel):
    batch_id: str

    message: str

    success: bool
