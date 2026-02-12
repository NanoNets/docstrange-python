# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["ExtractAsyncParams"]


class ExtractAsyncParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload (PDF, Word, Excel, PowerPoint, images)"""

    output_format: Required[str]
    """Output format(s): markdown, html, json, csv."""

    csv_options: str
    """CSV extraction options"""

    custom_instructions: str
    """Custom extraction instructions"""

    file_base64: str
    """Base64-encoded file content"""

    file_url: str
    """URL to download file from"""

    include_metadata: str
    """Comma-separated metadata types"""

    json_options: str
    """JSON extraction options"""

    prompt_mode: Literal["append", "replace"]
