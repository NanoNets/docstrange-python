# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["ClassifyBatchParams"]


class ClassifyBatchParams(TypedDict, total=False):
    categories: Required[str]
    """JSON array of category objects (max 50 categories)"""

    files: Required[SequenceNotStr[FileTypes]]
    """Files to classify (max 50)"""
