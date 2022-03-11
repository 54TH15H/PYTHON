sampleInput = input()
result = 0
for i in sampleInput.split():
    if len(i) > 1:
        if i[1].isnumeric():
            result += 1

print(result)
