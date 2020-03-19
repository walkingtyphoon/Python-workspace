from urllib import request
from urllib import parse

head = request.urlopen("https://mp.weixin.qq.com/s?__biz=MzU3NTc0NzE0Mw==&mid=2247483739&idx=1&sn"
                       "=e62a61120c73ebb93029a2897ca60ccd&chksm"
                       "=fd1f2473ca68ad658b9b0388e6fc122951812ba08ada771f3acc4f1f25953de92df837f21795&mpshare=1&scene"
                       "=1&srcid=&sharer_sharetime=1584410683814&sharer_shareid=b14cc42c8dff2f85ec3b42ef9ff07140&key"
                       "=e5d129685831bfd623675c86aca8c5d71f7039e1528f4d357e1ee960fa45ff25c931951e9e391cc21362eb047c4be8befc73a3c7bdb580dcd9b09cf0e793e3fa3f628004c4516333e0ad741f5b771893&ascene=1&uin=MzkzMDAwOTYz&devicetype=Windows+10&version=62080085&lang=zh_CN&exportkey=AVLGCY0spN1AMCYHOT1pGLc%3D&pass_ticket=JeeLLBclQmIly5Ufx2oeHDjvEaxGUIAkQ3OplCJz9sTRvWul2fEP5%2FfN6FvDrxlX")
print("读取数据", head.read())
print("按行读取数据", head.readline())
print("多行读取数据", head.readlines())
print("读取返回的信息：", head.getcode())
request.urlretrieve(
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1581932221441&di"
    "=09a3b2baa29cfe07c21337a30e5c4080&imgtype=jpg&src=http%3A%2F%2Fwww.rfuchina.com%2Fuploadfile%2F2019%2F0417"
    "%2F20190417091923688.jpg",
    "01/01.jpg")
# 将指定文件保存到本地

params = {"name": "张三", "age": "18", "greet": "hello world"}
result = parse.urlencode(params)
print(result)
# 将字符进行编码

