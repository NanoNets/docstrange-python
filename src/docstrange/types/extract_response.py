# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .extraction_result import ExtractionResult

__all__ = ["ExtractResponse"]


class ExtractResponse(BaseModel):
    message: str

    record_id: str

    status: Literal["completed", "processing", "failed"]

    success: bool

    created_at: Optional[datetime] = None

    file_size: Optional[int] = None

    filename: Optional[str] = None

    output_format: Optional[str] = None

    pages_processed: Optional[int] = None

    processing_time: Optional[float] = None

    result: Optional[ExtractionResult] = None
