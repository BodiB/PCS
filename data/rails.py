
# format: ("begin station name", "end station name", length in km, max speed in kph)

# connection = {
#     ("Hoorn", "Amsterdam Sloterdijk", 40.3, 130): [
#         ("Hoorn", "Purmerend Overwhere",  18, 130),
#         ("Purmerend Overwhere", "Purmerend",  1.5, 130),
#         ("Purmerend", "Purmerend Weidevenne", 1.6, 130),
#         ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 130),
#         ("Zaandam Kogerveld", "Zaandam",  2.5, 130),
#         ("Zaandam", "Amsterdam Sloterdijk", 7.6, 130), ],
#
#     # TODO Afstanden
#     ("Amsterdam Zuid", "Almere Centrum", 20, 130): [
#         ("Amsterdam Zuid", "Amsterdam RAI",  1, 130),
#         ("Amsterdam RAI", "Duivendrecht",  1, 130),
#         ("Duivendrecht", "Diemen Zuid", 1, 130),
#         ("Diemen Zuid", "Weesp", 1, 130),
#         ("Weesp", "Almere Poort",  1, 130),
#         ("Almere Poort", "Almere Muziekwijk", 1, 130),
#         ("Almere Muziekwijk", "Almere Centrum", 1, 130), ],
#
#     ("Almere Centrum", "Lelystad Centrum", 24.6, 130): [
#         ("Almere Centrum", "Almere Parkwijk",  1.8, 130),
#         ("Almere Parkwijk", "Almere Buiten",  3.0, 130),
#         ("Almere Buiten", "Almere Oostvaarders", 1.8, 130),
#         ("Almere Oostvaarders", "Lelystad Centrum", 18.0, 130), ],
#
#     ("Castricum", "Zaandam", 17.3, 130): [
#         ("Castricum", "Uitgeest", 4.0, 130),
#         ("Uitgeest", "Krommenie-Assendelft",  4.6, 130),
#         ("Krommenie-Assendelft", "Wormerveer",  2.7, 130),
#         ("Wormerveer", "Zaandijk Zaanse Schans",  2.5, 130),
#         ("Zaandijk Zaanse Schans", "Koog aan de Zaan",  1.3, 130),
#         ("Koog aan de Zaan", "Zaandam",  2.2, 130), ],
# }


rail_list = [
    # Hoorn - Zaandam
    ("Hoorn", "Purmerend Overwhere",  18, 130),
    ("Purmerend Overwhere", "Purmerend",  1.5, 130),
    ("Purmerend", "Purmerend Weidevenne", 1.6, 130),
    ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 130),
    ("Zaandam Kogerveld", "Zaandam",  2.5, 130),

    # Zandvoort - Haarlem
    ("Zandvoort aan zee", "Overveen", 6.3, 130),
    ("Overveen", "Haarlem", 2, 130),

    # Haarlem - Amsterdam Centraal
    ("Haarlem", "Haarlem Spaarnwoude", 2.6, 130),
    ("Haarlem Spaarnwoude", "Halfweg-Zwanenburg", 5, 130),
    ("Halfweg-Zwanenburg", "Amsterdam Sloterdijk", 6.4, 130),
    ("Amsterdam Sloterdijk", "Amsterdam Centraal", 4.6, 130),

    # Hoofddorp - Sloterdijk
    ("Hoofddorp", "Schiphol Airport", 4.7, 130),
    ("Schiphol Airport", "Amsterdam Lelylaan", 8.3, 130),
    ("Amsterdam Lelylaan", "Amsterdam Sloterdijk", 3.5, 130),

    # Den Helder - Alkmaar
    ("Den Helder", "Den Helder Zuid", 2.7, 130),
    ("Den Helder Zuid", "Anna Paulowna", 8.9, 130),
    ("Anna Paulowna",  "Schagen", 9.3, 130),
    ("Schagen", "Heerhugowaard", 14, 130),
    ("Heerhugowaard", "Alkmaar Noord", 4.9, 130),
    ("Alkmaar Noord", "Alkmaar", 1.8, 130),

    # Alkmaar - Uitgeest
    ("Alkmaar", "Heiloo", 5.1, 130),
    ("Heiloo", "Castricum", 6.8, 130),
    ("Castricum", "Uitgeest", 4.0, 130),

    # Uitgeest - Zaandam
    ("Uitgeest", "Krommenie-Assendelft",  4.6, 130),
    ("Krommenie-Assendelft", "Wormerveer",  2.7, 130),
    ("Wormerveer", "Zaandijk Zaanse Schans",  2.5, 130),
    ("Zaandijk Zaanse Schans", "Koog aan de Zaan",  1.3, 130),
    ("Koog aan de Zaan", "Zaandam",  2.2, 130),

    # Zaandam - Amsterdam Sloterdijk
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 130),
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 130),

    # Amsterdam Centraal - Amsterdam Amstel
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 130),
    ("Amsterdam Muiderpoort", "Amsterdam Amstel", 2.3, 130),

    # Amsterdam Centraal - Weesp
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 130),
    ("Amsterdam Muiderpoort", "Amsterdam Science Park", 1.5, 130),
    ("Amsterdam Science Park", "Diemen", 1.7, 130),
    ("Diemen", "Weesp", 6.2, 130),

    # Weesp - Amersfoort Vathorst
    ("Weesp", "Naarden-Bussum", 8.9, 130),
    ("Naarden-Bussum", "Bussum Zuid", 1.6, 130),
    ("Bussum Zuid", "Hilversum Media Park", 3.2, 130),
    ("Hilversum Media Park", "Hilversum", 1.5, 130),
    ("Hilversum", "Baarn", 1, 130),  # TODO
    ("Baarn", "Amersfoort", 1, 130),  # TODO
    ("Amersfoort", "Amersfoort Schothorst", 1, 130),  # TODO
    ("Amersfoort Schothorst", "Amersfoort Vathorst", 1, 130),  # TODO

    # Leiden Centraal - Schiphol Airport
    ("Leiden Centraal", "Sassenheim", 6.5, 130),
    ("Sassenheim", "Nieuw Vennep", 10.4, 130),
    ("Nieuw Vennep", "Hoofddorp", 5.3, 130),
    ("Hoofddorp", "Schiphol Airport", 4.7, 130),
    ("Hoofddorp", "Schiphol Airport", 4.7, 130),  # (Dubbel spoor)

    # Schiphol - Rotterdam Centraal (HSL)
    ("Rotterdam Centraal", "Schiphol Airport", 52.4, 130),

    # Rotterdam Centraal - Breda (HSL)
    ("Rotterdam Centraal", "Breda", 45.6, 130),

    # Zaandam - Hoorn
    ("Zaandam", "Zaandam Kogerveld", 2.5, 130),
    ("Zaandam Kogerveld", "Purmerend Weidevenne", 9.4, 130),
    ("Purmerend Weidevenne", "Purmerend", 1.6, 130),
    ("Purmerend", "Purmerend Overwhere", 1.5, 130),
    ("Purmerend Overwhere", "Hoorn", 18, 130),

    # Enkhuizen - Hoorn
    ("Enkhuizen", "Bovenkarspel Flora", 2.2, 130),
    ("Bovenkarspel Flora", "Bovenkarspel-Grootebroek", 1.2, 130),
    ("Bovenkarspel-Grootebroek", "Hoogkarspel", 3.5, 130),
    ("Hoogkarspel", "Hoorn Kersenboogerd", 7.8, 130),
    ("Hoorn Kersenboogerd", "Hoorn", 2.4, 80),

    # Zwolle - Weesp
    ("Zwolle", "Kampen Zuid", 1, 130),  # TODO
    ("Kampen Zuid", "Dronten", 1, 130),  # TODO
    ("Dronten", "Lelystad Centrum", 1, 130),  # TODO
    ("Lelystad Centrum", "Almere Oostvaarders", 18.0, 130),
    ("Almere Oostvaarders", "Almere Buiten", 1.8, 130),
    ("Almere Buiten", "Almere Parkwijk", 3.0, 130),
    ("Almere Parkwijk", "Almere Centrum", 1.8, 130),
    ("Almere Centrum", "Almere Muziekwijk", 1, 130),  # TODO
    ("Almere Muziekwijk", "Almere Poort", 1, 130),  # TODO
    ("Almere Poort", "Weesp", 1, 130),  # TODO

    # Weesp - Amsterdam RAI
    ("Weesp", "Diemen Zuid", 7.4, 130),
    ("Diemen Zuid", "Duivendrecht", 1.5, 130),
    ("Duivendrecht", "Amsterdam RAI", 3.7, 130),

    # Amsterdam RAI - Schiphol
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 130),
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 130),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 130),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 130),

    # Haarlem - Uitgeest
    ("Haarlem", "Bloemendaal", 2.5, 130),
    ("Bloemendaal", "Santpoort Zuid", 1.9, 130),
    ("Santpoort Zuid", "Santpoort Noord", 1.5, 130),
    ("Santpoort Noord", "Driehuis", 1.0, 130),
    ("Driehuis", "Beverwijk", 2.9, 130),
    ("Beverwijk",  "Heemskerk", 2.8, 130),
    ("Heemskerk", "Uitgeest", 3.8, 130),
    ("Uitgeest", "Castricum", 3.8, 130),

    # Heerhugowaard - Hoorn
    ("Heerhugowaard", "Obdam", 6.1, 130),
    ("Obdam", "Hoorn", 10.7, 130),

    # Haarlem - Leiden
    ("Haarlem", "Heemstede-Aerdenhout", 4.3, 130),
    ("Heemstede-Aerdenhout", "Hillegom", 6.9, 130),
    ("Hillegom", "Voorhout", 10.7, 130),
    ("Voorhout", "Leiden Centraal", 6.9, 130),

    # Leiden - Den Haag Laan van NOI
    ("Leiden Centraal", "De Vink", 1, 130),  # TODO
    ("De Vink", "Voorschoten", 1, 130),  # TODO
    ("Voorschoten", "Den Haag Mariahoeve", 1, 130),  # TODO
    ("Den Haag Mariahoeve", "Den Haag Laan van NOI", 1, 130),  # TODO

    # Den Haag Laan van NOI - Den Haag Centraal
    ("Den Haag Laan van NOI", "Den Haag Centraal", 1, 130),  # TODO

    # Den Haag Laan van NOI - Den Haag HS
    ("Den Haag Laan van NOI", "Den Haag HS", 1, 130),  # TODO

    # Den Haag Centraal - Den Haag HS
    ("Den Haag Centraal", "Den Haag HS", 1, 130),  # TODO

    # Den Haag HS - Rotterdam Centraal
    ("Den Haag HS", "Den Haag Moerwijk", 1, 130),  # TODO
    ("Den Haag Moerwijk", "Rijswijk", 1, 130),  # TODO
    ("Rijswijk", "Delft", 1, 130),  # TODO
    ("Delft", "Delft Zuid", 1, 130),  # TODO
    ("Delft Zuid", "Schiedam Centrum", 1, 130),  # TODO
    ("Schiedam Centrum", "Rotterdam Centraal", 1, 130),  # TODO

    # Rotterdam Centraal - Dordrecht
    ("Rotterdam Centraal", "Rotterdam Blaak", 1, 130),  # TODO
    ("Rotterdam Blaak", "Rotterdam Zuid", 1, 130),  # TODO
    ("Rotterdam Zuid", "Rotterdam Lombardijen", 1, 130),  # TODO
    ("Rotterdam Lombardijen", "Barendrecht", 1, 130),  # TODO
    ("Barendrecht", "Zwijndrecht", 1, 130),  # TODO
    ("Zwijndrecht", "Dordrecht", 1, 130),  # TODO

    # Amsterdam RAI - Amsterdam Bijlmer Arena
    ("Amsterdam RAI", "Amsterdam Bijlmer Arena", 4.8, 130),

    # Amsterdam Amstel - Utrecht Centraal
    ("Amsterdam Amstel", "Duivendrecht", 2.9, 130),
    ("Duivendrecht", "Amsterdam Bijlmer Arena", 1.4, 130),
    ("Amsterdam Bijlmer Arena", "Amsterdam Holendrecht", 1.8, 130),
    ("Amsterdam Holendrecht", "Abcoude", 2.5, 130),
    ("Abcoude", "Breukelen", 12.6, 130),
    ("Breukelen", "Maarssen", 5.1, 130),
    ("Maarssen", "Utrecht Zuilen", 5.3, 130),
    ("Utrecht Zuilen", "Utrecht Centraal", 2.0, 130),

    # Utrecht Centraal - Nijmegen (KORT)
    ("Utrecht Centraal", "Veenendaal-De Klomp", 1, 130),  # TODO
    ("Veenendaal-De Klomp", "Ede-Wageningen", 1, 130),  # TODO
    ("Ede-Wageningen", "Arnhem Centraal", 1, 130),  # TODO
    ("Arnhem Centraal", "Nijmegen", 1, 130),  # TODO

    # Utrecht Centraal - Nijmegen (HOE HET ZOU MOETEN)
    ("Utrecht Centraal", "Veenendaal-De Klomp", 1, 130),  # TODO
    ("Veenendaal-De Klomp", "Ede-Wageningen", 1, 130),  # TODO
    ("Ede-Wageningen", "Arnhem Centraal", 1, 130),  # TODO
    ("Arnhem Centraal", "Nijmegen", 1, 130),  # TODO

    # ("Voorhout", "Voorhout", 1, 130), #TODO

]

rail_list_NL = []
