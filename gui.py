#Tkinter interface for the Crisis Connect prototype

import tkinter as tk
from tkinter import messagebox, ttk

from emergency_data import EMERGENCY_SERVICES, SAFETY_INSTRUCTIONS
from location_service import LocationService
from utils import shorten_text, validate_coordinate

APP_TITLE = "Crisis Connect"
WINDOW_SIZE = "520x760"
BACKGROUND_COLOUR = "#f5f7fa"
PRIMARY_COLOUR = "#b71c1c"
SECONDARY_COLOUR = "#ffffff"
TEXT_COLOUR = "#1f2933"
MUTED_TEXT_COLOUR = "#52606d"


class CrisisConnectApp:
    #Desktop interface for locating emergency services

    def __init__(self) -> None:
        #Create the application window and shared state
        self.root = tk.Tk()
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(480, 700)
        self.root.configure(bg=BACKGROUND_COLOUR)

        self.location_service = LocationService(EMERGENCY_SERVICES)
        self.selected_service = tk.StringVar(value="Medical")
        self.latitude = tk.StringVar(value="-36.8485")
        self.longitude = tk.StringVar(value="174.7633")
        self.emergency_description = tk.StringVar()

        self._configure_styles()
        self._show_home_screen()

    def run(self) -> None:
        #Start the Tkinter event loop
        self.root.mainloop()

    def _configure_styles(self) -> None:
        #Configure reusable ttk widget styles
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Primary.TButton",
            font=("Arial", 12, "bold"),
            padding=12,
            background=PRIMARY_COLOUR,
            foreground=SECONDARY_COLOUR,
        )
        style.map(
            "Primary.TButton",
            background=[("active", "#8e0000")],
        )
        style.configure(
            "Secondary.TButton",
            font=("Arial", 11),
            padding=10,
        )
        style.configure(
            "Service.TRadiobutton",
            font=("Arial", 12, "bold"),
            padding=10,
            background=SECONDARY_COLOUR,
        )

    def _clear_window(self) -> None:
        #Remove all widgets from the current screen
        for widget in self.root.winfo_children():
            widget.destroy()

    def _create_page(self, heading: str, subtitle: str) -> tk.Frame:
        #Create a standard page container and header
        self._clear_window()
        page = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOUR,
            padx=28,
            pady=24,
        )
        page.pack(fill="both", expand=True)

        tk.Label(
            page,
            text=APP_TITLE,
            font=("Arial", 24, "bold"),
            bg=BACKGROUND_COLOUR,
            fg=PRIMARY_COLOUR,
        ).pack(pady=(0, 18))

        tk.Label(
            page,
            text=heading,
            font=("Arial", 20, "bold"),
            bg=BACKGROUND_COLOUR,
            fg=TEXT_COLOUR,
            wraplength=440,
        ).pack(pady=(0, 8))

        tk.Label(
            page,
            text=subtitle,
            font=("Arial", 11),
            bg=BACKGROUND_COLOUR,
            fg=MUTED_TEXT_COLOUR,
            wraplength=440,
            justify="center",
        ).pack(pady=(0, 24))
        return page

    def _show_home_screen(self) -> None:
        #Display the emergency service selection screen
        page = self._create_page(
            "What help do you need?",
            (
                "Select an emergency service. This is a school "
                "prototype and does not contact real responders."
            ),
        )

        service_frame = tk.Frame(
            page,
            bg=SECONDARY_COLOUR,
            bd=1,
            relief="solid",
            padx=18,
            pady=14,
        )
        service_frame.pack(fill="x", pady=10)

        for service_type in ("Police", "Fire", "Medical"):
            ttk.Radiobutton(
                service_frame,
                text=service_type,
                value=service_type,
                variable=self.selected_service,
                style="Service.TRadiobutton",
            ).pack(anchor="w", fill="x", pady=4)

        tk.Label(
            page,
            text="For a real emergency in New Zealand, call 111.",
            font=("Arial", 12, "bold"),
            bg=BACKGROUND_COLOUR,
            fg=PRIMARY_COLOUR,
        ).pack(pady=18)

        ttk.Button(
            page,
            text="Continue",
            command=self._show_details_screen,
            style="Primary.TButton",
        ).pack(fill="x", pady=8)

    def _show_details_screen(self) -> None:
        #Display location and emergency detail fields
        page = self._create_page(
            "Tell us where you are",
            "Enter your location and briefly describe what happened.",
        )

        form = tk.Frame(
            page,
            bg=SECONDARY_COLOUR,
            bd=1,
            relief="solid",
            padx=18,
            pady=18,
        )
        form.pack(fill="x", pady=8)

        self._add_label_and_entry(form, "Latitude", self.latitude)
        self._add_label_and_entry(form, "Longitude", self.longitude)
        self._add_label_and_entry(
            form,
            "Emergency description",
            self.emergency_description,
        )

        tk.Label(
            page,
            text=(
                "Example Auckland coordinates are already entered "
                "so the prototype can be tested quickly."
            ),
            font=("Arial", 10),
            bg=BACKGROUND_COLOUR,
            fg=MUTED_TEXT_COLOUR,
            wraplength=430,
        ).pack(pady=12)

        ttk.Button(
            page,
            text="View safety instructions",
            command=self._validate_details,
            style="Primary.TButton",
        ).pack(fill="x", pady=8)

        ttk.Button(
            page,
            text="Back",
            command=self._show_home_screen,
            style="Secondary.TButton",
        ).pack(fill="x", pady=4)

    @staticmethod
    def _add_label_and_entry(
        parent: tk.Widget,
        label_text: str,
        variable: tk.StringVar,
    ) -> None:
        #Add a labelled input field to a form
        tk.Label(
            parent,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg=SECONDARY_COLOUR,
            fg=TEXT_COLOUR,
        ).pack(anchor="w", pady=(8, 4))

        ttk.Entry(
            parent,
            textvariable=variable,
            font=("Arial", 11),
        ).pack(fill="x", ipady=7)

    def _validate_details(self) -> None:
        #Validate user input before showing instructions
        try:
            validate_coordinate(
                self.latitude.get(),
                -90.0,
                90.0,
                "Latitude",
            )
            validate_coordinate(
                self.longitude.get(),
                -180.0,
                180.0,
                "Longitude",
            )
        except ValueError as error:
            messagebox.showerror("Invalid location", str(error))
            return

        if not self.emergency_description.get().strip():
            messagebox.showerror(
                "Missing description",
                "Please briefly describe the emergency.",
            )
            return

        self._show_instructions_screen()

    def _show_instructions_screen(self) -> None:
        #Display safety guidance for the selected service
        service_type = self.selected_service.get()
        page = self._create_page(
            f"{service_type} safety instructions",
            (
                "Follow these steps while you prepare to contact "
                "the appropriate emergency service."
            ),
        )

        instructions_frame = tk.Frame(
            page,
            bg=SECONDARY_COLOUR,
            bd=1,
            relief="solid",
            padx=18,
            pady=16,
        )
        instructions_frame.pack(fill="x", pady=8)

        for number, instruction in enumerate(
            SAFETY_INSTRUCTIONS[service_type],
            start=1,
        ):
            tk.Label(
                instructions_frame,
                text=f"{number}. {instruction}",
                font=("Arial", 11),
                bg=SECONDARY_COLOUR,
                fg=TEXT_COLOUR,
                wraplength=400,
                justify="left",
                anchor="w",
            ).pack(fill="x", pady=8)

        ttk.Button(
            page,
            text="Find nearest service",
            command=self._show_result_screen,
            style="Primary.TButton",
        ).pack(fill="x", pady=14)

        ttk.Button(
            page,
            text="Back",
            command=self._show_details_screen,
            style="Secondary.TButton",
        ).pack(fill="x")

    def _show_result_screen(self) -> None:
        #Find and display the nearest emergency service
        latitude = validate_coordinate(
            self.latitude.get(),
            -90.0,
            90.0,
            "Latitude",
        )
        longitude = validate_coordinate(
            self.longitude.get(),
            -180.0,
            180.0,
            "Longitude",
        )
        service_type = self.selected_service.get()

        try:
            service, distance = self.location_service.find_nearest(
                latitude,
                longitude,
                service_type,
            )
        except ValueError as error:
            messagebox.showerror("Service unavailable", str(error))
            return

        arrival_time = self.location_service.estimate_arrival_time(
            distance
        )
        page = self._create_page(
            "Nearest service found",
            (
                "The result is calculated from the sample service "
                "data stored in this prototype."
            ),
        )

        result_frame = tk.Frame(
            page,
            bg=SECONDARY_COLOUR,
            bd=1,
            relief="solid",
            padx=20,
            pady=18,
        )
        result_frame.pack(fill="x", pady=10)

        result_lines = [
            ("Service", service.name),
            ("Type", service.service_type),
            ("Address", service.address),
            ("Distance", f"{distance:.2f} km"),
            (
                "Estimated arrival",
                f"Approximately {arrival_time} minutes",
            ),
            ("Emergency number", service.phone_number),
            (
                "Your description",
                shorten_text(self.emergency_description.get()),
            ),
        ]

        for label_text, value_text in result_lines:
            tk.Label(
                result_frame,
                text=f"{label_text}:",
                font=("Arial", 10, "bold"),
                bg=SECONDARY_COLOUR,
                fg=MUTED_TEXT_COLOUR,
                anchor="w",
            ).pack(fill="x", pady=(5, 1))

            tk.Label(
                result_frame,
                text=value_text,
                font=("Arial", 11),
                bg=SECONDARY_COLOUR,
                fg=TEXT_COLOUR,
                wraplength=395,
                justify="left",
                anchor="w",
            ).pack(fill="x", pady=(0, 5))

        tk.Label(
            page,
            text=(
                "Prototype only: no request has been sent. "
                "Call 111 in a real emergency."
            ),
            font=("Arial", 11, "bold"),
            bg=BACKGROUND_COLOUR,
            fg=PRIMARY_COLOUR,
            wraplength=430,
        ).pack(pady=14)

        ttk.Button(
            page,
            text="Start again",
            command=self._reset_application,
            style="Primary.TButton",
        ).pack(fill="x", pady=6)

    def _reset_application(self) -> None:
        #Reset input fields and return to the first screen
        self.selected_service.set("Medical")
        self.latitude.set("-36.8485")
        self.longitude.set("174.7633")
        self.emergency_description.set("")
        self._show_home_screen()
