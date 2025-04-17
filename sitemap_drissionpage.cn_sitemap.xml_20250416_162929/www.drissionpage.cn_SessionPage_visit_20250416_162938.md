# Content from: https://www.drissionpage.cn/SessionPage/visit

[跳到主要内容](https://www.drissionpage.cn/SessionPage/visit#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/visit)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/visit)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 概述](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 创建页面对象](https://www.drissionpage.cn/SessionPage/create_obj)
    * [🛩️ 访问网页](https://www.drissionpage.cn/SessionPage/visit)
    * [🛩️ 获取页面信息](https://www.drissionpage.cn/SessionPage/get_page_info)
    * [🛩️ 查找元素](https://www.drissionpage.cn/SessionPage/get_ele)
    * [🛩️ 获取元素信息](https://www.drissionpage.cn/SessionPage/get_ele_info)
    * [🛩️ 页面设置](https://www.drissionpage.cn/SessionPage/settings)
    * [🛩️ 启动配置](https://www.drissionpage.cn/SessionPage/session_opt)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)


  * [](https://www.drissionpage.cn/)
  * 🛫 SessionPage
  * 🛩️ 访问网页


本页总览
# 🛩️ 访问网页
`SessionPage`基于 requests 进行网络连接，因此可使用 requests 内置的所有请求方式，包括`get()`、`post()`、`head()`、`options()`、`put()`、`patch()`、`delete()`。
不过本库目前只对`get()`和`post()`做了封装和优化，其余方式可通过调用页面对象内置的`Session`对象使用。
## ✅️️ `get()`[​](https://www.drissionpage.cn/SessionPage/visit#️️-get "️️-get的直接链接")
此方法用于以 GET 方式请求页面。
### 📌 访问在线网页[​](https://www.drissionpage.cn/SessionPage/visit#-访问在线网页 "📌 访问在线网页的直接链接")
`get()`方法语法与 requests 的`get()`方法一致，在此基础上增加了连接失败重试功能。
与 requests 不一样的是，它不返回`Response`对象，而是从`SessionPae`对象的`html`等属性读取结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| 必填| 目标 url，可指向本地文件路径  
`show_errmsg`| `bool`| `False`| 连接出错时是否显示和抛出异常  
`retry`| `int`| `None`| 重试次数，为`None`时使用页面参数，默认`3`  
`interval`| `float`| `None`| 重试间隔（秒），为`None`时使用页面参数，默认`2`  
`timeout`| `float`| `None`| 加载超时时间（秒）  
`params`| `dict`| `None`| url 请求参数  
`data`| `dict``str`| `None`| 携带的数据  
`json`| `dict``str`| `None`| 要发送的 JSON 数据，会自动设置 Content-Type 为`'application/json'`  
`headers`| `dict`| `None`| 请求头  
`cookies`| `dict``CookieJar`| `None`| cookies 信息  
`files`| `Any`| `None`| 要上传的文件，可以是一个字典，其中键是文件名，值是文件对象或文件路径  
`auth`| `Any`| `None`| 身份认证信息  
`allow_redirects`| `bool`| `True`| 是否允许重定向  
`proxies`| `dict`| `None`| 代理信息  
`hooks`| `Any`| `None`| 回调方法  
`stream`| `bool`| `None`| 是否使用流式传输  
`verify`| `bool``str`| `None`| 是否验证 SSL 证书  
`cert`| `str``Tuple[str, str]`| `None`| SSL 客户端证书文件的路径(.pem 格式)，或('cert', 'key')元组  
返回类型| 说明  
---|---  
`bool`| 是否连接成功  
说明
`**kwargs`参数与 requests 中该参数使用方法一致，但有一个特点，如果该参数中设置了某一项（如`headers`），该项中的每个项会覆盖从配置中读取的同名项，而不会整个覆盖。 就是说，如果想继续使用配置中的`headers`信息，而只想修改其中一项，只需要传入该项的值即可。这样可以简化代码逻辑。
程序会根据要访问的网址自动在`headers`中加入`Host`和`Referer`项
程序会自动从返回内容中确定编码，一般情况无需手动设置
普通访问网页：
```
from DrissionPage import SessionPagepage = SessionPage()page.get('http://g1879.gitee.io/drissionpage')
```

使用连接参数访问网页：
```
from DrissionPage import SessionPagepage = SessionPage()url ='https://www.baidu.com'headers ={'referer':'gitee.com'}cookies ={'name':'value'}proxies ={'http':'127.0.0.1:1080','https':'127.0.0.1:1080'}page.get(url, headers=headers, cookies=cookies, proxies=proxies)
```

### 📌 读取本地文件[​](https://www.drissionpage.cn/SessionPage/visit#-读取本地文件 "📌 读取本地文件的直接链接")
`get()`的`url`参数可指向本地文件，实现本地 html 解析。
```
from DrissionPage import SessionPagepage = SessionPage()page.get(r'D:\demo.html')
```

## ✅️️ `post()`[​](https://www.drissionpage.cn/SessionPage/visit#️️-post "️️-post的直接链接")
此方法是用 POST 方式请求页面。用法与`get()`一致。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| 必填| 目标 url，可指向本地文件路径  
`show_errmsg`| `bool`| `False`| 连接出错时是否显示和抛出异常  
`retry`| `int`| `None`| 重试次数，为`None`时使用页面参数，默认`3`  
`interval`| `float`| `None`| 重试间隔（秒），为`None`时使用页面参数，默认`2`  
`timeout`| `float`| `None`| 加载超时时间（秒）  
`params`| `dict`| `None`| url 请求参数  
`data`| `dict``str`| `None`| 携带的数据  
`json`| `dict``str`| `None`| 要发送的 JSON 数据，会自动设置 Content-Type 为`'application/json'`  
`headers`| `dict`| `None`| 请求头  
`cookies`| `dict``CookieJar`| `None`| cookies 信息  
`files`| `Any`| `None`| 要上传的文件，可以是一个字典，其中键是文件名，值是文件对象或文件路径  
`auth`| `Any`| `None`| 身份认证信息  
`allow_redirects`| `bool`| `True`| 是否允许重定向  
`proxies`| `dict`| `None`| 代理信息  
`hooks`| `Any`| `None`| 回调方法  
`stream`| `bool`| `None`| 是否使用流式传输  
`verify`| `bool``str`| `None`| 是否验证 SSL 证书  
`cert`| `str``Tuple[str, str]`| `None`| SSL 客户端证书文件的路径(.pem 格式)，或('cert', 'key')元组  
返回类型| 说明  
---|---  
`bool`| 是否连接成功  
```
from DrissionPage import SessionPagepage = SessionPage()data ={'username':'****','pwd':'****'}page.post('http://example.com', data=data)# 或page.post('http://example.com', json=data)
```

`data`参数和`json`参数都可接收`str`和`dict`格式数据，即有以下 4 种传递数据的方式：
```
# 向 data 参数传入字符串page.post(url, data='abc=123')# 向 data 参数传入字典page.post(url, data={'abc':'123'})# 向 json 参数传入字符串page.post(url, json='abc=123')# 向 json 参数传入字典page.post(url, json={'abc':'123'})
```

具体使用哪种，按服务器要求而定。
## ✅️️ 其它请求方式[​](https://www.drissionpage.cn/SessionPage/visit#️️-其它请求方式 "✅️️ 其它请求方式的直接链接")
本库只针对常用的 GET 和 POST 方式作了优化，但也可以通过提取页面对象内的`Session`对象以原生 requests 代码方式执行其它请求方式。
```
from DrissionPage import SessionPagepage = SessionPage()# 获取内置的 Session 对象session = page.session# 以 head 方式发送请求response = session.head('https://www.baidu.com')print(response.headers)
```

**输出：**
```
{'Accept-Ranges': 'bytes', 'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Length': '277', 'Content-Type': 'text/html', 'Date': 'Tue, 04 Jan 2022 06:49:18 GMT', 'Etag': '"575e1f72-115"', 'Last-Modified': 'Mon, 13 Jun 2016 02:50:26 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18'}
```

[上一页🛩️ 创建页面对象](https://www.drissionpage.cn/SessionPage/create_obj)[下一页🛩️ 获取页面信息](https://www.drissionpage.cn/SessionPage/get_page_info)
  * [✅️️ `get()`](https://www.drissionpage.cn/SessionPage/visit#️️-get)
    * [📌 访问在线网页](https://www.drissionpage.cn/SessionPage/visit#-访问在线网页)
    * [📌 读取本地文件](https://www.drissionpage.cn/SessionPage/visit#-读取本地文件)
  * [✅️️ `post()`](https://www.drissionpage.cn/SessionPage/visit#️️-post)
  * [✅️️ 其它请求方式](https://www.drissionpage.cn/SessionPage/visit#️️-其它请求方式)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/visit)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/visit)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
