# s = input()
# t = input()
# djkv
# f1 = {}
# f2 = {}
# for i in s:
#     f1[i] = f1.get(i,0)+1
# for j in t:
#     f2[j] = f2.get(j,0)+1
# print(f1==f2)
# print(f1[max(f1,key=f1.get)])


from collections import Counter
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
common = Counter(a) & Counter(b)
result = sorted(common.elements())
print(' '.join(map(str, result)) if result else "No common elements")
