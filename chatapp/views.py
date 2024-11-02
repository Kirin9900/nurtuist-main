from django.shortcuts import render
from openai import OpenAI
import nurtuist.connectDB


# 配置 OpenAI 客户端
client = OpenAI(
    api_key="sk-deLT2Zv03vl7BDeFy2Vxx8VOIezHoCiorEXc40oVwWUtadu4",
    base_url="https://api.chatanywhere.com.cn"
)


def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.6,
    )
    return response.choices[0].message.content


def sign_up(request):
    # 注册数据获取
    if request.method == 'POST':
        newname = request.POST.get('username')
        password = request.POST.get('pwd')

        data = (newname, password)

        res = nurtuist.connectDB.insert_name(data)
        return render(request, 'chatapp/login1.html')
    return render(request, 'chatapp/注册.html')


username = None


def log_in(request):
    # 登录数据获取
    if request.method == 'POST':
        global username
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        data = (username, password)

        res = nurtuist.connectDB.select_date(data)
        if res is not None:
            return render(request, 'chatapp/page1.html')
        else:
            context = {'error_message': '该账号不存在或密码错误'}
            return render(request, 'chatapp/login1.html', context)
    else:
        return render(request, 'chatapp/login1.html')


def parse_menu_data(recipe):
    # 对GPT生成的食谱按日期分类
    menu = {"周一：": "", "周二：": "", "周三：": "", "周四：": "", "周五：": "", "周六：": "", "周日：": "", "其他：": ""}

    current_day = None
    for item in recipe.splitlines():
        if item in ["周一：", "周二：", "周三：", "周四：", "周五：", "周六：", "周日："]:
            current_day = item
        if current_day is None:
            current_day = "其他："
        menu[current_day] += item

    return menu


def get_recipe(request):
    # 数据收集页面
    if request.method == 'POST':
        # 从表单获取数据
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        body_fat = request.POST.get('zhi')
        blood_sugar = request.POST.get('sugar')
        food_habit = request.POST.get('habit')

        # 构建 GPT 的提示信息
        prompt = f"根据以下信息生成一份一周七天适合这样体质的食谱，标注好用量，每一天的食谱都以“周几：”开始，然后另起一行开始输出食谱，周日的食谱以“周日：”开始，只生成食谱，别说废话，：性别{sex}，年龄{age}岁，体重{weight}kg，身高{height}cm，体脂率{body_fat}%，血糖含量{blood_sugar}，食物偏好{food_habit}。"

        # 调用 GPT 生成食谱
        try:
            recipe = get_completion(prompt)
        except Exception as e:
            recipe = f"生成食谱时发生错误：{str(e)}"

        menu = parse_menu_data(recipe)
        data = (sex, age, weight, height, body_fat, blood_sugar, food_habit, username)
        data_2 = (menu["周一："], menu["周二："], menu["周三："], menu["周四："], menu["周五："], menu["周六："], menu["周日："],
                username)
        nurtuist.connectDB.update(data, data_2)

        key = nurtuist.connectDB.select_food(username)
        return render(request, 'chatapp/result.html', {'recipe': recipe})
    else:
        # 如果不是 POST 请求，则显示表单
        return render(request, 'chatapp/index.html')

    # 新增视图函数用于渲染 page1.html


# 以下都是各界面的显示代码
def page1_view(request):
    return render(request, 'chatapp/page1.html')

    # 新增个人页面的视图函数


def personal_page_view(request):
    return render(request, 'chatapp/个人页面.html')


def log_in_view(request):
    return render(request, 'chatapp/login1.html')


def index_view(request):
    return render(request, 'chatapp/index.html')


def sign_up_view(request):
    return render(request, 'chatapp/注册.html')


def get_food_view(request):
    res = nurtuist.connectDB.select_food(username)
    return render(request, 'chatapp/轮播图.html', {'recipe': res.values()})

def store(request):
    return render(request, 'chatapp/商城.html')

def distribution(request):
    return render(request, 'chatapp/配送.html')
