def helper(work):
    work_in_memory = work

    def helper(work):
        return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"

    return helper


help1 = helper("homework")
print(help1("cleaning"))
print(help1("driving"))