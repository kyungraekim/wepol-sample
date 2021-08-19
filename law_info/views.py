import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from law_info.api import LawInfoRequest, xmltext_to_dict
from law_info import models

sr = LawInfoRequest(
    key='hr45jWpc1dmMidXc5P3972DknBUxYAWElTbxlskPrRNqDD3ej5r6CW7ucKGAAI2LyH39Hkum3bE0A8HQQ9lAGQ%3D%3D',
    query='*',
    num_row=1,
    page_no=1)


# Create your views here.
def index(request):
    return HttpResponse("Good")

@login_required
def get_admin_info(request):
    xmltext = sr.get_admin_rule().text
    insert_to_database(xmltext, models.AdminRuleModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_law_info(request):
    xmltext = sr.get_law_info().text
    insert_to_database(xmltext, models.LawModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_ordin_info(request):
    xmltext = sr.get_ordin_info().text
    insert_to_database(xmltext, models.OrdinModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_expc_info(request):
    xmltext = sr.get_expc_info().text
    insert_to_database(xmltext, models.ExpcModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_detc_info(request):
    xmltext = sr.get_detc_info().text
    insert_to_database(xmltext, models.DetcModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_licbyl_info(request):
    xmltext = sr.get_licbyl_info().text
    insert_to_database(xmltext, models.LicbylModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_lstrm_info(request):
    xmltext = sr.get_lstrm_info().text
    insert_to_database(xmltext, models.LstrmModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_trty_info(request):
    xmltext = sr.get_trty_info().text
    insert_to_database(xmltext, models.TrtyModel)
    return HttpResponse(xmltext, content_type='text/xml')


@login_required
def get_all_info(request):
    xmls = []
    xmltext = sr.get_admin_rule().text
    insert_to_database(xmltext, models.AdminRuleModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_law_info().text
    insert_to_database(xmltext, models.LawModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_ordin_info().text
    insert_to_database(xmltext, models.OrdinModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_expc_info().text
    insert_to_database(xmltext, models.ExpcModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_detc_info().text
    insert_to_database(xmltext, models.DetcModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_licbyl_info().text
    insert_to_database(xmltext, models.LicbylModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_lstrm_info().text
    insert_to_database(xmltext, models.LstrmModel)
    xmls.append(xmltext_to_dict(xmltext))
    xmltext = sr.get_trty_info().text
    insert_to_database(xmltext, models.TrtyModel)
    xmls.append(xmltext_to_dict(xmltext))
    return HttpResponse(json.dumps(xmls, indent=2))


def insert_to_database(xmltext, model):
    content = xmltext_to_dict(xmltext)
    body = content[model.entry_key][model.body_key]

    key_map = model.json_map
    model.objects.get_or_create(**{k: body[v] for k, v in key_map.items()})
