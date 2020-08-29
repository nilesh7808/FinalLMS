from django.contrib import admin
from .models import Education, CProgram, JAVA, Networking, CloudComputing, DS, OS, Python, EthicalHack
# Register your models here.

admin.site.register(Education)
admin.site.register(CProgram)
admin.site.register(JAVA)
admin.site.register(Networking)
admin.site.register(DS)
admin.site.register(CloudComputing)
admin.site.register(OS)
admin.site.register(Python)
admin.site.register(EthicalHack)
