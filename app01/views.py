from django.shortcuts import render, redirect

# Create your views here.

from app01 import models


def depart_list(request):
    """ 部门列表 """
    # print(Department.objects.all())
    depart_list_data = models.Department.objects.all()
    return render(request, "depart_list.html", {"depart_list": depart_list_data})


def depart_add(request):
    """ 新建部门 """
    if request.method == "GET":
        return render(request, "add_depart.html")
    title = request.POST.get("title")
    if not (title and title != ""):
        return render(request, "add_depart.html", {"return_msg": "错误！未输入部门名称！", "placeholder": title})

    if len(models.Department.objects.filter(title=title)) > 0:
        return render(request, "add_depart.html", {"return_msg": "错误！部门名称重复", "placeholder": title})

    models.Department.objects.create(title=title)
    return render(request, "add_depart.html", {"return_msg": "添加成功！", "placeholder": title})


def depart_delete(request):
    depart_id = request.GET.get("id")
    models.Department.objects.filter(id=depart_id).delete()
    return redirect("/depart/list")


def depart_edit(request, pid):
    """ 编辑部门 """
    title = models.Department.objects.filter(id=pid).first()
    if request.method == "GET":
        return render(request, "edit_depart.html", {"pid": pid, "placeholder": title})

    new_title = request.POST.get("title")
    models.Department.objects.filter(id=pid).update(title=new_title)
    return render(request, "edit_depart.html", {"pid": pid, "placeholder": new_title})
