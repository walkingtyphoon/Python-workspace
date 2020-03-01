import pyecharts
from pyecharts.charts import Bar
from pyecharts import options as opts

print(pyecharts.__version__)

bar = (
    Bar()
        .add_xaxis(['a', 'b', 'c', 'd', 'e'])
        .add_yaxis('生活支出', [100, 25, 42, 34, 52])
        .add_yaxis("娱乐支出", [35, 27, 46, 58, 15])
        .set_global_opts(title_opts=opts.TitleOpts(title="这是主标题", subtitle="这是副标题"))
)
bar.render("02.html")
