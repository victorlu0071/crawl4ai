# Content from: https://www.drissionpage.cn/tutorials/QandA

[跳到主要内容](https://www.drissionpage.cn/tutorials/QandA#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/tutorials/QandA)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/tutorials/QandA)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🌏️ 知识星球](https://www.drissionpage.cn/tutorials/xingqiu)
  * [🎞️ 视频教程](https://www.drissionpage.cn/tutorials/video)
  * [🗨️ 公众号](https://www.drissionpage.cn/tutorials/gongzhonghao)
  * [📚 离线文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372029&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [👍 浏览器插件](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=11372024&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [❓ 常见问题](https://www.drissionpage.cn/tutorials/QandA)
  * [🥬 功能示例](https://www.drissionpage.cn/tutorials/functions/new_browser)


  * [](https://www.drissionpage.cn/)
  * ❓ 常见问题


本页总览
# ❓ 常见问题
本页收集一些用户使用过程中的常见问题。
欢迎各位开发者添砖加瓦，您可提交 issues、PR，也可以写成博客文章，链接发给本库作者，直接链接到文章。
## ❔ 如何在无界面 Linux 使用[​](https://www.drissionpage.cn/tutorials/QandA#-如何在无界面-linux-使用 "❔ 如何在无界�面 Linux 使用的直接链接")
CentOS 请参考这篇文章：[linux 部署说明](https://blog.csdn.net/sinat_39327967/article/details/132181129?spm=1001.2014.3001.5501)
Ubuntu 请参考这篇文章：[DrissionPage在UbuntuLinux的使用](https://zhuanlan.zhihu.com/p/674687748)
## ❔ 为什么浏览器不能退出无头模式？[​](https://www.drissionpage.cn/tutorials/QandA#-为什么浏览器不能退出无头模式 "❔ 为什么浏览器不能退出无头模式？的直接链接")
> 为什么设置过无头后，下次运行即使不设置`headless()`，浏览器依然进入无头状态？
因为上一次打开的浏览器没有关闭，只是因为开了无头不可见，程序继续接管了它。
如果要关闭浏览器，可在程序结束时使用`Chromium`对象的`quit()`语句。
也可以设置`co.headless(False)`，程序会自动关闭之前的无头浏览器再启动新的。
另请注意，`tab.close()`的功能是关闭当前标签页，而不是关闭浏览器，除非浏览器只有一个标签页。
## ❔ 如何禁用保存密码、恢复页面等提示气泡？[​](https://www.drissionpage.cn/tutorials/QandA#-如何禁用保存密码恢复页面等提示气泡 "❔ 如何禁用保存密码、恢复页面等提示气泡？的直接链接")
浏览器提示气泡出现时可以手动关闭，不关闭也不影响自动操作，在代码中阻止其显示也是可以的。 加一些浏览器配置代码即可禁止相应的气泡显示，需要添加下面这样的代码：
```
co = ChromiumOptions()# 阻止“自动保存密码”的提示气泡co.set_pref('credentials_enable_service',False)# 阻止“要恢复页面吗？Chrome未正确关闭”的提示气泡co.set_argument('--hide-crash-restore-bubble')
```

## ❔ 点击报错“该元素没有位置及大小”怎么办？[​](https://www.drissionpage.cn/tutorials/QandA#-点击报错该元素没有位置及大小怎么办 "❔ 点击报错“该元素没有位置及大小”怎么办？的直接链接")
没有位置及大小是正常的，很多元素都没有位置和大小。
这个时候你要检查是否页面中有同名元素，定位符没写准确拿到了另一个。
如果要点击的元素就是没有位置的，可以强制使用 js 点击，用法是 `.click(by_js=True)`，可以简写为 `.click('js')`。
## ❔ 如何使用启动参数、用户配置、实验项等功能？[​](https://www.drissionpage.cn/tutorials/QandA#-如何使用启动参数用户配置实验项等功能 "❔ 如何使用启动参数、用户配置、实验项等功能？的直接链接")
**arguments 启动参数**
  * 使用参考：<http://DrissionPage.cn/ChromiumPage/browser_opt#-set_argument>
  * 参数详见：<https://peter.sh/experiments/chromium-command-line-switches/>


**prefs 用户配置**
  * 使用参考：<http://DrissionPage.cn/ChromiumPage/browser_opt#-set_pref>
  * 参数详见：<https://src.chromium.org/viewvc/chrome/trunk/src/chrome/common/pref_names.cc>


**flags 实验项**
  * 使用参考：<http://DrissionPage.cn/ChromiumPage/browser_opt#-set_flag>
  * 参数详见：chrome://flags


注意
外部链接仅供参考，请谨慎使用任何高级功能，仅在确保一切都可以掌控时才可使用，因为使用这些功能可能会导致浏览器数据丢失或安全和隐私受到威胁。
## ❔ 如何匹配特殊字符（如`'&nbsp;'`）文本？[​](https://www.drissionpage.cn/tutorials/QandA#-如何匹配特殊字符如nbsp文本 "-如何匹配特殊字符如nbsp文本的直接链接")
需先将特殊字符转为十六进制形式，详见《查找元素》中《语法速查表》一节。
[上一页🗨️ 公众号](https://www.drissionpage.cn/tutorials/gongzhonghao)[下一页🥦 创建全新的浏览器](https://www.drissionpage.cn/tutorials/functions/new_browser)
  * [❔ 如何在无界面 Linux 使用](https://www.drissionpage.cn/tutorials/QandA#-如何在无界面-linux-使用)
  * [❔ 为什么浏览器不能退出无头模式？](https://www.drissionpage.cn/tutorials/QandA#-为什么浏览器不能退出无头模式)
  * [❔ 如何禁用保存密码、恢复页面等提示气泡？](https://www.drissionpage.cn/tutorials/QandA#-如何禁用保存密码恢复页面等提示气泡)
  * [❔ 点击报错“该元素没有位置及大小”怎么办？](https://www.drissionpage.cn/tutorials/QandA#-点击报错该元素没有位置及大小怎么办)
  * [❔ 如何使用启动参数、用户配置、实验项等功能？](https://www.drissionpage.cn/tutorials/QandA#-如何使用启动参数用户配置实验项等功能)
  * [❔ 如何匹配特殊字符（如`'&nbsp;'`）文本？](https://www.drissionpage.cn/tutorials/QandA#-如何匹配特殊字符如nbsp文本)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/tutorials/QandA)
  * [QQ群：391178600](https://www.drissionpage.cn/tutorials/QandA)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
