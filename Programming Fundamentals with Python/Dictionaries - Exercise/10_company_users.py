companies_dictionary = {}

while True:
    command = input()

    if command == "End":
        break

    company_name = command.split(" -> ")[0]
    employees_id = command.split(" -> ")[1]

    if company_name not in companies_dictionary:
        companies_dictionary[company_name] = []

    if employees_id not in companies_dictionary[company_name]:
        companies_dictionary[company_name].append(employees_id)

for company in companies_dictionary:
    print(company)
    [print(f"-- {id}") for id in companies_dictionary[company]]
