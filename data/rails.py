
# format: ("begin station name", "end station name", length in km, max speed in kph)

# connection = {
#     ("Hoorn", "Amsterdam Sloterdijk", 40.3, 160): [
#         ("Hoorn", "Purmerend Overwhere",  18, 160),
#         ("Purmerend Overwhere", "Purmerend",  1.5, 160),
#         ("Purmerend", "Purmerend Weidevenne", 1.6, 160),
#         ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 160),
#         ("Zaandam Kogerveld", "Zaandam",  2.5, 160),
#         ("Zaandam", "Amsterdam Sloterdijk", 7.6, 160), ],
#
#     # TODO Afstanden
#     ("Amsterdam Zuid", "Almere Centrum", 20, 160): [
#         ("Amsterdam Zuid", "Amsterdam RAI",  1, 160),
#         ("Amsterdam RAI", "Duivendrecht",  1, 160),
#         ("Duivendrecht", "Diemen Zuid", 1, 160),
#         ("Diemen Zuid", "Weesp", 1, 160),
#         ("Weesp", "Almere Poort",  1, 160),
#         ("Almere Poort", "Almere Muziekwijk", 1, 160),
#         ("Almere Muziekwijk", "Almere Centrum", 1, 160), ],
#
#     ("Almere Centrum", "Lelystad Centrum", 24.6, 160): [
#         ("Almere Centrum", "Almere Parkwijk",  1.8, 160),
#         ("Almere Parkwijk", "Almere Buiten",  3.0, 160),
#         ("Almere Buiten", "Almere Oostvaarders", 1.8, 160),
#         ("Almere Oostvaarders", "Lelystad Centrum", 18.0, 160), ],
#
#     ("Castricum", "Zaandam", 17.3, 160): [
#         ("Castricum", "Uitgeest", 4.0, 160),
#         ("Uitgeest", "Krommenie-Assendelft",  4.6, 160),
#         ("Krommenie-Assendelft", "Wormerveer",  2.7, 160),
#         ("Wormerveer", "Zaandijk Zaanse Schans",  2.5, 160),
#         ("Zaandijk Zaanse Schans", "Koog aan de Zaan",  1.3, 160),
#         ("Koog aan de Zaan", "Zaandam",  2.2, 160), ],
# }


rail_list = [
    # Hoorn - Zaandam
    ("Hoorn", "Purmerend Overwhere",  18, 160),
    ("Purmerend Overwhere", "Purmerend",  1.5, 160),
    ("Purmerend", "Purmerend Weidevenne", 1.6, 160),
    ("Purmerend Weidevenne", "Zaandam Kogerveld", 9.4, 160),
    ("Zaandam Kogerveld", "Zaandam",  2.5, 160),

    # Zandvoort - Haarlem
    ("Zandvoort aan zee", "Overveen", 6.3, 160),
    ("Overveen", "Haarlem", 2, 160),

    # Haarlem - Amsterdam Centraal
    ("Haarlem", "Haarlem Spaarnwoude", 2.6, 130),
    ("Haarlem Spaarnwoude", "Halfweg-Zwanenburg", 5, 130),
    ("Halfweg-Zwanenburg", "Amsterdam Sloterdijk", 6.4, 130),
    ("Amsterdam Sloterdijk", "Amsterdam Centraal", 4.6, 130),

    # Hoofddorp - Sloterdijk
    ("Hoofddorp", "Schiphol Airport", 4.7, 160),
    ("Schiphol Airport", "Amsterdam Lelylaan", 8.3, 160),
    ("Amsterdam Lelylaan", "Amsterdam Sloterdijk", 3.5, 160),

    # Den Helder - Alkmaar
    ("Den Helder", "Den Helder Zuid", 2.7, 160),
    ("Den Helder Zuid", "Anna Paulowna", 8.9, 160),
    ("Anna Paulowna",  "Schagen", 9.3, 160),
    ("Schagen", "Heerhugowaard", 14, 160),
    ("Heerhugowaard", "Alkmaar Noord", 4.9, 160),
    ("Alkmaar Noord", "Alkmaar", 1.8, 160),

    # Alkmaar - Uitgeest
    ("Alkmaar", "Heiloo", 5.1, 160),
    ("Heiloo", "Castricum", 6.8, 160),
    ("Castricum", "Uitgeest", 4.0, 160),

    # Uitgeest - Zaandam
    ("Uitgeest", "Krommenie-Assendelft",  4.6, 160),
    ("Krommenie-Assendelft", "Wormerveer",  2.7, 160),
    ("Wormerveer", "Zaandijk Zaanse Schans",  2.5, 160),
    ("Zaandijk Zaanse Schans", "Koog aan de Zaan",  1.3, 160),
    ("Koog aan de Zaan", "Zaandam",  2.2, 160),

    # Zaandam - Amsterdam Sloterdijk
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 160),
    ("Zaandam", "Amsterdam Sloterdijk", 7.7, 160),

    # Amsterdam Centraal - Amsterdam Amstel
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 160),
    ("Amsterdam Muiderpoort", "Amsterdam Amstel", 2.3, 160),

    # Amsterdam Centraal - Weesp
    ("Amsterdam Centraal", "Amsterdam Muiderpoort", 3.7, 160),
    ("Amsterdam Muiderpoort", "Amsterdam Science Park", 1.5, 160),
    ("Amsterdam Science Park", "Diemen", 1.7, 160),
    ("Diemen", "Weesp", 6.2, 160),

    # Weesp - Amersfoort Vathorst
    ("Weesp", "Naarden-Bussum", 8.9, 160),
    ("Naarden-Bussum", "Bussum Zuid", 1.6, 160),
    ("Bussum Zuid", "Hilversum Media Park", 3.2, 160),
    ("Hilversum Media Park", "Hilversum", 1.5, 160),
    ("Hilversum", "Baarn", 1, 160),  # TODO
    ("Baarn", "Amersfoort", 1, 160),  # TODO
    ("Amersfoort", "Amersfoort Schothorst", 1, 160),  # TODO
    ("Amersfoort Schothorst", "Amersfoort Vathorst", 1, 160),  # TODO

    # Leiden Centraal - Schiphol Airport
    ("Leiden Centraal", "Sassenheim", 6.5, 160),
    ("Sassenheim", "Nieuw Vennep", 10.4, 160),
    ("Nieuw Vennep", "Hoofddorp", 5.3, 160),
    ("Hoofddorp", "Schiphol Airport", 4.7, 160),
    ("Hoofddorp", "Schiphol Airport", 4.7, 160),  # (Dubbel spoor)

    # Schiphol - Rotterdam Centraal (HSL)
    ("Rotterdam Centraal", "Schiphol Airport", 52.4, 160),

    # Rotterdam Centraal - Breda (HSL)
    ("Rotterdam Centraal", "Breda", 45.6, 160),

    # Zaandam - Hoorn
    ("Zaandam", "Zaandam Kogerveld", 2.5, 160),
    ("Zaandam Kogerveld", "Purmerend Weidevenne", 9.4, 160),
    ("Purmerend Weidevenne", "Purmerend", 1.6, 160),
    ("Purmerend", "Purmerend Overwhere", 1.5, 160),
    ("Purmerend Overwhere", "Hoorn", 18, 160),

    # Enkhuizen - Hoorn
    ("Enkhuizen", "Bovenkarspel Flora", 2.2, 160),
    ("Bovenkarspel Flora", "Bovenkarspel-Grootebroek", 1.2, 160),
    ("Bovenkarspel-Grootebroek", "Hoogkarspel", 3.5, 160),
    ("Hoogkarspel", "Hoorn Kersenboogerd", 7.8, 160),
    ("Hoorn Kersenboogerd", "Hoorn", 2.4, 80),

    # Zwolle - Weesp
    ("Zwolle", "Kampen Zuid", 1, 160),  # TODO
    ("Kampen Zuid", "Dronten", 1, 160),  # TODO
    ("Dronten", "Lelystad Centrum", 1, 160),  # TODO
    ("Lelystad Centrum", "Almere Oostvaarders", 18.0, 160),
    ("Almere Oostvaarders", "Almere Buiten", 1.8, 160),
    ("Almere Buiten", "Almere Parkwijk", 3.0, 160),
    ("Almere Parkwijk", "Almere Centrum", 1.8, 160),
    ("Almere Centrum", "Almere Muziekwijk", 1, 160),  # TODO
    ("Almere Muziekwijk", "Almere Poort", 1, 160),  # TODO
    ("Almere Poort", "Weesp", 1, 160),  # TODO

    # Weesp - Amsterdam RAI
    ("Weesp", "Diemen Zuid", 7.4, 160),
    ("Diemen Zuid", "Duivendrecht", 1.5, 160),
    ("Duivendrecht", "Amsterdam RAI", 3.7, 160),

    # Amsterdam RAI - Schiphol
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 160),
    ("Amsterdam RAI", "Amsterdam Zuid", 1.2, 160),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 160),
    ("Schiphol Airport", "Amsterdam Zuid", 8.3, 160),

    # Haarlem - Uitgeest
    ("Haarlem", "Bloemendaal", 2.5, 160),
    ("Bloemendaal", "Santpoort Zuid", 1.9, 160),
    ("Santpoort Zuid", "Santpoort Noord", 1.5, 160),
    ("Santpoort Noord", "Driehuis", 1.0, 160),
    ("Driehuis", "Beverwijk", 2.9, 160),
    ("Beverwijk",  "Heemskerk", 2.8, 160),
    ("Heemskerk", "Uitgeest", 3.8, 160),
    ("Uitgeest", "Castricum", 3.8, 160),

    # Heerhugowaard - Hoorn
    ("Heerhugowaard", "Obdam", 6.1, 160),
    ("Obdam", "Hoorn", 10.7, 160),

    # Haarlem - Leiden
    ("Haarlem", "Heemstede-Aerdenhout", 4.3, 160),
    ("Heemstede-Aerdenhout", "Hillegom", 6.9, 160),
    ("Hillegom", "Voorhout", 10.7, 160),
    ("Voorhout", "Leiden Centraal", 6.9, 160),

    # Leiden - Den Haag Laan van NOI
    ("Leiden Centraal", "De Vink", 1, 160),  # TODO
    ("De Vink", "Voorschoten", 1, 160),  # TODO
    ("Voorschoten", "Den Haag Mariahoeve", 1, 160),  # TODO
    ("Den Haag Mariahoeve", "Den Haag Laan van NOI", 1, 160),  # TODO

    # Den Haag Laan van NOI - Den Haag Centraal
    ("Den Haag Laan van NOI", "Den Haag Centraal", 1, 160),  # TODO

    # Den Haag Laan van NOI - Den Haag HS
    ("Den Haag Laan van NOI", "Den Haag HS", 1, 160),  # TODO

    # Den Haag Centraal - Den Haag HS
    ("Den Haag Centraal", "Den Haag HS", 1, 160),  # TODO

    # Den Haag HS - Rotterdam Centraal
    ("Den Haag HS", "Den Haag Moerwijk", 1, 160),  # TODO
    ("Den Haag Moerwijk", "Rijswijk", 1, 160),  # TODO
    ("Rijswijk", "Delft", 1, 160),  # TODO
    ("Delft", "Delft Zuid", 1, 160),  # TODO
    ("Delft Zuid", "Schiedam Centrum", 1, 160),  # TODO
    ("Schiedam Centrum", "Rotterdam Centraal", 1, 160),  # TODO

    # Rotterdam Centraal - Dordrecht
    ("Rotterdam Centraal", "Rotterdam Blaak", 1, 160),  # TODO
    ("Rotterdam Blaak", "Rotterdam Zuid", 1, 160),  # TODO
    ("Rotterdam Zuid", "Rotterdam Lombardijen", 1, 160),  # TODO
    ("Rotterdam Lombardijen", "Barendrecht", 1, 160),  # TODO
    ("Barendrecht", "Zwijndrecht", 1, 160),  # TODO
    ("Zwijndrecht", "Dordrecht", 1, 160),  # TODO

    # Amsterdam RAI - Amsterdam Bijlmer Arena
    ("Amsterdam RAI", "Amsterdam Bijlmer Arena", 4.8, 160),

    # Amsterdam Amstel - Utrecht Centraal
    ("Amsterdam Amstel", "Duivendrecht", 2.9, 160),
    ("Duivendrecht", "Amsterdam Bijlmer Arena", 1.4, 160),
    ("Amsterdam Bijlmer Arena", "Amsterdam Holendrecht", 1.8, 160),
    ("Amsterdam Holendrecht", "Abcoude", 2.5, 160),
    ("Abcoude", "Breukelen", 12.6, 160),
    ("Breukelen", "Maarssen", 5.1, 160),
    ("Maarssen", "Utrecht Zuilen", 5.3, 160),
    ("Utrecht Zuilen", "Utrecht Centraal", 2.0, 160),

    # Utrecht Centraal - Nijmegen (KORT)
    ("Utrecht Centraal", "Veenendaal-De Klomp", 1, 160),  # TODO
    ("Veenendaal-De Klomp", "Ede-Wageningen", 1, 160),  # TODO
    ("Ede-Wageningen", "Arnhem Centraal", 1, 160),  # TODO
    ("Arnhem Centraal", "Nijmegen", 1, 160),  # TODO

    # Utrecht Centraal - Nijmegen (HOE HET ZOU MOETEN)
    ("Utrecht Centraal", "Veenendaal-De Klomp", 1, 160),  # TODO
    ("Veenendaal-De Klomp", "Ede-Wageningen", 1, 160),  # TODO
    ("Ede-Wageningen", "Arnhem Centraal", 1, 160),  # TODO
    ("Arnhem Centraal", "Nijmegen", 1, 160),  # TODO

    # ("Voorhout", "Voorhout", 1, 160), #TODO

]

rail_list_NL = []
