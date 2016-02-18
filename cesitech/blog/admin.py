from django.contrib import admin
from blog.models import *
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date')
    list_filter    = ('auteur',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('titre', 'contenu')
    def apercu_contenu(self, new):
        new = new.contenu[0:40]
        if len(new.contenu) > 40:
            return new+"..."
        else:
            return new
    apercu_contenu.short_description = 'Apercu du contenu'

class ContactAdmin(admin.ModelAdmin):
    list_display   = ('sujet', 'message', 'envoyeur')
    list_filter    = ('envoyeur',)
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('sujet', 'message')
    def apercu_contenu(self, new):
        new = new.contenu[0:40]
        if len(new.contenu) > 40:
            return new+"..."
        else:
            return new
    apercu_contenu.short_description = 'Apercu du contenu'

admin.site.register(Membre)
admin.site.register(New, NewAdmin)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Calendar)
