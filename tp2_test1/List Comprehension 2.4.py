##2.4
parties = ["ANC", "DA", "EFF", "IFP", "NFP", "FF+", "ATM", "COPE", "ACDP", "UDM", "GOOD", "ALJAMA", "BLF", "PAC", "COSATU", "PA", "COPE", "ICOSA", "UDM", "EFF", "NFP", "IFP", "PA", "ANC", "ATM", "ALJAMA", "ACDP", "GOOD", "BLF", "ICOSA", "FF+", "COSATU", "DA", "PAC"]


filtered_parties = [party for party in parties if len(party) >= 4]

print(filtered_parties)
