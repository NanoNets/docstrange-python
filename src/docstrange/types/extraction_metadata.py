# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExtractionMetadata"]


class ExtractionMetadata(BaseModel):
    bounding_boxes: Optional[object] = None
    """Element coordinates with page dimensions"""

    confidence_score: Optional[object] = None
    """Confidence scores per field"""
