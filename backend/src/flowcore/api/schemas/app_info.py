from pydantic import BaseModel


class AppInfoResponse(BaseModel):
    name: str
    version: str