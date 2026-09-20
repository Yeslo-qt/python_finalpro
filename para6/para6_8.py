class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be build!"


def check_material(amount_of_material, limit_value):
    if amount_of_material > limit_value:
        return "emough material"
    else:
        raise BuildingError(amount_of_material)


material = 1200
check_material(material, 300)
