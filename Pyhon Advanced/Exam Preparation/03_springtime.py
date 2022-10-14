def start_spring(**kwargs):
    spring = {}

    for value, key in kwargs.items():

        if key not in spring:
            spring[key] = []
        spring[key].append(value)

    sorted_spring = sorted(spring.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for el in sorted_spring:
        result += f"{el[0]}:\n"
        for part in sorted(el[1]):
            result += f"-{part}\n"

    return result


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

