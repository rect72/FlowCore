from fastapi.testclient import TestClient

from flowcore.main import app


client = TestClient(app)


def test_health_check() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_not_found_error_has_unified_format() -> None:
    response = client.get("/api/v1/unknown")

    assert response.status_code == 404

    response_data = response.json()

    assert response_data["error"]["code"] == "not_found"
    assert response_data["error"]["message"] == "Resource not found."
    assert response_data["error"]["request_id"] is not None
    assert response.headers["X-Request-ID"] == response_data["error"]["request_id"]