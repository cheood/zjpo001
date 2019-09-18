a = '6'
arrs = ["3", '23', "123", "334"]

for arr in arrs:
    if a in arr:
        print(arr + "中包含" + a)
else:
    print("arrs中都不包含" + a)

b = 4
if b > 3 and b < 5:
    print("b", b)
