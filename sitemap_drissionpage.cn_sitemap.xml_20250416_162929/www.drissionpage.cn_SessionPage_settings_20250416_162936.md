# Content from: https://www.drissionpage.cn/SessionPage/settings

[跳到主要内容](https://www.drissionpage.cn/SessionPage/settings#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/settings)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/settings)
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
  * 🛩️ 页面设置


本页总览
# 🛩️ 页面设置
本节介绍`SessionPage`运行参数设置。
这些设置是全局参数，设置后每次请求都会使用它们。
**示例：**
```
from DrissionPage import SessionPagepage = SessionPage()page.set.cookies([{'name':'a','value':'1'},{'name':'b','value':'2'}])
```

## ✅️️ `set.retry_times()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setretry_times "️️-setretry_times的直接链接")
此方法用于设置连接失败时重连次数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| 必填| 次数  
**返回：**`None`
## ✅️️ `set.retry_interval()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setretry_interval "️️-setretry_interval的直接链接")
此方法用于设置连接失败时重连间隔。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`interval`| `float`| 必填| 秒数  
**返回：**`None`
## ✅️️ `set.timeout()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-settimeout "️️-settimeout的直接链接")
此方法用于设置连接超时时间（秒）。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 秒数  
**返回：**`None`
**示例：**
```
page.set.timeout(20)
```

## ✅️️ `set.encoding()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setencoding "️️-setencoding的直接链接")
此方法用于设置网页编码。
默认情况下，程序会自动从 headers、页面上获取编码，但总有些奇葩网页的编码不准确。这时候可以主动设置编码。
可以针对已获取的`Rsponse`对象设置，或作为整体设置对之后的连接都有效。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`encoding`| `str`| 必填| 编码名称，如果要取消之前的设置，传入`None`  
`set_all`| `bool`| `True`| 是否设置对象参数，为`False`则只设置当前`Response`对象  
**返回：**`None`
## ✅️️ `set.cookies()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setcookies "️️-setcookies的直接链接")
此方法用于设置一个或多个 cookie。
设置一个 cookie 支持的格式：
  * `Cookie`：单个`Cookie`对象
  * `str`：`'name=value; domain=****; ...'`或`'name=****; value=****; domain=****; ...'`格式，只支持用`';'`分隔
  * `dict`：`{'name': '****', 'value': '****', 'domain': '****', ...}`或`{name: value, 'domain': '****', ...}`格式


设置多个 cookie 支持的格式：
  * `list`或`tuple`：上面几种形式的单个 cookie 放到列表中传入即可
  * `dict`：`{name1: value1, name2: value2, ..., 'domain': '****', ...}`格式
  * `str`：`'name1=value1; name2=value2; ... domain=****; ...'`格式，多个 cookie 之间只能用`';'`分隔
  * `CookieJar`：单个`CookieJar`对象

参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cookies`| `Cookie``CookieJar``list``tuple``str``dict`| 必填| cookies 信息  
**返回：**`None`
## ✅️️ `set.cookies.clear()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setcookiesclear "️️-setcookiesclear的直接链接")
此方法用于清除所有 cookie。
**参数：** 无
**返回：**`None`
## ✅️️ `set.cookies.remove()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setcookiesremove "️️-setcookiesremove的直接链接")
此方法用于删除一个 cookie。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| cookie 的 name 字段  
**返回：**`None`
## ✅️️ `set.headers()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setheaders "️️-setheaders的直接链接")
此方法用于设置 headers，会取代已有 headers。
headers 可以是`dict`格式的，也可以是文本格式。
文本格式不同字段用`\n`分隔，字段 key 和 value 用`': '`分隔，即从浏览器直接复制的格式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`headers`| `dict``str`| 必填| headers 信息  
**返回：**`None`
## ✅️️ `set.header()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setheader "️️-setheader的直接链接")
此方法用于设置 headers 中一个项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 设置名称  
`value`| `str`| 必填| 设置值  
**返回：**`None`
## ✅️️ `set.user_agent()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setuser_agent "️️-setuser_agent的直接链接")
此方法用于设置 user_agent。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`ua`| `str`| 必填| user_agent 信息  
**返回：**`None`
## ✅️️ `set.proxies()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setproxies "️️-setproxies的直接链接")
此方法用于设置代理 ip。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`http`| `str`| `None`| http 代理地址  
`https`| `str`| `None`| https 代理地址  
**返回：**`None`
## ✅️️ `set.auth()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setauth "️️-setauth的直接链接")
此方法用于设置认证元组或对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`auth`| `Tuple[str, str]``HTTPBasicAuth`| 必填| 认证元组或对象  
**返回：**`None`
## ✅️️ `set.hooks()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-sethooks "️️-sethooks的直接链接")
此方法用于设置回调方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`hooks`| `dict`| 必填| 回调方法  
**返回：**`None`
## ✅️️ `set.params()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setparams "️️-setparams的直接链接")
此方法用于设置查询参数字典。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`params`| `dict`| 必填| 查询参数字典  
**返回：**`None`
## ✅️️ `set.verify()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setverify "️️-setverify的直接链接")
此方法用于设置是否验证SSL证书。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
**返回：**`None`
## ✅️️ `set.cert()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setcert "️️-setcert的直接链接")
此方法用于设置SSL客户端证书。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cert`| `str``Tuple[str, str]`| 必填| SSL客户端证书文件的路径(.pem格式)，或(‘cert’, ‘key’)元组  
**返回：**`None`
## ✅️️ `set.stream()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setstream "️️-setstream的直接链接")
此方法用于设置是否使用流式响应内容。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
**返回：**`None`
## ✅️️ `set.trust_env()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-settrust_env "️️-settrust_env的直接链�接")
此方法用于设置是否信任环境。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| 必填| `bool`表示开或关  
**返回：**`None`
## ✅️️ `set.max_redirects()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setmax_redirects "️️-setmax_redirects的直接链接")
此方法用于设置连接最大重定向次数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
``times| `int`| 必填| 最大重定向次数  
**返回：**`None`
## ✅️️ `set.add_adapter()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-setadd_adapter "️️-setadd_adapter的直接链接")
此方法用于添加适配器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| 必填| 适配器对应url  
`adapter`| `HTTPAdapter`| 必填| 适配器对象  
**返回：**`None`
## ✅️️ `close()`[​](https://www.drissionpage.cn/SessionPage/settings#️️-close "️️-close的直接链接")
此方法用于关闭连接。
**参数：** 无
**返回：**`None`
[上一页🛩️ 获取元素信息](https://www.drissionpage.cn/SessionPage/get_ele_info)[下一页🛩️ 启动配置](https://www.drissionpage.cn/SessionPage/session_opt)
  * [✅️️ `set.retry_times()`](https://www.drissionpage.cn/SessionPage/settings#️️-setretry_times)
  * [✅️️ `set.retry_interval()`](https://www.drissionpage.cn/SessionPage/settings#️️-setretry_interval)
  * [✅️️ `set.timeout()`](https://www.drissionpage.cn/SessionPage/settings#️️-settimeout)
  * [✅️️ `set.encoding()`](https://www.drissionpage.cn/SessionPage/settings#️️-setencoding)
  * [✅️️ `set.cookies()`](https://www.drissionpage.cn/SessionPage/settings#️️-setcookies)
  * [✅️️ `set.cookies.clear()`](https://www.drissionpage.cn/SessionPage/settings#️️-setcookiesclear)
  * [✅️️ `set.cookies.remove()`](https://www.drissionpage.cn/SessionPage/settings#️️-setcookiesremove)
  * [✅️️ `set.headers()`](https://www.drissionpage.cn/SessionPage/settings#️️-setheaders)
  * [✅️️ `set.header()`](https://www.drissionpage.cn/SessionPage/settings#️️-setheader)
  * [✅️️ `set.user_agent()`](https://www.drissionpage.cn/SessionPage/settings#️️-setuser_agent)
  * [✅️️ `set.proxies()`](https://www.drissionpage.cn/SessionPage/settings#️️-setproxies)
  * [✅️️ `set.auth()`](https://www.drissionpage.cn/SessionPage/settings#️️-setauth)
  * [✅️️ `set.hooks()`](https://www.drissionpage.cn/SessionPage/settings#️️-sethooks)
  * [✅️️ `set.params()`](https://www.drissionpage.cn/SessionPage/settings#️️-setparams)
  * [✅️️ `set.verify()`](https://www.drissionpage.cn/SessionPage/settings#️️-setverify)
  * [✅️️ `set.cert()`](https://www.drissionpage.cn/SessionPage/settings#️️-setcert)
  * [✅️️ `set.stream()`](https://www.drissionpage.cn/SessionPage/settings#️️-setstream)
  * [✅️️ `set.trust_env()`](https://www.drissionpage.cn/SessionPage/settings#️️-settrust_env)
  * [✅️️ `set.max_redirects()`](https://www.drissionpage.cn/SessionPage/settings#️️-setmax_redirects)
  * [✅️️ `set.add_adapter()`](https://www.drissionpage.cn/SessionPage/settings#️️-setadd_adapter)
  * [✅️️ `close()`](https://www.drissionpage.cn/SessionPage/settings#️️-close)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/settings)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/settings)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
