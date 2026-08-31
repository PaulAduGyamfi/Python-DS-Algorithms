from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, field_validator

class Cadence(str, Enum):
    once = "once"; 
    daily = "daily"; 
    weekly = "weekly"


@dataclass
class ReportRequestDC:
    report_id: str
    cadence: Cadence
    recipients: list[str] = field(default_factory=list)

class ReportRequest(BaseModel):
    report_id: str = Field(min_length=3)
    cadence: Cadence
    recipients: list[str] = Field(min_length=1)
    run_after: datetime

    @field_validator("recipients")
    @classmethod
    def must_be_valid_email(cls, l):
        print("VALIDATOR RAN, got:", l)
        not_valid = [r for r in l if "@" not in r]
        if not_valid: 
            raise ValueError(f"not emails: {not_valid}")
        return l


#print(ReportRequestDC("R-0", Cadence.daily))
#print(ReportRequest(report_id="R-1", cadence="daily", recipients=["123test@gmail.com"], run_after="2026-09-01T09:00:00"))

try:
    print(ReportRequest(
        report_id="R-1", 
        cadence="daily", 
        recipients=["nope"], 
        run_after="2026-09-01T09:00:00"
        )) 
except Exception as e:
    print("REJECTED:", e)