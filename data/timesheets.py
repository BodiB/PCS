from traject import TimeSlot, Traject

# ("", 5, 5),
# CODE: "CS8A" beteken CS SPOOR 8A
# Omdat we CS als centraal punt pakken moeten we iig alle treinen
# vanaf CS hebben.
timeslots = [
    # CS1 SPR Zandvoort aan zee - Amsterdam Centraal
    # CS1 SPR SLUIT AAN OP Amsterdam Centraal - Beverwijk - Hoorn
    [("Zandvoort aan zee", -1, 4), ("Overveen", 11, 11), ("Haarlem", 15, 16),
     ("Haarlem Spaarnwoude", 19, 19), ("Halfweg-Zwanenburg", 24, 24),
     ("Amsterdam Sloterdijk", 29, 29), ("Amsterdam Centraal", 35, 41),
     ("Amsterdam Sloterdijk", 46, 46),
     ("Halfweg-Zwanenburg", 51, 51), ("Haarlem Spaarnwoude", 56, 56),
     ("Haarlem", 0, 1), ("Bloemendaal", 5, 5), ("Santpoort Zuid", 7, 7),
     ("Santpoort Noord", 10, 10), ("Driehuis", 12, 12), ("Beverwijk", 18, 18),
     ("Heemskerk", 21, 21), ("Uitgeest", 26, 26), ("Castricum", 30, 30),
     ("Heiloo", 36, 36), ("Alkmaar", 41, 43), ("Alkmaar Noord", 46, 46),
     ("Heerhugowaard", 51, 51), ("Obdam", 56, 58), ("Hoorn", 7, -1), ],

    [("Zandvoort aan zee", -1, 34), ("Overveen", 41, 41), ("Haarlem", 45, 46),
     ("Haarlem Spaarnwoude", 49, 49), ("Halfweg-Zwanenburg", 54, 54),
     ("Amsterdam Sloterdijk", 59, 59), ("Amsterdam Centraal", 5, 11),
     ("Amsterdam Sloterdijk", 16, 16),
     ("Halfweg-Zwanenburg", 21, 21), ("Haarlem Spaarnwoude", 26, 26),
     ("Haarlem", 30, 31), ("Bloemendaal", 35, 35), ("Santpoort Zuid", 37, 37),
     ("Santpoort Noord", 40, 40), ("Driehuis", 42, 42), ("Beverwijk", 48, 48),
     ("Heemskerk", 51, 51), ("Uitgeest", 56, 56), ("Castricum", 60, 60),
     ("Heiloo", 6, 6), ("Alkmaar", 11, 13), ("Alkmaar Noord", 16, 16),
     ("Heerhugowaard", 21, 21), ("Obdam", 26, 28), ("Hoorn", 37, -1), ],

    # CS1 SPR Hoorn - Beverwijk - Amsterdam Centraal
    # CS1 SPR SLUIT AAN OP Amsterdam Centraal - Zandvoort aan zee
    [("Hoorn", -1, 21), ("Obdam", 29, 30), ("Heerhugowaard", 36, 36),
     ("Alkmaar Noord", 41, 41), ("Alkmaar", 44, 49),  ("Heiloo", 54, 54),
     ("Castricum", 59, 59), ("Uitgeest", 4, 5), ("Heemskerk", 9, 9),
     ("Beverwijk", 12, 12), ("Driehuis", 17, 17), ("Santpoort Noord", 20, 20),
     ("Santpoort Zuid", 23, 23), ("Bloemendaal", 26, 26), ("Haarlem", 30, 30),
     ("Haarlem Spaarnwoude", 34, 34), ("Halfweg-Zwanenburg", 39, 39),
     ("Amsterdam Sloterdijk", 44, 44), ("Amsterdam Centraal", 50, 56),
     ("Amsterdam Sloterdijk", 1, 1),
     ("Halfweg-Zwanenburg", 6, 6), ("Haarlem Spaarnwoude", 11, 11),
     ("Haarlem", 15, 16), ("Overveen", 20, 20), ("Zandvoort aan zee", 26, -1),
     ],

    [("Hoorn", -1, 51), ("Obdam", 59, 60), ("Heerhugowaard", 6, 6),
     ("Alkmaar Noord", 11, 11), ("Alkmaar", 14, 19),  ("Heiloo", 24, 24),
     ("Castricum", 29, 29), ("Uitgeest", 34, 35), ("Heemskerk", 39, 39),
     ("Beverwijk", 42, 42), ("Driehuis", 47, 47), ("Santpoort Noord", 50, 50),
     ("Santpoort Zuid", 53, 53), ("Bloemendaal", 56, 56), ("Haarlem", 60, 60),
     ("Haarlem Spaarnwoude", 4, 4), ("Halfweg-Zwanenburg", 9, 9),
     ("Amsterdam Sloterdijk", 14, 14), ("Amsterdam Centraal", 20, 26),
     ("Amsterdam Sloterdijk", 31, 31),
     ("Halfweg-Zwanenburg", 36, 36), ("Haarlem Spaarnwoude", 41, 41),
     ("Haarlem", 45, 46), ("Overveen", 50, 50), ("Zandvoort aan zee", 56, -1),
     ],




    # CS8A IC Den Helder - Amsterdam Amstel (Eig tot Nijmegen)
    [("Den Helder", -1, 4), ("Den Helder Zuid", 8, 8), ("Anna Paulowna", 14, 15),
     ("Schagen", 22, 22), ("Heerhugowaard",  31, 31), ("Alkmaar Noord", 36, 36),
     ("Alkmaar", 41, 44), ("Heiloo", 49, 49), ("Castricum", 55, 55),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     #
     ("Zaandam", 9, 9), ("Amsterdam Sloterdijk", 15, 15),
     ("Amsterdam Centraal", 21, 24),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Amsterdam Muiderpoort", -2, -2, True),
     #
     ("Amsterdam Amstel", 31, 33), ],
    # ("Utrecht Centraal", 51, -54), #TODO AFMAKEN NAAR NIJMEGEN
    # ("Veenendaal-De Klomp", 11, 11), ("Ede-Wageningen", 18, 18),
    # ("Arnhem Centraal", 28, 35), ],

    [("Den Helder", -1, 34), ("Den Helder Zuid", 38, 38), ("Anna Paulowna", 44, 45),
     ("Schagen", 52, 52), ("Heerhugowaard",  1, 1), ("Alkmaar Noord", 6, 6),
     ("Alkmaar", 11, 14), ("Heiloo", 19, 19), ("Castricum", 25, 25),
     #
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     #
     ("Zaandam", 39, 39), ("Amsterdam Sloterdijk", 45, 45),
     ("Amsterdam Centraal", 51, 54),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Amsterdam Muiderpoort", -2, -2, True),
     #
     ("Amsterdam Amstel", 1, -1)],


    # CS10B SPR Hoofddorp - Amersfoort Vathorst
    [("Hoofddorp", -1, 4), ("Schiphol Airport", 9, 11), ("Amsterdam Lelylaan", 17, 17),
     ("Amsterdam Sloterdijk", 21, 23), ("Amsterdam Centraal", 29, 41),
     ("Amsterdam Muiderpoort", 46, 46), ("Amsterdam Science Park", 49, 49),
     ("Diemen", 52, 52), ("Weesp", 57, 59), ("Naarden-Bussum", 5, 5),
     ("Bussum Zuid", 8, 8), ("Hilversum Media Park", 12, 12),
     ("Hilversum", 14, 15), ("Baarn", 21, 21), ("Amersfoort", 28, 29),
     ("Amersfoort Schothorst", 32, 32), ("Amersfoort Vathorst", 36, -1)],

    [("Hoofddorp", -1, 34), ("Schiphol Airport", 39, 41), ("Amsterdam Lelylaan", 47, 47),
     ("Amsterdam Sloterdijk", 51, 53), ("Amsterdam Centraal", 59, 11),
     ("Amsterdam Muiderpoort", 17, 17), ("Amsterdam Science Park", 19, 19),
     ("Diemen", 22, 22), ("Weesp", 27, 29), ("Naarden-Bussum", 35, 35),
     ("Bussum Zuid", 38, 38), ("Hilversum Media Park", 42, 42),
     ("Hilversum", 44, 45), ("Baarn", 51, 51), ("Amersfoort", 58, 59),
     ("Amersfoort Schothorst", 2, 2), ("Amersfoort Vathorst", 6, -1)],

    # CS10B SPR Hoofddorp - Zwolle
    [("Hoofddorp", -1, 25), ("Schiphol Airport", 29, 30),
     ("Amsterdam Lelylaan", 37, 37), ("Amsterdam Sloterdijk", 41, 41),
     ("Amsterdam Centraal", 48, 53), ("Amsterdam Muiderpoort", 58, 58),
     ("Amsterdam Science Park", 1, 1), ("Diemen", 4, 4), ("Weesp", 9, 10),
     ("Almere Poort", 17, 17), ("Almere Muziekwijk", 21, 21),
     ("Almere Centrum", 24, 25), ("Almere Parkwijk", 28, 28),
     ("Almere Buiten", 31, 31), ("Almere Oostvaarders", 34, 39),
     ("Lelystad Centrum", 50, 54), ("Dronten", 6, 6), ("Kampen Zuid", 14, 14),
     ("Zwolle", 24, -1), ],

    [("Hoofddorp", -1, 55), ("Schiphol Airport", 59, 60),
     ("Amsterdam Lelylaan", 7, 7), ("Amsterdam Sloterdijk", 11, 11),
     ("Amsterdam Centraal", 18, 23), ("Amsterdam Muiderpoort", 28, 28),
     ("Amsterdam Science Park", 31, 31), ("Diemen", 34, 34), ("Weesp", 39, 40),
     ("Almere Poort", 47, 47), ("Almere Muziekwijk", 51, 51),
     ("Almere Centrum", 54, 55), ("Almere Parkwijk", 58, 58),
     ("Almere Buiten", 1, 1), ("Almere Oostvaarders", 4, 9),
     ("Lelystad Centrum", 20, 24), ("Dronten", 36, 36), ("Kampen Zuid", 44, 44),
     ("Zwolle", 54, -1), ],

    # SPR Leiden Centraal (Vanaf Nieuw Vennep) - Hoorn Kersenboogerd
    [("Nieuw Vennep", -1, 4), ("Hoofddorp", 9, 9), ("Schiphol Airport", 13, 15),
     ("Amsterdam Lelylaan", 22, 22), ("Amsterdam Sloterdijk", 26, 28),
     ("Zaandam", 34, 34), ("Zaandam Kogerveld", 38, 38),
     ("Purmerend Weidevenne", 44, 44), ("Purmerend", 47, 47),
     ("Purmerend Overwhere", 50, 50), ("Hoorn", 1, 3),
     ("Hoorn Kersenboogerd", 6, -1)],

    [("Nieuw Vennep", -1, 34), ("Hoofddorp", 39, 39), ("Schiphol Airport", 43, 45),
     ("Amsterdam Lelylaan", 52, 52), ("Amsterdam Sloterdijk", 56, 58),
     ("Zaandam", 4, 4), ("Zaandam Kogerveld", 8, 8),
     ("Purmerend Weidevenne", 14, 14), ("Purmerend", 17, 17),
     ("Purmerend Overwhere", 20, 20), ("Hoorn", 31, 33),
     ("Hoorn Kersenboogerd", 36, -1)],


    # IC Enkhuizen - Heerlen (tot aan Amsterdam Amstel)
    [("Enkhuizen", -1, 9), ("Bovenkarspel Flora", 13, 13),
     ("Bovenkarspel-Grootebroek", 15, 18), ("Hoogkarspel", 21, 23),
     ("Hoorn Kersenboogerd", 30, 30), ("Hoorn", 33, 40),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True),
     #
     ("Amsterdam Sloterdijk", 5, 5), ("Amsterdam Centraal", 11, 14),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Amsterdam Muiderpoort", -2, -2, True),
     #
     ("Amsterdam Amstel", 22, -1)],

    [("Enkhuizen", -1, 39), ("Bovenkarspel Flora", 43, 43),
     ("Bovenkarspel-Grootebroek", 45, 48), ("Hoogkarspel", 51, 53),
     ("Hoorn Kersenboogerd", 60, 60), ("Hoorn", 3, 10),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True),
     #
     ("Amsterdam Sloterdijk",  35, 35), ("Amsterdam Centraal", 41, 45),
     # Stations die niet worden aangedaan maar wel gepasseerd:
     ("Amsterdam Muiderpoort", -2, -2, True),
     #
     ("Amsterdam Amstel", 53, -1)],

    # SPR Zwolle - Amsterdam Centraal (RIJDT NORMAAL DOOR NAAR DEN HAAG CENTRAAL)
    [("Lelystad Centrum", -1, 37), ("Almere Oostvaarders", 50, 55),
     ("Almere Buiten", 58, 58), ("Almere Parkwijk", 1, 1),
     ("Almere Centrum", 4, 6), ("Almere Muziekwijk", 9, 9),
     ("Almere Poort", 13, 13), ("Weesp", 20, 21),
     ("Diemen", 26, 26), ("Amsterdam Science Park", 28, 28),
     ("Amsterdam Muiderpoort", 31, 31), ("Amsterdam Centraal", 37, 37), ],

    [("Lelystad Centrum", -1, 7), ("Almere Oostvaarders", 20, 25),
     ("Almere Buiten", 28, 28), ("Almere Parkwijk", 31, 31),
     ("Almere Centrum", 34, 36), ("Almere Muziekwijk", 39, 39),
     ("Almere Poort", 43, 43), ("Weesp", 50, 51),
     ("Diemen", 56, 56), ("Amsterdam Science Park", 58, 58),
     ("Amsterdam Muiderpoort", 61, 61), ("Amsterdam Centraal", 67, 67), ],

    # IC (Leeuwarden) Lelystad - Schiphol (Den Haag Centraal)
    [("Lelystad Centrum", -1, 43), ("Almere Oostvaarders", -2, -2, True),
     ("Almere Buiten", -2, -2, True), ("Almere Parkwijk", -2, -2, True),
     ("Almere Centrum", 57, 59, True), ("Almere Muziekwijk", -2, -2, True),
     ("Almere Poort", -2, -2, True), ("Weesp", -2, -2, True),
     ("Diemen Zuid", -2, -2, True), ("Duivendrecht", -2, -2, True),
     ("Amsterdam RAI", -2, -2, True),
     ("Amsterdam Zuid", 18, 19), ("Schiphol Airport", 25, 27), ],


    # IC (Dordrecht) Schiphol - Lelystad Centrum #TODO 2x per uur
    [("Dordrecht", -1, 8), ("Zwijndrecht", -2, -2, True),
     ("Barendrecht", -2, -2, True), ("Rotterdam Lombardijen", -2, -2, True),
     ("Rotterdam Zuid", -2, -2, True), ("Rotterdam Blaak", 20, 21),
     ("Rotterdam Centraal", 24, 27), ("Schiedam Centrum", 31, 31),
     ("Delft Zuid", -2, -2, True), ("Delft", 39, 39),
     ("Rijswijk", -2, -2, True), ("Den Haag Moerwijk", -2, -2, True),
     ("Den Haag HS", 46, 48), ("Den Haag Laan van NOI", 51, 51),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 60, 1),
     ("Sassenheim", -2, -2, True), ("Nieuw Vennep", -2, -2, True),
     ("Hoofddorp", -2, -2, True),  ("Schiphol Airport", 16, 18),
     ("Amsterdam Zuid", 24, 26), ("Amsterdam RAI", -2, -2, True),
     ("Duivendrecht", 31, 31), ("Diemen Zuid", -2, -2, True),
     ("Weesp", -2, -2, True),
     ("Almere Poort", -2, -2, True),  ("Almere Muziekwijk", -2, -2, True),
     ("Almere Centrum", 47, 49), ("Almere Parkwijk", -2, -2, True),
     ("Almere Buiten", 54, 54), ("Almere Oostvaarders", -2, -2, True),
     ("Lelystad Centrum", 6, -1), ],


]

timeslots_NL = []
