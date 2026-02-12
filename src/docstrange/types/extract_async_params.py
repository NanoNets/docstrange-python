# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import FileTypes

__all__ = ["ExtractAsyncParams"]


class ExtractAsyncParams(TypedDict, total=False):
    file: Required[FileTypes]
    """File to upload (PDF, Word, Excel, PowerPoint, images)"""

    output_format: Required[str]
    """Output format(s): `markdown`, `html`, `json`, `csv`.

    Comma-separate for multiple (e.g., `markdown,json`).
    """

    csv_options: str
    """CSV extraction options (e.g., `table`)"""

    custom_instructions: str
    """Custom extraction instructions (e.g., `Format dates as YYYY-MM-DD`)"""

    file_base64: str
    """Base64-encoded file content"""

    file_url: str
    """URL to download file from"""

    include_metadata: str
    """Comma-separated metadata: `bounding_boxes`, `confidence_score`"""

    json_options: str
    """JSON extraction options.

    Values: `hierarchy_output`, `table-of-contents`, field list
    `["field1", "field2"]`, or JSON schema `{...}`
    """

    prompt_mode: Literal["append", "replace"]
    """`append`: add to base prompt, `replace`: use only custom instructions"""
