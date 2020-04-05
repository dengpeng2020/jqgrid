import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from stu_app.models import StuMsg, StuClass


def stu_list(request):
    """
    访问员工的表单
    :param request:
    :return:
    """
    return render(request, "stu_list.html")


def get_stu(request):
    """
    获取所有员工信息的方法
    :param request: 每页分页的数量  页码
    :return:
    """

    rows = request.GET.get('rows')
    page = request.GET.get('page', 1)

    stu_list = StuMsg.objects.all().order_by('id')

    all_page = Paginator(stu_list, rows)
    page_num=all_page.num_pages  ##获取总页面数
    # 获取分页后第一页的对象
    # print(page_num,37)
    if int(page)>page_num:
        page=page_num
    page_obj = Paginator(stu_list, rows).page(page).object_list
    page_data = {
        "page": page,
        "total": all_page.num_pages,
        "records": all_page.count,
        "rows": list(page_obj)
    }

    # 对象序列化
    def myDefault(u):
        if isinstance(u, StuMsg):
            return {"id": u.pk,
                    "name": u.name,
                    "age": u.age,
                    "bir": u.bir.strftime('%Y-%m-%d'),
                    "stu_class": u.class_id.class_name}

    data = json.dumps(page_data, default=myDefault)
    return HttpResponse(data)


def get_class(request):
    """
    获取所有班级信息
    :param request:
    :return: 将班级信息填充为select进行返回
    """
    values_list = StuClass.objects.all().values_list('class_name', flat=True)
    select = "<select>"

    for i in values_list:
        html_con = "<option>{}</option>".format(i)
        select += html_con

    select += "</select>"

    return HttpResponse(select)


@csrf_exempt  # 解决csrf
def edit_stu(request):
    option = request.POST.get("oper")
    if option == "add":
        name = request.POST.get('name')
        age = request.POST.get('age')
        bir = request.POST.get('bir')
        stu_class = request.POST.get('stu_class')
        class_obj = StuClass.objects.all().get(class_name=stu_class)
        # 将获取到的表单数据保存到数据库
        StuMsg.objects.create(name=name, age=age, bir=bir, class_id=class_obj)

    elif option == "edit":
        id=request.POST.get('id')
        name = request.POST.get('name')
        age = request.POST.get('age')
        bir = request.POST.get('bir')
        stu_class = request.POST.get('stu_class')
        class_obj= StuClass.objects.all().get(class_name=stu_class)
        stu=StuMsg.objects.get(id=id)
        stu.name=name
        stu.age=age
        stu.bir=bir
        stu.class_id=class_obj
        stu.save()
    elif option == "del":
        stu_id = request.POST.get("id")
        StuMsg.objects.get(pk=stu_id).delete()

    return HttpResponse("success")