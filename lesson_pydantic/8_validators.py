from pydantic import BaseModel, field_validator

class ServerLogs(BaseModel):
    id: int
    logs: str

    @field_validator('logs')
    def logs_has_contain_lag(cls, value):
        if 'lag' not in value.lower():
            raise ValueError(f"Field doesn't contain the 'lag'")
        else:
            return value

response = {
    "id": 12412,
    "logs": "dsfdsfsdfsdf"
}