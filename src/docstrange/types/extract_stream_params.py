# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["ExtractStreamParams"]


class ExtractStreamParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload"""

    output_format: Required[str]
    """Output format(s)"""

    csv_options: str

    custom_instructions: str

    enable_streaming: bool

    file_base64: str
    """Base64-encoded file content"""

    file_url: str
    """URL to download file from"""

    include_metadata: str

    json_options: str

    prompt_mode: Literal["append", "replace"]
