# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["FileClassificationResult", "Page"]


class Page(BaseModel):
    category: str
    """Matched category name or 'Other' if no match"""

    confidence: int
    """Confidence score (0-100)"""

    page_number: int

    reasoning: str
    """Explanation for the classification"""

    identified_category: Optional[str] = None
    """
    Specific document type identified by the model (e.g.,
    'Invoice_Amazon_Electronics'). Always provided - contains a more detailed
    classification than the category.
    """


class FileClassificationResult(BaseModel):
    filename: str

    pages: List[Page]

    total_pages: int

    error: Optional[str] = None

    processing_time: Optional[float] = None
    """Time in seconds"""

    record_id: Optional[str] = None
    """Record ID for polling results"""
