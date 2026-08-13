#Validation and formatting helper functions


def validate_coordinate(
    value: str,
    minimum: float,
    maximum: float,
    field_name: str,
) -> float:
    #Convert and validate a coordinate entered by the user

    cleaned_value = value.strip()

    if not cleaned_value:
        raise ValueError(f"{field_name} is required.")

    try:
        coordinate = float(cleaned_value)
    except ValueError as error:
        raise ValueError(f"{field_name} must be a number.") from error

    if not minimum <= coordinate <= maximum:
        raise ValueError(
            f"{field_name} must be between {minimum} and {maximum}."
        )

    return coordinate


def shorten_text(text: str, maximum_length: int = 120) -> str:
    #Shorten long text for display in the interface
    cleaned_text = " ".join(text.split())
    if len(cleaned_text) <= maximum_length:
        return cleaned_text
    return cleaned_text[: maximum_length - 3] + "..."
