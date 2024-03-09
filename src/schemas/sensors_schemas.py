from pydantic import BaseModel


class Sensor(BaseModel):
    temperature: float
    humidity: float
    CO2CosIRValue: float
    CO2MG811Value: float
    MOX1: float
    MOX2: float
    MOX3: float
    MOX4: float
    COValue: float
    inhabited: int
    hour: int

    class Config:
        from_attributes = True
