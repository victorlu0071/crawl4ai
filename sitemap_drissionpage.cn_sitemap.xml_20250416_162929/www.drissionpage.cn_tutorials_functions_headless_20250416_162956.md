# Content from: https://www.drissionpage.cn/tutorials/functions/headless

[跳到主要内容](https://www.drissionpage.cn/tutorials/functions/headless#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/tutorials/functions/headless)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/tutorials/functions/headless)
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
  * [🥬 功能示例](https://www.drissionpage.cn/tutorials/functions/headless)
    * [🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)
    * [🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)
    * [🥦 无头模式](https://www.drissionpage.cn/tutorials/functions/headless)
    * [🥦 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies)


  * [](https://www.drissionpage.cn/)
  * 🥬 功能示例
  * 🥦 无头模式


# 🥦 无头模式
要使用无头模式很简单，在`ChromiumOptions`设置`headless()`即可。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().headless()browser = Chromium(co)
```

需要注意的是，程序结束时浏览器不会自动关闭，下次运行会继续接管该浏览器。
无头浏览器因为看不见很容易被忽视。可在程序结尾用`browser.quit()`将其关闭。
[上一页🥦 浏览器多开](https://www.drissionpage.cn/tutorials/functions/create_browsers)[下一页🥦 设置 cookies](https://www.drissionpage.cn/tutorials/functions/set_cookies)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/tutorials/functions/headless)
  * [QQ群：391178600](https://www.drissionpage.cn/tutorials/functions/headless)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
