from django.contrib import admin
from produtor.models import Produtor
from coletor.models import Coletor
from coleta.models import Oferta


admin.site.register(Produtor)
admin.site.register(Coletor)
admin.site.register(Oferta)
