# Content from: https://www.drissionpage.cn/advance/errors

[跳到主要内容](https://www.drissionpage.cn/advance/errors#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/errors)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/errors)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/intro)
    * [⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)
    * [⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)
    * [⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)
    * [⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)
    * [⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)
    * [⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)
    * [⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
    * [⚙️ 与其它项目对接](https://www.drissionpage.cn/advance/docking)


  * [](https://www.drissionpage.cn/)
  * 🧰 进阶使用
  * ⚙️ 异常的使用


本页总览
# ⚙️ 异常的使用
本节介绍 DrissionPage 中的自定义异常。
## ✅️️ 导入[​](https://www.drissionpage.cn/advance/errors#️️-导入 "✅️️ 导入的直接链接")
各种异常放在`DrissionPage.errors`路径中。
```
from DrissionPage.errors import*
```

## ✅️️ 异常介绍[​](https://www.drissionpage.cn/advance/errors#️️-异常介绍 "✅️️ 异常介绍的直接链接")
### 📌 `ElementNotFoundError`[​](https://www.drissionpage.cn/advance/errors#-elementnotfounderror "-elementnotfounderror的直接链接")
找不到元素时抛出。
### 📌 `AlertExistsError`[​](https://www.drissionpage.cn/advance/errors#-alertexistserror "-alertexistserror的直接链接")
执行 JS 或调用通过 JS 实现的功能时，若存在未处理的弹出框则抛出。
### 📌 `ContextLostError`[​](https://www.drissionpage.cn/advance/errors#-contextlosterror "-contextlosterror的直接链接")
页面被刷新后仍调用其中的元素时抛出。
### 📌 `ElementLostError`[​](https://www.drissionpage.cn/advance/errors#-elementlosterror "-elementlosterror的直接链接")
元素因页面或自身被刷新而失效后，仍对其进行调用时抛出。
### 📌 `CDPError`[​](https://www.drissionpage.cn/advance/errors#-cdperror "-cdperror的直接链接")
调用 cdp 方法产生异常时抛出。
### 📌 `PageDisconnectedError`[​](https://www.drissionpage.cn/advance/errors#-pagedisconnectederror "-pagedisconnectederror的直接链接")
页面关闭或连接断开后仍调用其功能时抛出。
### 📌 `JavaScriptError`[​](https://www.drissionpage.cn/advance/errors#-javascripterror "-javascripterror的直接链接")
JavaScript 运行错误时抛出。
### 📌 `NoRectError`[​](https://www.drissionpage.cn/advance/errors#-norecterror "-norecterror的直接链接")
对没有大小和位置信息的元素获取这些信息时抛出。
### 📌 `BrowserConnectError`[​](https://www.drissionpage.cn/advance/errors#-browserconnecterror "-browserconnecterror的直接链接")
连接浏览器出错时抛出。
### 📌 `NoResourceError`[​](https://www.drissionpage.cn/advance/errors#-noresourceerror "-noresourceerror的直接链接")
浏览器元素`src()`和`save()`获取资源失败时抛出。
### 📌 `CanNotClickError`[​](https://www.drissionpage.cn/advance/errors#-cannotclickerror "-cannotclickerror的直接链接")
点击元素时如元素不可点击，且设置允许抛出时抛出。
### 📌 `GetDocumentError`[​](https://www.drissionpage.cn/advance/errors#-getdocumenterror "-getdocumenterror的直接链接")
获取页面文档失败时抛出
获取页面文档失败时抛出。
### 📌 `WaitTimeoutError`[​](https://www.drissionpage.cn/advance/errors#-waittimeouterror "-waittimeouterror的直接链接")
自动等待失败，且设置允许抛出时抛出。
### 📌 `IncorrectURLError`[​](https://www.drissionpage.cn/advance/errors#-incorrecturlerror "-incorrecturlerror的直接链接")
访问格式不正确的 url 时抛出。
### 📌 `StorageError`[​](https://www.drissionpage.cn/advance/errors#-storageerror "-storageerror的直接链接")
操作数据时，如网站禁止操作则抛出。
### 📌 `CookieFormatError`[​](https://www.drissionpage.cn/advance/errors#-cookieformaterror "-cookieformaterror的直接链接")
导入 cookie 时如格式不正确则抛出。
### 📌 `LocatorError`[​](https://www.drissionpage.cn/advance/errors#-locatorerror "-locatorerror的直接链接")
传入的定位符格式不正确时抛出。
### 📌 `UnknownError`[​](https://www.drissionpage.cn/advance/errors#-unknownerror "-unknownerror的直接链接")
发生未知错误时抛出。
[上一页⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)[下一页⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)
  * [✅️️ 导入](https://www.drissionpage.cn/advance/errors#️️-导入)
  * [✅️️ 异常介绍](https://www.drissionpage.cn/advance/errors#️️-异常介绍)
    * [📌 `ElementNotFoundError`](https://www.drissionpage.cn/advance/errors#-elementnotfounderror)
    * [📌 `AlertExistsError`](https://www.drissionpage.cn/advance/errors#-alertexistserror)
    * [📌 `ContextLostError`](https://www.drissionpage.cn/advance/errors#-contextlosterror)
    * [📌 `ElementLostError`](https://www.drissionpage.cn/advance/errors#-elementlosterror)
    * [📌 `CDPError`](https://www.drissionpage.cn/advance/errors#-cdperror)
    * [📌 `PageDisconnectedError`](https://www.drissionpage.cn/advance/errors#-pagedisconnectederror)
    * [📌 `JavaScriptError`](https://www.drissionpage.cn/advance/errors#-javascripterror)
    * [📌 `NoRectError`](https://www.drissionpage.cn/advance/errors#-norecterror)
    * [📌 `BrowserConnectError`](https://www.drissionpage.cn/advance/errors#-browserconnecterror)
    * [📌 `NoResourceError`](https://www.drissionpage.cn/advance/errors#-noresourceerror)
    * [📌 `CanNotClickError`](https://www.drissionpage.cn/advance/errors#-cannotclickerror)
    * [📌 `GetDocumentError`](https://www.drissionpage.cn/advance/errors#-getdocumenterror)
    * [📌 `WaitTimeoutError`](https://www.drissionpage.cn/advance/errors#-waittimeouterror)
    * [📌 `IncorrectURLError`](https://www.drissionpage.cn/advance/errors#-incorrecturlerror)
    * [📌 `StorageError`](https://www.drissionpage.cn/advance/errors#-storageerror)
    * [📌 `CookieFormatError`](https://www.drissionpage.cn/advance/errors#-cookieformaterror)
    * [📌 `LocatorError`](https://www.drissionpage.cn/advance/errors#-locatorerror)
    * [📌 `UnknownError`](https://www.drissionpage.cn/advance/errors#-unknownerror)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/errors)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/errors)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
