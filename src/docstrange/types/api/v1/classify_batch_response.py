# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .file_classification_result import FileClassificationResult

__all__ = ["ClassifyBatchResponse"]


class ClassifyBatchResponse(BaseModel):
    batch_id: str

    failed_files: int

    message: str

    results: List[FileClassificationResult]

    success: bool

    successful_files: int

    total_files: int
