# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .extract_response import ExtractResponse

__all__ = ["BatchExtractResponse"]


class BatchExtractResponse(BaseModel):
    accepted_files: int

    batch_id: str

    message: str

    records: List[ExtractResponse]

    rejected_files: int

    success: bool

    total_files: int
