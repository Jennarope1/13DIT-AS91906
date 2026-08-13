# DIT13-91906
Ncea 91906

# Crisis Connect

Crisis Connect is a Python desktop prototype that helps a user identify
an appropriate nearby police, fire, or medical service.

## Technologies

- Python 3
- Tkinter
- Dataclasses
- Python maths library
- Visual Studio Code

## Files

- `main.py`: Starts the application.
- `gui.py`: Contains the Tkinter frontend.
- `emergency_service.py`: Defines the emergency service data class.
- `location_service.py`: Finds the nearest matching service.
- `haversine.py`: Calculates distance between coordinates.
- `emergency_data.py`: Stores prototype service and safety data.
- `utils.py`: Validates coordinates and formats text.
- `assets/`: Available for future images or icons.



## How the program works

1. The user selects police, fire, or medical help.
2. The user enters latitude, longitude, and a description.
3. The program validates the input.
4. Relevant safety instructions are displayed.
5. The Haversine formula compares the user's coordinates with stored
   service coordinates.
6. The closest matching service and a simulated arrival time appear.

