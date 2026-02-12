# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResultRetrieveParams"]


class ResultRetrieveParams(TypedDict, total=False):
    include_content: bool
    """Include full extracted content (default: true)"""
