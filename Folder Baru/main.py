import random


def generate(long):
    kata = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(long):
        acak = random.choice(kata)
        password += acak
    return password

def quotes():
    kata = ["Coding like poetry should be short and concise. ― Santosh Kalwar", 
            "It’s not a bug; it’s an undocumented feature. ― Anonymous",
            "First, solve the problem. Then, write the code. – John Johnson",
            "Code is like humor. When you have to explain it, it’s bad. – Cory House",
            "Make it work, make it right, make it fast. – Kent Beck",
            "Clean code always looks like it was written by someone who cares. — Robert C. Martin",
            "Of course, bad code can be cleaned up. But it’s very expensive.” — Robert C. Martin"
            ]
    keluaran = random.choice(kata)
    return keluaran

def math():
    asal = "x+-"
    a = random.randint(1, 100)
    b = random.choice(asal)
    c = random.randint(1, 100)
    kali = f"{a} {b} {c} =....?"
    return kali















    

