#Sample emergency service data used by the prototype

from emergency_service import EmergencyService

EMERGENCY_SERVICES = [
    EmergencyService(
        name="Auckland Central Police Station",
        service_type="Police",
        address="13-15 College Hill, Freemans Bay, Auckland",
        latitude=-36.8498,
        longitude=174.7545,
        phone_number="111",
    ),
    EmergencyService(
        name="Mount Wellington Police Station",
        service_type="Police",
        address="23-25 Penrose Road, Mount Wellington, Auckland",
        latitude=-36.9104,
        longitude=174.8395,
        phone_number="111",
    ),
    EmergencyService(
        name="Auckland City Fire Station",
        service_type="Fire",
        address="58 Pitt Street, Auckland Central",
        latitude=-36.8563,
        longitude=174.7590,
        phone_number="111",
    ),
    EmergencyService(
        name="Mount Roskill Fire Station",
        service_type="Fire",
        address="1500 Dominion Road, Mount Roskill, Auckland",
        latitude=-36.9246,
        longitude=174.7389,
        phone_number="111",
    ),
    EmergencyService(
        name="Auckland City Hospital Emergency Department",
        service_type="Medical",
        address="2 Park Road, Grafton, Auckland",
        latitude=-36.8607,
        longitude=174.7680,
        phone_number="111",
    ),
    EmergencyService(
        name="Middlemore Hospital Emergency Department",
        service_type="Medical",
        address="100 Hospital Road, Otahuhu, Auckland",
        latitude=-36.9624,
        longitude=174.8398,
        phone_number="111",
    ),
]

SAFETY_INSTRUCTIONS = {
    "Police": [
        "Move to a safe place if it is possible to do so.",
        "Do not confront a person who may be dangerous.",
        "Remember important details such as clothing or vehicles.",
        "Call 111 immediately if anyone is in immediate danger.",
    ],
    "Fire": [
        "Leave the building or danger area immediately.",
        "Do not stop to collect personal belongings.",
        "Stay low if there is smoke.",
        "Call 111 from a safe location and do not go back inside.",
    ],
    "Medical": [
        "Call 111 immediately for a life-threatening emergency.",
        "Keep the injured person still unless there is danger.",
        "Follow instructions given by the emergency operator.",
        "Do not give food or drink to an unconscious person.",
    ],
}
