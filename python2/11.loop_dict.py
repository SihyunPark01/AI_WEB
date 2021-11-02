# 리스트는 순서가 있는 데이터를 담고, 색인을 통해서 식별함
# 딕셔너리는 순서가 없는 데이터를 담고, 이름을 통해서 식별함


members = [
    {'city':'Seoul', 'job':'WEB', 'name':'egoing'},
    {'city':'Jeju', 'job':'Design', 'name':'leezche'}
]
print(members[0]['city'])
for member in members:
    print(member['name'], member['city'], member['job'])