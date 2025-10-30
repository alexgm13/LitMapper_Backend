from pydantic import BaseModel
from typing import Optional, Any

class Meta(BaseModel):
    pagination: Optional[dict]

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    errors: Optional[Any] = None
    meta: Optional[Meta] = None
    status_code: int