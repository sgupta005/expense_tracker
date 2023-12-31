from django.db import models
from django.contrib.auth.models import User
# Create your models here.


TYPE = (
    ('Postive', 'Postive'),
    ('Negavtive' , 'Negavtive')
    )

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    income = models.FloatField(default=0)
    expenses = models.FloatField(default=0)
    # balance = models.FloatField(blank=True , null=True)
    @property
    def balance(self):
        return self.income - self.expenses
    

class Expense(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    expense_type = models.CharField(max_length=100 , choices=TYPE)
    
    
    def __str__(self):
        return self.name
    