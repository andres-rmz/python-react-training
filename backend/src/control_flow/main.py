def evaluate_age(age: int) -> str:
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"
    
print(evaluate_age(12))
print(evaluate_age(36))
print(evaluate_age(70))

users: list[dict[str, str]] = [
    {"name": "Ana", "role": "admin"},
    {"name": "Luis", "role": "user"},
    {"name": "Maria", "role": "user"},
]

def get_admin_user(users: list[dict[str, str]]) -> list[str]:
    admins: list[str] = []

    for user in users:
        if user["role"] == "admin":
            admins.append(user["name"])

    return admins

print(get_admin_user(users))

def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed")

print(divide(10, 0))