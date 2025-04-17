# Content from: https://www.drissionpage.cn/browser_control/pages

[跳到主要内容](https://www.drissionpage.cn/browser_control/pages#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/pages)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/pages)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/pages)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/pages)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/pages)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/pages)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ Page 对象


本页总览
# 🛰️ Page 对象
`ChromiumPage`和`WebPage`是 4.1 之前用于连接和控制浏览器的对象。
4.1 这些功能由`Chromium`实现，但`ChromiumPage`和`WebPage`仍能正常使用。
对比`Chromium`，`ChromiumPage`和`WebPage`在连接浏览器时可以少写一行代码，但在多标签页操作的时候容易造成混乱。
更详细的用法可以看旧版文档。
## ✅️️ `ChromiumPage`[​](https://www.drissionpage.cn/browser_control/pages#️️-chromiumpage "️️-chromiumpage的直接链接")
`ChromiumPage`把浏览器管理功能和一个标签页（默认接管时激活那个）控制功能整合在一起。
可看作浏览器对象，但同时控制了一个标签页。
如果项目只需要使用单标签页，用`ChromiumPage`会比较方便。
`ChromiumPage`创建的标签页对象为`ChromiumTab`，没有切换模式功能。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`addr_or_opts`| `str``int``ChromiumOptions`| `None`| 浏览器启动配置或接管信息。传入 'ip: port' 字符串、端口数字或`ChromiumOptions`对象时按配置启动或接管浏览器；为`None`时使用配置文件配置启动浏览器  
`tab_id`| `str`| `None`| 要控制的标签页 id，不指定默认为激活的  
```
from DrissionPage import ChromiumPagepage = ChromiumPage()page.get('http://DrissionPage.cn')print(page.title)
```

## ✅️️ `WebPage`[​](https://www.drissionpage.cn/browser_control/pages#️️-webpage "️️-webpage的直接链接")
`WebPage`覆盖了`ChromiumPage`所有功能，并且增加了切换模式功能，创建的标签页对象为`MixTab`。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`mode`| `str`| `'d'`| 运行模式，可选`'d'`或`'s'`  
`chromium_options`| `bool``ChromiumOptions`| `None`| `ChromiumOptions`对象，传入`None`时从默认 ini 文件读取，传入`False`时不读取 ini 文件，使用默认配置  
`session_or_options`| `SessionOptions``None``False`| `None`| `Session`对象或`SessionOptions`对象，传入`None`时从默认 ini 文件读取，传入`False`时不读取 ini 文件，使用默认配置  
```
from DrissionPage import WebPagepage = WebPage()page.get('http://DrissionPage.cn')print(page.title)page.change_mode()print(page.title)
```

[上一页🛰️ 上传文件](https://www.drissionpage.cn/browser_control/upload)[下一页🛩️ 概述](https://www.drissionpage.cn/SessionPage/intro)
  * [✅️️ `ChromiumPage`](https://www.drissionpage.cn/browser_control/pages#️️-chromiumpage)
  * [✅️️ `WebPage`](https://www.drissionpage.cn/browser_control/pages#️️-webpage)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/pages)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/pages)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
