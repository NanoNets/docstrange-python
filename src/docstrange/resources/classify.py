# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import classify_sync_params, classify_batch_params
from .._types import Body, Query, Headers, NotGiven, FileTypes, SequenceNotStr, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.classify_response import ClassifyResponse
from ..types.batch_classify_response import BatchClassifyResponse

__all__ = ["ClassifyResource", "AsyncClassifyResource"]


class ClassifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NanoNets/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return ClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NanoNets/docstrange-python#with_streaming_response
        """
        return ClassifyResourceWithStreamingResponse(self)

    def batch(
        self,
        *,
        categories: str,
        files: SequenceNotStr[FileTypes],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchClassifyResponse:
        """
        Classify multiple documents asynchronously (max 50).

        Args:
          categories: JSON array of category objects

          files: Files to classify (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/classify/batch",
            body=maybe_transform(
                {
                    "categories": categories,
                    "files": files,
                },
                classify_batch_params.ClassifyBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchClassifyResponse,
        )

    def sync(
        self,
        *,
        categories: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyResponse:
        """
        Classify a single document.

        Args:
          categories: JSON array of category objects

          file: File to classify

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/classify/sync",
            body=maybe_transform(
                {
                    "categories": categories,
                    "file": file,
                },
                classify_sync_params.ClassifySyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyResponse,
        )


class AsyncClassifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/NanoNets/docstrange-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/NanoNets/docstrange-python#with_streaming_response
        """
        return AsyncClassifyResourceWithStreamingResponse(self)

    async def batch(
        self,
        *,
        categories: str,
        files: SequenceNotStr[FileTypes],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchClassifyResponse:
        """
        Classify multiple documents asynchronously (max 50).

        Args:
          categories: JSON array of category objects

          files: Files to classify (max 50)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/classify/batch",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "files": files,
                },
                classify_batch_params.ClassifyBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchClassifyResponse,
        )

    async def sync(
        self,
        *,
        categories: str,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyResponse:
        """
        Classify a single document.

        Args:
          categories: JSON array of category objects

          file: File to classify

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/classify/sync",
            body=await async_maybe_transform(
                {
                    "categories": categories,
                    "file": file,
                },
                classify_sync_params.ClassifySyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ClassifyResponse,
        )


class ClassifyResourceWithRawResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.batch = to_raw_response_wrapper(
            classify.batch,
        )
        self.sync = to_raw_response_wrapper(
            classify.sync,
        )


class AsyncClassifyResourceWithRawResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.batch = async_to_raw_response_wrapper(
            classify.batch,
        )
        self.sync = async_to_raw_response_wrapper(
            classify.sync,
        )


class ClassifyResourceWithStreamingResponse:
    def __init__(self, classify: ClassifyResource) -> None:
        self._classify = classify

        self.batch = to_streamed_response_wrapper(
            classify.batch,
        )
        self.sync = to_streamed_response_wrapper(
            classify.sync,
        )


class AsyncClassifyResourceWithStreamingResponse:
    def __init__(self, classify: AsyncClassifyResource) -> None:
        self._classify = classify

        self.batch = async_to_streamed_response_wrapper(
            classify.batch,
        )
        self.sync = async_to_streamed_response_wrapper(
            classify.sync,
        )
