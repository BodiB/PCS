
# format: ("begin station name", "end station name", length in km, max speed in kph)

connection = {
    ("Hoorn", "Amsterdam Sloterdijk", 40.3, 160): [
        # ("Hoorn", "Amsterdam Sloterdijk", 40.3, 160),
        ("Hoorn", "Purmerend Overwhere",  18, 160),
        ("Purmerend Overwhere", "Purmerend",  1.5, 160),
        ("Purmerend", "Purmerend Weidevenne", 1.6, 160),
        ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 160),
        ("Zaandam Kogerveld", "Zaandam",  2.5, 160),
        ("Zaandam", "Amsterdam Sloterdijk", 7.6, 160), ],

    ("Amsterdam Zuid", "Almere Centrum", 20, 160): [
        ("Amsterdam Zuid", "Amsterdam RAI",  1, 160),
        ("Amsterdam RAI", "Duivendrecht",  1, 160),
        ("Duivendrecht", "Diemen Zuid", 1, 160),
        ("Diemen Zuid", "Weesp", 1, 160),
        ("Weesp", "Almere Poort",  1, 160),
        ("Almere Poort", "Almere Muziekwijk", 1, 160),
        ("Almere Muziekwijk", "Almere Centrum", 1, 160), ],

    ("Almere Centrum", "Lelystad Centrum", 20, 160): [
        ("Almere Centrum", "Almere Parkwijk",  1, 160),
        ("Almere Parkwijk", "Almere Buiten",  1, 160),
        ("Almere Buiten", "Almere Oostvaarders", 1, 160),
        ("Almere Oostvaarders", "Lelystad Centrum", 1, 160), ]

}


rail_list = [
    ("Zandvoort aan zee", "Overveen", 6.3, 160),
    ("Overveen", "Haarlem", 2, 160),
    ("Haarlem", "Haarlem Spaarnwoude", 2.6, 130),
    ("Haarlem Spaarnwoude", "Halfweg-Zwanenburg", 5, 130),
    ("Halfweg-Zwanenburg", "Amsterdam Sloterdijk", 6.4, 130),
    ("Amsterdam Sloterdijk", "Amsterdam Centraal", 4.6, 130),

    ("Hoofddorp", "Schiphol Airport", 4.7, 160),
    ("Schiphol Airport", "Amsterdam Lelylaan", 8.3, 160),
    ("Amsterdam Lelylaan", "Amsterdam Sloterdijk", 3.5, 160),

    ("Hoorn", "Purmerend Overwhere",  18, 160),
    ("Purmerend Overwhere", "Purmerend",  1.5, 160),
    ("Purmerend", "Purmerend Weidevenne", 1.6, 160),
    ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 160),
    ("Zaandam Kogerveld", "Zaandam",  2.5, 160),
    ("Zaandam", "Amsterdam Sloterdijk", 7.6, 160),

    ("Den Helder", "Den Helder Zuid", 2.7, 160),
    ("Den Helder Zuid", "Anna Paulowna", 8.9, 160),
    ("Anna Paulowna",  "Schagen", 9.3, 160),
    ("Schagen", "Heerhugowaard", 14, 160),
    ("Heerhugowaard", "Alkmaar Noord", 4.9, 160),
    ("Alkmaar Noord", "Alkmaar", 1.8, 160),
    ("Alkmaar", "Heiloo", 5.1, 160),
    ("Heiloo", "Castricum", 6.8, 160),
    ("Castricum", "Zaandam", 17.3, 160),
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 160),
    ("Amsterdam Centraal", "Amsterdam Amstel", 6, 160),

    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 160),
    ("Amsterdam Muiderpoort", "Amsterdam Science Park", 1.5, 160),
    ("Amsterdam Science Park", "Diemen", 1.7, 160),
    ("Diemen", "Weesp", 6.2, 160),
    ("Weesp", "Naarden-Bussum", 8.9, 160),
    ("Naarden-Bussum", "Bussum Zuid", 1.6, 160),
    ("Bussum Zuid", "Hilversum Media Park", 3.2, 160),
    ("Hilversum Media Park", "Hilversum", 1.5, 160),
    ("Hilversum", "Baarn", 7.1, 160),

    # SPR Leiden Centraal (Vanaf Nieuw Vennep) - Hoorn Kersenboogerd
    ("Nieuw Vennep", "Hoofddorp", 5.1, 160),
    ("Hoofddorp", "Schiphol Airport", 4.7, 160),
    ("Schiphol Airport", "Amsterdam Lelylaan", 8.3, 160),
    ("Amsterdam Lelylaan", "Amsterdam Sloterdijk", 3.4, 160),
    ("Amsterdam Sloterdijk", "Zaandam", 7.6, 160),
    ("Zaandam", "Zaandam Kogerveld", 2.5, 160),
    ("Zaandam Kogerveld", "Purmerend Weidevenne", 9.4, 160),
    ("Purmerend Weidevenne", "Purmerend", 1.6, 160),
    ("Purmerend", "Purmerend Overwhere", 1.5, 160),
    ("Purmerend Overwhere", "Hoorn", 18, 160),
    ("Hoorn", "Hoorn Kersenboogerd", 2.4, 160),

    # IC Enkhuizen - Heerlen (tot aan Amsterdam Amstel)
    ("Enkhuizen", "Bovenkarspel Flora", 2.2, 160),
    ("Bovenkarspel Flora", "Bovenkarspel-Grootebroek", 1.2, 160),
    ("Bovenkarspel-Grootebroek", "Hoogkarspel", 3.5, 160),

    ("Hoogkarspel", "Hoorn Kersenboogerd", 7.8, 160),
    ("Hoorn Kersenboogerd", "Hoorn", 2, 80),
    # ("Hoorn", "Amsterdam Sloterdijk", 40.3, 160),
    ("Amsterdam Sloterdijk", "Amsterdam Centraal", 4.5, 160),
    ("Amsterdam Centraal", "Amsterdam Amstel", 5.8, 160),

    ("Lelystad Centrum", "Almere Oostvaarders", 1, 160),
    ("Almere Oostvaarders", "Almere Buiten", 1, 160),
    ("Almere Buiten", "Almere Parkwijk", 1, 160),
    ("Almere Parkwijk", "Almere Centrum", 1, 160),
    ("Almere Centrum", "Almere Muziekwijk", 1, 160),
    ("Almere Muziekwijk", "Almere Poort", 1, 160),
    ("Almere Poort", "Weesp", 1, 160),
    ("Weesp", "Diemen", 6.2, 160),

    #???
    ("Weesp", "Diemen Zuid", 3, 160),
    ("Diemen Zuid", "Duivendrecht", 3, 160),
    ("Duivendrecht", "Amsterdam RAI", 2, 160),
    ("Amsterdam RAI", "Amsterdam Zuid", 1, 160),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 160),
]

rail_list_NL = []
