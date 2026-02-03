numbers: list[int] = [1,2,3,4,5,6]

evens_traditioanls: list[int] = []
for n in numbers:
    if n % 2 == 0:
        evens_traditioanls.append(n)

evens: list[int] = [n for n in numbers if n % 2 == 0]

print(evens_traditioanls)
print(evens)


users: list[dict[str, str]] = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "user"},
    {"name": "Maria", "role": "user"},
]

user_roles: dict[str, str] = {
    user["name"]: user["role"]
    for user in users
}

print(user_roles)

permissions: list[str] = ["read", "write"]

print(any(p == "admin" for p in permissions))
print(all(p in ["read", "write"] for p in permissions))

for index, permission in enumerate(permissions):
    print(index, permission)