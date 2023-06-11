from django.db import models


# Model fields == class attributes in Model classes


'''
PostgreSQL: varying char (30)
SQL Server: VARCHAR(30)

PostgeSQL: decimal
SQL Server: money
'''


class Employee(models.Model):
    # Var char (30) => strings with max length 30
    first_name = models.CharField(
        max_length=30,
    )

    # Int => 0
    years_of_experience = models.PositiveIntegerField()

    # text => stings with unlimited length
    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField()

    # This will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    # This will be automatically set on each `save`/ `update`
    updated_on = models.DateTimeField(
        auto_now=True,
    )


# Employee.objects.raw('SELECT *')  # raw SQL
# Employee.objects.all()            # Select
# Employee.objects.create()         # Insert
# Employee.objects.filter()         # Select + Where
# Employee.objects.update()         # Update

'''
Django ORM (Object-relation mapping
'''
