# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .extraction_format_result import ExtractionFormatResult

__all__ = ["ExtractionResult"]


class ExtractionResult(BaseModel):
    csv: Optional[ExtractionFormatResult] = None

    html: Optional[ExtractionFormatResult] = None

    json_: Optional[ExtractionFormatResult] = FieldInfo(alias="json", default=None)

    markdown: Optional[ExtractionFormatResult] = None
