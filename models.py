# #making ORM models
# from django.db import models
# from django.apps import AppConfig
#
#
#
# # field = models.ForeignKey(AppConfig.get_model(PRODUCT_MODEL))
# class site(models.Model):
#     id = models.AutoField(primary_key=True)
#     url = models.CharField(max_length=100)
#     html_tag_title = models.TextField(default="")
#     html_tag_meta_title = models.TextField(default="")
#     html_tag_meta_description = models.TextField(default="")
#     html_tag_meta_image = models.TextField(default="")
#     server_time_created = models.DateTimeField(auto_now_add=True)
#
#
#     def __str__(self):
#         return self.url
#     class Meta:
#         db_table = "site"
# class site_visit(models.Model):
#     id = models.AutoField(primary_key=True)
#     keyword = models.CharField(max_length=100)
#     time = models.IntegerField()
#     class Meta:
#         db_table = "site_visit"
#     def __str__(self):
#         return self.keyword
#
#
