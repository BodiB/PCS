from traject import TimeSlot, Traject

timeslots = [
    # Zandvoort aan zee - Amsterdam Centraal
    [("Zandvoort aan zee", -1, 4), ("Overveen", 11, 11), ("Haarlem", 15, 16),
     ("Haarlem Spaarnwoude", 19, 19), ("Halfweg-Zwanenburg", 24, 24),
     ("Amsterdam Sloterdijk", 29, 29), ("Amsterdam Centraal", 35, -1)],

    [("Zandvoort aan zee", -1, 34), ("Overveen", 41, 41), ("Haarlem", 45, 46),
     ("Haarlem Spaarnwoude", 49, 49), ("Halfweg-Zwanenburg", 54, 54),
     ("Amsterdam Sloterdijk", 59, 59), ("Amsterdam Centraal", 5, -1)],


    # Hoofddorp - Amsterdam Centraal
    # [("Hoofddorp", -1, 4), ("Schiphol Airport", 9, 11), ("Amsterdam Lelylaan", 17, 17),
    #  ("Amsterdam Sloterdijk", 21, 23), ("Amsterdam Centraal", 29, -1)],

    [("Hoofddorp", -1, 4), ("Schiphol Airport", 9, 11), ("Amsterdam Lelylaan", 17, 17),
     ("Amsterdam Sloterdijk", 21, 23), ("Amsterdam Centraal",
                                        29, 41), ("Amsterdam Muiderpoort", 46, 46),
     ("Amsterdam Science Park", 49, 49), ("Diemen", 52, 52), ("Weesp", 57, 59),
     ("Naarden-Bussum", 5, 5), ("Bussum Zuid",
                                8, 8), ("Hilversum Media Park", 12, 12),
     ("Hilversum", 14, 15), ("Baarn", 21, -1)],

    [("Hoofddorp", -1, 25), ("Schiphol Airport", 29, 30), ("Amsterdam Lelylaan", 37, 37),
     ("Amsterdam Sloterdijk", 41, 41), ("Amsterdam Centraal", 48, -1)],

    # [("Hoofddorp", -1, 34), ("Schiphol Airport", 39, 41), ("Amsterdam Lelylaan", 47, 47),
    # ("Amsterdam Sloterdijk", 51, 53), ("Amsterdam Centraal", 59, -1)],

    [("Hoofddorp", -1, 34), ("Schiphol Airport", 39, 41), ("Amsterdam Lelylaan", 47, 47),
     ("Amsterdam Sloterdijk", 51, 53), ("Amsterdam Centraal", 59, 11),
     ("Amsterdam Muiderpoort", 17, 17), ("Amsterdam Science Park", 19, 19),
     ("Diemen", 22, 22), ("Weesp", 27, 29), ("Naarden-Bussum", 35, 35),
     ("Bussum Zuid", 38, 38), ("Hilversum Media Park", 42, 42),
     ("Hilversum", 44, 45), ("Baarn", 51, -1)],

    [("Hoofddorp", -1, 55), ("Schiphol Airport", 59, 0), ("Amsterdam Lelylaan", 7, 7),
     ("Amsterdam Sloterdijk", 11, 11), ("Amsterdam Centraal", 18, -1)],


    # Den Helder - Amsterdam Amstel (Eig tot Nijmegen)
    [("Den Helder", -1, 4), ("Den Helder Zuid", 8, 8), ("Anna Paulowna", 14, 15),
     ("Schagen", 22, 22), ("Heerhugowaard",  31, 31), ("Alkmaar Noord", 36, 36),
     ("Alkmaar", 41, 44), ("Heiloo", 49, 49), ("Castricum", 55, 55),
     ("Zaandam", 9, 9), ("Amsterdam Sloterdijk", 15, 15),
     ("Amsterdam Centraal", 21, 24), ("Amsterdam Amstel", 31, -1)],

    [("Den Helder", -1, 34), ("Den Helder Zuid", 38, 38), ("Anna Paulowna", 44, 45),
     ("Schagen", 52, 52), ("Heerhugowaard",  1, 1), ("Alkmaar Noord", 6, 6),
     ("Alkmaar", 11, 14), ("Heiloo", 19, 19), ("Castricum", 25, 25),
     ("Zaandam", 39, 39), ("Amsterdam Sloterdijk", 45, 45),
     ("Amsterdam Centraal", 51, 54), ("Amsterdam Amstel", 1, -1)],


    # Amsterdam Centraal - Baarn (Momenteel in de actieve 4 en 34 sprinters Hoofddorp-Amsterdam Centraal verwerkt, behalve de eerste.)
    [("Amsterdam Centraal", -1, 11), ("Amsterdam Muiderpoort", 17, 17),
     ("Amsterdam Science Park", 19, 19), ("Diemen", 22, 22), ("Weesp", 27, 29),
     ("Naarden-Bussum", 35, 35), ("Bussum Zuid", 38, 38),
     ("Hilversum Media Park", 42, 42), ("Hilversum", 44, 45), ("Baarn", 51, -1)],

    # [("Amsterdam Centraal", -1, 41), ("Amsterdam Muiderpoort", 46, 46),
    #  ("Amsterdam Science Park", 49, 49), ("Diemen", 52, 52), ("Weesp", 57, 59),
    #  ("Naarden-Bussum", 5, 5), ("Bussum Zuid", 8, 8), ("Hilversum Media Park", 12, 12),
    #  ("Hilversum", 14, 15), ("Baarn", 21, -1)],


    # SPR Leiden Centraal (Vanaf Nieuw Vennep) - Hoorn Kersenboogerd
    [("Nieuw Vennep", -1, 4), ("Hoofddorp", 9, 9), ("Schiphol Airport", 13, 15),
     ("Amsterdam Lelylaan", 22, 22), ("Amsterdam Sloterdijk", 26, 28),
     ("Zaandam", 34, 34), ("Zaandam Kogerveld", 38, 38),
     ("Purmerend Weidevenne", 44, 44), ("Purmerend", 47, 47),
     ("Purmerend Overwhere", 50, 50), ("Hoorn", 1, 3),
     ("Hoorn Kersenboogerd", 6, -1)],

    [("Nieuw Vennep", -1, 34), ("Hoofddorp", 9, 39), ("Schiphol Airport", 43, 45),
     ("Amsterdam Lelylaan", 52, 52), ("Amsterdam Sloterdijk", 56, 58),
     ("Zaandam", 4, 4), ("Zaandam Kogerveld", 8, 8),
     ("Purmerend Weidevenne", 14, 14), ("Purmerend", 17, 17),
     ("Purmerend Overwhere", 20, 20), ("Hoorn", 31, 33),
     ("Hoorn Kersenboogerd", 36, -1)],


    # IC Enkhuizen - Heerlen (tot aan Amsterdam Amstel)
    [("Enkhuizen", -1, 9), ("Bovenkarspel Flora", 13, 13),
     ("Bovenkarspel-Grootebroek", 15, 18), ("Hoogkarspel", 21, 23),
     ("Hoorn Kersenboogerd", 30, 30), ("Hoorn", 33, 40),
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True), ("Amsterdam Sloterdijk", 5, 5),
     ("Amsterdam Centraal", 11, 14), ("Amsterdam Amstel", 22, -1)],

    [("Enkhuizen", -1, 39), ("Bovenkarspel Flora", 43, 43),
     ("Bovenkarspel-Grootebroek", 45, 48), ("Hoogkarspel", 51, 53),
     ("Hoorn Kersenboogerd", 0, 0), ("Hoorn", 3, 10),
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True), ("Amsterdam Sloterdijk",  35, 35),
     ("Amsterdam Centraal", 41, 45), ("Amsterdam Amstel", 53, -1)],
]

timeslots_NL = []
