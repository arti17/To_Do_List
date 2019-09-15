from django.db import models

status_choices = [('new', 'New'), ('in_progress', 'In progress'),  ('done', 'Done')]


class Task(models.Model):
    description = models.TextField(max_length=300, null=False, verbose_name='Описание')
    full_description = models.TextField(max_length=600, null=True)
    status = models.CharField(max_length=50, null=False, default='new', choices=status_choices, verbose_name='Статус')
    date = models.DateField(null=True, default=None, verbose_name='Дата')

    def __str__(self):
        return "{} | {}".format(self.description, self.status)
