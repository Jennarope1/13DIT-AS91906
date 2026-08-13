#Business logic for finding nearby emergency services

from collections.abc import Iterable

from emergency_service import EmergencyService
from haversine import calculate_distance


class LocationService:
    #Find emergency services near a user's location

    def __init__(self, services: Iterable[EmergencyService]) -> None:
        #Create a location service using supplied buildings
        self._services = list(services)

    def find_nearest(
        self,
        latitude: float,
        longitude: float,
        service_type: str,
    ) -> tuple[EmergencyService, float]:
        #Return the closest matching service and its distance.
        matching_services = [
            service
            for service in self._services
            if service.service_type == service_type
        ]

        if not matching_services:
            raise ValueError(f"No services were found for {service_type}.")

        nearest_service = min(
            matching_services,
            key=lambda service: calculate_distance(
                latitude,
                longitude,
                service.latitude,
                service.longitude,
            ),
        )

        distance = calculate_distance(
            latitude,
            longitude,
            nearest_service.latitude,
            nearest_service.longitude,
        )
        return nearest_service, distance

    @staticmethod
    def estimate_arrival_time(distance_km: float) -> int:
        #Estimate a simple prototype arrival time in minutes
        average_emergency_speed_kmh = 45.0
        travel_minutes = distance_km / average_emergency_speed_kmh * 60
        return max(3, round(travel_minutes))
