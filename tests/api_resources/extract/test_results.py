# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docstrange import Docstrange, AsyncDocstrange
from tests.utils import assert_matches_type
from docstrange.types import ExtractResponse
from docstrange.pagination import SyncPageNumberPagination, AsyncPageNumberPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Docstrange) -> None:
        result = client.extract.results.retrieve(
            record_id="record_id",
        )
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Docstrange) -> None:
        result = client.extract.results.retrieve(
            record_id="record_id",
            include_content=True,
        )
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Docstrange) -> None:
        response = client.extract.results.with_raw_response.retrieve(
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Docstrange) -> None:
        with client.extract.results.with_streaming_response.retrieve(
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ExtractResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Docstrange) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            client.extract.results.with_raw_response.retrieve(
                record_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Docstrange) -> None:
        result = client.extract.results.list()
        assert_matches_type(SyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Docstrange) -> None:
        result = client.extract.results.list(
            page=1,
            page_size=1,
            sort_by="created_at",
            sort_order="asc",
        )
        assert_matches_type(SyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Docstrange) -> None:
        response = client.extract.results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(SyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Docstrange) -> None:
        with client.extract.results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(SyncPageNumberPagination[ExtractResponse], result, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncDocstrange) -> None:
        result = await async_client.extract.results.retrieve(
            record_id="record_id",
        )
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncDocstrange) -> None:
        result = await async_client.extract.results.retrieve(
            record_id="record_id",
            include_content=True,
        )
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.results.with_raw_response.retrieve(
            record_id="record_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ExtractResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.results.with_streaming_response.retrieve(
            record_id="record_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ExtractResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncDocstrange) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `record_id` but received ''"):
            await async_client.extract.results.with_raw_response.retrieve(
                record_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDocstrange) -> None:
        result = await async_client.extract.results.list()
        assert_matches_type(AsyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDocstrange) -> None:
        result = await async_client.extract.results.list(
            page=1,
            page_size=1,
            sort_by="created_at",
            sort_order="asc",
        )
        assert_matches_type(AsyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.results.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(AsyncPageNumberPagination[ExtractResponse], result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.results.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(AsyncPageNumberPagination[ExtractResponse], result, path=["response"])

        assert cast(Any, response.is_closed) is True
