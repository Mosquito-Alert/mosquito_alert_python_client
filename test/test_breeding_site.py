# coding: utf-8

"""
    Mosquito Alert API

    Introducing API v1 for Mosquito Alert platform, a project desgined to facilitate citizen science initiatives and enable collaboration among scientists, public health officials, and environmental managers in the investigation and control of disease-carrying mosquitoes.

    The version of the OpenAPI document: v1
    Contact: it@mosquitoalert.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from mosquito_alert_api.models.breeding_site import BreedingSite

class TestBreedingSite(unittest.TestCase):
    """BreedingSite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BreedingSite:
        """Test BreedingSite
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BreedingSite`
        """
        model = BreedingSite()
        if include_optional:
            return BreedingSite(
                uuid = '',
                short_id = '',
                user_uuid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                location = mosquito_alert_api.models.report_location.ReportLocation(
                    type = 'current', 
                    point = mosquito_alert_api.models.report_location_point.ReportLocation_point(
                        latitude = 1.337, 
                        longitude = 1.337, ), 
                    timezone = 'Africa/Abidjan', 
                    country_id = 56, 
                    nuts_2 = '', 
                    nuts_3 = '', ),
                note = '',
                tags = [
                    ''
                    ],
                published = True,
                photos = [
                    mosquito_alert_api.models.report_photo.ReportPhoto(
                        uuid = '', 
                        url = '', )
                    ],
                site_type = 'basin',
                has_water = True,
                in_public_area = True,
                has_near_mosquitoes = True,
                has_larvae = True
            )
        else:
            return BreedingSite(
                uuid = '',
                short_id = '',
                user_uuid = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at_local = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                sent_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                received_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                location = mosquito_alert_api.models.report_location.ReportLocation(
                    type = 'current', 
                    point = mosquito_alert_api.models.report_location_point.ReportLocation_point(
                        latitude = 1.337, 
                        longitude = 1.337, ), 
                    timezone = 'Africa/Abidjan', 
                    country_id = 56, 
                    nuts_2 = '', 
                    nuts_3 = '', ),
                published = True,
                photos = [
                    mosquito_alert_api.models.report_photo.ReportPhoto(
                        uuid = '', 
                        url = '', )
                    ],
        )
        """

    def testBreedingSite(self):
        """Test BreedingSite"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()