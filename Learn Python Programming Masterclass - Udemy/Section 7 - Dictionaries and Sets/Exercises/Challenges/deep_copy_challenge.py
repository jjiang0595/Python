from contents import recipes


def my_deepcopy(d: dict) -> dict:
    d1 = {}
    for key, value in d.items():
        list_copy = value.copy()
        d1[key] = list_copy
    return d1


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
