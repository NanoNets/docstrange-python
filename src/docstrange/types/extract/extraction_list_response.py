# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .pagination_info import PaginationInfo
from ..extract_response import ExtractResponse

__all__ = ["ExtractionListResponse"]


class ExtractionListResponse(BaseModel):
    pagination: PaginationInfo

    results: List[ExtractResponse]

    success: bool
