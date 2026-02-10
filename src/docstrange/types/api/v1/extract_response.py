# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .extraction_format_result import ExtractionFormatResult

__all__ = ["ExtractResponse", "Result"]


class Result(BaseModel):
    """Results by format (only requested formats populated)"""

    csv: Optional[ExtractionFormatResult] = None

    html: Optional[ExtractionFormatResult] = None

    json_: Optional[ExtractionFormatResult] = FieldInfo(alias="json", default=None)

    markdown: Optional[ExtractionFormatResult] = None


class ExtractResponse(BaseModel):
    message: str

    record_id: str
    """Job ID for retrieving results"""

    status: Literal["completed", "processing", "failed"]

    success: bool

    created_at: Optional[datetime] = None

    file_size: Optional[int] = None
    """Size in bytes"""

    filename: Optional[str] = None

    output_format: Optional[str] = None

    pages_processed: Optional[int] = None

    processing_time: Optional[float] = None
    """Time in seconds"""

    result: Optional[Result] = None
    """Results by format (only requested formats populated)"""
