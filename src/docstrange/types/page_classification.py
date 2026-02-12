# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageClassification"]


class PageClassification(BaseModel):
    category: str
    """Matched category name or 'Other' if no match"""

    confidence: int
    """Confidence score (0-100)"""

    page_number: int

    reasoning: str
    """Explanation for the classification"""

    identified_category: Optional[str] = None
    """Specific document type identified by the model."""
