##2.3

def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
    if voter_id in voter_info:
        
        voter_info[voter_id]["name"] = name
        voter_info[voter_id]["voting_district"] = voting_district
        voter_info[voter_id]["has_voted"] = has_voted
    else:
        
        voter_info[voter_id] = {
            "name": name,
            "voting_district": voting_district,
            "has_voted": has_voted
        }
