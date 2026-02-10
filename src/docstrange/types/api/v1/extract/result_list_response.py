# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ....._models import BaseModel
from ..extract_response import ExtractResponse

__all__ = ["ResultListResponse", "Pagination"]


class Pagination(BaseModel):
    has_next: Optional[bool] = None

    has_previous: Optional[bool] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    total_count: Optional[int] = None

    total_pages: Optional[int] = None


class ResultListResponse(BaseModel):
    pagination: Pagination

    results: List[ExtractResponse]

    success: bool
