# ...
def get_vat(가격):
    부가가치세율 = 0.1
    return 가격*부가가치세율
# ...

print(get_vat(10000))

# 가격 = 10000
# return은 값으로 만들어주므로 return값이 곧 그 함수의 출력값