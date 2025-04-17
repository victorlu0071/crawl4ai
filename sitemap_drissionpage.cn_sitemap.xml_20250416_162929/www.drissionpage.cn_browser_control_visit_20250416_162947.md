# Content from: https://www.drissionpage.cn/browser_control/visit

[跳到主要内容](https://www.drissionpage.cn/browser_control/visit#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/visit)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/visit)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 元素交互](https://www.drissionpage.cn/browser_control/ele_operation)
    * [🛰️ 获取元素信息](https://www.drissionpage.cn/browser_control/get_ele_info)
    * [🛰️ iframe 操作](https://www.drissionpage.cn/browser_control/iframe)
    * [🛰️ 动作链](https://www.drissionpage.cn/browser_control/actions)
    * [🛰️ 模式切换](https://www.drissionpage.cn/browser_control/mode_change)
    * [🛰️ 等待](https://www.drissionpage.cn/browser_control/waiting)
    * [🛰️ 监听网络数据](https://www.drissionpage.cn/browser_control/listener)
    * [🛰️ 获取控制台信息](https://www.drissionpage.cn/browser_control/console)
    * [🛰️ 截图和录像](https://www.drissionpage.cn/browser_control/screen)
    * [🛰️ 上传文件](https://www.drissionpage.cn/browser_control/upload)
    * [🛰️ Page 对象](https://www.drissionpage.cn/browser_control/pages)
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/visit)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/visit)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 访问网页


本页总览
# 🛰️ 访问网页
本节介绍 Tab 对象访问网页的相关内容。
## ✅️️ 连接方法[​](https://www.drissionpage.cn/browser_control/visit#️️-连接方法 "✅️️ 连接方法的直接链接")
### 📌 `get()`[​](https://www.drissionpage.cn/browser_control/visit#-get "-get的直接链接")
该方法用于跳转到一个网址。当连接失败时，程序会进行重试。
可指定本地文件路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| 必填| 目标 url，可指向本地文件路径  
`show_errmsg`| `bool`| `False`| 连接出错时是否显示和抛出异常  
`retry`| `int`| `None`| 重试次数，为`None`时使用页面参数，默认`3`  
`interval`| `float`| `None`| 重试间隔（秒），为`None`时使用页面参数，默认`2`  
`timeout`| `float`| `None`| 加载超时时间（秒）  
-------| -------| ---| ------ 以下参数仅 s 模式有效 ------  
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
`bool`| 访问是否成功  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')
```

### 📌 `post()`[​](https://www.drissionpage.cn/browser_control/visit#-post "-post的直接链接")
此方法用内置的`Session`对象以 POST 方式发送请求。
因为`post()`是使用`requests`的`post()`方法发送请求，参数和用法与`requests`一致。
此方法返回请求结果`Response`对象。
s 模式时，`post()`后结果还可用页面对象的`html`或`json`属性获取。
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
`Response`| 获取到的`Response`对象  
## ✅️️ 设置超时和重试[​](https://www.drissionpage.cn/browser_control/visit#️️-设置超时和重试 "✅️️ 设置超时和重试的直接链接")
网络不稳定时，访问页面不一定成功，`get()`方法内置了超时和重试功能。通过`retry`、`interval`、`timeout`三个参数进行设置。 其中，如不指定`timeout`参数，该参数会使用`ChromiumPage`的`timeouts`属性的`page_load`参数中的值。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn', retry=1, interval=1, timeout=1.5)
```

## ✅️️ 加载模式[​](https://www.drissionpage.cn/browser_control/visit#️️-加载模式 "✅️️ 加载模式的直接链接")
### 📌 概述[​](https://www.drissionpage.cn/browser_control/visit#-概述 "📌 概述的直接链接")
加载模式是指 d 模式下程序在页面加载阶段的行为模式，有以下三种：
  * `normal()`：常规模式，会等待页面加载完毕，超时自动重试或停止，默认使用此模式
  * `eager()`：加载完 DOM 或超时即停止加载，不加载页面资源
  * `none()`：超时也不会自动停止，除非加载完成


前两种模式下，页面加载过程会阻塞程序，直到加载完毕才执行后面的操作。
`none()`模式下，只在连接阶段阻塞程序，加载阶段可自行根据情况执行`stop_loading()`停止加载。
这样提供给用户非常大的自由度，可等到关键数据包或元素出现就主动停止页面加载，大幅提升执行效率。
注意
加载完成是指主文档完成，并不包括由 js 触发的加载和重定向的加载。 当文档加载完成，程序就判断加载完毕，此后发生的重定向或 js 加载数据需用其它逻辑处理。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.load_mode.eager()# 设置为eager模式tab.get('http://DrissionPage.cn')
```

### 📌 模式设置[​](https://www.drissionpage.cn/browser_control/visit#-模式设置 "📌 模式设置的直接链接")
可通过 ini 文件、`ChromiumOptions`对象和页面对象的`set.load_mode.****()`方法进行设置。
运行时可随时动态设置。
**配置对象中设置**
```
from DrissionPage import ChromiumOptions, Chromiumco = ChromiumOptions().set_load_mode('none')browser = Chromium(co)
```

**运行中设置**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.load_mode.none()
```

### 📌 `none`模式技巧[​](https://www.drissionpage.cn/browser_control/visit#-none模式技巧 "-none模式技巧的直接链接")
**示例 1，配合监听器**
跟监听器配合，可在获取到需要的数据包时，主动停止加载。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.load_mode.none()# 设置加载模式为nonetab.listen.start('api/getkeydata')# 指定监听目标并启动监听tab.get('http://www.hao123.com/')# 访问网站packet = tab.listen.wait()# 等待数据包tab.stop_loading()# 主动停止加载print(packet.response.body)# 打印数据包正文
```

**示例 2，配合元素查找**
跟元素查找配合，可在获取到某个指定元素时，主动停止加载。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.load_mode.none()# 设置加载模式为nonetab.get('http://www.hao123.com/')# 访问网站ele = tab.ele('中国日报')# 查找text包含“中国日报”的元素tab.stop_loading()# 主动停止加载print(ele.text)# 打印元素text
```

**示例 2，配合页面特征**
可等待到页面到达某种状态时，主动停止加载。比如多级跳转的登录，可等待 title 变化到最终目标网址时停止。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.load_mode.none()# 设置加载模式为nonetab.get('http://www.hao123.com/')# 访问网站tab.wait.title_change('hao123')# 等待title变化出现目标文本tab.stop_loading()# 主动停止加载
```

[上一页🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)[下一页🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
  * [✅️️ 连接方法](https://www.drissionpage.cn/browser_control/visit#️️-连接方法)
    * [📌 `get()`](https://www.drissionpage.cn/browser_control/visit#-get)
    * [📌 `post()`](https://www.drissionpage.cn/browser_control/visit#-post)
  * [✅️️ 设置超时和重试](https://www.drissionpage.cn/browser_control/visit#️️-设置超时和重试)
  * [✅️️ 加载模式](https://www.drissionpage.cn/browser_control/visit#️️-加载模式)
    * [📌 概述](https://www.drissionpage.cn/browser_control/visit#-概述)
    * [📌 模式设置](https://www.drissionpage.cn/browser_control/visit#-模式设置)
    * [📌 `none`模式技巧](https://www.drissionpage.cn/browser_control/visit#-none模式技巧)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/visit)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/visit)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
