from django.urls import path

from law_info import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin-rule', views.get_admin_info, name='admin_rule'),
    path('law', views.get_law_info, name='law'),
    path('ordin', views.get_ordin_info, name='ordin'),
    path('expc', views.get_expc_info, name='expc'),
    path('detc', views.get_detc_info, name='detc'),
    path('lstrm', views.get_lstrm_info, name='lstrm'),
    path('licbyl', views.get_licbyl_info, name='licbyl'),
    path('trty', views.get_trty_info, name='trty'),
    path('all', views.get_all_info, name='all'),
    path('upload-page', views.render_upload_xml, name='upload_page'),
    path('upload', views.upload_xml, name='upload')
]
