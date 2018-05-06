from django.db import models

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bcover_img = models.CharField(max_length=200)
    bauthor = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    def __str__(self):
        return "%d" % self.pk



