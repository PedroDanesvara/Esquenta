from django.contrib import admin
from produtor.models import Pessoa
from coletor.models import Coletor
from coleta.models import Oferta


admin.site.register(Pessoa)
admin.site.register(Coletor)
admin.site.register(Oferta)
