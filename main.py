import requests, random, string, multiprocessing
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
shtuf = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

print('Xbox Username Checker\n[1] | Start 3L Search\n[2] | Start 4L Search')
choice = input('Choice: ')

def _3_letter_check_mixed():
    print('starting 3 letter check (mixed)')
    while True:
        user = str(random.choice(string.ascii_letters)).lower() + str(shtuf[random.randrange(35)]).lower() + str(shtuf[random.randrange(35)]).lower()
        
        with open('3Lchecked.txt', 'a+') as c:
            if user not in c.readlines():
                c.write(user + '\n')
                proxie_list = []
                with open("https.txt", "r") as f:                   
                    for proxy in f.readlines():
                        proxie_list.append(proxy.replace("\n", ""))
                proxies = {
                'https://': random.choice(proxie_list)
                }
                try:
                    r = requests.get(f'https://xboxgamertag.com/search/{user}', headers=headers, proxies=proxies, timeout=5)
                except:
                    print(f'REQUEST FAILED : {user}')
                if r.status_code == 404:
                    with open('3Lusernames.txt', 'a+') as t:
                        print(f'{user} : AVAILABLE')
                        t.write(user + '\n')
                else:
                    print(f'{user} : taken')
def _3_letter_check_letter_only():
    print('starting 3 letter check')
    while True:
        user = random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
        
        with open('3Lchecked.txt', 'a+') as c:
            if user not in c.readlines():
                    c.write(user + '\n')
                    proxie_list = []
                    with open("https.txt", "r") as f:                   
                        for proxy in f.readlines():
                            proxie_list.append(proxy.replace("\n", ""))
                    proxies = {
                    'https://': random.choice(proxie_list)
                    }
                    try:
                        r = requests.get(f'https://xboxgamertag.com/search/{user}', headers=headers, proxies=proxies, timeout=5)
                    except:
                        print(f'REQUEST FAILED : {user}')
                    if r.status_code == 404:
                        with open('3Lusernames.txt', 'a+') as t:
                            print(f'{user} : AVAILABLE')
                            t.write(user + '\n')
                    else:
                        print(f'{user} : taken')

def _4_letter_check_mixed():
    print('starting 4 letter check (mixed)')
    while True:
        user = str(random.choice(string.ascii_letters)).lower() + str(shtuf[random.randrange(35)]).lower() + str(shtuf[random.randrange(35)]).lower() + str(shtuf[random.randrange(35)]).lower()
        
        with open('4Lchecked.txt', 'a+') as c:
            if user not in c.readlines():
                c.write(user + '\n')
                proxie_list = []
                with open("https.txt", "r") as f:                   
                    for proxy in f.readlines():
                        proxie_list.append(proxy.replace("\n", ""))
                proxies = {
                'https://': random.choice(proxie_list)
                }
                try:
                    r = requests.get(f'https://xboxgamertag.com/search/{user}', headers=headers, proxies=proxies, timeout=5)
                except:
                    print(f'REQUEST FAILED : {user}')
                if r.status_code == 404:
                    with open('4Lusernames.txt', 'a+') as t:
                        print(f'{user} : AVAILABLE')
                        t.write(user + '\n')
                else:
                    print(f'{user} : taken')

def _4_letter_check_letter_only():
    print('starting 4 letter check')
    while True:
        user = random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower() + random.choice(string.ascii_letters).lower()
        
        with open('4Lchecked.txt', 'a+') as c:
            if user not in c.readlines():
                    c.write(user + '\n')
                    proxie_list = []
                    with open("https.txt", "r") as f:                   
                        for proxy in f.readlines():
                            proxie_list.append(proxy.replace("\n", ""))
                    proxies = {
                    'https://': random.choice(proxie_list)
                    }
                    try:
                        r = requests.get(f'https://xboxgamertag.com/search/{user}', headers=headers, proxies=proxies, timeout=5)
                    except:
                        print(f'REQUEST FAILED : {user}')
                    if r.status_code == 404:
                        with open('4Lusernames.txt', 'a+') as t:
                            print(f'{user} : AVAILABLE')
                            t.write(user + '\n')
                    else:
                        print(f'{user} : taken')
def start3L():    
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=_3_letter_check_mixed)
        if __name__ == "__main__":
            p.start()
            processes.append(p)
    for i in range(10):
        p = multiprocessing.Process(target=_3_letter_check_letter_only)
        if __name__ == "__main__":
            p.start()
            processes.append(p)
    for p in processes:
        p.join()

def start4L():    
    processes = []
    for i in range(10):
        p = multiprocessing.Process(target=_4_letter_check_mixed)
        if __name__ == "__main__":
            p.start()
            processes.append(p)
    for i in range(10):
        p = multiprocessing.Process(target=_4_letter_check_letter_only)
        if __name__ == "__main__":
            p.start()
            processes.append(p)
    for p in processes:
        p.join()

    
if choice == 1:
    start3L()
else:
    start4L()