from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class IdentityMidWare(MiddlewareMixin):

    def process_request(self, request):
        if request.path_info in ["/login/", "/image/code/"]:  # 排除不需要中间件的路由
            return
        info = request.session.get('info')
        if info:
            return
        return redirect('/login/')
