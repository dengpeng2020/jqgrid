from django.db import models

# Create your models here.
class StuMsg(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bir = models.DateTimeField(blank=True, null=True)
    class_id = models.ForeignKey(to="StuClass", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "t_stu"

    def __str__(self):
        return self.name


class StuClass(models.Model):
    class_name = models.CharField(max_length=40)