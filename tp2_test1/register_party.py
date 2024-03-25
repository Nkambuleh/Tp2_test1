

def register_party(parties):
    for party in parties:
        party_name = party.get("party_name")
        reg_number = party.get("reg_number")
        member_count = party.get("member_count")
        
        
        if member_count >= 1000:
            print(f"Party '{party_name}' with registration number '{reg_number}' has enough members for registration.")
        else:
            print(f"Party '{party_name}' with registration number '{reg_number}' does not have enough members for registration.")
