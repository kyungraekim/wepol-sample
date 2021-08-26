from django.db import models


class AdminRuleModel(models.Model):
    """
    "행정규칙일련번호": "2100000198576", 20
    "행정규칙명": "112종합상황실 운영 및 신고처리 규칙", 200
    "행정규칙종류": "예규", 10
    "발령일자": "20210122", 200
    "발령번호": "582", 20
    "소관부처명": "경찰청", 50
    "현행연혁구분": "현행", 20
    "제개정구분코드": "200409", 10
    "제개정구분명": "타법개정", 20
    "행정규칙ID": "36654", 20
    "행정규칙상세링크": "/DRF/lawService.do?OC=sapphire_5&target=admrul&ID=2100000198576&type=HTML&mobileYn=", 500
    "시행일자": "20210122", 20
    "생성일자": "20210319", 20
    """
    admin_rule_id = models.AutoField(primary_key=True)
    admin_rule_identification = models.CharField(max_length=20, null=True)
    admin_rule_serial = models.CharField(max_length=20, null=True)
    admin_rule_name = models.CharField(max_length=200, null=True)
    admin_rule_type = models.CharField(max_length=10, null=True)
    issue_date = models.CharField(max_length=20, null=True)
    issue_number = models.CharField(max_length=20, null=True)
    competent_department_name = models.CharField(max_length=50, null=True)
    history_class = models.CharField(max_length=20, null=True)
    revision_class_code = models.CharField(max_length=10, null=True)
    revision_class_name = models.CharField(max_length=20, null=True)
    admin_rule_detail_link = models.CharField(max_length=500, null=True)
    effective_date = models.CharField(max_length=20, null=True)
    creation_date = models.CharField(max_length=20, null=True)

    entry_key = 'AdmRulSearch'
    body_key = 'admrul'
    json_map = {
        "admin_rule_identification": "행정규칙ID",
        "admin_rule_serial": "행정규칙일련번호",
        "admin_rule_name": "행정규칙명",
        "admin_rule_type": "행정규칙종류",
        "issue_date": "발령일자",
        "issue_number": "발령번호",
        "competent_department_name": "소관부처명",
        "history_class": "현행연혁구분",
        "revision_class_code": "제개정구분코드",
        "revision_class_name": "제개정구분명",
        "admin_rule_detail_link": "행정규칙상세링크",
        "effective_date": "시행일자",
        "creation_date": "생성일자",
    }

    class Meta:
        db_table = 'admin_rules'


class LawModel(models.Model):
    """
    "법령일련번호": "232157", 20
    "현행연혁코드": "현행", 20
    "법령명한글": "10ㆍ27법난 피해자의 명예회복 등에 관한 법률", 200
    "법령약칭명": "10ㆍ27법난법", 200
    "법령ID": "010719", 20
    "공포일자": "20210518", 20
    "공포번호": "18146", 20
    "제개정구분명": "일부개정", 20
    "소관부처코드": "1371000", 20
    "소관부처명": "문화체육관광부", 20
    "법령구분명": "법률", 20
    "시행일자": "20210518", 20
    "자법타법여부": null, 20
    "법령상세링크": "/DRF/lawService.do?OC=sapphire_5&target=law&MST=232157&type=HTML&mobileYn=&efYd=20210518", 500
    """
    law_id = models.AutoField(primary_key=True)
    law_identification = models.CharField(max_length=20, null=True)
    law_serial = models.CharField(max_length=20, null=True)
    current_history_code = models.CharField(max_length=20, null=True)
    law_korean_name = models.CharField(max_length=200, null=True)
    law_short_name = models.CharField(max_length=200, null=True)
    announcement_date = models.CharField(max_length=20, null=True)
    announcement_number = models.CharField(max_length=20, null=True)
    revision_class_name = models.CharField(max_length=20, null=True)
    competent_department_code = models.CharField(max_length=20, null=True)
    competent_department_name = models.CharField(max_length=20, null=True)
    law_class_name = models.CharField(max_length=20, null=True)
    effective_date = models.CharField(max_length=20, null=True)
    is_other_law = models.CharField(max_length=20, null=True)
    law_detail_link = models.CharField(max_length=500, null=True)

    entry_key = "LawSearch"
    body_key = "law"
    json_map = {
        "law_serial": "법령일련번호",
        "current_history_code": "현행연혁코드",
        "law_korean_name": "법령명한글",
        "law_short_name": "법령약칭명",
        "law_identification": "법령ID",
        "announcement_date": "공포일자",
        "announcement_number": "공포번호",
        "revision_class_name": "제개정구분명",
        "competent_department_code": "소관부처코드",
        "competent_department_name": "소관부처명",
        "law_class_name": "법령구분명",
        "effective_date": "시행일자",
        "is_other_law": "자법타법여부",
        "law_detail_link": "법령상세링크",
    }

    class Meta:
        db_table = 'laws'


class OrdinModel(models.Model):
    """
    "자치법규일련번호": "1013533", 20
    "자치법규명": "2018성공개최평창군위원회 설립 및 지원 조례", 500
    "자치법규ID": "2018824", 20
    "공포일자": "20150102", 20
    "공포번호": "2120", 10
    "제개정구분명": "일부개정", 10
    "지자체기관명": "강원도 평창군", 20
    "자치법규종류": "조례", 10
    "시행일자": "20150102", 20
    "자치법규상세링크": "/DRF/lawService.do?OC=sapphire_5&target=ordin&MST=1013533&type=HTML&mobileYn=", 500
    "자치법규분야명": null, 10
    "참조데이터구분": "0", 1
    """
    ordin_id = models.AutoField(primary_key=True)
    ordin_identification = models.CharField(max_length=20, null=True)
    ordin_serial = models.CharField(max_length=20, null=True)
    ordin_name = models.CharField(max_length=500, null=True)
    announcement_date = models.CharField(max_length=20, null=True)
    announcement_number = models.CharField(max_length=10, null=True)
    revision_class_name = models.CharField(max_length=10, null=True)
    local_gov_agency_name = models.CharField(max_length=20, null=True)
    ordin_type = models.CharField(max_length=10, null=True)
    effective_date = models.CharField(max_length=20, null=True)
    ordin_detail_link = models.CharField(max_length=500, null=True)
    ordin_field_name = models.CharField(max_length=10, null=True)
    reference_data_class = models.CharField(max_length=1, null=True)

    entry_key = "OrdinSearch"
    body_key = "law"
    json_map = {
        "ordin_identification": "자치법규ID",
        "ordin_serial": "자치법규일련번호",
        "ordin_name": "자치법규명",
        "announcement_date": "공포일자",
        "announcement_number": "공포번호",
        "revision_class_name": "제개정구분명",
        "local_gov_agency_name": "지자체기관명",
        "ordin_type": "자치법규종류",
        "effective_date": "시행일자",
        "ordin_detail_link": "자치법규상세링크",
        "ordin_field_name": "자치법규분야명",
        "reference_data_class": "참조데이터구분",
    }

    class Meta:
        db_table = 'ordins'


class ExpcModel(models.Model):
    """
    "법령해석례일련번호": "313107", 10
    "안건명": "1959년 12월 31일 이전에 퇴직한 군인의 퇴직급여금 지급에 관한특별법 시행령 제4조제2항 및 3항", 500
    "안건번호": "05-0096", 20
    "질의기관명": "국방부", 20 --> 30
    "질의기관코드": "1290000", 10
    "회신기관명": "법제처", 20
    "회신기관코드": "1170000", 10
    "회신일자": "2005.12.23", 20
    "해석례분야명": null, 20
    "법령해석례상세링크": "/DRF/lawService.do?OC=sapphire_5&target=expc&ID=313107&type=HTML&mobileYn=", 500
    """
    expc_id = models.AutoField(primary_key=True)
    expc_serial = models.CharField(max_length=10, null=True)
    agenda_name = models.CharField(max_length=500, null=True)
    agenda_number = models.CharField(max_length=20, null=True)
    inquiry_org_name = models.CharField(max_length=30, null=True)
    inquiry_org_code = models.CharField(max_length=10, null=True)
    reply_org_name = models.CharField(max_length=20, null=True)
    reply_org_code = models.CharField(max_length=10, null=True)
    reply_date = models.CharField(max_length=20, null=True)
    expc_class_name = models.CharField(max_length=20, null=True)
    expc_detail_link = models.CharField(max_length=500, null=True)

    entry_key = 'Expc'
    body_key = 'expc'
    json_map = {
        "expc_serial": "법령해석례일련번호",
        "agenda_name": "안건명",
        "agenda_number": "안건번호",
        "inquiry_org_name": "질의기관명",
        "inquiry_org_code": "질의기관코드",
        "reply_org_name": "회신기관명",
        "reply_org_code": "회신기관코드",
        "reply_date": "회신일자",
        "expc_class_name": "해석례분야명",
        "expc_detail_link": "법령해석례상세링크",
    }

    class Meta:
        db_table = 'expcs'


class DetcModel(models.Model):
    """
    "헌재결정례일련번호": "137495", 10
    "종국일자": "2008.05.29", 20
    "사건번호": "2005헌마1173", 20
    "사건명": "1959년 12월 31일 이전에 퇴직한 군인의 퇴직급여금 지급에 관한 특별법 제1조   위헌확인", 500
    "헌재결정례상세링크": "/DRF/lawService.do?OC=sapphire_5&target=detc&ID=137495&type=HTML&mobileYn=", 500
    """
    detc_id = models.AutoField(primary_key=True)
    detc_serial = models.CharField(max_length=10, null=True)
    end_date = models.CharField(max_length=20, null=True)
    case_number = models.CharField(max_length=20, null=True)
    case_name = models.CharField(max_length=500, null=True)
    detc_detail_link = models.CharField(max_length=500, null=True)

    entry_key = 'DetcSearch'
    body_key = 'Detc'
    json_map = {
        "detc_serial": "헌재결정례일련번호",
        "end_date": "종국일자",
        "case_number": "사건번호",
        "case_name": "사건명",
        "detc_detail_link": "헌재결정례상세링크",
    }

    class Meta:
        db_table = 'detc'


class LicbylModel(models.Model):
    """
    "별표일련번호": "7979211", 10
    "관련법령일련번호": "208317", 10
    "관련법령ID": "006082", 10
    "별표명": "(     ) 공무원 근무성적평정서", 500
    "관련법령명": "헌법재판소 공무원 평정 규칙", 500
    "별표번호": "000100", 10
    "별표종류": "서식", 20
    "소관부처명": "헌법재판소", 50
    "공포일자": "20190401", 10
    "공포번호": "00406", 10
    "제개정구분명": "일부개정", 20
    "법령종류": "헌법재판소규칙", 20
    "별표서식파일링크": "/LSW/flDownload.do?flSeq=41474251", 200
    "별표서식PDF파일링크": "/LSW/flDownload.do?flSeq=41474253", 200
    "별표법령상세링크": "/DRF/lawService.do?OC=sapphire_5&target=licbyl&ID=7979211&type=HTML&mobileYn=", 200
    """
    licbyl_id = models.AutoField(primary_key=True)
    licbyl_serial = models.CharField(max_length=10, null=True)
    related_law_serial = models.CharField(max_length=10, null=True)
    related_law_id = models.CharField(max_length=10, null=True)
    licbyl_name = models.CharField(max_length=500, null=True)
    related_law_name = models.CharField(max_length=500, null=True)
    licbyl_number = models.CharField(max_length=10, null=True)
    licbyl_type = models.CharField(max_length=20, null=True)
    competent_department_name = models.CharField(max_length=50, null=True)
    announcement_date = models.CharField(max_length=10, null=True)
    announcement_number = models.CharField(max_length=10, null=True)
    revision_class_name = models.CharField(max_length=20, null=True)
    law_type = models.CharField(max_length=20, null=True)
    licbyl_format_file_link = models.CharField(max_length=200, null=True)
    licbyl_format_pdf_link = models.CharField(max_length=200, null=True)
    licbyl_law_detail_link = models.CharField(max_length=200, null=True)

    entry_key = "licBylSearch"
    body_key = "licbyl"
    json_map = {
        "licbyl_serial": "별표일련번호",
        "related_law_serial": "관련법령일련번호",
        "related_law_id": "관련법령ID",
        "licbyl_name": "별표명",
        "related_law_name": "관련법령명",
        "licbyl_number": "별표번호",
        "licbyl_type": "별표종류",
        "competent_department_name": "소관부처명",
        "announcement_date": "공포일자",
        "announcement_number": "공포번호",
        "revision_class_name": "제개정구분명",
        "law_type": "법령종류",
        "licbyl_format_file_link": "별표서식파일링크",
        "licbyl_format_pdf_link": "별표서식PDF파일링크",
        "licbyl_law_detail_link": "별표법령상세링크",
    }

    class Meta:
        db_table = 'licbyls'


class LstrmModel(models.Model):
    """
    "법령용어ID": "3945293", 10
    "법령용어명": "(InstrumentMeterologicalCondition;IMC)", 200
    "법령용어상세검색": "/LSW/lsTrmInfoR.do?trmSeqs=3945293&mobile=", 500
    "법령용어상세링크": "/DRF/lawService.do?OC=sapphire_5&target=lstrm&trmSeqs=3945293&mobile=&type=XML", undefined
    "사전구분코드": "011402", 10
    "법령종류코드": "010102", undefined
    """
    lstrm_id = models.AutoField(primary_key=True)
    lstrm_identification = models.CharField(max_length=20, null=True)
    lstrm_name = models.CharField(max_length=200, null=True)
    lstrm_detail_search = models.CharField(max_length=500, null=True)
    lstrm_detail_link = models.CharField(max_length=500, null=True)
    dict_class_code = models.CharField(max_length=10, null=True)
    law_type_code = models.CharField(max_length=10, null=True)

    entry_key = "LsTrmSearch"
    body_key = "lstrm"
    json_map = {
        "lstrm_identification": "법령용어ID",
        "lstrm_name": "법령용어명",
        "lstrm_detail_search": "법령용어상세검색",
        "lstrm_detail_link": "법령용어상세링크",
        "dict_class_code": "사전구분코드",
        "law_type_code": "법령종류코드",
    }

    class Meta:
        db_table = 'lstrms'


class TrtyModel(models.Model):
    """
    "조약일련번호": "2308", 10
    "조약명": "11.7-12.2GHz(제2 및 제3지역) 및 11.7-12.5GHz(제1지역) 주파수대에서의 방송위성 업무의 계획수립을 위한 세계무선통신 주관청회의 최종의정서", 500
    "조약구분코드": "440102", 10
    "조약구분명": "다자조약", 20
    "발효일자": "19790101", 20
    "서명일자": null, 20
    "관보게제일자": "19781229", 20
    "조약번호": "666", 20
    "국가번호": null, 10
    "조약상세링크": "/DRF/lawService.do?OC=sapphire_5&target=trty&ID=2308&type=HTML&mobileYn=", 500
    """
    trty_id = models.AutoField(primary_key=True)
    trty_serial = models.CharField(max_length=10, null=True)
    trty_name = models.CharField(max_length=500, null=True)
    trty_class_code = models.CharField(max_length=10, null=True)
    trty_class_name = models.CharField(max_length=20, null=True)
    effective_date = models.CharField(max_length=20, null=True)
    signature_date = models.CharField(max_length=20, null=True)
    gazette_publication_date = models.CharField(max_length=20, null=True)
    trty_number = models.CharField(max_length=20, null=True)
    country_number = models.CharField(max_length=10, null=True)
    trty_detail_link = models.CharField(max_length=500, null=True)

    entry_key = "TrtySearch"
    body_key = "Trty"
    json_map = {
        "trty_serial": "조약일련번호",
        "trty_name": "조약명",
        "trty_class_code": "조약구분코드",
        "trty_class_name": "조약구분명",
        "effective_date": "발효일자",
        "signature_date": "서명일자",
        "gazette_publication_date": "관보게제일자",
        "trty_number": "조약번호",
        "country_number": "국가번호",
        "trty_detail_link": "조약상세링크",
    }

    class Meta:
        db_table = 'trtys'


__ENTRY_TO_MODEL = {
    model.entry_key: model for model in [
        AdminRuleModel, LawModel, DetcModel, ExpcModel,
        OrdinModel, LstrmModel, TrtyModel, LicbylModel,
    ]
}


def get_model_by_key(json_dict):
    entry_key = list(json_dict.keys())[0]
    result = __ENTRY_TO_MODEL.get(entry_key, None)
    if result is None:
        raise AttributeError("Invalid key; Not any of {}".format(list(__ENTRY_TO_MODEL.keys())))
    return result
