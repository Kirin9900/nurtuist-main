# NurtuistWithGPT - 基于Django的健康饮食管理平台

## 项目简介

**NurtuistWithGPT** 是一个基于 Django 框架的 Web 应用程序，旨在为用户提供个性化的健康饮食建议。通过集成 OpenAI 的 API，本项目能够根据用户的个人信息（如性别、年龄、体重、身高、体脂率、血糖水平及食物偏好）生成为期一周的健康食谱。项目还提供了用户注册、登录、个人信息管理和查看个性化食谱等功能，确保每位用户都能获得专属的健康饮食计划。

## 技术栈

- **后端框架**: Django
- **前端技术**: HTML, CSS, JavaScript
- **数据库**: MySQL
- **第三方API**: OpenAI API 用于生成个性化食谱

## 功能概述

### 用户管理

- **注册与登录**: 用户可以通过填写表单完成注册，并使用用户名和密码登录系统。
- **个人信息维护**: 登录后的用户可以查看和修改自己的个人信息。

### 食谱管理

- **个性化食谱生成**: 用户提交个人健康信息后，系统将调用 OpenAI API 生成一份为期一周的个性化食谱。
- **食谱展示**: 生成的食谱将按照日期进行分类，并在用户界面中清晰展示。

### 其他功能

- **错误处理**: 对于 API 调用失败等异常情况，系统会向用户显示友好的错误信息。
- **安全性**: 使用 Django 内置的安全机制来保护用户数据安全，包括 CSRF 保护等。

## 安装与部署

### 环境准备

- Python 3.8 或更高版本
- Django 4.2 或更高版本
- MySQL 8.0 或更高版本
- 安装必要的依赖包

### 安装步骤

1. **克隆仓库**:

   ```bash
   git clone <你的仓库地址>
   cd nurtuist-main
   ```

2. **创建并激活虚拟环境**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **安装依赖**:

   ```bash
   pip install -r requirements.txt
   ```

4. **配置 MySQL 数据库**:
   在 `nurtuist/settings.py` 文件中配置 MySQL 数据库连接：

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'nurtuist',
           'USER': 'root',
           'PASSWORD': 'lc040728',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

5. **配置 OpenAI API Key**:
   在 `chatapp/views.py` 文件中配置您的 OpenAI API Key 和基础 URL：

   ```python
   from openai import OpenAI
   client = OpenAI(
       api_key="sk-deLT2Zv03vl7BDeFy2Vxx8VOIezHoCiorEXc40oVwWUtadu4",
       base_url="https://api.chatanywhere.com.cn"
   )
   ```

6. **迁移数据库**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **运行服务器**:

   ```bash
   source .venv/bin/activate
   python manage.py runserver 8080
   ```

8. **访问应用**:
   打开浏览器，输入 `http://127.0.0.1:8000/` 即可访问应用。

![login](/templates/img/img.png)


## 开发指南

### 目录结构

```
nurtuistWithGPT/
│
├── nurtuist/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── chatapp/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   │   ├── chatapp/
│   │   │   ├── login1.html
│   │   │   ├── 注册.html
│   │   │   ├── page1.html
│   │   │   ├── 个⼈⻚⾯.html
│   │   │   ├── 商城.html
│   │   │   ├── 轮播图.html
│   │   │   └── result.html
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   ├── apps.py
│   └── forms.py
│
├── manage.py
└── requirements.txt
```

### 视图函数说明

- **sign_up**: 处理用户注册逻辑。

- **log_in**: 处理用户登录逻辑。

- **get_recipe**: 根据用户提供的个人信息，调用 OpenAI API 生成个性化食谱。

- **parse_menu_data**: 将生成的食谱按日期分类。

- **page1_view**, **personal_page_view**, **log_in_view**, **index_view**, **sign_up_view**: 分别对应不同页面的渲染。

  

## 贡献者指南

欢迎所有开发者贡献代码！如果您发现了 Bug 或有好的建议，请通过 Pull Request 的形式提交。

## 许可证

本项目遵循 MIT 许可证，详情请见 LICENSE 文件。

---

**NurtuistWithGPT** 致力于帮助更多人实现健康生活的目标，我们期待您的加入，共同打造更完善的健康饮食管理系统。