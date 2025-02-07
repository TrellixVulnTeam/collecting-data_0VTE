import os
import unittest
from MicceduParser import *
from utils import *

class MicceduParserTests(unittest.TestCase):
    def setUp(self):
        self.parser = MicceduParser()

    def test_get_archive_links_should_return_7_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2015/']
        # act
        results = self.parser.get_archives_links()
        # assert
        self.assertEqual(len(results), 7)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_district_links_for_2019_should_return_8_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=1',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=2',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=4',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=3',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=25',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=5',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=6',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=1&id=7'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # act
        results = self.parser.extract_district_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 8)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2019_should_return_85_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10501',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10706'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2018_should_return_85_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=10603',
                 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=10204',
                 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11105'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2017_should_return_85_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=10701',
                 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=10711',
                 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=10101'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2016_should_return_85_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10503',
                 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10706',
                 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10908'
                 ]
        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)
        for link in links:
            self.assertTrue(link in results)

    def test_extract_areas_links_for_2015_should_return_85_links(self):
        # arrange

        district_and_area_links = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2015/')
        # act
        results = self.parser.extract_area_links(district_and_area_links)

        # assert
        self.assertEqual(len(results), 85)

    def test_get_district_and_area_links_for_2019_should_return_93_links(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10501',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903',
                 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10706'
                 ]
        # act
        results = self.parser.get_district_and_area_links(
            'http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo')
        # assert
        self.assertEqual(len(results), 93)
        for link in links:
            self.assertTrue(link in results)

    def test_get_archive_year(self):
        # arrange
        links = ['http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo',
                 'http://indicators.miccedu.ru/monitoring/2015/']

        years = ['2019',
                 '2018',
                 '2017',
                 '2016',
                 '2015']

        # act
        results = [self.parser.get_archive_year(link) for link in links]

        # assert
        for year in years:
            self.assertTrue(year in results)

    def test_get_institutes_with_data_for_2019_should_return_3_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10403'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 3)
        self.assertEqual(len(results[0]), 10)
        self.assertEqual(results[0][3], '')
        self.assertEqual(results[1][2], '4018,7')
        self.assertEqual(results[2][8], '77,4')

    def test_get_institutes_with_data_for_2019_should_return_23_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10903'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 23)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0],
                         'федеральное государственное бюджетное образовательное учреждение высшего образования «Новосибирский государственный медицинский университет» Министерства здравоохранения Российской Федерации')
        self.assertEqual(results[22][5], '9')
        self.assertEqual(results[21][5], '3711,65')

    def test_get_institutes_with_data_for_2018_should_return_16_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11107'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 16)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0],
                         'Филиал АНО ВО "Московский институт государственного управления и права" в Республике Саха (Якутия)')
        self.assertEqual(results[0][5], '201')

    def test_get_institutes_with_data_for_2018_should_return_16_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11107'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 16)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[10][0],
                         'Филиал АНО ВО "Московский институт государственного управления и права" в Республике Саха (Якутия)')
        self.assertEqual(results[0][5], '201')

    def test_get_institutes_with_data_for_2018_should_return_29_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=10806'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 29)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[5][0],
                         'федеральное государственное бюджетное образовательное учреждение высшего образования «Башкирский государственный медицинский университет» Министерства здравоохранения Российской Федерации')
        self.assertEqual(results[11][4], '1')

    def test_get_institutes_with_data_for_2018_should_return_1_row_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11108'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 1)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[0][0],
                         'Чукотский филиал федерального государственного автономного образовательного учреждения высшего профессионального образования "Северо-Восточный федеральный университет имени М.К. Аммосова"')
        self.assertEqual(results[0][2], '91,2')

    def test_get_institutes_with_data_for_2017_should_return_4_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=11106'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 4)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[2][0],
                         'Сахалинский институт железнодорожного транспорта - филиала федерального государственного бюджетного образовательного учреждения высшего образования "Дальневосточный государственный университет путей сообщения" в г. Южно-Сахалинске')
        self.assertEqual(results[2][2], '118,6')

    def test_get_institutes_with_data_for_2017_should_return_9_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=10402'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 9)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[8][0],
                         'Кировский филиал федерального государственного бюджетного образовательного учреждения высшего образования «Российская академия народного хозяйства и государственной службы при Президенте Российской Федерации»')
        self.assertEqual(results[8][2], '10,25')

    def test_get_institutes_with_data_for_2016_should_return_12_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10402'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 12)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[11][0],
                         'Филиал федерального государственного бюджетного образовательного учреждения высшего образования "Вятский государственный университет" в г. Вятские Поляны')
        self.assertEqual(results[11][5], '21,1')

    def test_get_institutes_with_data_for_2016_should_return_8_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10801'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 8)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[6][0], 'Курганский филиал РАНХиГС')
        self.assertEqual(results[7][2], '3,5')

    def test_get_institutes_with_data_for_2015_should_return_12_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2015/material.php?type=2&id=11004'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 12)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[11][0],
                         'филиал федерального государственного бюджетного образовательного учреждения высшего профессионального образования "Российский государственный гуманитарный университет" в г. Улан-Удэ Республики Бурятия')
        self.assertEqual(results[0][5], '119')

    def test_get_institutes_with_data_for_2015_should_return_17_rows_10_columns(self):
        # arrange
        test_link = 'http://indicators.miccedu.ru/monitoring/2015/material.php?type=2&id=10202'
        # action
        results = self.parser.get_institutes_with_data(test_link)
        # assert
        self.assertEqual(len(results), 17)
        self.assertEqual(len(results[0]), 10)

        self.assertEqual(results[0][0], 'Государственный институт экономики, финансов, права и технологий')
        self.assertEqual(results[0][5], '1239,4')

    def test_get_institute_links_2019_should_return_3_institutes_1(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=124',
                      'http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=123']
        area_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10403'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 3)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2019_should_return_3_institutes_2(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=10000374',
                      'http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=1']
        area_link = 'http://indicators.miccedu.ru/monitoring/2019/_vpo/material.php?type=2&id=10711'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 3)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2018_should_return_0_institutes(self):
        # arrange
        test_links = []
        area_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=10106'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 0)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2018_should_return_3_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2018/_vpo/inst.php?id=322',
                      'http://indicators.miccedu.ru/monitoring/2018/_vpo/inst.php?id=10001068',
                      'http://indicators.miccedu.ru/monitoring/2018/_vpo/inst.php?id=10003240']
        area_link = 'http://indicators.miccedu.ru/monitoring/2018/_vpo/material.php?type=2&id=11006'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 3)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2017_should_return_7_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=110281',
                      'http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=10000912',
                      'http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=10001285']
        area_link = 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=10104'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 7)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2017_should_return_11_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=12013106',
                      'http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=1737']
        area_link = 'http://indicators.miccedu.ru/monitoring/2017/_vpo/material.php?type=2&id=11004'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 11)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    # !!!!!!!!!!!!!!!!!!!! 2
    def test_get_institute_links_2016_should_return_8_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=10000715',
                      'http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=10007048']
        area_link = 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=10204'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 8)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2016_should_return_5_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=10006893',
                      'http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=1979']
        area_link = 'http://indicators.miccedu.ru/monitoring/2016/_vpo/material.php?type=2&id=11106'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 5)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_institute_links_2015_should_return_7_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2015/inst.php?id=12013090',
                      'http://indicators.miccedu.ru/monitoring/2015/inst.php?id=113427']
        area_link = 'http://indicators.miccedu.ru/monitoring/2015/material.php?type=2&id=11302'
        soup = BeautifulSoup(get_page_html(area_link))
        # act

        result = self.parser.get_institute_links(soup,area_link)
        # assert
        self.assertEqual(len(result), 7)
        for test_link in test_links:
            self.assertTrue(test_link in result)

        # !!!!!!!!!!!!

    def test_get_institute_links_2015_should_return_9_institutes(self):
        # arrange
        test_links = ['http://indicators.miccedu.ru/monitoring/2015/inst.php?id=10006813',
                      'http://indicators.miccedu.ru/monitoring/2015/inst.php?id=12007014']
        area_link = 'http://indicators.miccedu.ru/monitoring/2015/material.php?type=2&id=10103'
        soup = BeautifulSoup(get_page_html(area_link))
        # act
        result = self.parser.get_institute_links(soup, area_link)
        # assert
        self.assertEqual(len(result), 9)
        for test_link in test_links:
            self.assertTrue(test_link in result)

    def test_get_general_institute_indicators_and_values_2019_should_return_6_rows_2_columns(self):
        #arrange
        indicators_and_values = [
            ["Дополнительный показатель", "75,99"],
            ["Заработная плата ППС", "192,9"],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=1585"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_general_institute_indicators_and_values(soup)

        #assert
        self.assertEqual(len(result), 6)
        self.assertEqual(len(result[0]), 2)
        for indicator_and_value in indicators_and_values:
            self.assertTrue(indicator_and_value in result)

    def test_get_general_institute_indicators_and_values_2018_should_return_7_rows_2_columns(self):
        #arrange
        indicators_and_values = [
            ["Финансово-экономическая деятельность", "1959,38"],
            ["Трудоустройство", "50*"],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2018/_vpo/inst.php?id=10000374"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_general_institute_indicators_and_values(soup)

        #assert
        self.assertEqual(len(result), 7)
        self.assertEqual(len(result[0]), 2)
        for indicator_and_value in indicators_and_values:
            self.assertTrue(indicator_and_value in result)

    #!!!!
    def test_get_general_institute_indicators_and_values_2017_should_return_7_rows_2_columns(self):
        #arrange
        indicators_and_values = [
            ["Образовательная деятельность", "53,69"],
            ["Трудоустройство", "70*"],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=1847"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_general_institute_indicators_and_values(soup)

        #assert
        self.assertEqual(len(result), 7)
        self.assertEqual(len(result[0]), 2)
        for indicator_and_value in indicators_and_values:
            self.assertTrue(indicator_and_value in result)


    def test_get_general_institute_indicators_and_values_2016_should_return_6_rows_2_columns(self):
        #arrange
        indicators_and_values = [
            ["Международная деятельность", "12,04"],
            ["Образовательная деятельность", "58,98"],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=1599"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_general_institute_indicators_and_values(soup)

        #assert
        self.assertEqual(len(result), 7)
        self.assertEqual(len(result[0]), 2)
        for indicator_and_value in indicators_and_values:
            self.assertTrue(indicator_and_value in result)

    def test_get_general_institute_indicators_and_values_2015_should_return_7_rows_2_columns(self):
        #arrange
        indicators_and_values = [
            ["Финансово-экономическая деятельность", "2153,59"],
            ["Образовательная деятельность", "70,92"],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2015/inst.php?id=1656"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_general_institute_indicators_and_values(soup)

        #assert
        self.assertEqual(7, len(result))
        self.assertEqual(2, len(result[0]))

    def test_get_institute_indicators_and_values_2017_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=10001068"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(62, len(result))
        self.assertEqual(2, len(result[0]))


    def test_get_institute_indicators_and_values_2019_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=10000172"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(61, len(result))
        self.assertEqual(2, len(result[0]))


    def test_get_institute_indicators_and_values_2018_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2018/_vpo/inst.php?id=1658"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(62, len(result))
        self.assertEqual(2, len(result[0]))


    def test_get_institute_indicators_and_values_2017_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2017/_vpo/inst.php?id=1832"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(62, len(result))
        self.assertEqual(2, len(result[0]))


    def test_get_institute_indicators_and_values_2016_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2016/_vpo/inst.php?id=1952"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(62, len(result))
        self.assertEqual(2, len(result[0]))



    def test_general_institute_indicators_and_values_2015_should_return_62_rows_2_columns(self):

        institute_link = "http://indicators.miccedu.ru/monitoring/2015/inst.php?id=1656"
        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_institute_indicators_and_values(soup)

        # assert
        self.assertEqual(62, len(result))
        self.assertEqual(2, len(result[0]))

    def test_get_addition_characteristics_should_return_56_rows_and_2_columns(self):
        indicators_and_values = [
            ["Наличие электронной библиотечной системы",
             "да да/нет"],
            ["Доходы вуза из иностранных источников на выполнение НИОКР",
             "0,00 тыс. руб."],
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=2025"

        soup = BeautifulSoup(get_page_html(institute_link), "html.parser")
        # act
        result = self.parser.get_addition_characteristics(soup)

        # assert
        self.assertEqual(56+3, len(result))
        self.assertEqual(2, len(result[0]))
        for indicator_and_value in indicators_and_values:
            self.assertTrue(indicator_and_value in result)


    def test_get_directions_2019_should_return_9_rows(self):
        directions = [
            "40.00.00 - Юриспруденция",
            "43.00.00 - Сервис и туризм"
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=1847"
        page_html = get_page_html(institute_link)
        soup = BeautifulSoup(page_html, "html.parser")
        # act
        result = self.parser.get_directions(soup)

        # assert
        self.assertEqual(9, len(result))
        for indicator_and_value in directions:
            self.assertTrue(indicator_and_value in result)

    def test_get_directions_2019_should_return_nothing(self):
        institute_link = "http://indicators.miccedu.ru/monitoring/2019/_vpo/inst.php?id=14013535"
        page_html = get_page_html(institute_link)
        soup = BeautifulSoup(page_html, "html.parser")
        # act
        result = self.parser.get_directions(soup)

        # assert
        self.assertEqual(0, len(result))


    def test_get_directions_2015_should_return_11_rows(self):
        directions = [
            "05.00.00 - НАУКИ О ЗЕМЛЕ",
            "43.00.00 - СЕРВИС И ТУРИЗМ"
        ]
        institute_link = "http://indicators.miccedu.ru/monitoring/2015/material.php?type=2&id=10307"
        page_html = get_page_html(institute_link)
        soup = BeautifulSoup(page_html, "html.parser")
        # act
        result = self.parser.get_directions(soup)

        # assert
        self.assertEqual(11, len(result))
        for indicator_and_value in directions:
            self.assertTrue(indicator_and_value in result)

    def test_get_directions_2015_should_return_nothing(self):
        institute_link = "http://indicators.miccedu.ru/monitoring/2015/inst.php?id=12013221"
        page_html = get_page_html(institute_link)
        soup = BeautifulSoup(page_html, "html.parser")
        # act
        result = self.parser.get_directions(soup)
        self.assertEqual(0, len(result))


    def export_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo", os.path.join(os.getcwd(), "year2018.json"))
        self.assertTrue(True)

    def export_2017_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2017/index.php?m=vpo", os.path.join(os.getcwd(), "year2017.json"))
        self.assertTrue(True)

    def export_2015_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2015", os.path.join(os.getcwd(), "new2015.json"))
        self.assertTrue(True)
    def test_export_2019_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2019/index.php?m=vpo", os.path.join(os.getcwd(), "new2019.json"))
        self.assertTrue(True)

    def export_2016_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2016/index.php?m=vpo", os.path.join(os.getcwd(), "new2016.json"))
        self.assertTrue(True)

    def export_2018_year_to_json(self):
        result = self.parser.export_year_to_json("http://indicators.miccedu.ru/monitoring/2018/index.php?m=vpo",
                                                 os.path.join(os.getcwd(), "new2018.json"))
        self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()
