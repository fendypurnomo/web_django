from django.db import models

class Reporter(models.Model):
  full_name = models.CharField(max_length=70)

  def __str__(self):
    return self.full_name

class Article(models.Model):
  headline = models.CharField(max_length=200)
  pub_date = models.DateField()
  content = models.TextField()
  reporter = models.ForeignKey(
    Reporter,
    related_name='reporter',
    on_delete=models.CASCADE,
    verbose_name='Reporter name'
  )

  def __str__(self):
    return self.headline
