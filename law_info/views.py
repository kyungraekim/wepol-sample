import json

from django.contrib.auth.decorators import login_required
from django.db import DataError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from law_info import models
from law_info.api import LawInfoRequest, xmltext_to_dict

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
    _insert_to_database(content, model)


def _insert_to_database(content, model):
    body = content[model.entry_key][model.body_key]
    if not isinstance(body, list):
        body = [body]
    key_map = model.json_map
    for line_no, content in enumerate(body):
        try:
            model.objects.get_or_create(**{k: content.get(v, None) for k, v in key_map.items()})
        except DataError as err:
            print('Insert failed at {}'.format(line_no))
            raise err
    return len(body)


@login_required
def render_upload_xml(request):
    if request.method == 'POST':
        json_dict = xmltext_to_dict(request.FILES['file'])
        model = models.get_model_by_key(json_dict)
        size = _insert_to_database(json_dict, model)
        return render(request, 'upload.html', {'uploaded_items': size})
    return render(request, 'upload.html')


@csrf_exempt
def upload_xml(request):
    if request.method == 'POST':
        json_dict = xmltext_to_dict(request.FILES['file'])
        model = models.get_model_by_key(json_dict)
        size = _insert_to_database(json_dict, model)
        return HttpResponse('Uploaded {} items'.format(size))
    return HttpResponse('Invalid')
