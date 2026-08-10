from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from flowcore.core.models import Base


class OrganizationModel(Base):
    __tablename__ = "organizations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)