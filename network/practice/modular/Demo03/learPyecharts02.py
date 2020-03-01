from pyecharts.charts import Bar
# 导入设置柱状图
from pyecharts import options as opts
# 导入设置选项

bar = (
    Bar()
        .add_xaxis(['a', 'b', 'c', 'd', 'e'])
        .add_yaxis('生活支出', [100, 25, 42, 34, 52])
        .add_yaxis("娱乐支出", [35, 27, 46, 58, 15])
        .set_global_opts(title_opts=opts
        .TitleOpts(title="这是主标题", subtitle="这是副标题"),
        toolbox_opts=opts
        .ToolboxOpts(is_show=True))
)
bar.render("03.html")

