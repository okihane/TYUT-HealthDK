import requests
from bs4 import BeautifulSoup
import  time
from urllib import parse
import json
import random
#from datetime import datetime
#namenum是用户名，passwd是密码，分别改成自己的，这里我填了两个账号，可以填写多个，最后到主函数那里添加上相应的调用
#校区
xq = '迎西'
namenum = {
	'zs':'2021510001',
	'ls':'2021510002',
}
passwd = {
	'zs':'202222',
	'ls':'202222',
}
#推送开关，on/off
ts = 'off'

headers = {
'Host':'tyutgs.wjx.cn',
'Connection':'keep-alive',
'Cache-Control':'max-age=0',
'Upgrade-Insecure-Requests':'1',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'X-Requested-With':'com.tencent.mm',
'User-Agent':'Mozilla/5.0 (Linux; Android 10; LM-G820 Build/QKQ1.190929.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3189 MMWEBSDK/20211202 Mobile Safari/537.36 MMWEBID/12 MicroMessenger/8.0.18.2060(0x28001257) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Origin':'https://tyutgs.wjx.cn',
'Sec-Fetch-Site':'same-origin',
'Sec-Fetch-Mode':'navigate',
'Sec-Fetch-Dest':'empty',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
}

##
def abcd1(_0x17164c):
	return abcd2(_0x17164c, 3597397)
##
def abcd2(_0x1b1e02, _0x23f273):
  	if abcdx():
  		return
  	_0x1f9ba1 = 2147483648
  	_0x3b83ae = 2147483647
  	_0x4ad458 = int(_0x1b1e02 / _0x1f9ba1)
  	_0x470088 = int(_0x23f273 / _0x1f9ba1)
  	_0x5bc159 = _0x1b1e02 & _0x3b83ae
  	_0x35dfa5 = _0x23f273 & _0x3b83ae
  	_0x353774 = _0x4ad458 ^ _0x470088
  	_0x4a742c = _0x5bc159 ^ _0x35dfa5
  	return _0x353774 * _0x1f9ba1 + _0x4a742c
##
def abcd3(_0x420610, _0x1b425f):
	if (_0x420610 - 62) < 0:
		_0xea36a8 = _0x1b425f[_0x420610:(_0x420610+1)]
		return _0xea36a8
	_0x45571c = _0x420610 % 62
	_0x4e6181 = int(_0x420610 / 62)
	return abcd3(_0x4e6181, _0x1b425f) + _0x1b425f[_0x45571c:(_0x45571c+1)]
##
def abcd4(_0x11dbf0, _0x1558df):
	if abcdx():
		return
	_0x556c7b = list(_0x1558df)
	_0x27312b = len(_0x1558df)
	for _0x107cfb in range(0,len(_0x11dbf0)):
		_0x410c33 = int(_0x11dbf0[_0x107cfb])
		_0x43a652 = _0x556c7b[_0x410c33]
		_0x433a77 = _0x556c7b[_0x27312b - 1 - _0x410c33]
		_0x556c7b[_0x410c33] = _0x433a77
		_0x556c7b[_0x27312b - 1 - _0x410c33] = _0x43a652
	_0x1558df = ''.join(_0x556c7b)
	return _0x1558df
##
def abcdu(_0x92722d):
	#naive = datetime.now()
	#_0x2eb3ad = -480
	#_0x3a4ef4 = naive.utcoffset()
	#_0x58cdae = _0x2eb3ad - _0x3a4ef4
	timeArray = time.strptime(_0x92722d, "%Y-%m-%d %H:%M:%S")
	return time.mktime(timeArray)
##
def abcdx():
	return False

##二次调整顺序
def rejq(jqpram):
	#计算jqParam的ASCII数值
	asc_value = 0
	for i in jqpram:
		asc_value += ord(i)
	# ASCII数值取模jqParam长度
	start_location = asc_value % len(jqpram)
	# 调换顺序
	e = ''
	for j in range(len(jqpram)):
		c = start_location + j
		if c >= len(jqpram):
			c -= len(jqpram)
		e += jqpram[c]
	return e

##获取jqParam参数
def get_jqParam(rndnum, initstime, activityId):
	_0x3098bf = rndnum.split(".")[0]
	_0x4aaf4a = abcd2(int(_0x3098bf),3597397)
	_0x5b9ae2 = initstime
	_0x4eae39 = int(abcdu(_0x5b9ae2.replace("/","-"))) - 28800
	_0x5050a2 = str(_0x4eae39)
	if _0x4eae39 % 10 > 0:
		_0x5050a2 = _0x5050a2[::-1]
	_0xd16fcc = int(_0x5050a2 + "89123")
	_0x149db2 = list(str(_0xd16fcc)+str(_0x4aaf4a))
	_0x1b3de6 = abcd4(_0x149db2, "kgESOLJUbB2fCteoQdYmXvF8j9IZs3K0i6w75VcDnG14WAyaxNqPuRlpTHMrhz")
	_0x3a5cf2 = _0xd16fcc + _0x4aaf4a + int(activityId)
	jqParam = abcd3(_0x3a5cf2, _0x1b3de6)
	return  rejq(jqParam)

##获取jqsign参数
def get_jqsign(jqnonce):
	c=''
	for i in jqnonce:
		a = ord(i)
		b=a^4
		c += chr(b)
	return c

##获取用户登陆cookie
def getcookie(name,passd):
	loginurl = 'https://tyutgs.wjx.cn/user/loginForm.aspx?user_token=RzCs8KPQb4VEfycFVJ8OM9VfMIonoDn8mvZRKvZASDFp4VcCIv5Gml6SfyIestsKb65WsTOr%2f3MaE1Ok2DHEQFUyW2Ob7XXKOQRU4g7TSxFEpwtYN%2bizadoRdU7%2bJrYW&returnUrl=%2fuser%2fqlist.aspx%3fu%3d%25e6%2589%258b%25e6%259c%25ba%25e7%2594%25a8%25e6%2588%25b7tivliw38j0y8djcff6vstq%26userSystem%3d1%26systemId%3d55677040#1'
	logindata = getlogindata(loginurl,name,passd)
	cookie = requests.post(loginurl,data=logindata,headers=headers).headers.get('Set-Cookie')
	cookielist = cookie.split(',')
	cookie = cookielist[0].split(';')[0] +';' + cookielist[2].split(';')[0]
	return cookie

##获取js参数位置
def getflag(script,value):
	flag1 = script.find(value)
	while True:
		flag1 += 1
		if script[flag1]=='=':
			break
	flag2 = flag1
	while True:
		flag2 += 1
		if script[flag2]==';':
			return flag1,flag2

##获取js参数值
def getvalue(script,value):
	flag1,flag2 = getflag(script,value)
	value = ''
	for i in range(flag1,flag2):
		if (script[i]!='=') & (script[i]!=' ') & (script[i]!='"'):
			value += script[i]
	return value

#获取logindata
def getlogindata(loginurl,name,passd):
	argument = {}
	argument['__EVENTTARGET'] = 'btnSubmit'
	argument['__EVENTARGUMENT'] = ''
	argument['__VIEWSTATE'] = ''
	argument['__VIEWSTATEGENERATOR'] = 'EA405E62'
	argument['__EVENTVALIDATION'] = ''
	argument['hideIsPhone'] = ''
	argument['hfQueryCond'] = ''
	argument['hfQuery'] = f'10000|{name}〒30000|{passd}'
	argument['hfPwd'] = '2'
	argument['phoneVal'] = ''
	argument['txtVerifyCode_1'] = ''
	argument['checkCode'] = ''
	argument['hidPhone'] = ''
	argument['password'] = ''
	argument['name'] = ''
	url = loginurl
	text = requests.get(url,headers=headers).text
	soup = BeautifulSoup(text)
	viewstate = soup.find(id='__VIEWSTATE')
	argument['__VIEWSTATE'] = viewstate.get('value')
	eventvalidation = soup.find_all(id='__EVENTVALIDATION')
	argument['__EVENTVALIDATION'] = eventvalidation[0].get('value')
	logindata = parse.urlencode(argument)
	return logindata

##获取问卷链接
def geturl1(cookie):
	urls = 'https://tyutgs.wjx.cn/user/qlist.aspx?u=%e6%89%8b%e6%9c%ba%e7%94%a8%e6%88%b7tivliw38j0y8djcff6vstq&userSystem=1&systemId=55677040'
	headers["Cookie"] = cookie
	text = requests.get(urls,headers=headers).text
	soup = BeautifulSoup(text)
	title = []
	titleend = []
	url1 = []
	for link in soup.find_all('dl'):
		if str(link.span.string).find('疫情')>0:
			title.append(link.span.string)
			url1.append('https://tyutgs.wjx.cn'+link.a.get('href'))
		else:
			titleend.append(link.span.string)
	return title+titleend,url1

##获取问卷提交链接
def geturl2(url1):
	#soup = BeautifulSoup(open("response_body.html"))
	soup = BeautifulSoup(requests.get(url1,headers=headers).text)
	argument = {}
	if soup.find_all('form')[0].get('action'):
		url2 = soup.find_all('form')[0].get('action')
	else:
		return 
	argument['starttime'] = soup.find(id="starttime").get('value')
	scripts = soup.find_all('script')
	script = str(scripts[0])
	activityId = getvalue(script,'activityId')
	activityId = int(activityId)^2130030173
	for script in scripts:
		if script.get('src')==None:
			if str(script.string).find('relusername')>0:
				for name in ['relusername','relts','relsign','relrealname','reldept','relext','rndnum','jqnonce']:
					argument[name] = getvalue(str(script.string),name)
				break
			else:
				continue
	argument['jqpram'] = get_jqParam(argument['rndnum'],argument['starttime'],activityId)
	argument['t'] = str(int(argument['relts'])*1000+12953)
	argument['jqsign'] = get_jqsign(argument['jqnonce'])
	argument['rn'] = argument.pop('rndnum')
	url2 = url2+'&hmt=1&mst=34284&vpsiu=1&source=directphone&submittype=1&ktimes=4&hlv=1&iwx=1'+'&'+parse.urlencode(argument)
	#print(url2)
	urlqiniu = 'https://tyutgs.wjx.cn/joinnew/GetQiniuToken.ashx?ms=4096&q=3&activity='+str(activityId)
	return url2,urlqiniu

#
def getqiniu(url):
	text = requests.get(url,headers=headers).text
	# data = ''+text+''
	# headertemp = headers
	# headertemp['Content-Type']='multipart/form-data; boundary=----WebKitFormBoundarynnZ6k0ln5GTF1FtP'
	# text = requests.get(url,headers=headertemp).text
	return text

##获取企业微信tokem
def gettoken():
	corpid='??????'
	corpsecret='??????'
	access_token_url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}'
	reg = requests.get(url=access_token_url)
	return json.loads(reg.text)['access_token']

##调用企业微信发送通知
def send(access_token,user,text):
	agentid=1000003
	send_msg_url = f'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}'
	send_msg = {
				"touser": user,
	            "msgtype": "text",
	            "agentid": agentid,
	            "text": {
	                "content": text,
	            },
	        }
	requests.post(send_msg_url, data=json.dumps(send_msg))

##用户填写问卷
def whoup(who,token):
	submitdata = {'明向':'submitdata=1%241%7D2%24%E5%B1%B1%E8%A5%BF%E7%9C%81%E6%99%8B%E4%B8%AD%E5%B8%82%E6%A6%86%E6%AC%A1%E5%8C%BA%E4%B9%8C%E9%87%91%E5%B1%B1%E9%95%87%E6%98%8E%E5%90%91%E5%A4%A7%E9%81%93%E5%A4%AA%E5%8E%9F%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6%E6%98%8E%E5%90%91%E6%A0%A1%E5%8C%BA%5B112.72173%2C37.746074%5D%7D3%24','虎峪':'submitdata=1%241%7D2%24%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%AA%E5%8E%9F%E5%B8%82%E4%B8%87%E6%9F%8F%E6%9E%97%E5%8C%BA%E4%B8%8B%E5%85%83%E8%A1%97%E9%81%93%E6%89%BF%E8%96%AA%E4%B8%AD%E8%B7%AF%E5%A4%AA%E5%8E%9F%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6%E8%99%8E%E5%B3%AA%E6%A0%A1%E5%8C%BA%5B112.526249%2C37.854154%5D%7D3%24','迎西':'submitdata=1%241%7D2%24%E5%B1%B1%E8%A5%BF%E7%9C%81%E5%A4%AA%E5%8E%9F%E5%B8%82%E4%B8%87%E6%9F%8F%E6%9E%97%E5%8C%BA%E5%8D%83%E5%B3%B0%E8%A1%97%E9%81%93%E5%AE%97%E5%A4%8D%E8%B7%AF%E5%A4%AA%E5%8E%9F%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6%E8%BF%8E%E8%A5%BF%E6%A0%A1%E5%8C%BA%5B112.52244%2C37.860976%5D%7D3%24'}
	cookie = getcookie(namenum[who],passwd[who])
	titletemp,url1temp = geturl1(cookie)
	retext = ''
	success = 0
	for i in range(len(url1temp)):
		#print(titletemp[i])
		if geturl2(url1temp[i]):
			url2temp,urlqiniutemp = geturl2(url1temp[i])
			#print(url2temp)
		else:
			continue
		keyqiniutemp = getqiniu(urlqiniutemp)
		#print(keyqiniutemp)
		qiniu = keyqiniutemp.split('〒')[1]
		d = ''
		for j in range(6):
			b="ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
			c=len(b)
			charat = int(c*random.random())
			d+=b[charat]
		key = qiniu+str(int(time.time()))+d+'.jpg%252C8355%252Cmmexport1667907033737.jpg%7D4%241%7C5%7D5%241%7D6%243%7D7%241'
		submitdata[xq]+=key
		text = requests.post(url2temp,data=submitdata[xq],headers=headers).text
		#print(text)
		if text.find('complete')>0:
			success += 1
			retext += '\n✅'+titletemp[i]
		elif text.find('验证')>0:
			retext += '\n❎需要验证❎'+titletemp[i]+'\n'+text
		else:
			retext += '\n❎'+titletemp[i]+'\n'+text
	retext = '共'+str(len(titletemp))+'个问卷，已填'+str(success)+'个'+retext
	print(retext)
	if ts=='on':
		send(token,who,retext)

##入口
if __name__ == '__main__':
	if ts == 'on':
		token = gettoken()
	else:
		token = 'token'
	whoup('zs',token)
	#whoup('ls',token)
