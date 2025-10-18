from pydantic import BaseModel, Field, field_validator
import re

class Structure(BaseModel):
    tldr: str = Field(description="generate a too long; didn't read summary. Show novelties of this article.")
    motivation: str = Field(description="describe the motivation in this paper")
    method: str = Field(description="A concise description (≤100 words) of the method, covering main models, algorithms, and key innovations.")
    result: str = Field(description="result of this paper")
    conclusion: str = Field(description="conclusion of this paper")