##2.5 Normal List Data structure


parties = ["ANC", "DA", "EFF", "IFP", "NFP", "FF+", "ATM", "COPE", "ACDP", "UDM", "GOOD", "ALJAMA", "BLF", "PAC", "COSATU", "PA", "COPE", "ICOSA", "UDM", "EFF", "NFP", "IFP", "PA", "ANC", "ATM", "ALJAMA", "ACDP", "GOOD", "BLF", "ICOSA", "FF+", "COSATU", "DA", "PAC"]


filtered_parties = []

for party in parties:
    if len(party) >= 4:
        filtered_parties.append(party)

print(filtered_parties)
