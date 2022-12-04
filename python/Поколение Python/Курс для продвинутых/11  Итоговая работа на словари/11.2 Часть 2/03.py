d = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}

scores = {j: i[0] for i in d.items() for j in i[1]}
result = 0

for _ in input():
    result += scores[_]

print(result)