
voter_records = [
    {'voter_id': 1, 'name': 'John', 'registered': True},
    {'voter_id': 2, 'name': 'Jane', 'registered': False},
    {'voter_id': 3, 'name': 'Alice', 'registered': True},
    {'voter_id': 4, 'name': 'Bob', 'registered': False},
    {'voter_id': 5, 'name': 'Charlie', 'registered': True}
]


registered_voters = list(filter(lambda record: record['registered'], voter_records))

print(registered_voters)
