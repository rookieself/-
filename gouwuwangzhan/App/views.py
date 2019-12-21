import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse

from App.app_constains import *
from App.forms import UserRegisterForm, UserLoginForm
from App.models import axf, MainNav, MainMustBuy, MainShop, MainShow, MainFoodTypes, Goods, AXFUser, Cart
from py1814aixianfeng.settings import DEFAULT_FROM_EMAIL

# 首页视图
def index(request):
    # 获取轮播图片中所有的数据
    wheels = axf.objects.all()
    # 获取导航中所有的数据
    navs = MainNav.objects.all()
    # 获取每日必买所有的数据
    mustbuys = MainMustBuy.objects.all()
    shop_goods = MainShop.objects.all()
    shop_goods_1 = shop_goods[0:1]
    shop_goods_1_3 = shop_goods[1:3]
    shop_goods_3_7 = shop_goods[3:7]
    shop_goods_7_11 = shop_goods[7:]
    # 获取商品的详细商品数据
    mainshows = MainShow.objects.all()
    return render(request, 'main/home.html',
                  {'wheels': wheels, 'title': '首页', 'navs': navs, 'mustbuys': mustbuys, 'shop_goods_1': shop_goods_1,
                   'shop_goods_1_3': shop_goods_1_3, 'shop_goods_3_7': shop_goods_3_7,
                   'shop_goods_7_11': shop_goods_7_11, 'mainshows': mainshows})


# 闪购视图函数
def show_market(request):
    # 获取typeid数据
    typeid = request.GET.get('typeid', '103541')
    # 定义子类型数据
    childid = request.GET.get('childid', '0')

    # 排序的规则，先获取再设置
    rule_sort = request.GET.get('sort', 0)
    # 获取闪购侧边栏的数据
    foodtypes = MainFoodTypes.objects.all()

    # 定义一个列表，存放数据
    foodtype_childname_list = []
    # 定义一个排序规则的列表
    order_list = [['综合排序', ORDER_TOTAL],
                  ['价格升序', ORDER_PRICE_UP],
                  ['价格降序', ORDER_PRICE_DOWN],
                  ['销量升序', ORDER_SALE_UP],
                  ['销量降序', ORDER_SALE_DOWN]]

    # 判断typeid是否存在
    if typeid:
        # # 获取右侧商品的所有数据
        # goods_list = Goods.objects.all()

        # 分析表的结构，判断typeid和categoryid值是否相等
        goods_list = Goods.objects.filter(categoryid=typeid)

        # 加入一个判断，childid是否为0，如果为0，0表示全部的分类
        if childid == ALL_TYPE:
            pass
        else:
            goods_list = goods_list.filter(childcid=childid)

        # 排序
        if rule_sort == ORDER_TOTAL:
            pass
        elif rule_sort == ORDER_PRICE_UP:
            goods_list = goods_list.order_by('price')
        elif rule_sort == ORDER_PRICE_DOWN:
            goods_list = goods_list.order_by('-price')
        elif rule_sort == ORDER_SALE_UP:
            goods_list = goods_list.order_by('productnum')
        elif rule_sort == ORDER_SALE_DOWN:
            goods_list = goods_list.order_by('-productnum')

        # 获取foodtype的对象
        foodtype = MainFoodTypes.objects.get(typeid=typeid)

        # 获取childtypenames字段
        foodtypechildnames = foodtype.childtypenames

        # 使用split切割
        foodtypechildname_list = foodtypechildnames.split('#')
        # 遍历
        for childname in foodtypechildname_list:
            foodtype_childname_list.append(childname.split(':'))

    return render(request, 'main/market.html',
                  {'foodtypes': foodtypes, 'goods_list': goods_list, 'typeid': int(typeid),
                   'foodtype_childname_list': foodtype_childname_list, 'childid': childid, 'rule_sort': rule_sort,
                   'order_list': order_list})

# 我的页面展示
def show_mine(request):
    # 获取头像和用户名
    # username = request.session['username']
    # 判断用户是否存在，如果没有该用户就使用原始图片
    username = request.session.get('username')
    if username:
        # 拿一整条数据
        user = AXFUser.objects.filter(username=username).first()
        return render(request, 'main/mine.html', {'user': user})
    else:
        return render(request, 'main/mine.html')


def show_login(request):
    if request.method == "GET":
        return render(request, 'user/login.html')
    else:
        # 拿数据和forms里的数据来进行对比
        user_login_form = UserLoginForm(request.POST)
        if user_login_form.is_valid():
            # 获取用户名和密码
            username = user_login_form.cleaned_data['username']
            password = user_login_form.cleaned_data['password']

            # 从数据库中获取username和password的值
            # 验证用户名，验证是否激活，密码是否正确
            user = AXFUser.objects.filter(username=username)
            if user.exists():
                user = user.first()
                # 判断是否被激活
                if user.is_active:
                    # 验证密码
                    if check_password(password, user.password):
                        print(password, user.password)
                        # 添加缓存
                        request.session['username'] = username
                        return redirect(reverse('App:show_mine'))
                    else:
                        print(type(password), type(user.password))
                        return render(request, 'user/login.html', {'msg': '密码不正确'})
                else:
                    print('没有激活')
                    return render(request, 'user/login.html', {'msg': '用户没有激活'})
            else:
                return render(request, 'user/login.html', {'msg': '没有该用户，请先去注册'})
        else:
            return render(request, 'user/login.html', {'user_login_form': 'user_login_form'})


def user_register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    else:
        # 获取数据，把数据上传到数据库中，forms表单数据的实时验证
        # 涉及文件的上传，request.files--->内存，磁盘--forms
        user_register_form = UserRegisterForm(request.POST, request.FILES)
        if user_register_form.is_valid():
            # 如果注册成功，将数据在控制台打印
            print(user_register_form.cleaned_data)
            # return HttpResponse('ok')
            # 获取数据，将数据进行校验，校验成功后添加到数据库中
            datas = user_register_form.cleaned_data
            if datas['password'] == datas['repassword']:
                user = AXFUser()
                user.username = datas['username']
                password = datas['password']
                password = make_password(password)
                user.password = password

                user.email = datas['email']
                user.uicon = datas['uicon']
                user.save()

                # 获取uuid(全局的唯一标识)
                u_token = uuid.uuid4().hex
                # 设置u_token和username进行绑定----》缓存到redis
                cache.set(u_token, user.username, timeout=60 * 60 * 24)

                print('u_token', u_token)

                data = {
                    'username': user.username,
                    'active_url': 'http://127.0.0.1:8000/App/active',
                    'u_token': u_token
                }

                # message = '<a href="#">激活</a>'
                message = loader.get_template('user/active.html').render(data)

                send_mail('爱鲜蜂用户激活', message, DEFAULT_FROM_EMAIL, [user.email, ], html_message=message)

            else:
                return render(request, 'user/register.html', {'msg': '密码不一致'})
            return render(request, 'user/registersuccess.html')
        else:
            return render(request, 'user/register.html', {'user_register_form': user_register_form})


# 完成异步请求，当失去当前焦点时检测是否正确，
# 通过ajax来判断用户名是否正确
def check_username(request):
    # 获取username
    username = request.GET.get('username')

    reslut = AXFUser.objects.filter(username=username)

    # 根据返回的结果，判断
    if reslut.exists():
        return JsonResponse({'status': 'fail', 'msg': '用户已存在'})
    else:
        return JsonResponse({'status': 'ok', 'msg': '用户名可用'})


# 实现激活的页面
def user_active(request):
    # 获取全局唯一的标识
    u_token = request.GET.get('u_token')
    # 去缓存中找
    value = cache.get(u_token)
    # 查询用户
    user = AXFUser.objects.filter(username=value).first()
    # 修改用户激活字段
    user.is_active = True

    user.save()

    return redirect(reverse('App:show_login'))

# 注销
def user_logout(request):
    # 清除数据（用户名，头像）
    request.session.flush()

    return redirect(reverse('App:show_mine'))


# 购物车
def show_cart(request):
    # 获取闪购页面的数据
    # 两步：查询和渲染：根据用户添加对应的商品
    cart_goods = Cart.objects.filter(user=request.user)
    total_price = get_totalprice(request)

    return render(request, 'main/cart.html', {'cart_goods': cart_goods, 'total_price': total_price})


# 添加购物车，把点击的行为，转化为数据，存到数据库中
def add_cart(request):
    # 获取gid
    gid = request.GET.get('gid', '')
    # 通过id找用户，返回商品的条目（过滤）
    print(request.user.id)

    carts = Cart.objects.filter(user_id=request.user.id).filter(goods_id=gid)
    # 判断有没有商品，有获取商品并加1，没有则添加（用ajax局部刷新）
    if carts.exists():
        # 展示数量
        cart = carts.first()
        cart.goods_num = cart.goods_num + 1
    else:
        # 如果当前还没有该商品，获取购物车的对象
        cart = Cart()
        # 根据gid获取商品的名称,根据键获取该商品的goods条目
        goods = Goods.objects.get(pk=gid)
        # 添加商品到购物车,给谁添加？
        cart.goods = goods
        # 添加商品给哪一个用户，所以必须是登录之后
        # 如果没有登录，则直接跳转到登录页面
        # 如果登录，则直接添加到购物车下面，。。。中间键
        cart.user = request.user
    # 保存数据
    cart.save()
    data = {'status': 'ok', 'goods_num': cart.goods_num}
    # 局部刷新的动作，所以用ajax的返回
    return JsonResponse(data)


def sub_cart(request):
    # 获取gid
    gid = request.GET.get("gid",'')
    print(gid)
    username = request.session.get('username')
    users = AXFUser.objects.filter(username=username)
    user = users.first()
    id = user.id
    # print(id)
    # return HttpResponse("ok")
    # 通过id找用户，返回商品的条目（过滤）
    carts = Cart.objects.filter(user_id=id).filter(goods_id=gid)
    print(carts)
    # return "ok"
    # 判断有没有商品，有获取商品并加1，没有则添加（用ajax局部刷新）
    if carts.exists():
        # 展示数量
        cart = carts.first()
        if cart.goods_num > 0:
            cart.goods_num = cart.goods_num - 1
    else:
        # 如果当前还没有该商品，获取购物车的对象
        cart = Cart()
        # 根据gid获取商品的名称,根据键获取该商品的goods条目
        goods = Goods.objects.get(pk=gid)
        # 添加商品到购物车,给谁添加？
        cart.goods = goods
        # 添加商品给哪一个用户，所以必须是登录之后
        # 如果没有登录，则直接跳转到登录页面
        # 如果登录，则直接添加到购物车下面，。。。中间键
        # cart.user = request.user
    # # 保存数据
    cart.save()
    data = {'status': 'ok', 'goods_num': cart.goods_num}
    # # 局部刷新的动作，所以用ajax的返回
    # return "ok"
    return JsonResponse(data)


# 定义一个方法，用于求商品的总和
def get_totalprice(request):
    # 先到数据库中拿数据，挑选选中的数据
    username = request.session.get('username')
    users = AXFUser.objects.filter(username=username)
    user = users.first()
    id = user.id
    carts = Cart.objects.filter(user_id=id).filter(is_select=True)
    total_price = 0
    #     统计价格：遍历carts,获取商品的数量和价格
    for goods in carts:
        total_price += goods.goods_num * goods.goods.marketprice
    return total_price


# 创建改变选中状态的视图
def change_cart_state(request):
    # 确定是哪一个商品，先找用户，在找商品
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    # 指向明确
    cart.is_select = not cart.is_select

    cart.save()

    return JsonResponse({'status': 'ok', 'is_select': cart.is_select, 'total_price': get_totalprice(request)})


# 购物车商品的添加
def add_shopping(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {}
    # 判断商品和其数量是否大于一
    print('ok2')
    cart.goods_num = cart.goods_num + 1
    cart.save()
    data['cart_gooods_num'] = cart.goods_num
    data['status'] = 'ok'
    data['total_price'] = get_totalprice(request)
    print(data['total_price'])
    # print(data)
    # return HttpResponse("ok")

    return JsonResponse(data)
# 购物车的商品减少
def sub_shopping(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    data = {}
    # 判断商品和其数量是否大于一
    if cart.goods_num > 1:
        print('ok1')
        cart.goods_num = cart.goods_num - 1
        cart.save()
        data['cart_gooods_num'] = cart.goods_num
    else:
        print('ok')
        cart.delete()
        data['cart_gooods_num'] = 0
    data['status'] = 'ok'
    data['total_price'] = get_totalprice(request)
    print(data['total_price'])

    return JsonResponse(data)


def success_cart(request):
    username = request.session.get('username')
    users = AXFUser.objects.filter(username=username)
    user = users.first()
    id = user.id
    carts = Cart.objects.filter(user_id=id)
    carts.delete()
    return render(request,'user/success_cart.html')