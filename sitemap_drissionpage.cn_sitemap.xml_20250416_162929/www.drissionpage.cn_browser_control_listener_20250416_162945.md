# Content from: https://www.drissionpage.cn/browser_control/listener

[跳到主要内容](https://www.drissionpage.cn/browser_control/listener#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/listener)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/listener)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/listener)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/listener)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/listener)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/listener)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 监听网络数据


本页总览
# 🛰️ 监听网络数据
许多网页的数据来自接口，在网站使用过程中动态加载，如使用 JS 加载内容的翻页列表。
这些数据通常以 json 形式发送，浏览器接收后，对其进行解析，再加载到 DOM 相应位置。
做数据采集的时候，我们往往从 DOM 中去获取解析后数据的，可能存在数据不全、加载响应不及时、难以判断加载完成等问题。
如果我们可以拿到浏览器收发的数据包，根据数据包状态判断下一步操作，甚至直接获取数据，岂不是爽爆了？
DrissionPage 每个页面对象（包括 Tab 和 Frame 对象）内置了一个监听器，专门用于抓取浏览器数据包。
可以提供等待和捕获指定数据包，实时返回指定数据包功能。
## ✅️ 示例[​](https://www.drissionpage.cn/browser_control/listener#️-示例 "✅️ 示例的直接链接")
先看两个示例了解监听器工作方式。
注意
要先启动监听，再执行动作，`listen.start()`之前的数据包是获取不到的。
### 📌 等待并获取[​](https://www.drissionpage.cn/browser_control/listener#-等待并获取 "📌 等待并获取的直接链接")
点击下一页，等待数据包，再点击下一页，循环。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://gitee.com/explore/all')# 访问网址，这行产生的数据包不监听tab.listen.start('gitee.com/explore')# 开始监听，指定获取包含该文本的数据包for _ inrange(5):  tab('@rel=next').click()# 点击下一页  res = tab.listen.wait()# 等待并获取一个数据包print(res.url)# 打印数据包url
```

**输出：**
```
https://gitee.com/explore/all?page=2https://gitee.com/explore/all?page=3https://gitee.com/explore/all?page=4https://gitee.com/explore/all?page=5https://gitee.com/explore/all?page=6
```

### 📌 实时获取[​](https://www.drissionpage.cn/browser_control/listener#-实时获取 "📌 实时获取的直接链接")
跟上一个示例做同样的事情，不过换一种方式。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.listen.start('gitee.com/explore')# 开始监听，指定获取包含该文本的数据包tab.get('https://gitee.com/explore/all')# 访问网址i =0for packet in tab.listen.steps():print(packet.url)# 打印数据包url  tab('@rel=next').click()# 点击下一页  i +=1if i ==5:break
```

## ✅️ 设置目标和启动监听[​](https://www.drissionpage.cn/browser_control/listener#️-设置目标和启动监听 "✅️ 设置目标和启动监听的直接链接")
### 📌 `listen.start()`[​](https://www.drissionpage.cn/browser_control/listener#-listenstart "-listenstart的直接链接")
此方法用于启动监听器，启动同时可设置获取的目标特征。
可设置多个特征，符合条件的数据包会被获取。
如果监听未停止时调用这个方法，可清除已抓取的队列。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`targets`| `str``list``tuple``set`| `None`| 要匹配的数据包 url 特征，可用列表指定多个，为`True`时获取所有  
`is_regex`| `bool`| `None`| 设置的 target 是否正则表达式，为`None`时保持原来设置  
`method`| `str``list``tuple``set`| `None`| 设置监听的请求类型，可指定多个，默认`('GET', 'POST')`，为`True`时监听所有，为`None`时保持原来设置  
`res_type`| `str``list``tuple``set`| `None`| 设置监听的 ResourceType 类型，可指定多个，为`True`时监听所有，为`None`时保持原来设置  
**返回：** `None`
注意
当`targets`不为`None`，`is_regex`会自动设为`False`。 即如要使用正则，每次设置`targets`时需显式指定`is_regex=True`。
### 📌 `listen.set_targets()`[​](https://www.drissionpage.cn/browser_control/listener#-listenset_targets "-listenset_targets的直接链接")
此方法可在监听过程中修改监听目标，也可在监听开始前设置。
如监听未启动，不会启动监听。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`targets`| `str``list``tuple``set`| `True`| 要匹配的数据包 url 特征，可用列表指定多个，为`True`时获取所有  
`is_regex`| `bool`| `False`| 设置的 target 是否正则表达式  
`method`| `str``list``tuple``set`| `('GET', 'POST')`| 设置监听的请求类型，可指定多个，默认`('GET', 'POST')`，为`True`时监听所有  
`res_type`| `str``list``tuple``set`| `True`| 设置监听的 ResourceType 类型，可指定多个，为`True`时监听所有  
**返回：** `None`
## ✅️ 等待和获取数据包[​](https://www.drissionpage.cn/browser_control/listener#️-等待和获取数据包 "✅️ 等待和获取数据包的直接链接")
### 📌 `listen.wait()`[​](https://www.drissionpage.cn/browser_control/listener#-listenwait "-listenwait的直接链接")
此方法用于等待符合要求的数据包到达指定数量。
所有符合条件的数据包都会存储到队列，`wait()`实际上是逐个从队列中取结果，不用担心页面已刷走而丢包。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`count`| `int`| `1`| 需要捕捉的数据包数量  
`timeout`| `float``None`| `None`| 超时时间（秒），为`None`无限等待  
`fit_count`| `bool`| `True`| 是否必需满足总数要求，如超时，为`True`返回`False`，为`False`返回已捕捉到的数据包  
`raise_err`| `bool`| `None`| 超时时是否抛出错误，为`None`时根据`Settings`设置，如不抛出，超时返回`False`  
返回类型| 说明  
---|---  
`DataPacket`| `count`为`1`且未超时，返回一个数据包对象  
`List[DataPacket]`| `count`大于`1`，未超时或`fit_count`为`False`，返回数据包对象组成的列表  
`False`| 超时且`fit_count`为`True`时  
### 📌 `listen.steps()`[​](https://www.drissionpage.cn/browser_control/listener#-listensteps "-listensteps的直接链接")
此方法返回一个可迭代对象，用于`for`循环，每次循环可从中获取到的数据包。
可实现实时获取并返回数据包。
如果`timeout`超时，会中断循环。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`count`| `int`| `None`| 需捕获的数据包总数，为`None`表示无限  
`timeout`| `float``None`| `None`| 每个数据包等待时间（秒），为`None`表示无限等待  
`gap`| `int`| `1`| 每接收到多少个数据包返回一次数据  
返回类型| 说明  
---|---  
`DataPacket`| `gap`为`1`时，返回一个数据包对象  
`List[DataPacket]`| `gap`大于`1`，返回数据包对象组成的列表  
### 📌 `listen.wait_silent()`[​](https://www.drissionpage.cn/browser_control/listener#-listenwait_silent "-listenwait_silent的直接链接")
此方法用于等待所有指定的请求完成。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None`| `None`| 等待时间（秒），为`None`表示无限等待  
`targets_only`| `bool`| `False`| 是否只等待`targets`指定的请求结束  
`limit`| `int`| `0`| 剩下多少个连接时视为结束  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
## ✅️ 暂停和恢复[​](https://www.drissionpage.cn/browser_control/listener#️-暂停和恢复 "✅️ 暂停和恢复的直接链接")
### 📌 `listen.pause()`[​](https://www.drissionpage.cn/browser_control/listener#-listenpause "-listenpause的直接链接")
此方法用于暂停监听。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`clear`| `bool`| `True`| 是否清空已获取队列  
**返回：** `None`
### 📌 `listen.resume()`[​](https://www.drissionpage.cn/browser_control/listener#-listenresume "-listenresume的直接链接")
此方法用于继续暂停的监听。
**参数：** 无
**返回：**`None`
### 📌 `listen.stop()`[​](https://www.drissionpage.cn/browser_control/listener#-listenstop "-listenstop的直接链接")
此方法用于终止监听器的运行，会清空已获取的队列，不清空 targets。
**参数：** 无
**返回：**`None`
## ✅️ `DataPacket`对象[​](https://www.drissionpage.cn/browser_control/listener#️-datapacket对象 "️-datapacket对象的直接链接")
`DataPacket`对象是获取到的数据包结果对象，包含了数据包各种信息。
### 📌 `对象属性`[​](https://www.drissionpage.cn/browser_control/listener#-对象属性 "-对象属性的直接链接")
属性名称| 数据类型| 说明  
---|---|---  
`tab_id`| `str`| 产生这个请求的标签页的 id  
`frameId`| `str`| 产生这个请求的框架 id  
`target`| `str`| 产生这个请求的监听目标  
`url`| `str`| 数据包请求网址  
`method`| `str`| 请求类型  
`is_failed`| `bool`| 是否连接失败  
`resourceType`| `str`| 资源类型  
`request`| `Request`| 保存请求信息的对象  
`response`| `Response`| 保存响应信息的对象  
`fail_info`| `FailInof`| 保存连接失败信息的对象  
### 📌 `wait_extra_info()`[​](https://www.drissionpage.cn/browser_control/listener#-wait_extra_info "-wait_extra_info的直接链接")
有些数据包有`extra_info`数据，但这些数据可能会迟于数据包返回，用这个方法可以等待这些数据加载到数据包对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None`| `None`| 超时时间（秒），`None`为无限等待  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
### 📌 `Request`对象[​](https://www.drissionpage.cn/browser_control/listener#-request对象 "-request对象的直接链接")
`Request`对象是`DataPacket`对象内用于保存请求信息的对象，有以下属性：
属性名称| 数据类型| 说明  
---|---|---  
`url`| `str`| 请求的网址  
`method`| `str`| 请求类型  
`params`| `dict`| 以`dict`格式返回 url 中的参数  
`headers`| `CaseInsensitiveDict`| 以大小写不敏感字典返回 headers 数据  
`cookies`| `List[dict]`| 返回发送的 cookies  
`postData`| `str``dict`| post 类型的请求所提交的数据，json 以`dict`格式返回  
除以上常用属性，还有以下属性，自行体会：
urlFragment、hasPostData、postDataEntries、mixedContentType、initialPriority、referrerPolicy、isLinkPreload、trustTokenParams、isSameSite
### 📌 `Response`对象[​](https://www.drissionpage.cn/browser_control/listener#-response对象 "-response对象的直接链接")
`Response`对象是`DataPacket`对象内用于保存响应信息的对象，有以下属性：
属性名称| 数据类型| 说明  
---|---|---  
`url`| `str`| 请求的网址  
`headers`| `CaseInsensitiveDict`| 以大小写不敏感字典返回 headers 数据  
`body`| `str``bytes``dict`| 如果是 json 格式，转换为`dict`；如果是 base64 格式，转换为`bytes`，其它格式直接返回文本  
`raw_body`| `str`| 未被处理的 body 文本  
`status`| `int`| 请求状态  
`statusText`| `str`| 请求状态文本  
除以上属性，还有以下属性，自行体会：
headersText、mimeType、requestHeaders、requestHeadersText、connectionReused、connectionId、remoteIPAddress、remotePort、fromDiskCache、fromServiceWorker、fromPrefetchCache、encodedDataLength、timing、serviceWorkerResponseSource、responseTime、cacheStorageCacheName、protocol、alternateProtocolUsage、securityState、securityDetails
### 📌 `FailInfo`对象[​](https://www.drissionpage.cn/browser_control/listener#-failinfo对象 "-failinfo对象的直接链接")
`FailInfo`对象是`DataPacket`对象内用于保存连接失败信息的对象，有以下属性：
属性名称| 数据类型| 说明  
---|---|---  
`errorText`| `str`| 错误信息文本  
`canceled`| `bool`| 是否取消  
`blockedReason`| `str`| 拦截原因  
`corsErrorStatus`| `str`| cors 错误状态  
[上一页🛰️ 等待](https://www.drissionpage.cn/browser_control/waiting)[下一页🛰️ 获取控制台信息](https://www.drissionpage.cn/browser_control/console)
  * [✅️ 示例](https://www.drissionpage.cn/browser_control/listener#️-示例)
    * [📌 等待并获取](https://www.drissionpage.cn/browser_control/listener#-等待并获取)
    * [📌 实时获取](https://www.drissionpage.cn/browser_control/listener#-实时获取)
  * [✅️ 设置目标和启动监听](https://www.drissionpage.cn/browser_control/listener#️-设置目标和启动监听)
    * [📌 `listen.start()`](https://www.drissionpage.cn/browser_control/listener#-listenstart)
    * [📌 `listen.set_targets()`](https://www.drissionpage.cn/browser_control/listener#-listenset_targets)
  * [✅️ 等待和获取数据包](https://www.drissionpage.cn/browser_control/listener#️-等待和获取数据包)
    * [📌 `listen.wait()`](https://www.drissionpage.cn/browser_control/listener#-listenwait)
    * [📌 `listen.steps()`](https://www.drissionpage.cn/browser_control/listener#-listensteps)
    * [📌 `listen.wait_silent()`](https://www.drissionpage.cn/browser_control/listener#-listenwait_silent)
  * [✅️ 暂停和恢复](https://www.drissionpage.cn/browser_control/listener#️-暂停和恢复)
    * [📌 `listen.pause()`](https://www.drissionpage.cn/browser_control/listener#-listenpause)
    * [📌 `listen.resume()`](https://www.drissionpage.cn/browser_control/listener#-listenresume)
    * [📌 `listen.stop()`](https://www.drissionpage.cn/browser_control/listener#-listenstop)
  * [✅️ `DataPacket`对象](https://www.drissionpage.cn/browser_control/listener#️-datapacket对象)
    * [📌 `对象属性`](https://www.drissionpage.cn/browser_control/listener#-对象属性)
    * [📌 `wait_extra_info()`](https://www.drissionpage.cn/browser_control/listener#-wait_extra_info)
    * [📌 `Request`对象](https://www.drissionpage.cn/browser_control/listener#-request对象)
    * [📌 `Response`对象](https://www.drissionpage.cn/browser_control/listener#-response对象)
    * [📌 `FailInfo`对象](https://www.drissionpage.cn/browser_control/listener#-failinfo对象)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/listener)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/listener)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
