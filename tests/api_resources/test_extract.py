# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docstrange import Docstrange, AsyncDocstrange
from tests.utils import assert_matches_type
from docstrange.types import ExtractResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sync(self, client: Docstrange) -> None:
        extract = client.extract.sync(
            file=b"raw file contents",
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_sync_with_all_params(self, client: Docstrange) -> None:
        extract = client.extract.sync(
            file=b"raw file contents",
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: Docstrange) -> None:
        response = client.extract.with_raw_response.sync(
            file=b"raw file contents",
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: Docstrange) -> None:
        with client.extract.with_streaming_response.sync(
            file=b"raw file contents",
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.sync(
            file=b"raw file contents",
            output_format="markdown",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncDocstrange) -> None:
        extract = await async_client.extract.sync(
            file=b"raw file contents",
            output_format="markdown",
            csv_options="",
            custom_instructions="",
            file_base64="",
            file_url="",
            include_metadata="",
            json_options="",
            prompt_mode="append",
        )
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.extract.with_raw_response.sync(
            file=b"raw file contents",
            output_format="markdown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncDocstrange) -> None:
        async with async_client.extract.with_streaming_response.sync(
            file=b"raw file contents",
            output_format="markdown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
