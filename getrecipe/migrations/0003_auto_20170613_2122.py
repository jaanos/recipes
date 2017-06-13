# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-06-13 21:22
from __future__ import unicode_literals

from django.db import migrations
import csv


class Migration(migrations.Migration):

    def populate_db(apps, schema_editor):
        Sestavina = apps.get_model('getrecipe', 'Sestavina')
        Mera = apps.get_model('getrecipe', 'Mera')
        Priprava = apps.get_model('getrecipe', 'Priprava')
        Recept = apps.get_model('getrecipe', 'Recept')

        with open('razne_mere.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    m, c = Mera.objects.get_or_create(ime = row[0])
                    #nova_mera = Mera(ime = row[0])
                    #nova_mera.save()
                
        with open('razne_sestavine.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    s,c = Sestavina.objects.get_or_create(ime=row[0])
                    #nova_sestavina = Sestavina(ime = row[0])
                    #nova_sestavina.save()
            
        with open('glavni_recepti.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 5:
                    ime, tezavnost, cas, url_slike, url_recepta, postopek = row
                    r, c = Recept.objects.get_or_create(ime = ime, zahtevnost = int(tezavnost),
                                                           cas_priprave = int(cas), povezava_do_slike_jedi = url_slike,
                                                           povezava = url_recepta, postopek = postopek, ocena = 0)

        with open('recepti-sestavine.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    ime, sest, kol, m = row
                    recept = Recept.objects.get(ime = ime)
                    sestavina = Sestavina.objects.get(ime = sest)
                    mera = Mera.objects.get(ime = m)
                    if kol == '':
                        kol = 1
                    else:
                        kol = float(kol)
                    p, c = Priprava.objects.get_or_create(recept=recept, mera=mera, sestavina=sestavina, kolicina=float(kol))

    dependencies = [
        ('getrecipe', '0002_auto_20170612_2142'),
    ]

    operations = [
        migrations.RunPython(populate_db)
    ]