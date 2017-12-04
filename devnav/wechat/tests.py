# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.

from django.test import TestCase
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

#python manage.py test：执行所有的测试用例
#python manage.py test app_name, 执行该app的所有测试用例
#python manage.py test app_name.case_name: 执行指定的测试用例

