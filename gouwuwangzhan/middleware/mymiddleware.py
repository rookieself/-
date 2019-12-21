from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 定义一个常量的列表，专门用于处理Json请求,一定先加/,前面的浏览器不会给你添加，后面的会自动添加
from App.models import AXFUser

LOGIN_JSON_PATH = ['/App/addcart/','/App/changecartstate/','/App/subshopping/',]
# 定义一个普通的request请求路径
LOGIN_PATH = ['/App/cart/',]


# 登录验证中间件
class LoginMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 查看当前的路径
        print(request.path)
        if request.path in LOGIN_JSON_PATH:
            # goods_id = request.GET.get('gid')
            username = request.session.get('username', '')

            if username:
                # 登陆
                # 获取用户，
                user = AXFUser.objects.filter(username=username)

                # 判断用户是否存在，进行数据绑定
                if user.exists():
                    request.user = user.first()
                else:
                    return JsonResponse({'status': 'fail', 'msg': '用户不存在'})

            else:
                # 没登陆
                return JsonResponse({'status': 'fail', 'msg': '用户没有登陆'})

        if request.path in LOGIN_PATH:
            username = request.session.get('username')
            # 对用户进行判断
            if username:
                # 登录  获取用户，通过用户表拿到用户的名字
                user = AXFUser.objects.filter(username=username)
                #     判断用户是否存在，进行数据的绑定
                if user.exists():
                    request.user = user.first()
                else:
                    # 这里用的Json的方式，所以也必须用Json的方式来返回数据
                    return redirect(reverse('App:show_login'))

            else:
                # 没有登录，返回结果
                return JsonResponse({'status': 'fail', 'msg': '没有登录'})
