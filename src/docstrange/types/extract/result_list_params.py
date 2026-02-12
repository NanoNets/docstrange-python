# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ResultListParams"]


class ResultListParams(TypedDict, total=False):
    page: int

    page_size: int

    sort_by: Literal["created_at", "updated_at", "original_filename", "file_size", "processing_status"]

    sort_order: Literal["asc", "desc"]
