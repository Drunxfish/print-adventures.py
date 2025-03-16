# # assoc lijst doorlopen
# asoclijst = {'Wick': 22, 'Alex': 21}
# for i,k in asoclijst.items():
#     print(i, " Is ", k, " Oud")



# slice van lijst
# output: le
name  = "alex"
print(name[1:3])


# in of not in
lijst = [1, 2, 3, 4, 5]

for i in lijst:
    if 6 in lijst:
        print("6 is in de lijst")
    elif 6 not in lijst:
        print("6 is niet in de lijst")
    break