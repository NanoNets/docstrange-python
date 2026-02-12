# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PageClassification"]


class PageClassification(BaseModel):
    category: str

    confidence: int

    page_number: int

    reasoning: str

    identified_category: Optional[str] = None
