from django.db import models

class ShortURL(models.Model):
	short = models.CharField(max_length=16, primary_key=True)
	target = models.URLField()

	def __str__(self):
		return "{} -> {}".format(self.short, self.target)


# class Image(models.Model):
# 	fingerprint = models.TextField()
# 	image = models.ImageField(upload_to='gallery/')