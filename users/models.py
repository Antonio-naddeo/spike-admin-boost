from django.db import models

class Account(models.Model):
    state_choices = (
        ('MG', 'Minas Gerais'),
        ('SP', 'São Paulo'),
        ('RJ', 'Rio de Janeiro'),
        ('BA', 'Bahia'),
        ('DF', 'Distrito Federal'),
    )

    name = models.CharField(max_length=150)
    bio= models.TextField()
    birth = models.DateField()
    cpf = models.CharField(max_length=20)
    interests = models.CharField(max_length=150)
    state = models.CharField(choices=state_choices, max_length=2)

    
