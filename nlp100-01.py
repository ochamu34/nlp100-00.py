a="パトカー"
b="タクシー"

for i in range(4):
    c=a[0++i]+b[0++i]
    print(c)

for i in range(8):
    d=c[0++i*2]
    print(d)