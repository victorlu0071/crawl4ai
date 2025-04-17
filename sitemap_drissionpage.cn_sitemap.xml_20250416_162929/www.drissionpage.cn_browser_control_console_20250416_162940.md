# Content from: https://www.drissionpage.cn/browser_control/console

[跳到主要内容](https://www.drissionpage.cn/browser_control/console#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/console)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/console)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/console)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/console)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/console)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/console)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 获取控制台信息


本页总览
# 🛰️ 获取控制台信息
获取控制台信息的逻辑和监听网络数据差不多，是通过监听控制台数据实现的。
注意
不是所有显示在控制台的信息都能获取，需要用`console.log()`等方法输出到控制台的才能获取。
## ✅️ 示例[​](https://www.drissionpage.cn/browser_control/console#️-示例 "✅️ 示例的直接链接")
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.console.start()tab.run_js('console.log("DrissionPage");')data = tab.console.wait()print(data.text)# 输出：DrissionPage
```

## ✅️ 启动和停止[​](https://www.drissionpage.cn/browser_control/console#️-启动和停止 "✅️ 启动和停止的直接链接")
### 📌 `console.start()`[​](https://www.drissionpage.cn/browser_control/console#-consolestart "-consolestart的直接链接")
此方法用于启动控制台信息监听。
**参数：** 无
**返回：**`None`
### 📌 `console.stop()`[​](https://www.drissionpage.cn/browser_control/console#-consolestop "-consolestop的直接链��接")
此方法用于停止监听，清空已监听到的信息列表。
**参数：** 无
**返回：**`None`
## ✅️ 获取信息[​](https://www.drissionpage.cn/browser_control/console#️-获取信息 "✅️ 获取信息的直接链接")
### 📌 `console.wait()`[​](https://www.drissionpage.cn/browser_control/console#-consolewait "-consolewait的直接链接")
此方法用于等待一条控制台信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None`| `None`| 超时时间（秒），为`None`无限等待  
返回类型| 说明  
---|---  
`ConsoleData`| 控制台信息数据包对象  
`False`| 等待超时时  
### 📌 `console.steps()`[​](https://www.drissionpage.cn/browser_control/console#-consolesteps "-consolesteps的直接链接")
此方法返回一个可迭代对象，用于`for`循环，每次循环可从中获取到的信息。
可实现实时获取并返回数据包。
如果`timeout`超时，会中断循环。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None`| `None`| 每个信息等待时间（秒），为`None`表示无限等待  
返回类型| 说明  
---|---  
`ConsoleData`| 控制台信息数据包对象  
### 📌 `console.messages`[​](https://www.drissionpage.cn/browser_control/console#-consolemessages "-consolemessages的直接链接")
此属性以`list`方式返回获取到的信息，返回后会清空列表。
返回类型| 说明  
---|---  
`List[ConsoleData]`| 控制台信息对象组成的列表  
## ✅️ 其它[​](https://www.drissionpage.cn/browser_control/console#️-其它 "✅️ 其它的直接链接")
### 📌 `console.listening`[​](https://www.drissionpage.cn/browser_control/console#-consolelistening "-consolelistening的直接链接")
此属性返回监听是否进行中。
**返回：** `bool`
### 📌 `console.clear()`[​](https://www.drissionpage.cn/browser_control/console#-consoleclear "-consoleclear的直接链接")
此方法用于清空已获取但未返回的信息。
**参数：** 无
**返回：**`None`
## ✅️ `ConsoleData`对象[​](https://www.drissionpage.cn/browser_control/console#️-consoledata对象 "️-consoledata对象的直接链接")
`ConsoleData`对象是获取到的数据包结果对象，包含了数据包各种信息。
### 📌 `对象属性`[​](https://www.drissionpage.cn/browser_control/console#-对象属性 "-对象属性的直接链接")
属性名称| 数据类型| 说明  
---|---|---  
`source`| `str`| 来源  
`level`| `str`| 类型  
`text`| `str`| 内容文本  
`body`| `Any`| 把`text`进行 json 解析  
`url`| `str`| 网址  
`line`| `str`| 行号  
`column`| `str`| 列号  
[上一页🛰️ 监听网络数据](https://www.drissionpage.cn/browser_control/listener)[下一页🛰️ 截图和录像](https://www.drissionpage.cn/browser_control/screen)
  * [✅️ 示例](https://www.drissionpage.cn/browser_control/console#️-示例)
  * [✅️ 启动和停止](https://www.drissionpage.cn/browser_control/console#️-启动和停止)
    * [📌 `console.start()`](https://www.drissionpage.cn/browser_control/console#-consolestart)
    * [📌 `console.stop()`](https://www.drissionpage.cn/browser_control/console#-consolestop)
  * [✅️ 获取信息](https://www.drissionpage.cn/browser_control/console#️-获取信息)
    * [📌 `console.wait()`](https://www.drissionpage.cn/browser_control/console#-consolewait)
    * [📌 `console.steps()`](https://www.drissionpage.cn/browser_control/console#-consolesteps)
    * [📌 `console.messages`](https://www.drissionpage.cn/browser_control/console#-consolemessages)
  * [✅️ 其它](https://www.drissionpage.cn/browser_control/console#️-其它)
    * [📌 `console.listening`](https://www.drissionpage.cn/browser_control/console#-consolelistening)
    * [📌 `console.clear()`](https://www.drissionpage.cn/browser_control/console#-consoleclear)
  * [✅️ `ConsoleData`对象](https://www.drissionpage.cn/browser_control/console#️-consoledata对象)
    * [📌 `对象属性`](https://www.drissionpage.cn/browser_control/console#-对象属性)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/console)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/console)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
