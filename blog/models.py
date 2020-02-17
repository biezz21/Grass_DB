from django.db import models

# Create your models here.
class grass_db(models.Model):
	class Meta:
		db_table = 'grass'
	id = models.AutoField(primary_key=True)

	Growth_type			= models.CharField(max_length=200 ,blank=True)
	Cultivar			= models.CharField(max_length=200 ,blank=True)
	Common_N			= models.CharField(max_length=200 ,blank=True)
	Scientific_N		= models.CharField(max_length=200 ,blank=True)
	Wiki				= models.CharField(max_length=200 ,blank=True)
	Genbank				= models.CharField(max_length=200 ,blank=True)
	image				= models.CharField(max_length=200 ,blank=True)
	link				= models.CharField(max_length=200, blank=True)