from pyecharts.charts import Bar
from pyecharts import options as opts

bar = (
    Bar().add_xaxis(['一月', '二月', '三月', '四月', '五月'])
        .add_yaxis('生活支出', [100, 25, 42, 34, 52])
        .add_yaxis("娱乐支出", [35, 27, 46, 58, 15])
        .set_global_opts(title_opts=opts.TitleOpts(title="2月消费记录",subtitle="这是副标题"))
)
bar.render("01.html")
# bar = (
# #     Bar()
# #     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# #     .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# #     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# #     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# # )
# # bar.render()
