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

def test_app_info() -> None:
    response = client.get("/api/v1/info")

    assert response.status_code == 200
    assert response.json() == {
        "name": "FlowCore",
        "version": "0.1.0",
    }
def test_get_organization_by_id() -> None:
    create_response = client.post(
        "/api/v1/organizations",
        json={"name": "Test Organization"},
    )

    organization_id = create_response.json()["id"]

    response = client.get(
        f"/api/v1/organizations/{organization_id}"
    )

    assert response.status_code == 200
    assert response.json()["id"] == organization_id
    assert response.json()["name"] == "Test Organization"


def test_get_missing_organization_returns_404() -> None:
    response = client.get("/api/v1/organizations/999999")

    assert response.status_code == 404

    response_data = response.json()

    assert response_data["error"]["code"] == "not_found"
    assert response_data["error"]["message"] == "Resource not found."
    assert response_data["error"]["request_id"] is not None