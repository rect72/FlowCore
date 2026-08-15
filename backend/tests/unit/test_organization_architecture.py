from pathlib import Path


def test_domain_does_not_depend_on_infrastructure() -> None:
    domain_path = Path("src/flowcore/modules/organizations/domain")

    for file_path in domain_path.glob("*.py"):
        content = file_path.read_text(encoding="utf-8")

        assert "infrastructure" not in content


def test_domain_does_not_depend_on_sqlalchemy() -> None:
    domain_path = Path("src/flowcore/modules/organizations/domain")

    for file_path in domain_path.glob("*.py"):
        content = file_path.read_text(encoding="utf-8")

        assert "sqlalchemy" not in content.lower()


def test_domain_does_not_depend_on_fastapi() -> None:
    domain_path = Path("src/flowcore/modules/organizations/domain")

    for file_path in domain_path.glob("*.py"):
        content = file_path.read_text(encoding="utf-8")

        assert "fastapi" not in content.lower()