
# format: ("begin station name", "end station name", length in km, max speed in kph)

rail_list = [
    # Hoorn - Zaandam
    ("Hoorn", "Purmerend Overwhere",  18, 120),
    ("Purmerend Overwhere", "Purmerend",  1.5, 120),
    ("Purmerend", "Purmerend Weidevenne", 1.6, 120),
    ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 120),
    ("Zaandam Kogerveld", "Zaandam",  2.5, 120),

    # Zandvoort - Haarlem
    ("Zandvoort aan zee", "Overveen", 6.3, 90),
    ("Overveen", "Haarlem", 2, 70),

    # Haarlem - Amsterdam Centraal
    ("Haarlem", "Haarlem Spaarnwoude", 2.6, 80),
    ("Haarlem Spaarnwoude", "Halfweg-Zwanenburg", 5, 120),
    ("Halfweg-Zwanenburg", "Amsterdam Sloterdijk", 6.4, 120),
    ("Amsterdam Sloterdijk", "Amsterdam Centraal", 4.6, 120),

    # Hoofddorp - Sloterdijk
    ("Hoofddorp", "Schiphol Airport", 4.7, 120),
    ("Schiphol Airport", "Amsterdam Lelylaan", 8.3, 100),
    ("Amsterdam Lelylaan", "Amsterdam Sloterdijk", 3.5, 90),

    # Den Helder - Alkmaar
    ("Den Helder", "Den Helder Zuid", 2.7, 120),
    ("Den Helder Zuid", "Anna Paulowna", 8.9, 120),
    ("Anna Paulowna",  "Schagen", 9.3, 120),
    ("Schagen", "Heerhugowaard", 14, 120),
    ("Heerhugowaard", "Alkmaar Noord", 4.9, 120),
    ("Alkmaar Noord", "Alkmaar", 1.8, 120),

    # Alkmaar - Uitgeest
    ("Alkmaar", "Heiloo", 5.1, 120),
    ("Heiloo", "Castricum", 6.8, 120),
    ("Castricum", "Uitgeest", 4.0, 120),

    # Uitgeest - Zaandam
    ("Uitgeest", "Krommenie-Assendelft",  4.6, 120),
    ("Krommenie-Assendelft", "Wormerveer",  2.7, 120),
    ("Wormerveer", "Zaandijk Zaanse Schans",  2.5, 120),
    ("Zaandijk Zaanse Schans", "Koog aan de Zaan",  1.3, 120),
    ("Koog aan de Zaan", "Zaandam",  2.2, 120),

    # Zaandam - Amsterdam Sloterdijk
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 120),
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 120),

    # Amsterdam Centraal - Amsterdam Amstel
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 70),
    ("Amsterdam Muiderpoort", "Amsterdam Amstel", 2.3, 70),

    # Amsterdam Centraal - Weesp
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 70),
    ("Amsterdam Muiderpoort", "Amsterdam Science Park", 1.5, 70),
    ("Amsterdam Science Park", "Diemen", 1.7, 80),
    ("Diemen", "Weesp", 6.2, 120),

    # Weesp - Amersfoort Vathorst
    ("Weesp", "Naarden-Bussum", 8.9, 120),
    ("Naarden-Bussum", "Bussum Zuid", 1.6, 70),
    ("Bussum Zuid", "Hilversum Media Park", 3.2, 120),
    ("Hilversum Media Park", "Hilversum", 1.5, 70),
    ("Hilversum", "Baarn", 7.3, 120),
    ("Baarn", "Amersfoort", 8.8, 120),
    ("Amersfoort", "Amersfoort Schothorst", 3.4, 120),
    ("Amersfoort Schothorst", "Amersfoort Vathorst", 2.8, 120),

    # Leiden Centraal - Schiphol Airport
    ("Leiden Centraal", "Sassenheim", 6.5, 120),
    ("Sassenheim", "Nieuw Vennep", 10.4, 120),
    ("Nieuw Vennep", "Hoofddorp", 5.3, 120),
    ("Hoofddorp", "Schiphol Airport", 4.7, 120),
    ("Hoofddorp", "Schiphol Airport", 4.7, 120),  # (Dubbel spoor)

    # Schiphol - Rotterdam Centraal (HSL)
    ("Rotterdam Centraal", "Schiphol Airport", 52.4, 350),

    # Rotterdam Centraal - Breda (HSL)
    ("Rotterdam Centraal", "Breda", 45.6, 350),

    # Rotterdam Centraal - Parijs (HSL)
    ("Rotterdam Centraal", "Paris-Nord", 470, 350),

    # Zaandam - Hoorn
    ("Zaandam", "Zaandam Kogerveld", 2.5, 120),
    ("Zaandam Kogerveld", "Purmerend Weidevenne", 9.4, 120),
    ("Purmerend Weidevenne", "Purmerend", 1.6, 70),
    ("Purmerend", "Purmerend Overwhere", 1.5, 70),
    ("Purmerend Overwhere", "Hoorn", 18, 120),

    # Enkhuizen - Hoorn
    ("Enkhuizen", "Bovenkarspel Flora", 2.2, 120),
    ("Bovenkarspel Flora", "Bovenkarspel-Grootebroek", 1.2, 60),
    ("Bovenkarspel-Grootebroek", "Hoogkarspel", 3.5, 120),
    ("Hoogkarspel", "Hoorn Kersenboogerd", 7.8, 120),
    ("Hoorn Kersenboogerd", "Hoorn", 2.4, 80),

    # Zwolle - Weesp
    ("Zwolle", "Kampen Zuid", 15, 120),
    ("Kampen Zuid", "Dronten", 13.4, 120),
    ("Dronten", "Lelystad Centrum", 20.6, 120),
    ("Lelystad Centrum", "Almere Oostvaarders", 18.0, 120),
    ("Almere Oostvaarders", "Almere Buiten", 1.8, 120),
    ("Almere Buiten", "Almere Parkwijk", 3.0, 120),
    ("Almere Parkwijk", "Almere Centrum", 1.8, 70),
    ("Almere Centrum", "Almere Muziekwijk", 2, 120),
    ("Almere Muziekwijk", "Almere Poort", 4, 120),
    ("Almere Poort", "Weesp", 9.6, 120),

    # Weesp - Amsterdam RAI
    ("Weesp", "Diemen Zuid", 7.4, 120),
    ("Diemen Zuid", "Duivendrecht", 1.5, 60),
    ("Duivendrecht", "Amsterdam RAI", 3.7, 120),

    # Amsterdam RAI - Schiphol
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 60),
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 60),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 120),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 120),

    # Haarlem - Uitgeest
    ("Haarlem", "Bloemendaal", 2.5, 90),
    ("Bloemendaal", "Santpoort Zuid", 1.9, 90),
    ("Santpoort Zuid", "Santpoort Noord", 1.5, 60),
    ("Santpoort Noord", "Driehuis", 1.0, 50),
    ("Driehuis", "Beverwijk", 2.9, 120),
    ("Beverwijk",  "Heemskerk", 2.8, 120),
    ("Heemskerk", "Uitgeest", 3.8, 120),
    ("Uitgeest", "Castricum", 3.8, 120),

    # Heerhugowaard - Hoorn
    ("Heerhugowaard", "Obdam", 6.1, 120),
    ("Obdam", "Hoorn", 10.7, 120),

    # Haarlem - Leiden
    ("Haarlem", "Heemstede-Aerdenhout", 4.3, 120),
    ("Heemstede-Aerdenhout", "Hillegom", 6.9, 120),
    ("Hillegom", "Voorhout", 10.7, 120),
    ("Voorhout", "Leiden Centraal", 6.9, 120),

    # Leiden - Den Haag Laan van NOI
    ("Leiden Centraal", "De Vink", 2.7, 120),
    ("De Vink", "Voorschoten", 3.6, 120),
    ("Voorschoten", "Den Haag Mariahoeve", 6, 120),
    ("Den Haag Mariahoeve", "Den Haag Laan van NOI", 2.3, 120),

    # Den Haag Laan van NOI - Den Haag Centraal
    ("Den Haag Laan van NOI", "Den Haag Centraal", 1.3, 50),

    # Den Haag Laan van NOI - Den Haag HS
    ("Den Haag Laan van NOI", "Den Haag HS", 1.7, 50),

    # Den Haag Centraal - Den Haag HS
    ("Den Haag Centraal", "Den Haag HS", 1.6, 50),

    # Den Haag HS - Rotterdam Centraal
    ("Den Haag HS", "Den Haag Moerwijk", 2, 120),
    ("Den Haag Moerwijk", "Rijswijk", 1.7, 120),
    ("Rijswijk", "Delft", 4.5, 120),
    ("Delft", "Delft Zuid", 1.9, 120),
    ("Delft Zuid", "Schiedam Centrum", 8.4, 120),
    ("Schiedam Centrum", "Rotterdam Centraal", 3.9, 120),

    # Rotterdam Centraal - Dordrecht
    ("Rotterdam Centraal", "Rotterdam Blaak", 1.7, 120),
    ("Rotterdam Blaak", "Rotterdam Zuid", 2.3, 120),
    ("Rotterdam Zuid", "Rotterdam Lombardijen", 3, 120),
    ("Rotterdam Lombardijen", "Barendrecht", 3.2, 120),
    ("Barendrecht", "Zwijndrecht", 7.6, 120),
    ("Zwijndrecht", "Dordrecht", 1, 120),

    # Amsterdam RAI - Amsterdam Bijlmer Arena
    ("Amsterdam RAI", "Amsterdam Bijlmer Arena", 4.8, 120),

    # Amsterdam Amstel - Utrecht Centraal
    ("Amsterdam Amstel", "Duivendrecht", 2.9, 120),
    ("Duivendrecht", "Amsterdam Bijlmer Arena", 1.4, 120),
    ("Amsterdam Bijlmer Arena", "Amsterdam Holendrecht", 1.8, 120),
    ("Amsterdam Holendrecht", "Abcoude", 2.5, 120),
    ("Abcoude", "Breukelen", 12.6, 120),
    ("Breukelen", "Maarssen", 5.1, 120),
    ("Maarssen", "Utrecht Zuilen", 5.3, 120),
    ("Utrecht Zuilen", "Utrecht Centraal", 2.0, 120),

    # Rotterdam Centraal - Gouda
    ("Rotterdam Centraal", "Rotterdam Noord", 4.7, 120),
    ("Rotterdam Noord", "Rotterdam Alexander", 4.9, 120),
    ("Rotterdam Alexander", "Capelle Schollevaar", 2.2, 120),
    ("Capelle Schollevaar", "Nieuwerkerk a/d IJssel", 2.6, 120),
    ("Nieuwerkerk a/d IJssel", "Gouda", 9.2, 120),

    # Gouda - Woerden
    ("Gouda", "Gouda Goverwelle", 2.4, 120),
    ("Gouda Goverwelle", "Woerden", 13.8, 120),

    # Woerden - Breukelen
    ("Woerden", "Breukelen", 12.5, 120),

]

rail_list_NL = []
