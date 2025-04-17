# Content from: https://www.drissionpage.cn/SessionPage/session_opt

[跳到主要内容](https://www.drissionpage.cn/SessionPage/session_opt#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/session_opt)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/session_opt)
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
  * 🛩️ 启动配置


本页总览
# 🛩️ 启动配置
我们用`SessionOptions`对象管理`SessionPage`对象初始配置。
注意
`SessionOptions`仅用于管理启动配置，程序启动后再修改无效。
## ✅️️ 创建对象[​](https://www.drissionpage.cn/SessionPage/session_opt#️️-创建对象 "✅️️ 创建对象的直接链接")
### 📌 导入[​](https://www.drissionpage.cn/SessionPage/session_opt#-导入 "📌 导入的直接链接")
```
from DrissionPage import SessionOptions
```

### 📌 初始化参数[​](https://www.drissionpage.cn/SessionPage/session_opt#-初始化参数 "📌 初始化参数的直接链接")
`SessionOptions`对象用于管理`Session`对象的初始化配置。可从配置文件中读取配置来进行初始化。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`read_file`| `bool`| `True`| 是否从 ini 文件中读取配置信息，为`False`则用默认配置创建  
`ini_path`| `Path``str`| `None`| 指定 ini 文件路径，为`None`则读取内置 ini 文件  
创建配置对象：
```
from DrissionPage import SessionOptionsso = SessionOptions()
```

默认情况下，`SessionOptions`对象会从 ini 文件中读取配置信息，当指定`read_file`参数为`False`时，则以默认配置创建。
提醒
对象创建时已带有默认 headers，如要清除，可调用`clear_headers()`方法。
## ✅️️ 使用方法[​](https://www.drissionpage.cn/SessionPage/session_opt#️️-使用方法 "✅️️ 使用方法的直接链接")
创建配置对象后，可调整配置内容，然后在页面对象创建时以参数形式把配置对象传递进去。
```
from DrissionPage import SessionPage, SessionOptions# 创建配置对象（默认从 ini 文件中读取配置）so = SessionOptions()# 设置代理so.set_proxies('http://localhost:1080')# 设置 cookiescookies =['key1=val1; domain=****','key2=val2; domain=****']so.set_cookies(cookies)# 以该配置创建页面对象page = SessionPage(session_or_options=so)
```

## ✅️️ 用于设置的方法[​](https://www.drissionpage.cn/SessionPage/session_opt#️️-用于设置的方法 "✅️️ 用于设置的方法的直接链接")
### 📌 `set_headers()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_headers "-set_headers的直接链接")
该方法用于设置整个 headers 参数，传入值会覆盖原来的 headers。
headers 可以是`dict`格式的，也可以是文本格式。
文本格式不同字段用`\n`分隔，字段 key 和 value 用`': '`分隔，即从浏览器直接复制的格式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`headers`| `dict``str`| 必填| headers 信息  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
**示例：**
```
so.set_headers ={'user-agent':'Mozilla/5.0 (Macint...','connection':'keep-alive'...}
```

### 📌 `set_a_header()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_a_header "-set_a_header的直接链接")
该方法用于设置`headers`中的一个项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 设置名称  
`value`| `str`| 必填| 设置值  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
**示例：**
```
so.set_a_header('accept','text/html')so.set_a_header('Accept-Charset','GB2312')
```

**输出：**
```
{'accept': 'text/html', 'accept-charset': 'GB2312'}
```

### 📌 `remove_a_header()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-remove_a_header "-remove_a_header的直接链接")
此方法用于从`headers`中移除一个设置项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 要删除的设置  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
**示例：**
```
so.remove_a_header('accept')
```

### 📌 `clear_headers()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-clear_headers "-clear_headers的直接链接")
此方法用于清空已设置的`headers`参数。
**参数：** 无
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象自身  
### 📌 `set_cookies()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_cookies "-set_cookies的直接链接")
此方法用于设置一个或多个 cookie，每次设置会覆盖之前所有 cookies 信息。
详细用法见实用教程相关章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cookies`| `Cookie``CookieJar``list``tuple``str``dict`| 必填| cookies  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
**示例：**
```
cookies =['key1=val1; domain=****','key2=val2; domain=****']so.set_cookies(cookies)
```

### 📌 `set_timeout()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_timeout "-set_timeout的直接链接")
此方法用于设置连接超时属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 连接等待秒数  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_retry()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_retry "-set_retry的直接链接")
此方法用于设置页面连接超时时的重试次数和间隔。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| `None`| 连接失败重试次数  
`interval`| `float`| `None`| 连接失败重试间隔（秒）  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `retry_times`[​](https://www.drissionpage.cn/SessionPage/session_opt#-retry_times "-retry_times的直接链接")
该属性返回连接失败时的重试次数。
**类型：**`int`
### 📌 `retry_interval`[​](https://www.drissionpage.cn/SessionPage/session_opt#-retry_interval "-retry_interval的直接链接")
该属性返回连接失败时的重试间隔（秒）。
**类型：**`float`
### 📌 `set_proxies()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_proxies "-set_proxies的直接链接")
此方法用于设置代理信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`http`| `str`| `None`| http 代理地址  
`https`| `str`| `None`| https 代理地址  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
**示例：**
```
so.set_proxies('http://127.0.0.1:1080')
```

### 📌 `set_download_path()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_download_path "-set_download_path的直接链接")
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 默认下载保存路径  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_auth()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_auth "-set_auth的直接链接")
此方法用于设置认证元组信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`auth`| `tuple``HTTPBasicAuth`| 必填| 认证元组或对象  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_hooks()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_hooks "-set_hooks的直接链接")
此方法用于设置回调方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`hooks`| `dict`| 必填| 回调方法  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_params()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_params "-set_params的直接链接")
此方法用于设置查询参数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`params`| `dict`| 必填| 查询参数字典  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_cert()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_cert "-set_cert的直接链接")
此方法用于设置 SSL 客户端证书文件的路径（.pem格式），或 ('cert', 'key') 元组。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cert`| `str``tuple`| 必填| 证书路径或元组  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_verify()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_verify "-set_verify的直接链接")
此方法用于设置是否验证SSL证书。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `add_adapter()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-add_adapter "-add_adapter的直接链接")
此方法用于添加适配器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| 必填| 适配器对应 url  
`adapter`| `HTTPAdapter`| 必填| 适配器对象  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_stream()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_stream "-set_stream的直接链接")
此方法用于设置是否使用流式响应内容。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_trust_env()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_trust_env "-set_trust_env的直接链接")
此方法用于设置是否信任环境。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
### 📌 `set_max_redirects()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-set_max_redirects "-set_max_redirects的直接链接")
此方法用于设置最大重定向次数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| 必填| 最大重定向次数  
返回类型| 说明  
---|---  
`SessionOptions`| 配置对象本身  
## ✅️️ 保存设置到文件[​](https://www.drissionpage.cn/SessionPage/session_opt#️️-保存设置到文件 "✅️️ 保存设置到文件的直接链接")
您可以把不同的配置保存到各自的 ini 文件，以便适应不同的场景。
注意
`hooks`和`adapters`配置是不会保存到文件中的。
### 📌 `save()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-save "-save的直接链接")
此方法用于保存配置项到一个 ini 文件。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| ini 文件的路径， 传入`None`保存到当前读取的配置文件  
返回类型| 说明  
---|---  
`str`| 保存的 ini 文件绝对路径  
**示例：**
```
# 保存当前读取的ini文件so.save()# 把当前配置保存到指定的路径so.save(path=r'D:\tmp\settings.ini')
```

### 📌 `save_to_default()`[​](https://www.drissionpage.cn/SessionPage/session_opt#-save_to_default "-save_to_default的直接链接")
此方法用于保存配置项到固定的默认 ini 文件。默认 ini 文件是指随 DrissionPage 内置的那个。
**参数：** 无
返回类型| 说明  
---|---  
`str`| 保存的 ini 文件绝对路径  
**示例：**
```
so.save_to_default()
```

## ✅️️ `SessionOptions`属性[​](https://www.drissionpage.cn/SessionPage/session_opt#️️-sessionoptions属性 "️️-sessionoptions属性的直接链接")
### 📌 `headers`[​](https://www.drissionpage.cn/SessionPage/session_opt#-headers "-headers的直接链接")
该属性返回 headers 设置信息。
**类型：**`dict`
### 📌 `cookies`[​](https://www.drissionpage.cn/SessionPage/session_opt#-cookies "-cookies的直接链接")
此属性以`list`方式返回 cookies 设置信息。
**类型：**`list`
### 📌 `proxies`[​](https://www.drissionpage.cn/SessionPage/session_opt#-proxies "-proxies的直接链接")
此属性返回代理信息。
**类型：**`dict` **格式：**`{'http': 'http://**.**.**.**:****', 'https': 'http://**.**.**.**:****'}`
### 📌 `auth`[​](https://www.drissionpage.cn/SessionPage/session_opt#-auth "-auth的直接链接")
此属性返回认证设置。
**类型：**`tuple` 、`HTTPBasicAuth`
### 📌 `hooks`[​](https://www.drissionpage.cn/SessionPage/session_opt#-hooks "-hooks的直接链接")
此属性返回回调方法设置。
**类型：**`dict`
### 📌 `params`[​](https://www.drissionpage.cn/SessionPage/session_opt#-params "-params的直接链接")
此属性返回查询参数设置。
**类型：**`dict`
### 📌 `verify`[​](https://www.drissionpage.cn/SessionPage/session_opt#-verify "-verify的直接链接")
此属性返回是否验证 SSL 证书设置。
**类型：**`bool`
### 📌 `cert`[​](https://www.drissionpage.cn/SessionPage/session_opt#-cert "-cert的直接链接")
此属性返回 SSL 证书设置。
**类型：**`str` 、`tuple`
### 📌 `adapters`[​](https://www.drissionpage.cn/SessionPage/session_opt#-adapters "-adapters的直接链接")
此属性返回适配器设置。
**类型：**`List[HTTPAdapter]`
### 📌 `stream`[​](https://www.drissionpage.cn/SessionPage/session_opt#-stream "-stream的直接链接")
此属性返回是否使用流式响应设置。
**类型：**`bool`
### 📌 `trust_env`[​](https://www.drissionpage.cn/SessionPage/session_opt#-trust_env "-trust_env的直接链接")
此属性返回是否信任环境设置。
**类型：**`bool`
### 📌 `max_redirects`[​](https://www.drissionpage.cn/SessionPage/session_opt#-max_redirects "-max_redirects的直接链接")
此属性返回`max_redirects`设置。
**类型：**`int`
### 📌 `timeout`[​](https://www.drissionpage.cn/SessionPage/session_opt#-timeout "-timeout的直接链接")
此属性返回连接超时设置。
**类型：**`int` 、`float`
### 📌 `download_path`[​](https://www.drissionpage.cn/SessionPage/session_opt#-download_path "-download_path的直接链接")
此属性返回默认下载路径设置。
**类型：**`str`
[ 上一页🛩️ 页面设置](https://www.drissionpage.cn/SessionPage/settings)[下一页⤵️ 概述](https://www.drissionpage.cn/download/intro)
  * [✅️️ 创建对象](https://www.drissionpage.cn/SessionPage/session_opt#️️-创建对象)
    * [📌 导入](https://www.drissionpage.cn/SessionPage/session_opt#-导入)
    * [📌 初始化参数](https://www.drissionpage.cn/SessionPage/session_opt#-初始化参数)
  * [✅️️ 使用方法](https://www.drissionpage.cn/SessionPage/session_opt#️️-使用方法)
  * [✅️️ 用于设置的方法](https://www.drissionpage.cn/SessionPage/session_opt#️️-用于设置的方法)
    * [📌 `set_headers()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_headers)
    * [📌 `set_a_header()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_a_header)
    * [📌 `remove_a_header()`](https://www.drissionpage.cn/SessionPage/session_opt#-remove_a_header)
    * [📌 `clear_headers()`](https://www.drissionpage.cn/SessionPage/session_opt#-clear_headers)
    * [📌 `set_cookies()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_cookies)
    * [📌 `set_timeout()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_timeout)
    * [📌 `set_retry()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_retry)
    * [📌 `retry_times`](https://www.drissionpage.cn/SessionPage/session_opt#-retry_times)
    * [📌 `retry_interval`](https://www.drissionpage.cn/SessionPage/session_opt#-retry_interval)
    * [📌 `set_proxies()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_proxies)
    * [📌 `set_download_path()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_download_path)
    * [📌 `set_auth()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_auth)
    * [📌 `set_hooks()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_hooks)
    * [📌 `set_params()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_params)
    * [📌 `set_cert()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_cert)
    * [📌 `set_verify()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_verify)
    * [📌 `add_adapter()`](https://www.drissionpage.cn/SessionPage/session_opt#-add_adapter)
    * [📌 `set_stream()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_stream)
    * [📌 `set_trust_env()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_trust_env)
    * [📌 `set_max_redirects()`](https://www.drissionpage.cn/SessionPage/session_opt#-set_max_redirects)
  * [✅️️ 保存设置到文件](https://www.drissionpage.cn/SessionPage/session_opt#️️-保存设置到文件)
    * [📌 `save()`](https://www.drissionpage.cn/SessionPage/session_opt#-save)
    * [📌 `save_to_default()`](https://www.drissionpage.cn/SessionPage/session_opt#-save_to_default)
  * [✅️️ `SessionOptions`属性](https://www.drissionpage.cn/SessionPage/session_opt#️️-sessionoptions属性)
    * [📌 `headers`](https://www.drissionpage.cn/SessionPage/session_opt#-headers)
    * [📌 `cookies`](https://www.drissionpage.cn/SessionPage/session_opt#-cookies)
    * [📌 `proxies`](https://www.drissionpage.cn/SessionPage/session_opt#-proxies)
    * [📌 `auth`](https://www.drissionpage.cn/SessionPage/session_opt#-auth)
    * [📌 `hooks`](https://www.drissionpage.cn/SessionPage/session_opt#-hooks)
    * [📌 `params`](https://www.drissionpage.cn/SessionPage/session_opt#-params)
    * [📌 `verify`](https://www.drissionpage.cn/SessionPage/session_opt#-verify)
    * [📌 `cert`](https://www.drissionpage.cn/SessionPage/session_opt#-cert)
    * [📌 `adapters`](https://www.drissionpage.cn/SessionPage/session_opt#-adapters)
    * [📌 `stream`](https://www.drissionpage.cn/SessionPage/session_opt#-stream)
    * [📌 `trust_env`](https://www.drissionpage.cn/SessionPage/session_opt#-trust_env)
    * [📌 `max_redirects`](https://www.drissionpage.cn/SessionPage/session_opt#-max_redirects)
    * [📌 `timeout`](https://www.drissionpage.cn/SessionPage/session_opt#-timeout)
    * [📌 `download_path`](https://www.drissionpage.cn/SessionPage/session_opt#-download_path)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/session_opt)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/session_opt)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
