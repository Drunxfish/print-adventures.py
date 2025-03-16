# Globals, Scope, Pip, PyPi
from faker import Faker

# -------- Global/Scope ----------------
# number = 200

# def modify():
#     global number
#     number = 100
#     return number

# # number = modify()
# modify()
# print(number)
# --------------------------------------


# ----------    Pip   ------------------
# Preferred Installer Program  = pip #
info = Faker()

print(info.name())
print(info.address())

# --------------------------------------
