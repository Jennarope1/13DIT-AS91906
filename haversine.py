#Geographical distance calculations
from math import asin, cos, radians, sin, sqrt

EARTH_RADIUS_KM = 6371.0


def calculate_distance(
    latitude_one: float,
    longitude_one: float,
    latitude_two: float,
    longitude_two: float,
) -> float:
    #Calculate the great-circle distance between two coordinates
    latitude_change = radians(latitude_two - latitude_one)
    longitude_change = radians(longitude_two - longitude_one)
    latitude_one_radians = radians(latitude_one)
    latitude_two_radians = radians(latitude_two)

    haversine_value = (
        sin(latitude_change / 2) ** 2
        + cos(latitude_one_radians)
        * cos(latitude_two_radians)
        * sin(longitude_change / 2) ** 2
    )

    central_angle = 2 * asin(sqrt(haversine_value))
    return EARTH_RADIUS_KM * central_angle
