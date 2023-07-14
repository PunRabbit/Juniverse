from dataclasses import dataclass
from fastapi import APIRouter
from typing import Optional


@dataclass(frozen=True)
class ApiConstructor:
    prefix: Optional[str] = ""


