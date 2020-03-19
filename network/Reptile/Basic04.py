import urllib
from urllib import request

url = request.urlopen("https://mp.weixin.qq.com/s?__biz=MzU3NTc0NzE0Mw==&mid=2247483739&idx=1&sn"
                      "=e62a61120c73ebb93029a2897ca60ccd&chksm"
                      "=fd1f2473ca68ad658b9b0388e6fc122951812ba08ada771f3acc4f1f25953de92df837f21795&mpshare=1&scene"
                      "=1&srcid=&sharer_sharetime=1584410683814&sharer_shareid=b14cc42c8dff2f85ec3b42ef9ff07140&key"
                      "=e5d129685831bfd623675c86aca8c5d71f7039e1528f4d357e1ee960fa45ff25c931951e9e391cc21362eb047c4be8befc73a3c7bdb580dcd9b09cf0e793e3fa3f628004c4516333e0ad741f5b771893&ascene=1&uin=MzkzMDAwOTYz&devicetype=Windows+10&version=62080085&lang=zh_CN&exportkey=AVLGCY0spN1AMCYHOT1pGLc%3D&pass_ticket=JeeLLBclQmIly5Ufx2oeHDjvEaxGUIAkQ3OplCJz9sTRvWul2fEP5%2FfN6FvDrxlX")
value = urllib.urlopen(url)
print(value.readlines())

