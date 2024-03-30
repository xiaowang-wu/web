from django.utils.safestring import mark_safe
import copy

"""
自定义分页组件
request 请求
data_count 符合条件的数据
page_parm 请求的页面数据的参数
"""


class pagination:
    def __init__(self, request, data_count, page_parm='page', page_size=9, ):

        object_get = copy.deepcopy(request.GET)  # 处理搜索后，翻页不能并行 对应行标记我 s ，此处深拷贝进行地址变更
        object_get._mutable = True  # s 此处可以修改  将所复制的请求地址修改为可修改
        self.object_get = object_get  # s   设置对象参数

        self.object_get.setlist('page', [1])
        page = int(request.GET.get(page_parm, 1))
        if type(page) != int:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.select_data = data_count[self.start:self.end + 1]
        self.page_parm = page_parm
        data_row = data_count.count()
        count, mode = divmod(data_row, page_size)
        if mode:
            count = count + 1
        self.count = count
        # self.page_show = page_show
        self.page_size = page_size
        self.request = request

    def html(self):
        if self.page < 6:
            self.page_start = 1
            self.page_end = 11
        else:
            if self.page + 5 >= self.count:
                self.page_end = self.count
                self.page_start = self.count - 10
            else:
                self.page_start = self.page - 5
                self.page_end = self.page + 5
        if self.page_end > self.count:

            self.page_end = self.count
        page_str = []
        if self.page <= 1:
            self.object_get.setlist(self.page_parm, [1])  # s  在原有的地址基础上添加 page_pram=1
            pre = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
                self.object_get.urlencode())  # s 此处进行地址解析http://127.0.0.1:8000/pretty/mobile/?q=00&page=2
        else:
            self.object_get.setlist(self.page_parm, [self.page - 1])
            pre = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">«</span></a></li>'.format(
                self.object_get.urlencode())
        page_str.append(pre)
        for i in range(self.page_start, self.page_end + 1):
            if self.page == i:
                self.object_get.setlist(self.page_parm, [i])  # s
                html = '<li class="active"><a href="?{}">{}</a></li>'.format(self.object_get.urlencode(), i)  # s
            else:
                self.object_get.setlist(self.page_parm, [i])
                html = '<li><a href="?{}">{}</a></li>'.format(self.object_get.urlencode(), i)
            page_str.append(html)
        if self.page >= self.count:
            self.object_get.setlist(self.page_parm, [self.count])
            after = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">»</span></a></li>'.format(
                self.object_get.urlencode())
        else:
            self.object_get.setlist(self.page_parm, [self.page + 1])
            after = '<li><a href="?{}" aria-label="Previous"><span aria-hidden="true">»</span></a></li>'.format(
                self.object_get.urlencode())
        page_str.append(after)
        page_list = mark_safe("".join(page_str))
        return page_list
