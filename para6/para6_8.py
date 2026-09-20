class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be build!"


def check_material(amount_of_material, limit_value):
    if "13" in str(amount_of_material):
        print(f"This number: {amount_of_material} in ban!")
        raise BuildingError(amount_of_material)
    if amount_of_material > limit_value:
        return "emough material"
    else:
        raise BuildingError(amount_of_material)



material = 1300
check_material(material, 300)
