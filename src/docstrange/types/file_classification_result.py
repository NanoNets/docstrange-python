# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .page_classification import PageClassification

__all__ = ["FileClassificationResult"]


class FileClassificationResult(BaseModel):
    filename: str

    pages: List[PageClassification]

    total_pages: int

    error: Optional[str] = None

    processing_time: Optional[float] = None

    record_id: Optional[str] = None
