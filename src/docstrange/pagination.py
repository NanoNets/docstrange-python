# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional, cast
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PageNumberPaginationPagination", "SyncPageNumberPagination", "AsyncPageNumberPagination"]

_T = TypeVar("_T")


class PageNumberPaginationPagination(BaseModel):
    has_next: Optional[bool] = None

    total_count: Optional[int] = None


class SyncPageNumberPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    pagination: Optional[PageNumberPaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        total_pages = None
        if self.pagination is not None:
            if self.pagination.total_count is not None:
                total_pages = self.pagination.total_count
        if total_pages is not None and last_page >= total_pages:
            return None

        return PageInfo(params={"page": last_page + 1})


class AsyncPageNumberPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    results: List[_T]
    pagination: Optional[PageNumberPaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        results = self.results
        if not results:
            return []
        return results

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        last_page = cast("int | None", self._options.params.get("page")) or 1

        total_pages = None
        if self.pagination is not None:
            if self.pagination.total_count is not None:
                total_pages = self.pagination.total_count
        if total_pages is not None and last_page >= total_pages:
            return None

        return PageInfo(params={"page": last_page + 1})
