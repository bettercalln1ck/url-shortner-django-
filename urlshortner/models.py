from django.db import models
import random
import hashlib
import socket
import base64

hostname=socket.gethostname()
ipaddress=socket.gethostbyname(hostname)

id=100

# Create your models here.

"""def code_generator(size=6,chars='asfdgfdhfghdjbfd'):
    new_code=''
    for _ in range(size):
        new_code +=random.choice(chars)
    return new_code """

class shorturl(models.Model):
    url =models.CharField(max_length=500)
    shortenurl=models.CharField(max_length=50,unique=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        #d=self.timestamp
        #num=hashlib.md5(str(str(ipaddress)+str(d)).encode('utf-8'))
        self.shortenurl=create_shortcode(self.url)
        super(shorturl,self).save(*args,*kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        return "http://127.0.0.1:8000/{shortenurl}".format(shortenurl=self.shortenurl)  

def create_shortcode(instance):
    code=hashlib.md5(str(instance).encode('utf-8')).hexdigest()
    new_code=code[0:6]
    #klass=instance.__class__
    qs=shorturl.objects.filter(shortenurl=new_code).exists()
    if qs:
        code=base64.b64encode(str(instance))
        new_code=code[0:6]
        return new_code
    return new_code    

"""def base_encode(id):
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    base = len(characters)
    ret = [] 
    while id > 0:
        val = id % base
        ret.append(characters[val])
        id = id // base
    return "".join(ret[::-1])    """




    

