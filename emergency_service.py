#Data model for an emergency service building

from dataclasses import dataclass


@dataclass(frozen=True)
class EmergencyService:
    #Store information about an emergency service building

    name: str
    service_type: str
    address: str
    latitude: float
    longitude: float
    phone_number: str