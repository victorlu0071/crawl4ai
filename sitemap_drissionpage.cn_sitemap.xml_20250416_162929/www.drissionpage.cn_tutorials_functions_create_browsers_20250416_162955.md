# Content from: https://www.drissionpage.cn/tutorials/functions/create_browsers

[跳到主要内容](https://www.drissionpage.cn/tutorials/functions/create_browsers#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/tutorials/functions/create_browsers)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/tutorials/functions/create_browsers)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏️ 知识星球](https://www.drissionpage.cn/tutorials/xingqiu)
  * [🎞️ 视频教程](https://www.drissionpage.cn/tutorials/video)
  * [🗨️ 公众号](https://www.drissionpage.cn/tutorials/gongzhonghao)
  * [📚 离线文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372029&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [👍 浏览器插件](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372024&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [❓ 常见问题](https://www.drissionpage.cn/tutorials/QandA)
  * [🥬 功能示例](https://www.drissionpage.cn/tutorials/functions/create_browsers)
    * [🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)
    * [🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
    * [🥦 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies)


  * [](https://www.drissionpage.cn/)
  * 🥬 功能示例
  * 🥦 浏览器多开


本页总览
# 🥦 浏览器多开
本节介绍如何启动多个浏览器同时使用。
## ✅️️ 直接指定端口[​](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-直接指定端口 "✅️️ 直接指定端口的直接链接")
使用`Chromium()`启动浏览器时可以直接指定端口来启动多个浏览器。
如果指定端口已有浏览器在运行，会接管这个浏览器。
使用端口号创建的浏览器用户数据文件夹会保留，只要临时文件夹未被清理，下次使用该端口时还会使用这些数据，比如登录信息和插件。
```
from DrissionPage import Chromiumbrowser1 = Chromium(9222)browser2 = Chromium(9333)
```

## ✅️️ 自动设置端口[​](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-自动设置端口 "✅️️ 自动设置端口的直接链接")
使用`ChromiumOptions`对象的`auto_port()`方法，可自动获取空闲端口，并创建全新浏览器（无用户数据和插件）。
这时多个页面对象可共用一个`ChromiumOptions`对象，不会产生冲突。
浏览器关闭后会自动删除用户文件夹，不会过多占用硬盘空间。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().auto_port()browser1 = Chromium(co)browser2 = Chromium(co)
```

## ✅️️ 手动指定端口和路径[​](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-手动指定端口和路径 "✅️️ 手动指定端口和路径的直接链接")
也可以用指定独立端口和用户文件夹路径的方式启动多个浏览器。
需要注意的是，端口和用户文件夹每个浏览器都要独立使用，不能共用。
因此，这时每个页面对象需要自己的配置对象。
```
from DrissionPage import Chromium, ChromiumOptionsco1 = ChromiumOptions().set_local_port(9222).set_user_data_path('data1')co2 = ChromiumOptions().set_local_port(9333).set_user_data_path('data2')browser1 = Chromium(co1)browser2 = Chromium(co2)
```

[上一页🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)[下一页🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
  * [✅️️ 直接指定端口](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-直接指定端口)
  * [✅️️ 自动设置端口](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-自动设置端口)
  * [✅️️ 手动指定端口和路径](https://www.drissionpage.cn/tutorials/functions/create_browsers#️️-手动指定端口和路径)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/tutorials/functions/create_browsers)
  * [QQ群：391178600](https://www.drissionpage.cn/tutorials/functions/create_browsers)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
