from traject import TimeSlot, Traject

# CODE: "CS8A" beteken CS SPOOR 8A

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
     ("Heerhugowaard", 51, 51), ("Obdam", 56, 58), ("Hoorn", 7, -1)],

    [("Zandvoort aan zee", -1, 34), ("Overveen", 41, 41), ("Haarlem", 45, 46),
     ("Haarlem Spaarnwoude", 49, 49), ("Halfweg-Zwanenburg", 54, 54),
     ("Amsterdam Sloterdijk", 59, 59), ("Amsterdam Centraal", 5, 11),
     ("Amsterdam Sloterdijk", 16, 16),
     ("Halfweg-Zwanenburg", 21, 21), ("Haarlem Spaarnwoude", 26, 26),
     ("Haarlem", 30, 31), ("Bloemendaal", 35, 35), ("Santpoort Zuid", 37, 37),
     ("Santpoort Noord", 40, 40), ("Driehuis", 42, 42), ("Beverwijk", 48, 48),
     ("Heemskerk", 51, 51), ("Uitgeest", 56, 56), ("Castricum", 60, 60),
     ("Heiloo", 6, 6), ("Alkmaar", 11, 13), ("Alkmaar Noord", 16, 16),
     ("Heerhugowaard", 21, 21), ("Obdam", 26, 28), ("Hoorn", 37, -1)],

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

    # CS2A IC Den Haag Centraal - Amsterdam Centraal
    [("Den Haag Centraal", -1, 17), ("Den Haag Laan van NOI", -2, -2, True),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 29, 33),
     ("Voorhout", -2, -2, True), ("Hillegom", -2, -2, True),
     ("Heemstede-Aerdenhout", 48, 48), ("Haarlem", 53, 55),
     ("Haarlem Spaarnwoude", -2, -2, True), ("Halfweg-Zwanenburg", -2, -2, True),
     ("Amsterdam Sloterdijk", 4, 4),
     ("Amsterdam Centraal", 10, 20), ("Amsterdam Sloterdijk", 25, 25),
     ("Halfweg-Zwanenburg", -2, -2, True), ("Haarlem Spaarnwoude", -2, -2, True),
     ("Haarlem", 35, 37), ("Heemstede-Aerdenhout", 42, 42),
     ("Hillegom", -2, -2, True), ("Voorhout", -2, -2, True),
     ("Leiden Centraal", 56, 60), ("De Vink", -2, -2, True),
     ("Voorschoten", -2, -2, True), ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", -2, -2, True), ("Den Haag Centraal", 11, -1)],

    [("Den Haag Centraal", -1, 47), ("Den Haag Laan van NOI", -2, -2, True),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 59, 3),
     ("Voorhout", -2, -2, True), ("Hillegom", -2, -2, True),
     ("Heemstede-Aerdenhout", 18, 18), ("Haarlem", 23, 25),
     ("Haarlem Spaarnwoude", -2, -2, True), ("Halfweg-Zwanenburg", -2, -2, True),
     ("Amsterdam Sloterdijk", 34, 34),
     ("Amsterdam Centraal", 40, 50), ("Amsterdam Sloterdijk", 55, 55),
     ("Halfweg-Zwanenburg", -2, -2, True), ("Haarlem Spaarnwoude", -2, -2, True),
     ("Haarlem", 5, 7), ("Heemstede-Aerdenhout", 12, 12),
     ("Hillegom", -2, -2, True), ("Voorhout", -2, -2, True),
     ("Leiden Centraal", 26, 30), ("De Vink", -2, -2, True),
     ("Voorschoten", -2, -2, True), ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", -2, -2, True), ("Den Haag Centraal", 41, -1)],

    # CS2A IC (Vlissingen) Dordrecht - Amsterdam Centraal - v.v.#verlengen
    [("Dordrecht", -1, 25), ("Zwijndrecht", -2, -2, True),
     ("Barendrecht", -2, -2, True), ("Rotterdam Lombardijen", -2, -2, True),
     ("Rotterdam Zuid", -2, -2, True), ("Rotterdam Blaak", 36, 36),
     ("Rotterdam Centraal", 39, 42), ("Schiedam Centrum", 46, 46),
     ("Delft Zuid", -2, -2, True), ("Delft", 54, 54), ("Rijswijk", -2, -2, True),
     ("Den Haag Moerwijk", -2, -2, True), ("Den Haag HS", 1, 3),
     ("Den Haag Laan van NOI", 6, 6),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 15, 19),
     ("Voorhout", -2, -2, True), ("Hillegom", -2, -2, True),
     ("Heemstede-Aerdenhout", 34, 34), ("Haarlem", 39, 40),
     ("Haarlem Spaarnwoude", -2, -2, True), ("Halfweg-Zwanenburg", -2, -2, True),
     ("Amsterdam Sloterdijk", 49, 49),
     ("Amsterdam Centraal", 55, 64), ("Amsterdam Sloterdijk", 9, 9),
     ("Halfweg-Zwanenburg", -2, -2, True), ("Haarlem Spaarnwoude", -2, -2, True),
     ("Haarlem", 19, 20), ("Heemstede-Aerdenhout", 25, 25),
     ("Hillegom", -2, -2, True), ("Voorhout", -2, -2, True),
     ("Leiden Centraal", 40, 45), ("De Vink", -2, -2, True),
     ("Voorschoten", -2, -2, True), ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", 54, 54), ("Den Haag HS", 57, 59),
     ("Den Haag Moerwijk", -2, -2, True), ("Rijswijk", -2, -2, True),
     ("Delft", 5, 5),  ("Delft Zuid", -2, -2, True),
     ("Schiedam Centrum", 13, 13), ("Rotterdam Centraal", 18, 21),
     ("Rotterdam Blaak", 24, 24), ("Rotterdam Zuid", -2, -2, True),
     ("Rotterdam Lombardijen", -2, -2, True),  ("Barendrecht", -2, -2, True),
     ("Zwijndrecht", -2, -2, True), ("Dordrecht", 36, -1)],

    [("Dordrecht", -1, 55), ("Zwijndrecht", -2, -2, True),
     ("Barendrecht", -2, -2, True), ("Rotterdam Lombardijen", -2, -2, True),
     ("Rotterdam Zuid", -2, -2, True), ("Rotterdam Blaak", 6, 6),
     ("Rotterdam Centraal", 9, 12), ("Schiedam Centrum", 16, 16),
     ("Delft Zuid", -2, -2, True), ("Delft", 24, 24), ("Rijswijk", -2, -2, True),
     ("Den Haag Moerwijk", -2, -2, True), ("Den Haag HS", 31, 33),
     ("Den Haag Laan van NOI", 36, 36),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 45, 49),
     ("Voorhout", -2, -2, True), ("Hillegom", -2, -2, True),
     ("Heemstede-Aerdenhout", 4, 4), ("Haarlem", 9, 10),
     ("Haarlem Spaarnwoude", -2, -2, True), ("Halfweg-Zwanenburg", -2, -2, True),
     ("Amsterdam Sloterdijk", 19, 19),
     ("Amsterdam Centraal", 25, 34), ("Amsterdam Sloterdijk", 39, 39),
     ("Halfweg-Zwanenburg", -2, -2, True), ("Haarlem Spaarnwoude", -2, -2, True),
     ("Haarlem", 49, 50), ("Heemstede-Aerdenhout", 55, 55),
     ("Hillegom", -2, -2, True), ("Voorhout", -2, -2, True),
     ("Leiden Centraal", 10, 15), ("De Vink", -2, -2, True),
     ("Voorschoten", -2, -2, True), ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", 24, 24), ("Den Haag HS", 27, 29),
     ("Den Haag Moerwijk", -2, -2, True), ("Rijswijk", -2, -2, True),
     ("Delft", 35, 35),  ("Delft Zuid", -2, -2, True),
     ("Schiedam Centrum", 43, 43), ("Rotterdam Centraal", 48, 51),
     ("Rotterdam Blaak", 54, 54), ("Rotterdam Zuid", -2, -2, True),
     ("Rotterdam Lombardijen", -2, -2, True),  ("Barendrecht", -2, -2, True),
     ("Zwijndrecht", -2, -2, True), ("Dordrecht", 6, -1)],

    # CS4B IC Den Helder - Utrecht Centraal (Nijmegen)#verlengen
    [("Den Helder", -1, 4), ("Den Helder Zuid", 8, 8), ("Anna Paulowna", 14, 15),
     ("Schagen", 22, 22), ("Heerhugowaard",  31, 31), ("Alkmaar Noord", 36, 36),
     ("Alkmaar", 41, 44), ("Heiloo", 49, 49), ("Castricum", 55, 55),
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     ("Zaandam", 9, 9), ("Amsterdam Sloterdijk", 15, 15),
     ("Amsterdam Centraal", 21, 24),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 31, 33),  ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True), ("Abcoude", -2, -2, True),
     ("Breukelen", -2, -2, True), ("Maarssen", -2, -2, True),
     ("Utrecht Zuilen", -2, -2, True), ("Utrecht Centraal", 51, -1)],

    [("Den Helder", -1, 34), ("Den Helder Zuid", 38, 38), ("Anna Paulowna", 44, 45),
     ("Schagen", 52, 52), ("Heerhugowaard",  1, 1), ("Alkmaar Noord", 6, 6),
     ("Alkmaar", 11, 14), ("Heiloo", 19, 19), ("Castricum", 25, 25),
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     ("Zaandam", 39, 39), ("Amsterdam Sloterdijk", 45, 45),
     ("Amsterdam Centraal", 51, 54),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 1, 3), ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True),
     ("Abcoude", -2, -2, True), ("Breukelen", -2, -2, True),
     ("Maarssen", -2, -2, True), ("Utrecht Zuilen", -2, -2, True),
     ("Utrecht Centraal", 21, -1)],

    # CS4B IC Alkmaar - Utrecht Centraal (Maastricht)#verlengen
    [("Alkmaar", -1, 27), ("Heiloo", -2, -2, True), ("Castricum", 35, 35),
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     ("Zaandam", 49, 49), ("Amsterdam Sloterdijk", 55, 55),
     ("Amsterdam Centraal", 1, 5),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 13, 13),  ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True), ("Abcoude", -2, -2, True),
     ("Breukelen", -2, -2, True), ("Maarssen", -2, -2, True),
     ("Utrecht Zuilen", -2, -2, True), ("Utrecht Centraal", 31, -1)],

    [("Alkmaar", -1, 57), ("Heiloo", -2, -2, True), ("Castricum", 5, 5),
     ("Uitgeest",  -2, -2, True), ("Krommenie-Assendelft",  -2, -2, True),
     ("Wormerveer",  -2, -2, True), ("Zaandijk Zaanse Schans",  -2, -2, True),
     ("Koog aan de Zaan",  -2, -2, True),
     ("Zaandam", 19, 19), ("Amsterdam Sloterdijk", 25, 25),
     ("Amsterdam Centraal", 31, 35),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 43, 43),  ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True), ("Abcoude", -2, -2, True),
     ("Breukelen", -2, -2, True), ("Maarssen", -2, -2, True),
     ("Utrecht Zuilen", -2, -2, True), ("Utrecht Centraal", 1, -1)],


    # CS5B IC Enkhuizen - Utrecht Centraal (Heerlen) #verlengen
    [("Enkhuizen", -1, 9), ("Bovenkarspel Flora", 13, 13),
     ("Bovenkarspel-Grootebroek", 15, 18), ("Hoogkarspel", 21, 23),
     ("Hoorn Kersenboogerd", 30, 30), ("Hoorn", 33, 40),
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True),
     ("Amsterdam Sloterdijk", 5, 5), ("Amsterdam Centraal", 11, 14),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 22, 22),  ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True), ("Abcoude", -2, -2, True),
     ("Breukelen", -2, -2, True), ("Maarssen", -2, -2, True),
     ("Utrecht Zuilen", -2, -2, True), ("Utrecht Centraal", 40, -1)],

    [("Enkhuizen", -1, 39), ("Bovenkarspel Flora", 43, 43),
     ("Bovenkarspel-Grootebroek", 45, 48), ("Hoogkarspel", 51, 53),
     ("Hoorn Kersenboogerd", 60, 60), ("Hoorn", 3, 10),
     ("Purmerend Overwhere", -2, -2, True), ("Purmerend", -2, -2, True),
     ("Purmerend Weidevenne", -2, -2, True), ("Zaandam Kogerveld",  -2, -2, True),
     ("Zaandam",  -2, -2, True),
     ("Amsterdam Sloterdijk",  35, 35), ("Amsterdam Centraal", 41, 46),
     ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Amstel", 54, 54), ("Duivendrecht", -2, -2, True),
     ("Amsterdam Bijlmer Arena", -2, -2, True),
     ("Amsterdam Holendrecht", -2, -2, True), ("Abcoude", -2, -2, True),
     ("Breukelen", -2, -2, True), ("Maarssen", -2, -2, True),
     ("Utrecht Zuilen", -2, -2, True), ("Utrecht Centraal", 12, -1)],

    # CS5B Sprinter Uitgeest - Amsterdam Centraal - Utrecht Centraal (Rhenen)#verlengen
    # https://www.rijdendetreinen.nl/treinarchief/2020-01-27/7441
    # https://www.rijdendetreinen.nl/treinarchief/2020-01-27/7444
    [("Uitgeest", -1, 33), ("Krommenie-Assendelft", 37, 37),
     ("Wormerveer", 40, 45), ("Zaandijk Zaanse Schans", 48, 48),
     ("Koog aan de Zaan", 51, 51), ("Zaandam", 54, 54),
     ("Amsterdam Sloterdijk", 60, 60), ("Amsterdam Centraal", 6, 8),
     ("Amsterdam Muiderpoort", 13, 13), ("Amsterdam Amstel", 16, 16),
     ("Duivendrecht", 20, 20), ("Amsterdam Bijlmer Arena", 23, 26),
     ("Amsterdam Holendrecht", 29, 29), ("Abcoude", 32, 32),
     ("Breukelen", 41, 41), ("Maarssen", 46, 46), ("Utrecht Zuilen", 50, 50),
     ("Utrecht Centraal", 54, -1)],

    [("Uitgeest", -1, 3), ("Krommenie-Assendelft", 7, 7),
     ("Wormerveer", 10, 15), ("Zaandijk Zaanse Schans", 18, 18),
     ("Koog aan de Zaan", 21, 21), ("Zaandam", 24, 24),
     ("Amsterdam Sloterdijk", 30, 30), ("Amsterdam Centraal", 36, 38),
     ("Amsterdam Muiderpoort", 43, 43), ("Amsterdam Amstel", 46, 46),
     ("Duivendrecht", 50, 50), ("Amsterdam Bijlmer Arena", 53, 56),
     ("Amsterdam Holendrecht", 59, 59), ("Abcoude", 2, 2),
     ("Breukelen", 11, 11), ("Maarssen", 16, 16), ("Utrecht Zuilen", 20, 20),
     ("Utrecht Centraal", 24, -1)],

    # CS5B Uitgeest - Amsterdam Centraal - Rotterdam Centraal
    [('Uitgeest', -1, 48), ('Krommenie-Assendelft', 52, 52),
     ('Wormerveer', 56, 56), ('Zaandijk Zaanse Schans', 59, 59),
     ('Koog aan de Zaan', 2, 2), ('Zaandam', 5, 5),
     ('Amsterdam Sloterdijk', 11, 11), ('Amsterdam Centraal', 17, 19),
     ('Amsterdam Muiderpoort', 24, 24), ('Amsterdam Amstel', 28, 28),
     ('Duivendrecht', 31, 31), ('Amsterdam Bijlmer Arena', 34, 34),
     ('Amsterdam Holendrecht', 37, 37), ('Abcoude', 40, 40),
     ('Breukelen', 48, 50), ('Woerden', 58, 58), ('Gouda Goverwelle', 7, 7),
     ('Gouda', 10, 11), ('Nieuwerkerk a/d IJssel', 18, 18),
     ('Capelle Schollevaar', 21, 21), ('Rotterdam Alexander', 24, 24),
     ('Rotterdam Noord', 28, 28), ('Rotterdam Centraal', 34, -1)],

    [('Uitgeest', -1, 18), ('Krommenie-Assendelft', 22, 22),
     ('Wormerveer', 26, 26), ('Zaandijk Zaanse Schans', 29, 29),
     ('Koog aan de Zaan', 32, 32), ('Zaandam', 35, 35),
     ('Amsterdam Sloterdijk', 41, 41), ('Amsterdam Centraal', 47, 49),
     ('Amsterdam Muiderpoort', 54, 54), ('Amsterdam Amstel', 58, 58),
     ('Duivendrecht', 1, 1), ('Amsterdam Bijlmer Arena', 4, 4),
     ('Amsterdam Holendrecht', 7, 7), ('Abcoude', 10, 10),
     ('Breukelen', 18, 20), ('Woerden', 28, 28), ('Gouda Goverwelle', 37, 37),
     ('Gouda', 40, 41), ('Nieuwerkerk a/d IJssel', 48, 48),
     ('Capelle Schollevaar', 51, 51), ('Rotterdam Alexander', 54, 54),
     ('Rotterdam Noord', 58, 58), ('Rotterdam Centraal', 4, -1)],

    # CS7A Sprinter Rotterdam Centraal - Amsterdam Centraal - Uitgeest
    [("Rotterdam Centraal", -1, 25), ("Rotterdam Noord", 30, 30),
     ("Rotterdam Alexander", 35, 35), ("Capelle Schollevaar", 38, 38),
     ("Nieuwerkerk a/d IJssel", 41, 41), ("Gouda", 48, 49),
     ("Gouda Goverwelle", 52, 52), ("Woerden", 1, 1), ("Breukelen", 10, 11),
     ("Abcoude", 19, 19), ('Amsterdam Holendrecht', 22, 22),
     ('Amsterdam Bijlmer Arena', 25, 25), ('Duivendrecht', 28, 28),
     ('Amsterdam Amstel', 32, 32), ('Amsterdam Muiderpoort', 35, 35),
     ('Amsterdam Centraal', 41, 43), ('Amsterdam Sloterdijk', 48, 48),
     ('Zaandam', 55, 55), ('Koog aan de Zaan', 58, 58),
     ('Zaandijk Zaanse Schans', 60, 60), ('Wormerveer', 4, 4),
     ('Krommenie-Assendelft', 7, 7), ('Uitgeest', 12, -1)],

    [("Rotterdam Centraal", -1, 55), ("Rotterdam Noord", 60, 60),
     ("Rotterdam Alexander", 5, 5), ("Capelle Schollevaar", 8, 8),
     ("Nieuwerkerk a/d IJssel", 11, 11), ("Gouda", 18, 19),
     ("Gouda Goverwelle", 22, 22), ("Woerden", 31, 31), ("Breukelen", 40, 41),
     ("Abcoude", 49, 49), ('Amsterdam Holendrecht', 52, 52),
     ('Amsterdam Bijlmer Arena', 55, 55), ('Duivendrecht', 58, 58),
     ('Amsterdam Amstel', 2, 2), ('Amsterdam Muiderpoort', 5, 5),
     ('Amsterdam Centraal', 11, 13), ('Amsterdam Sloterdijk', 18, 18),
     ('Zaandam', 25, 25), ('Koog aan de Zaan', 28, 28),
     ('Zaandijk Zaanse Schans', 30, 30), ('Wormerveer', 34, 34),
     ('Krommenie-Assendelft', 37, 37), ('Uitgeest', 42, -1)],

    # CS7A Sprinter (Rhenen) Utrecht Centraal - Uitgeest #verlengen
    [('Utrecht Centraal', -1, 37), ('Utrecht Zuilen', 40, 40),
     ('Maarssen', 45, 45), ('Breukelen', 49, 49), ('Abcoude', 58, 58),
     ('Amsterdam Holendrecht', 1, 1), ('Amsterdam Bijlmer Arena', 4, 5),
     ('Duivendrecht', 7, 7), ('Amsterdam Amstel', 11, 11),
     ('Amsterdam Muiderpoort', 15, 15), ('Amsterdam Centraal', 21, 23),
     ('Amsterdam Sloterdijk', 28, 28), ('Zaandam', 35, 35),
     ('Koog aan de Zaan', 38, 38), ('Zaandijk Zaanse Schans', 40, 40),
     ('Wormerveer', 44, 48), ('Krommenie-Assendelft', 52, 52),
     ('Uitgeest', 56, -1)],

    [('Utrecht Centraal', -1, 7), ('Utrecht Zuilen', 10, 10),
     ('Maarssen', 15, 15), ('Breukelen', 19, 19), ('Abcoude', 28, 28),
     ('Amsterdam Holendrecht', 31, 31), ('Amsterdam Bijlmer Arena', 34, 35),
     ('Duivendrecht', 37, 37), ('Amsterdam Amstel', 41, 41),
     ('Amsterdam Muiderpoort', 45, 45), ('Amsterdam Centraal', 51, 53),
     ('Amsterdam Sloterdijk', 58, 58), ('Zaandam', 5, 5),
     ('Koog aan de Zaan', 8, 8), ('Zaandijk Zaanse Schans', 10, 10),
     ('Wormerveer', 14, 18), ('Krommenie-Assendelft', 22, 22),
     ('Uitgeest', 26, -1)],

    # CS8A IC (Maastricht) Utrecht Centraal - Alkmaar #verlengen
    [('Utrecht Centraal', -1, 59), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 17, 17), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 25, 29), ('Amsterdam Sloterdijk', 35, 35),
     ('Zaandam', 41, 42), ('Koog aan de Zaan', -2, -2, True),
     ('Zaandijk Zaanse Schans', -2, -2, True), ('Wormerveer', -2, -2, True),
     ('Krommenie-Assendelft', -2, -2, True), ('Uitgeest', -2, -2, True),
     ('Castricum', 54, 54), ('Heiloo', -2, -2, True), ('Alkmaar', 3, -1)],

    [('Utrecht Centraal', -1, 29), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 47, 47), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 55, 59), ('Amsterdam Sloterdijk', 5, 5),
     ('Zaandam', 11, 12), ('Koog aan de Zaan', -2, -2, True),
     ('Zaandijk Zaanse Schans', -2, -2, True), ('Wormerveer', -2, -2, True),
     ('Krommenie-Assendelft', -2, -2, True), ('Uitgeest', -2, -2, True),
     ('Castricum', 24, 24), ('Heiloo', -2, -2, True), ('Alkmaar', 33, -1)],

    # CS8A IC (Nijmegen) Utrecht Centraal - Den Helder #verlengen
    [('Utrecht Centraal', -1, 38), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 57, 57), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 5, 9), ('Amsterdam Sloterdijk', 15, 15),
     ('Zaandam', 22, 22), ('Koog aan de Zaan', -2, -2, True),
     ('Zaandijk Zaanse Schans', -2, -2, True), ('Wormerveer', -2, -2, True),
     ('Krommenie-Assendelft', -2, -2, True), ('Uitgeest', -2, -2, True),
     ('Castricum', 34, 34), ('Heiloo', 40, 40), ('Alkmaar', 46, 49),
     ('Alkmaar Noord', 52, 52), ('Heerhugowaard', 58, 58), ('Schagen', 6, 6),
     ('Anna Paulowna', 13, 15), ('Den Helder Zuid', 22, 22),
     ('Den Helder', 26, -1)],

    [('Utrecht Centraal', -1, 8), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 27, 27), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 35, 39), ('Amsterdam Sloterdijk', 45, 45),
     ('Zaandam', 52, 52), ('Koog aan de Zaan', -2, -2, True),
     ('Zaandijk Zaanse Schans', -2, -2, True), ('Wormerveer', -2, -2, True),
     ('Krommenie-Assendelft', -2, -2, True), ('Uitgeest', -2, -2, True),
     ('Castricum', 4, 4), ('Heiloo', 10, 10), ('Alkmaar', 16, 19),
     ('Alkmaar Noord', 22, 22), ('Heerhugowaard', 28, 28), ('Schagen', 36, 36),
     ('Anna Paulowna', 43, 45), ('Den Helder Zuid', 52, 52),
     ('Den Helder', 56, -1)],

    # CS8A IC (Heerlen) Utrecht Centraal - Enkhuizen #verlengen
    [('Utrecht Centraal', -1, 45), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 6, 6), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 14, 19), ('Amsterdam Sloterdijk', 25, 25),
     ('Zaandam', -2, -2, True), ('Zaandam Kogerveld', -2, -2, True),
     ('Purmerend Weidevenne', -2, -2, True), ('Purmerend', -2, -2, True),
     ('Purmerend Overwhere', -2, -2, True), ('Hoorn', 51, 56),
     ('Hoorn Kersenboogerd', 59, 60), ('Hoogkarspel', 6, 8),
     ('Bovenkarspel-Grootebroek', 13, 16), ('Bovenkarspel Flora', 18, 18),
     ('Enkhuizen', 22, -1)],

    [('Utrecht Centraal', -1, 15), ('Utrecht Zuilen', -2, -2, True),
     ('Maarssen', -2, -2, True), ('Breukelen', -2, -2, True),
     ('Abcoude', -2, -2, True), ('Amsterdam Holendrecht', -2, -2, True),
     ('Amsterdam Bijlmer Arena', -2, -2, True), ('Duivendrecht', -2, -2, True),
     ('Amsterdam Amstel', 36, 36), ('Amsterdam Muiderpoort', -2, -2, True),
     ('Amsterdam Centraal', 44, 49), ('Amsterdam Sloterdijk', 55, 55),
     ('Zaandam', -2, -2, True), ('Zaandam Kogerveld', -2, -2, True),
     ('Purmerend Weidevenne', -2, -2, True), ('Purmerend', -2, -2, True),
     ('Purmerend Overwhere', -2, -2, True), ('Hoorn', 21, 26),
     ('Hoorn Kersenboogerd', 29, 30), ('Hoogkarspel', 36, 38),
     ('Bovenkarspel-Grootebroek', 43, 46), ('Bovenkarspel Flora', 48, 48),
     ('Enkhuizen', 52, -1)],

    # CS10A IC Amsterdam Centraal - Amersfoort(Berlijn)#verlengen
    [("Amsterdam Centraal", -1, 0), ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Science Park", -2, -2, True), ("Diemen",  -2, -2, True),
     ("Weesp",  -2, -2, True), ("Naarden-Bussum",  -2, -2, True),
     ("Bussum Zuid", -2, -2, True), ("Hilversum Media Park",  -2, -2, True),
     ("Hilversum", 20, 23), ("Baarn",  -2, -2, True), ("Amersfoort", 34, -1)],

    # CS10A ICD Amsterdam Centraal - Rotterdam Centraal
    [("Amsterdam Centraal", -1, 22), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 34, 37),
     ("Rotterdam Centraal", 3, -1)],

    [("Amsterdam Centraal", -1, 53), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 4, 7),
     ("Rotterdam Centraal", 33, -1)],

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
     ("Zwolle", 24, -1)],

    [("Hoofddorp", -1, 55), ("Schiphol Airport", 59, 60),
     ("Amsterdam Lelylaan", 7, 7), ("Amsterdam Sloterdijk", 11, 11),
     ("Amsterdam Centraal", 18, 23), ("Amsterdam Muiderpoort", 28, 28),
     ("Amsterdam Science Park", 31, 31), ("Diemen", 34, 34), ("Weesp", 39, 40),
     ("Almere Poort", 47, 47), ("Almere Muziekwijk", 51, 51),
     ("Almere Centrum", 54, 55), ("Almere Parkwijk", 58, 58),
     ("Almere Buiten", 1, 1), ("Almere Oostvaarders", 4, 9),
     ("Lelystad Centrum", 20, 24), ("Dronten", 36, 36), ("Kampen Zuid", 44, 44),
     ("Zwolle", 54, -1)],

    # CS11B IC Amsterdam Centraal - Amersfoort
    [("Amsterdam Centraal", -1, 30), ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Science Park", -2, -2, True), ("Diemen", -2, -2, True),
     ("Weesp", -2, -2, True), ("Naarden-Bussum", -2, -2, True),
     ("Bussum Zuid", -2, -2, True), ("Hilversum Media Park", -2, -2, True),
     ("Hilversum", 50, 53), ("Baarn", -2, -2, True), ("Amersfoort", 4, -1)],

    # CS11B IC Amsterdam Centraal - Almere Centrum
    [("Amsterdam Centraal", -1, 8), ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Science Park", -2, -2, True), ("Diemen", -2, -2, True),
     ("Weesp", -2, -2, True), ("Almere Poort", -2, -2, True),
     ("Almere Muziekwijk", -2, -2, True), ("Almere Centrum", 28, -1)],

    [("Amsterdam Centraal", -1, 38), ("Amsterdam Muiderpoort", -2, -2, True),
     ("Amsterdam Science Park", -2, -2, True), ("Diemen", -2, -2, True),
     ("Weesp", -2, -2, True), ("Almere Poort", -2, -2, True),
     ("Almere Muziekwijk", -2, -2, True), ("Almere Centrum", 58, -1)],

    # CS13B Thalys Paris-Nord - Amsterdam Centraal #TODO goed leggen
    [("Paris-Nord", -1, 13), ("Rotterdam Centraal", 122, 126),
     ("Schiphol Airport", 25, 25), ("Amsterdam Lelylaan", -2, -2, True),
     ("Amsterdam Sloterdijk", -2, -2, True), ("Amsterdam Centraal", 44, -1)],

    # CS14A ICD Amsterdam Centraal - Breda
    [("Amsterdam Centraal", -1, 8), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 21, 23),
     ("Rotterdam Centraal", 49, 51), ("Breda", 15, -1)
     ],

    [("Amsterdam Centraal", -1, 38), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 51, 53),
     ("Rotterdam Centraal", 19, 21), ("Breda", 45, -1)
     ],

    # CS14B SPR Zwolle - Den Haag Centraal
    [("Zwolle", -1, 7), ("Kampen Zuid", 17, 17), ("Dronten", 25, 25),
     ("Lelystad Centrum", 37, 40), ("Almere Oostvaarders", 50, 55),
     ("Almere Buiten", 58, 58), ("Almere Parkwijk", 1, 1),
     ("Almere Centrum", 4, 6), ("Almere Muziekwijk", 9, 9),
     ("Almere Poort", 13, 13), ("Weesp", 20, 21),
     ("Diemen", 26, 26), ("Amsterdam Science Park", 28, 28),
     ("Amsterdam Muiderpoort", 31, 31), ("Amsterdam Centraal", 37, 41),
     ("Amsterdam Sloterdijk", 48, 48), ("Amsterdam Lelylaan", 52, 52),
     ("Schiphol Airport", 58, 60), ("Hoofddorp", 4, 4),
     ("Nieuw Vennep", 9, 9), ("Sassenheim", 16, 16),
     ("Leiden Centraal", 21, 34), ("De Vink", 37, 37), ("Voorschoten", 41, 41),
     ("Den Haag Mariahoeve", 46, 46), ("Den Haag Laan van NOI", 49, 49),
     ("Den Haag Centraal", 52, 52), ],

    [("Zwolle", -1, 37), ("Kampen Zuid", 47, 47), ("Dronten", 55, 55),
     ("Lelystad Centrum", 7, 10), ("Almere Oostvaarders", 20, 25),
     ("Almere Buiten", 28, 28), ("Almere Parkwijk", 31, 31),
     ("Almere Centrum", 34, 36), ("Almere Muziekwijk", 39, 39),
     ("Almere Poort", 43, 43), ("Weesp", 50, 51),
     ("Diemen", 56, 56), ("Amsterdam Science Park", 58, 58),
     ("Amsterdam Muiderpoort", 1, 1), ("Amsterdam Centraal", 7, 11),
     ("Amsterdam Sloterdijk", 18, 18), ("Amsterdam Lelylaan", 22, 22),
     ("Schiphol Airport", 28, 30), ("Hoofddorp", 34, 34),
     ("Nieuw Vennep", 39, 39), ("Sassenheim", 46, 46),
     ("Leiden Centraal", 51, 64), ("De Vink", 7, 7), ("Voorschoten", 11, 11),
     ("Den Haag Mariahoeve", 16, 16), ("Den Haag Laan van NOI", 19, 19),
     ("Den Haag Centraal", 22, 22), ],

    # CS14B SPR Amersfoort Vathorst - Hoofddorp
    [("Amersfoort Vathorst", -1, 54), ("Amersfoort Schothorst", 57, 57),
     ("Amersfoort", 1, 2), ("Baarn", 9, 9), ("Hilversum", 15, 16),
     ("Hilversum Media Park", 18, 18), ("Bussum Zuid", 22, 22),
     ("Naarden-Bussum", 25, 25), ("Weesp", 31, 33),
     ("Diemen", 38, 38), ("Amsterdam Science Park", 40, 40),
     ("Amsterdam Muiderpoort", 43, 43), ("Amsterdam Centraal", 49, 60),
     ("Amsterdam Sloterdijk", 6, 8), ("Amsterdam Lelylaan", 11, 11),
     ("Schiphol Airport", 18, 20), ("Hoofddorp", 24, -1)],

    [("Amersfoort Vathorst", -1, 24), ("Amersfoort Schothorst", 27, 27),
     ("Amersfoort", 31, 32), ("Baarn", 39, 39), ("Hilversum", 45, 46),
     ("Hilversum Media Park", 48, 48), ("Bussum Zuid", 52, 52),
     ("Naarden-Bussum", 55, 55), ("Weesp", 1, 3),
     ("Diemen", 8, 8), ("Amsterdam Science Park", 10, 10),
     ("Amsterdam Muiderpoort", 13, 13), ("Amsterdam Centraal", 19, 30),
     ("Amsterdam Sloterdijk", 36, 38), ("Amsterdam Lelylaan", 41, 41),
     ("Schiphol Airport", 48, 50), ("Hoofddorp", 54, -1)],

    # CS15A ICD Amsterdam Centraal - Rotterdam Centraal (Brussel-Zuid/Midi)#verlengen
    [("Amsterdam Centraal", -1, 25), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 38, 40),
     ("Rotterdam Centraal", 6, 10), ("Breda", 34, -1)],

    # CS15A Thalys Amsterdam Centraal - Paris-Nord#TODO GOED LEGGEN
    [("Amsterdam Centraal", -1, 15), ("Amsterdam Sloterdijk", -2, -2, True),
     ("Amsterdam Lelylaan", -2, -2, True), ("Schiphol Airport", 31, 34),
     ("Rotterdam Centraal", 54, 54), ("Paris-Nord", 160, -1)],
    # ======================EINDE TREINEN NAAR CENTRAAL============================
    # =========================AANKOMSTEN CENTRAAL=================================
    # CS11A Rotterdam Centraal - Amsterdam Centraal
    [('Rotterdam Centraal', -1, 55),
     ('Schiphol Airport', 19, 21), ('Amsterdam Lelylaan', -2, -2, True),
     ('Amsterdam Sloterdijk', -2, -2, True), ('Amsterdam Centraal', 35, -1)],
    [('Rotterdam Centraal', -1, 25),
     ('Schiphol Airport', 49, 51), ('Amsterdam Lelylaan', -2, -2, True),
     ('Amsterdam Sloterdijk', -2, -2, True), ('Amsterdam Centraal', 5, -1)],

    # CS13B Amersfoort - Amsterdam Centraal
    [('Amersfoort', -1, 56), ('Baarn', -2, -2, True), ('Hilversum', 8, 10),
     ('Hilversum Media Park', -2, -2, True), ('Bussum Zuid', -2, -2, True),
     ('Naarden-Bussum', -2, -2, True), ('Weesp', -2, -2, True),
     ('Diemen', -2, -2, True), ('Amsterdam Science Park', -2, -2, True),
     ('Amsterdam Muiderpoort', -2, -2, True), ('Amsterdam Centraal', 30, -1)],


    # CS14A ICD Breda - Amsterdam Centraal
    [('Breda', -1, 45), ('Rotterdam Centraal', 8, 11),
     ('Schiphol Airport', 36, 38), ('Amsterdam Lelylaan', -2, -2, True),
     ('Amsterdam Sloterdijk', -2, -2, True), ('Amsterdam Centraal', 51, -1)],

    # CS15A ICD Breda - Amsterdam Centraal
    [('Breda', -1, 15), ('Rotterdam Centraal', 38, 41),
     ('Schiphol Airport', 6, 8), ('Amsterdam Lelylaan', -2, -2, True),
     ('Amsterdam Sloterdijk', -2, -2, True), ('Amsterdam Centraal', 21, -1)],

    # CS15B ICD (Brussel-Zuid/Midi) Breda - Amsterdam Centraal
    [('Breda', -1, 26), ('Rotterdam Centraal', 49, 58),
     ('Schiphol Airport', 22, 24), ('Amsterdam Lelylaan', -2, -2, True),
     ('Amsterdam Sloterdijk', -2, -2, True), ('Amsterdam Centraal', 38, -1)],

    # ======================EINDE TREINEN VIA CENTRAAL=============================
    # ======================EINDE TREINEN VIA CENTRAAL=============================
    # ======================EINDE TREINEN VIA CENTRAAL=============================
    # ======================EINDE TREINEN VIA CENTRAAL=============================
    # ======================EINDE TREINEN VIA CENTRAAL=============================

    # IC (Leeuwarden) Zwolle - Den Haag Centraal #TODO (Verlengen?)
    [("Zwolle", -1, 17), ("Kampen Zuid", -2, -2, True),
     ("Dronten", -2, -2, True),
     ("Lelystad Centrum", 42, 43), ("Almere Oostvaarders", -2, -2, True),
     ("Almere Buiten", -2, -2, True), ("Almere Parkwijk", -2, -2, True),
     ("Almere Centrum", 57, 59, True), ("Almere Muziekwijk", -2, -2, True),
     ("Almere Poort", -2, -2, True), ("Weesp", -2, -2, True),
     ("Diemen Zuid", -2, -2, True), ("Duivendrecht", -2, -2, True),
     ("Amsterdam RAI", -2, -2, True),
     ("Amsterdam Zuid", 18, 19), ("Schiphol Airport", 25, 27),
     ("Hoofddorp", -2, -2, True), ("Nieuw Vennep", -2, -2, True),
     ("Sassenheim", -2, -2, True), ("Leiden Centraal", 43, 45),
     ("De Vink", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", -2, -2, True),
     ("Den Haag Centraal", 56, -1)],

    # IC (Groningen) Zwolle - Den Haag Centraal #TODO (Verlengen?)
    [("Zwolle", -1, 47), ("Kampen Zuid", -2, -2, True),
     ("Dronten", -2, -2, True),
     ("Lelystad Centrum", 12, 13), ("Almere Oostvaarders", -2, -2, True),
     ("Almere Buiten", -2, -2, True), ("Almere Parkwijk", -2, -2, True),
     ("Almere Centrum", 27, 29, True), ("Almere Muziekwijk", -2, -2, True),
     ("Almere Poort", -2, -2, True), ("Weesp", -2, -2, True),
     ("Diemen Zuid", -2, -2, True), ("Duivendrecht", -2, -2, True),
     ("Amsterdam RAI", -2, -2, True),
     ("Amsterdam Zuid", 48, 49), ("Schiphol Airport", 55, 57),
     ("Hoofddorp", -2, -2, True), ("Nieuw Vennep", -2, -2, True),
     ("Sassenheim", -2, -2, True), ("Leiden Centraal", 13, 15),
     ("De Vink", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("Den Haag Mariahoeve", -2, -2, True),
     ("Den Haag Laan van NOI", -2, -2, True),
     ("Den Haag Centraal", 26, -1)],

    # SPR Leiden Centraal - Hoorn Kersenboogerd
    [("Leiden Centraal", -1, 52), ("Sassenheim", 57, 57),
     ("Nieuw Vennep", 4, 4), ("Hoofddorp", 9, 9),
     ("Schiphol Airport", 13, 15), ("Amsterdam Lelylaan", 22, 22),
     ("Amsterdam Sloterdijk", 26, 28), ("Zaandam", 34, 34),
     ("Zaandam Kogerveld", 38, 38), ("Purmerend Weidevenne", 44, 44),
     ("Purmerend", 47, 47), ("Purmerend Overwhere", 50, 50),
     ("Hoorn", 1, 3), ("Hoorn Kersenboogerd", 6, -1)],

    [("Leiden Centraal", -1, 22), ("Sassenheim", 27, 27),
     ("Nieuw Vennep", 34, 34), ("Hoofddorp", 39, 39),
     ("Schiphol Airport", 43, 45), ("Amsterdam Lelylaan", 52, 52),
     ("Amsterdam Sloterdijk", 56, 58), ("Zaandam", 4, 4),
     ("Zaandam Kogerveld", 8, 8), ("Purmerend Weidevenne", 14, 14),
     ("Purmerend", 17, 17), ("Purmerend Overwhere", 20, 20),
     ("Hoorn", 31, 33), ("Hoorn Kersenboogerd", 36, -1)],


    # IC Schiphol - Lelystad Centrum
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
     ("Lelystad Centrum", 6, -1)],

    [("Dordrecht", -1, 38), ("Zwijndrecht", -2, -2, True),
     ("Barendrecht", -2, -2, True), ("Rotterdam Lombardijen", -2, -2, True),
     ("Rotterdam Zuid", -2, -2, True), ("Rotterdam Blaak", 50, 51),
     ("Rotterdam Centraal", 54, 57), ("Schiedam Centrum", 1, 1),
     ("Delft Zuid", -2, -2, True), ("Delft", 9, 9),
     ("Rijswijk", -2, -2, True), ("Den Haag Moerwijk", -2, -2, True),
     ("Den Haag HS", 16, 18), ("Den Haag Laan van NOI", 21, 21),
     ("Den Haag Mariahoeve", -2, -2, True), ("Voorschoten", -2, -2, True),
     ("De Vink", -2, -2, True), ("Leiden Centraal", 30, 31),
     ("Sassenheim", -2, -2, True), ("Nieuw Vennep", -2, -2, True),
     ("Hoofddorp", -2, -2, True),  ("Schiphol Airport", 46, 48),
     ("Amsterdam Zuid", 54, 56), ("Amsterdam RAI", -2, -2, True),
     ("Duivendrecht", 1, 1), ("Diemen Zuid", -2, -2, True),
     ("Weesp", -2, -2, True),
     ("Almere Poort", -2, -2, True),  ("Almere Muziekwijk", -2, -2, True),
     ("Almere Centrum", 17, 19), ("Almere Parkwijk", -2, -2, True),
     ("Almere Buiten", 24, 24), ("Almere Oostvaarders", -2, -2, True),
     ("Lelystad Centrum", 36, -1)],


]

timeslots_NL = []

# TIMESHEET VERTREK CENTRAAL:
# 00 14B Sprinter Hoofddorp
# 00 10A IC Berlijn
# 04 2A IC Vlissingen
# 05 4B IC Maastricht
# 08 5B Sprinter Rhenen
# 08 14A ICD Breda
# 08 11B IC Almere
# 09 8A IC Den Helder
# 11 11A Sprinter Amersfoort Vathorst
# 11 14B Sprinter Den Haag Centraal
# 11 1 Sprinter Hoorn
# 13 7A Sprinter Uitgeest
# 14 4B IC Heerlen
# 15 15A Thalys Paris-Nord
# 19 8A IC Enkhuizen
# 19 5B Sprinter Rotterdam Centraal
# 20 2A IC Den Haag Centraal
# 22 10A ICD Rotterdam Centraal
# 23 7A Sprinter Uitgeest
# 23 10B Sprinter Zwolle
# 24 4B IC Nijmegen
# 25 15A ICD Brussel-Zuid/Midi
# 26 1 Sprinter Zandvoort
# 29 8A IC Alkmaar
# 30 11B Amersfoort Centraal
# 30 14B Sprinter Hoofddorp
# 34 2A IC Vlissingen
# 35 4B IC Maastricht
# 38 14A ICD Breda
# 38 11B IC Almere
# 39 8A IC Den Helder
# 39 5B Sprinter Rhenen
# 41 11A Sprinter Amersfoort Vathorst
# 41 14B Sprinter Den Haag Centraal
# 41 1 Sprinter Hoorn
# 43 7A Sprinter Uitgeest
# 44 4B IC Heerlen
# 49 8A IC Enkhuizen
# 49 5B Sprinter Rotterdam Centraal
# 50 2A IC Den Haag Centraal
# 53 10A ICD Rotterdam Centraal
# 53 7A Sprinter Uitgeest
# 53 10B Sprinter Zwolle
# 54 4B IC Nijmegen
# 56 1 Sprinter Zandvoort
# 59 8A IC Alkmaar

# EN AANKOMSTEN DIE NIET DOORGAAN:
# 7 11A ICD van Rotterdam Centraal
# 21 15A ICD van Breda
# 30 13B IC Amersfoort Centraal
# 35 11A ICD Rotterdam Centraal
# 38 15B ICD Brussel-Zuid/Midi
# 44 13 Thalys Paris-Nord
# 51 14A ICD Breda
