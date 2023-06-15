from enum import Enum

from django.db import models

# Model fields == class attributes in Model classes


'''
PostgreSQL: varying char (30)
SQL Server: VARCHAR(30)

PostgeSQL: decimal
SQL Server: money
'''


# class EmployeeLevel(Enum):
#     JUNIOR = 'Junior',
#     REGULAR = 'Regular',
#     SENIOR = 'Senior'


class AuditIfoMixin(models.Model):
    class Meta:
        # 1. No table will be created in the DB
        # 2. Can be inherited in other models
        abstract = True

    # This will be automatically set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    # This will be automatically set on each `save`/ `update`
    updated_on = models.DateTimeField(
        auto_now=True,
    )


# class DeletableMixin(models.Model):
#     is_deleted = models.BooleanField(default=False)


class Department(AuditIfoMixin, models.Model):
    name = models.CharField(
        max_length=15,
    )

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.name}'


class Project(AuditIfoMixin, models.Model):
    name = models.CharField(
        max_length=30,
    )
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()


class Employee(AuditIfoMixin, models.Model):
    class Meta:
        ordering = ('years_of_experience', 'age',)

    LEVEL_JUNIOR = 'Junior'
    LEVEL_REGULAR = 'Regular'
    LEVEL_SENIOR = 'Senior'

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    # Var char (30) => strings with max length 30
    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=50,
        null=True,
    )

    level = models.CharField(
        max_length=len(LEVEL_REGULAR),
        choices=LEVELS,
        verbose_name='Seniority level'
    )

    age = models.IntegerField(
        default=-7,
    )

    # Int => 0
    years_of_experience = models.PositiveIntegerField()

    # text => stings with unlimited length
    review = models.TextField()

    start_date = models.DateField()

    email = models.EmailField(
        # Adds `UNIQUE` constraint
        unique=True,
        # editable=False,
    )

    is_full_time = models.BooleanField(
        null=True,
    )

    # One-to-many
    department = models.ForeignKey(
        Department,
        on_delete=models.RESTRICT,
    )

    # Many-to-many
    projects = models.ManyToManyField(
        Project,
        related_name='employees',
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'Id: {self.pk}; Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=15,
    )

    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

# Employee.objects.raw('SELECT *')  # raw SQL
# Employee.objects.all()            # Select
# Employee.objects.create()         # Insert
# Employee.objects.filter()         # Select + Where
# Employee.objects.update()         # Update


'''
Django ORM (Object-relation mapping)
'''


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(
        Employee,
        on_delete=models.RESTRICT
    )
    project_id = models.ForeignKey(
        Project,
        on_delete=models.RESTRICT
    )

    date_joined = models.DateField(
        auto_now_add=True,
    )
    # Additional info


class NullBlankDemo(models.Model):
    # blank = models.IntegerField(
    #     blank=True,
    #     null=False,
    # )
    # null = models.IntegerField(
    #     blank=False,
    #     null=True,
    # )
    blank_null = models.IntegerField(
        blank=True,  # Form validation
        null=True,
    )
    default = models.IntegerField()
    # --- SAME ---
    # default = models.IntegerField(
    #     blank=False,
    #     null=False,
    # )
