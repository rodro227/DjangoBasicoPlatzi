import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model): #Clase que hereda
    #atributos, el id por defecto lo crea django
    question_text = models.CharField(max_length=200)  #tipo especial de django que viene de models
    pub_date = models.DateTimeField("date published")  #tipos de datos equiparados a clases

    #metodo para que nos muestre el texto cada que se invoque un objeto tipo Question
    def __str__(self):
        return self.question_text
    
    #falso si la diferencia es menor que un día
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)   
    #cada registro se corresponda con Questions
    #con cascade se elimina la respuesta
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text