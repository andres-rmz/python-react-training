# Basic variables
age: int = 37
name: str = "Andrés"
height: float = 1.75
is_active: bool = True

print(age, name, height, is_active)

def calculate_year_of_birth(current_year: int, age: int) -> int:
    return current_year - age

year_of_birth = calculate_year_of_birth(2026, age)
print(f"Year of birth: {year_of_birth}")

skills: list[str] = ["Python", "C#", ".NET"]
skills.append("React")

for skill in skills:
    print(skill)

user: dict[str, str] = {
    "name": name,
    "role": "Software Engineer"
}

print(user["name"])