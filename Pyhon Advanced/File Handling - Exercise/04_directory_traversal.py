import os

# First decision with Recursive Function:
#
# def directory_traversal(path, files):
#     for el in os.listdir(path):
#         if os.path.isdir(os.path.join(path, el)):
#             directory_traversal(os.path.join(path, el), files)
#         else:
#             extension = el.split('.')[-1]
#             if extension not in files:
#                 files[extension] = []
#             files[extension].append(el)
#
#
# result = {}
# directory_traversal('./', result)
# sorted_result = sorted(result)
#
# with open('./report.txt', 'w') as file:
#     for key in sorted_result:
#         file.write(f'.{key}\n')
#         for element in sorted(result[key]):
#             file.write(f'- - - {element}\n')


# Second decision with Os.Walk Method:
result = {}

for _, _, files in os.walk('.'):
    for file in files:
        extension = file.split('.')[-1]
        if extension not in result:
            result[extension] = []
        result[extension].append(file)

sorted_result = sorted(result)

with open('./report.txt', 'w') as file:
    for key in sorted_result:
        file.write(f'.{key}\n')
        for element in sorted(result[key]):
            file.write(f'- - - {element}\n')
