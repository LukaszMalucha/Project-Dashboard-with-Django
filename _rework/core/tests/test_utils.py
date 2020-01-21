# from django.contrib.auth import get_user_model
# from django.test import TestCase
#
# from core.models import MyProfile
# from core.utils import content_file_name
#
#
# class ContentFileTests(TestCase):
#
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             email="test@gmail.com",
#             password="test1234",
#             name="Test User"
#         )
#
#         self.my_profile = MyProfile.objects.filter(owner__email="test@gmail.com").first()
#         self.filename = content_file_name(self.my_profile, "C:/Images/test_image.jpg")
#
#     def tearDown(self):
#         self.user.delete()
#         self.my_profile.delete()
#
#     def test_content_file_name(self):
#         self.assertEqual(str(self.filename)[10:], "1-portrait.jpg")
#
