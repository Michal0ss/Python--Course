# Loop Control Statements = change a loops execution from its normal sequence

# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as a placeholder

while True:
    name = input("enter ur name: ")
    if name != "":
        break

phone_number="123-456-7890"

for i in phone_number:
    if i =="-":
        continue
    print(i, end="")

for x in range(1, 21):
    if x==13:
        pass
    else:
        print(x)
