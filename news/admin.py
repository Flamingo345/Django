from django.contrib import admin
from .models import Reporter, Article  # 导入模型

# 注册模型（自动生成管理界面）
admin.site.register(Reporter)
admin.site.register(Article)
