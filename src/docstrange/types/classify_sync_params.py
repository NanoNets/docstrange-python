# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["ClassifySyncParams"]


class ClassifySyncParams(TypedDict, total=False):
    categories: Required[str]
    """
    JSON array of category objects: [{"name": "Category Name", "description":
    "Optional description"}]
    """

    file: Required[FileTypes]
    """File to classify (PDF, PNG, JPG, JPEG, TIFF, BMP, WebP)"""
