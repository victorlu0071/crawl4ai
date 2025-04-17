# Content from: https://www.drissionpage.cn/advance/docking

[跳到主要内容](https://www.drissionpage.cn/advance/docking#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/docking)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/docking)
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
  * ⚙️ 与其它项目对接


本页总览
# ⚙️ 与其它项目对接
DrissionPage 提供 2 个小工具，用于与 selenium 和 playwright 项目对接。
可从旧项目对象中生成`ChromiumPage`对象。
注意
只支持 chromium 内核的浏览器。
## ✅️️ 与 selenium 对接[​](https://www.drissionpage.cn/advance/docking#️️-与-selenium-对接 "✅️️ 与 selenium 对接的直接链接")
`from_selenium()`方法接收 selenium 的`WebDriver`对象，返回`ChromiumPage`对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`driver`| `WebDriver`| 必填| selenium 的`WebDriver`对象  
返回类型| 说明  
---|---  
`ChromiumPage`| `ChromiumPage`对象  
```
from DrissionPage.common import from_seleniumfrom selenium.webdriver import Chrome# 创建WebDriver对象driver = Chrome()# 从该WebDriver对象创建ChromiumPage对象page = from_selenium(driver)# 用ChromiumPage对象操作浏览器page.get('http://DrissionPage.cn')
```

## ✅️️ 与 playwright 对接[​](https://www.drissionpage.cn/advance/docking#️️-与-playwright-对接 "✅️️ 与 playwright 对接的直接链接")
`from_playwright()`方法接收 playwright 的`Page`或`Browser`对象，返回`ChromiumPage`对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`page_or_browser`| `Page``Browser`| 必填| playwright 的`Page`或`Browser`对象  
返回类型| 说明  
---|---  
`ChromiumPage`| `ChromiumPage`对象  
```
from DrissionPage.common import from_playwrightfrom playwright.sync_api import sync_playwrightwith sync_playwright()as p:  browser = p.chromium.launch()# 用playwright启动浏览器  pw_page = browser.new_page()# 创建一个新的页面# 从Page对象创建ChromiumPage对象  page = from_playwright(pw_page)# 或 从Browser对象创建ChromiumPage对象  page = from_playwright(browser)# 用ChromiumPage对象操作浏览器  page.get("http://DrissionPage.cn")
```

[上一页⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
  * [✅️️ 与 selenium 对接](https://www.drissionpage.cn/advance/docking#️️-与-selenium-对接)
  * [✅️️ 与 playwright 对接](https://www.drissionpage.cn/advance/docking#️️-与-playwright-对接)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/docking)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/docking)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
