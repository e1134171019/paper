# -*- coding: utf-8 -*-

import json

import httpx

from paper_collector.crossref import CrossrefConnector
from paper_collector.openalex import OpenAlexConnector


def test_openalex_connector_maps_page_and_next_cursor() -> None:
    payload = {
        "meta": {"next_cursor": "next-oa"},
        "results": [
            {
                "id": "https://openalex.org/W123",
                "doi": "https://doi.org/10.1109/TPEL.2025.123",
                "title": "A DAB Paper",
                "publication_year": 2025,
                "primary_location": {
                    "landing_page_url": "https://example.org/article",
                    "pdf_url": "https://example.org/article.pdf",
                    "source": {"display_name": "IEEE Transactions on Power Electronics"},
                },
            }
        ],
    }

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["search"] == "dual active bridge"
        assert request.url.params["cursor"] == "*"
        return httpx.Response(200, json=payload)

    client = httpx.Client(transport=httpx.MockTransport(handler))
    connector = OpenAlexConnector(client=client)

    page = connector.fetch_page("dual active bridge", None, 25)

    assert page.next_cursor == "next-oa"
    assert len(page.candidates) == 1
    candidate = page.candidates[0]
    assert candidate.provider == "openalex"
    assert candidate.source_record_id == "W123"
    assert candidate.doi == "https://doi.org/10.1109/TPEL.2025.123"
    assert candidate.pdf_url == "https://example.org/article.pdf"


def test_crossref_connector_maps_page_and_next_cursor() -> None:
    payload = {
        "message": {
            "next-cursor": "next-cr",
            "items": [
                {
                    "DOI": "10.1109/TPEL.2025.456",
                    "title": ["Another DAB Paper"],
                    "container-title": ["IEEE Transactions on Power Electronics"],
                    "published": {"date-parts": [[2025, 2, 1]]},
                    "URL": "https://doi.org/10.1109/TPEL.2025.456",
                    "link": [
                        {
                            "URL": "https://example.org/paper.pdf",
                            "content-type": "application/pdf",
                        }
                    ],
                }
            ],
        }
    }

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["query.bibliographic"] == "dual active bridge"
        assert request.url.params["cursor"] == "*"
        return httpx.Response(
            200,
            content=json.dumps(payload).encode(),
            headers={"content-type": "application/json"},
        )

    client = httpx.Client(transport=httpx.MockTransport(handler))
    connector = CrossrefConnector(client=client)

    page = connector.fetch_page("dual active bridge", None, 25)

    assert page.next_cursor == "next-cr"
    candidate = page.candidates[0]
    assert candidate.provider == "crossref"
    assert candidate.source_record_id == "10.1109/TPEL.2025.456"
    assert candidate.publication_year == 2025
    assert candidate.pdf_url == "https://example.org/paper.pdf"
