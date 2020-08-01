from django.db import models

# Create your models here.
class authors(models.Model):
    name=models.CharField(max_length=256)
    def __str__(s):
        return s.name
    class Meta:
        db_table = 'authors'

class topics(models.Model):
    topic=models.CharField(max_length=256)
    def __str__(s):
        return s.topic
    class Meta:
        db_table = 'topics'

class collections(models.Model):
    collection_name=models.CharField(max_length=256)
    def __str__(s):
        return s.collection_name
    class Meta:
        db_table = 'collections'

class quotes(models.Model):
    quote=models.CharField(max_length=256)
    author=models.ForeignKey(authors,on_delete=models.CASCADE)
    topic=models.ForeignKey(topics,on_delete=models.CASCADE)
    collection=models.ForeignKey(collections,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'quotes'
    




