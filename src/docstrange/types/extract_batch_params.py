# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes, SequenceNotStr

__all__ = ["ExtractBatchParams"]


class ExtractBatchParams(TypedDict, total=False):
    files: Required[SequenceNotStr[FileTypes]]
    """Files to process (max 50)"""

    output_format: Required[str]
    """Output format(s) for all files"""

    csv_options: str

    custom_instructions: str

    include_metadata: str

    json_options: str

    prompt_mode: Literal["append", "replace"]
