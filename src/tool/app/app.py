from pydantic import BaseModel


class MiddlewareConfig(BaseModel):
    allow_origins: list
    allow_credentials: bool
    allow_methods: list
    allow_headers: list


class RunConfig(BaseModel):
    workers: int
    host: str
    reload: bool
    port: int
