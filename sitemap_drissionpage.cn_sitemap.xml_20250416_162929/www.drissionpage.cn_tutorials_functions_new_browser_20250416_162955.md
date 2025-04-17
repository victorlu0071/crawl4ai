# Content from: https://www.drissionpage.cn/tutorials/functions/new_browser

[跳到主要内容](https://www.drissionpage.cn/tutorials/functions/new_browser#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/tutorials/functions/new_browser)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/tutorials/functions/new_browser)
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
  * [🥬 功能示例](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)
    * [🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
    * [🥦 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies)


  * [](https://www.drissionpage.cn/)
  * 🥬 功能示例
  * 🥦 创建全新的浏览器


本页总览
# 🥦 创建全新的浏览器
默认设置下，DrissionPage 会在 9222 端口创建浏览器，如果该端口下浏览器已经启动，则会接管使用。
并且会重复使用用户文件夹，即该端口登录过的账号，下次启动时可能仍有效，使用的插件也一样。
这为调试和日常使用带来大量便利，无须总是要处理登录和加载插件。
但项目中往往需要创建全新的浏览器环境，不希望复用之前的用户数据，可用以下方法实现：
## ✅️️ `auto_port()`方法[​](https://www.drissionpage.cn/tutorials/functions/new_browser#️️-auto_port方法 "️️-auto_port方法的直接链接")
使用`ChromiumOptions`对象的`atuo_port()`方法，可指定程序自动创建全新的浏览器，多个浏览器互不干扰。
```
from DrissionPage import ChromiumOptions, Chromiumco = ChromiumOptions().auto_port()browser1 = Chromium(co)browser2 = Chromium(co)
```

如此即可创建两个全新且独立的浏览器。
可以注意到，示例中两个`Chromium`对象共用了一个`ChromiumOptions`对象，这在设置`auto_port()`时才会生效。
如果没有设置`auto_port()`，两个页面对象其实是同一个。
注意
如果使用`atuo_port()`后再使用`set_local_port()`、`set_address()`或`set_user_data_path()`，会覆盖`auto_port()`设置。
## ✅️️ 手动配置[​](https://www.drissionpage.cn/tutorials/functions/new_browser#️️-手动配置 "✅️️ 手动配置的直接链接")
如果有更细致的需求，不使用`auto_port()`，可自行使用`set_local_port()`、`set_address()`和`set_user_data_path()`为每个浏览器指定端口和用户文件夹。
注意
  * 务必注意的是，每个浏览器的端口和用户文件夹都必须是独立的，不能复用
  * 每个浏览器都要一个`ChromiumOptions`对象，不能复用


```
from DrissionPage import Chromium, ChromiumOptionsco1 = ChromiumOptions().set_local_port(9111).set_user_data_path('data1')co2 = ChromiumOptions().set_local_port(9222).set_user_data_path('data2')browser1 = Chromium(co1)browser2 = Chromium(co2)
```

[上一页❓ 常见问题](https://www.drissionpage.cn/tutorials/QandA)[下一页🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)
  * [✅️️ `auto_port()`方法](https://www.drissionpage.cn/tutorials/functions/new_browser#️️-auto_port方法)
  * [✅️️ 手动配置](https://www.drissionpage.cn/tutorials/functions/new_browser#️️-手动配置)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/tutorials/functions/new_browser)
  * [QQ群：391178600](https://www.drissionpage.cn/tutorials/functions/new_browser)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
