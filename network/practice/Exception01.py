# try:
#     print("[+]1337/0=" + str(1337 / 0))
# except Exception as e:
#     print("[-]Error.", str(e))

# import socket
#
#
# def reBanner(ip, port):
#     try:
#         socket.setdefaulttimeout(2)
#         s = socket.socket()
#         s.connect((ip, port))
#         banner = s.recv(1024)
#         return banner
#     except Exception as e:
#         return e
#
#
# def main():
#     ip1 = "192.168.95.148"
#     ip2 = "192.168.95.148"
#     port = 21
#     banner1 = reBanner(ip1, port)
#     if banner1:
#         print("[+]"+ip1+':'+str(banner1))
#     banner2 = reBanner(ip2, port)
#     if banner2:
#         print("[+]"+ip2+":"+str(banner2))
#     if __name__ == '__main__':
#         main()
portliest = [21, 22, 80, 110, 445]
with open("01.txt", "w") as t:
    for IP in range(1, 255):
        for port in portliest:
            t.write("[+]Checking 192.168.1." + str(IP) + ":" + str(port)+"\n")

with open("01.txt", "r") as tx:
    for line in tx.readlines():
        if ":22" in line.strip("\n"):
            print(line.strip("\n"))
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。

t.close()
tx.close()

