# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from docstrange import Docstrange, AsyncDocstrange
from tests.utils import assert_matches_type
from docstrange.types import ClassifyResponse, BatchClassifyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClassify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Docstrange) -> None:
        classify = client.classify.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        )
        assert_matches_type(BatchClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Docstrange) -> None:
        response = client.classify.with_raw_response.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(BatchClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Docstrange) -> None:
        with client.classify.with_streaming_response.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(BatchClassifyResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: Docstrange) -> None:
        classify = client.classify.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        )
        assert_matches_type(ClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: Docstrange) -> None:
        response = client.classify.with_raw_response.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = response.parse()
        assert_matches_type(ClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: Docstrange) -> None:
        with client.classify.with_streaming_response.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = response.parse()
            assert_matches_type(ClassifyResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClassify:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncDocstrange) -> None:
        classify = await async_client.classify.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        )
        assert_matches_type(BatchClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.classify.with_raw_response.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(BatchClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncDocstrange) -> None:
        async with async_client.classify.with_streaming_response.batch(
            categories='[{"name": "Invoice"}, {"name": "Contract"}, {"name": "Receipt"}]',
            files=[b"Example data"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(BatchClassifyResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncDocstrange) -> None:
        classify = await async_client.classify.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        )
        assert_matches_type(ClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncDocstrange) -> None:
        response = await async_client.classify.with_raw_response.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        classify = await response.parse()
        assert_matches_type(ClassifyResponse, classify, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncDocstrange) -> None:
        async with async_client.classify.with_streaming_response.sync(
            categories='[{"name": "Invoice", "description": "Bills and invoices"}, {"name": "Contract", "description": "Legal agreements"}]',
            file=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            classify = await response.parse()
            assert_matches_type(ClassifyResponse, classify, path=["response"])

        assert cast(Any, response.is_closed) is True
