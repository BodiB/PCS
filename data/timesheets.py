from traject import TimeSlot, Traject

timeslots = [
    # Zandvoort aan zee - Amsterdam Centraal
    [("Zandvoort aan zee", -1, 4), ("Overveen", 11, 11), ("Haarlem", 15, 16), ("Haarlem Spaarnwoude", 19, 19), ("Halfweg-Zwanenburg", 24, 24), ("Amsterdam Sloterdijk", 29, 29), ("Amsterdam Centraal", 35, -1)],
    [("Zandvoort aan zee", -1, 34), ("Overveen", 41, 41), ("Haarlem", 45, 46), ("Haarlem Spaarnwoude", 49, 49), ("Halfweg-Zwanenburg", 54, 54), ("Amsterdam Sloterdijk", 59, 59), ("Amsterdam Centraal", 5, -1)],
    # Hoofddorp - Amsterdam Centraal
    [("Hoofddorp", -1, 4), ("Schiphol Airport", 9, 11), ("Amsterdam Lelylaan", 17, 17), ("Amsterdam Sloterdijk", 21,23), ("Amsterdam Centraal", 29, -1)], 
    [("Hoofddorp", -1, 25), ("Schiphol Airport", 29, 30), ("Amsterdam Lelylaan", 37, 37), ("Amsterdam Sloterdijk", 41,41), ("Amsterdam Centraal", 48, -1)], 
    [("Hoofddorp", -1, 34), ("Schiphol Airport", 39, 41), ("Amsterdam Lelylaan", 47, 47), ("Amsterdam Sloterdijk", 51,53), ("Amsterdam Centraal", 59, -1)], 
    [("Hoofddorp", -1, 55), ("Schiphol Airport", 59, 0), ("Amsterdam Lelylaan", 7, 7), ("Amsterdam Sloterdijk", 11,11), ("Amsterdam Centraal", 18, -1)], 
    # Den Helder - Amsterdam Amstel (Eig tot Nijmegen)
    [("Den Helder", -1, 4), ("Den Helder Zuid", 8, 8), ("Anna Paulowna", 14, 15), ("Schagen", 22, 22), ("Heerhugowaard",  31, 31), ("Alkmaar Noord", 36, 36), ("Alkmaar", 41, 44), ("Heiloo", 49, 49), ("Castricum", 55, 55), ("Zaandam", 9, 9), ("Amsterdam Sloterdijk", 15, 15), ("Amsterdam Centraal", 21, 24), ("Amsterdam Amstel", 31, -1)],
    [("Den Helder", -1, 34), ("Den Helder Zuid", 38, 38), ("Anna Paulowna", 44, 45), ("Schagen", 52, 52), ("Heerhugowaard",  1, 1), ("Alkmaar Noord", 6, 6), ("Alkmaar", 11, 14), ("Heiloo", 19, 19), ("Castricum", 25, 25), ("Zaandam", 39, 39), ("Amsterdam Sloterdijk", 45, 45), ("Amsterdam Centraal", 51, 54), ("Amsterdam Amstel", 1, -1)],
    # Amsterdam Centraal - Baarn
    [("Amsterdam Centraal", -1, 11), ("Amsterdam Muiderpoort", 17, 17), ("Amsterdam Science Park", 19, 19), ("Diemen", 22, 22), ("Weesp", 27, 29), ("Naarden-Bussum", 35, 35), ("Bussum Zuid", 38, 38), ("Hilversum Media Park", 42, 42), ("Hilversum", 44, 45), ("Baarn", 51, -1)],
    [("Amsterdam Centraal", -1, 41), ("Amsterdam Muiderpoort", 46, 46), ("Amsterdam Science Park", 49, 49), ("Diemen", 52, 52), ("Weesp", 57, 59), ("Naarden-Bussum", 5, 5), ("Bussum Zuid", 8, 8), ("Hilversum Media Park", 12, 12), ("Hilversum", 14, 15), ("Baarn", 21, -1)], 
]
