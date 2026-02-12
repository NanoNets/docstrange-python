# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PaginationInfo"]


class PaginationInfo(BaseModel):
    has_next: Optional[bool] = None

    has_previous: Optional[bool] = None

    page: Optional[int] = None

    page_size: Optional[int] = None

    total_count: Optional[int] = None

    total_pages: Optional[int] = None
