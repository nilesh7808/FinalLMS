from django.db import models

# Create your models here.
class Education(models.Model):
    #attributes of class Education
    course_name = models.CharField(max_length=150)
    img = models.ImageField(upload_to='pics')
    #description of course_name
    desc = models.TextField()

class CProgram(models.Model):
    #for upload files in media of c Programming
    pdfs = models.FileField(upload_to='PDFS')
    #for description of pdf file
    lines = models.CharField(max_length=50)

class JAVA(models.Model):
    #for upload files in media of java
    j_pdfs = models.FileField(upload_to='JPDFS')
    #for description of pdf file
    j_lines = models.CharField(max_length=50)

class Networking(models.Model):
    #for upload files in media of network
    net_pdfs = models.FileField(upload_to='NetPDFS')
    #for description of pdf file
    net_lines = models.CharField(max_length=50)

class DS(models.Model):
    #for upload files in media of ds
    ds_pdfs = models.FileField(upload_to='DSPDFS')
    #for description of pdf file
    ds_lines = models.CharField(max_length=50)

class CloudComputing(models.Model):
    #for upload files in media of CloudComputing
    cc_pdfs = models.FileField(upload_to='CCPDFS')
    #for description of pdf file
    cc_lines = models.CharField(max_length=50)

class OS(models.Model):
    #for upload files in media of OS
    os_pdfs = models.FileField(upload_to='OSPDFS')
    #for description of pdf file
    os_lines = models.CharField(max_length=50)

class Python(models.Model):
    #for upload files in media of python
    py_pdfs = models.FileField(upload_to='PYPDFS')
    #for description of pdf file
    py_lines = models.CharField(max_length=50)

class EthicalHack(models.Model):
    #for upload files in media of Ethical Hacking
    hack_pdfs = models.FileField(upload_to='EHPDFS')
    #for description of pdf file
    hack_lines = models.CharField(max_length=50)
