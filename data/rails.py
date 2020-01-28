
# format: ("begin station name", "end station name", length in km, max speed in kph)

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
    ("Hilversum", "Baarn", 7.3, 130), 
    ("Baarn", "Amersfoort", 8.8, 130),  
    ("Amersfoort", "Amersfoort Schothorst", 3.4, 130), 
    ("Amersfoort Schothorst", "Amersfoort Vathorst", 2.8, 130),  

    # Leiden Centraal - Schiphol Airport
    ("Leiden Centraal", "Sassenheim", 6.5, 130),
    ("Sassenheim", "Nieuw Vennep", 10.4, 130),
    ("Nieuw Vennep", "Hoofddorp", 5.3, 130),
    ("Hoofddorp", "Schiphol Airport", 4.7, 130),
    ("Hoofddorp", "Schiphol Airport", 4.7, 130),  # (Dubbel spoor)

    # Schiphol - Rotterdam Centraal (HSL)
    ("Rotterdam Centraal", "Schiphol Airport", 52.4, 350),

    # Rotterdam Centraal - Breda (HSL)
    ("Rotterdam Centraal", "Breda", 45.6, 350),

    # Rotterdam Centraal - Parijs (HSL)
    ("Rotterdam Centraal", "Paris-Nord", 470, 350),

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
    ("Zwolle", "Kampen Zuid", 15, 130),  
    ("Kampen Zuid", "Dronten", 13.4, 130),  
    ("Dronten", "Lelystad Centrum", 20.6, 130),  
    ("Lelystad Centrum", "Almere Oostvaarders", 18.0, 130),
    ("Almere Oostvaarders", "Almere Buiten", 1.8, 130),
    ("Almere Buiten", "Almere Parkwijk", 3.0, 130),
    ("Almere Parkwijk", "Almere Centrum", 1.8, 130),
    ("Almere Centrum", "Almere Muziekwijk", 2, 130),  
    ("Almere Muziekwijk", "Almere Poort", 4, 130),  
    ("Almere Poort", "Weesp", 9.6, 130),  

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
    ("Leiden Centraal", "De Vink", 2.7, 130),
    ("De Vink", "Voorschoten", 3.6, 130),  
    ("Voorschoten", "Den Haag Mariahoeve", 6, 130),  
    ("Den Haag Mariahoeve", "Den Haag Laan van NOI", 2.3, 130), 

    # Den Haag Laan van NOI - Den Haag Centraal
    ("Den Haag Laan van NOI", "Den Haag Centraal", 1.3, 130), 

    # Den Haag Laan van NOI - Den Haag HS
    ("Den Haag Laan van NOI", "Den Haag HS", 1.7, 130), 

    # Den Haag Centraal - Den Haag HS
    ("Den Haag Centraal", "Den Haag HS", 1.6, 130), 

    # Den Haag HS - Rotterdam Centraal
    ("Den Haag HS", "Den Haag Moerwijk", 2, 130),  
    ("Den Haag Moerwijk", "Rijswijk", 1.7, 130),  
    ("Rijswijk", "Delft", 4.5, 130), 
    ("Delft", "Delft Zuid", 1.9, 130),  
    ("Delft Zuid", "Schiedam Centrum", 8.4, 130),  
    ("Schiedam Centrum", "Rotterdam Centraal", 3.9, 130),  

    # Rotterdam Centraal - Dordrecht
    ("Rotterdam Centraal", "Rotterdam Blaak", 1.7, 130),  
    ("Rotterdam Blaak", "Rotterdam Zuid", 2.3, 130),  
    ("Rotterdam Zuid", "Rotterdam Lombardijen", 3, 130),  
    ("Rotterdam Lombardijen", "Barendrecht", 3.2, 130),  
    ("Barendrecht", "Zwijndrecht", 7.6, 130),  
    ("Zwijndrecht", "Dordrecht", 1, 130),  

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
    ("Utrecht Centraal", "Veenendaal-De Klomp", 33.1, 130), 
    ("Veenendaal-De Klomp", "Ede-Wageningen", 7, 130),  
    ("Ede-Wageningen", "Arnhem Centraal", 16.3, 130), 
    ("Arnhem Centraal", "Nijmegen", 18.4, 130),  

    # Utrecht Centraal - Nijmegen (HOE HET ZOU MOETEN)
    #???
#    ("Utrecht Centraal", "Veenendaal-De Klomp", 1, 130),  # TODO
#    ("Veenendaal-De Klomp", "Ede-Wageningen", 1, 130),  # TODO
#    ("Ede-Wageningen", "Arnhem Centraal", 1, 130),  # TODO
#    ("Arnhem Centraal", "Nijmegen", 1, 130),  # TODO

    # Rotterdam Centraal - Gouda
    ("Rotterdam Centraal", "Rotterdam Noord", 4.7, 130),  
    ("Rotterdam Noord", "Rotterdam Alexander", 4.9, 130),  
    ("Rotterdam Alexander", "Capelle Schollevaar", 2.2, 130),
    ("Capelle Schollevaar", "Nieuwerkerk a/d IJssel", 2.6, 130), 
    ("Nieuwerkerk a/d IJssel", "Gouda", 9.2, 130), 

    # Gouda - Woerden
    ("Gouda", "Gouda Goverwelle", 2.4, 130),  
    ("Gouda Goverwelle", "Woerden", 13.8, 130), 

    # Woerden - Breukelen
    ("Woerden", "Breukelen", 12.5, 130),  

]

rail_list_NL = []
