from django.db import models

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    user = models.IntegerField(null=True)
    post = models.IntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    image =  models.URLField(blank=True)
    
    def datepublished(self): return self.date.strftime('%d %b %Y' )