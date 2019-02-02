# -*- coding: utf-8 -*-
__author__ = 'bobby'

# 独立使用django的model
import sys
import os

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + "../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mxshop.settings")

import django

django.setup()

from goods.models import GoodsCategory

from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    dict_lv1 = dict(code=lev1_cat["code"], name=lev1_cat["name"], category_type=1)
    ins_lv1 = GoodsCategory.objects.create(**dict_lv1)

    for lev2_cat in lev1_cat["sub_categorys"]:
        dict_lv2 = dict(code=lev2_cat["code"], name=lev2_cat["name"], category_type=2, parent_category=ins_lv1)
        ins_lv2 = GoodsCategory.objects.create(**dict_lv2)

        for lev3_cat in lev2_cat["sub_categorys"]:
            dict_lv3 = dict(code=lev3_cat["code"], name=lev3_cat["name"], category_type=3, parent_category=ins_lv2)
            ins_lv3 = GoodsCategory.objects.create(**dict_lv3)
