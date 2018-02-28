from django.db import models


class Documents(models.Model):
    id = models.BigIntegerField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'documents'


class Lemma(models.Model):
    id = models.BigAutoField(primary_key=True)
    doc_id = models.BigIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    amount = models.BigIntegerField(blank=True, null=True)
    tf_idf = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'lemma'
