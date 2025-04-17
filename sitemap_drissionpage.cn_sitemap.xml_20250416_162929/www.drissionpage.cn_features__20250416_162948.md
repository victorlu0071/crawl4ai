# Content from: https://www.drissionpage.cn/features/

[跳到主要内容](https://www.drissionpage.cn/features/#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/)


  * [](https://www.drissionpage.cn/)
  * 💖 特性


本页总览
# 💖 特性
## ✅️️ 强大的自研内核[​](https://www.drissionpage.cn/features/#️️-强大的自研内核 "✅️️ 强大的自研内核的直接链接")
  * 不依赖 webdriver
  * 无需为不同版本的浏览器下载不同的驱动
  * 运行速度更快
  * 可以跨 iframe 查找元素，无需切入切出
  * 可同时操作多个标签页，无需切换
  * 方便好用的数据包监听功能
  * 可处理非`open`状态的 shadow-root


## ✅️️ 无处不在的等待[​](https://www.drissionpage.cn/features/#️️-无处不在的等待 "✅️️ 无处不在的等待的直接链接")
网络环境不稳定，很多时候程序需要稍微等待一下才能继续运行。
等待太少，会导致程序出错，等待太多，又会浪费时间。
为了解决这些问题，本库在大量需要等待的部分内置了超时功能，并且可以随时灵活设置，大幅降低程序复杂性。
  * 查找元素内置等待。可以为每次查找元素单独设定等待时间。使用灵活。
  * 等待下拉列表选项。很多下拉列表使用 js 加载，本库选择下拉列表时，会自动等待列表项出现。
  * 等待弹窗。有时预期的 alert 未必立刻出现，本库处理弹窗消息时也可以设置等待。
  * 等待元素状态改变。使用`wait.ele()`方法可等待元素出现、消失、删除等状态。
  * 等待页面进入加载状态或加载完成。不仅节省时间，还大幅提高程序稳定性。
  * 点击功能也内置等待，如遇元素被遮挡可不断重试点击。
  * 设置页面加载时限及加载策略。有时不需要完整加载页面资源，可根据实际需要设置加载策略。


## ✅️️ 极简的定位语法[​](https://www.drissionpage.cn/features/#️️-极简的定位语法 "✅️️ 极简的定位语法的直接链接")
本库制定了一套简洁高效的查找元素语法，支持链式操作，支持相对定位。
每次查找内置等待，可以独立设置每次查找超时时间。
同是设置了超时等待的查找，与 selenium 对比一下：
```
# 使用 selenium：element = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,'//*[contains(text(), "some text")]')))# 使用 DrissionPage：element = tab('some text', timeout=10)
```

## ✅️️ 无需切入切出的使用方式[​](https://www.drissionpage.cn/features/#️️-无需切入切出的使用方式 "✅️️ 无需切入切出的使用方式的直接链接")
使用过 selenium 的人都知道，selenium 同一时间只能操作一个标签页或`<iframe>`。
需要用`switch_to()`方法来回切换，相当麻烦。
DrissionPage 则无需这些麻烦的操作，它把每个标签页和`<iframe>`都看作独立的对象，可以同时并发操作。
而且可以直接跨多层`<iframe>`获取里面的元素，然后直接处理，非常方便。
对比一下，获取 2 层`<iframe>`内一个 id 为`'div1'`的元素：
```
# 使用 seleniumdriver.switch_to.frame(0)driver.switch_to.frame(0)ele = driver.find_element(By.ID,'div1')driver.switch_to.default_content()# 使用 DrissionPageele = tab('#div1')
```

多标签页同时操作，selenium 无此功能：
```
tab1 = browser.get_tab(1)tab2 = browser.get_tab(2)tab1.get('https://www.baidu.com')tab2.get('https://www.163.com')
```

## ✅️️ 高度集成的便利功能[​](https://www.drissionpage.cn/features/#️️-高度集成的便利功能 "✅️️ 高度集成的便利功能的直接链接")
很多操作方法集成了常用功能，如`click()`中内置`by_js`参数，可以直接改用 js 方式点击，而无需写独立的 js 语句。
数量太多，不一一阐述，可在使用中体验。
## ✅️️ 强大的下载功能[​](https://www.drissionpage.cn/features/#️️-强大的下载功能 "✅️️ 强大的下载功能的直接链接")
DrissionPage 内置一个下载工具，可实现大文件分块多线程下载文件。
并且可以直接读取缓存数据保存图片，而无需控制页面作另存操作。
## ✅️️ 自动重试连接[​](https://www.drissionpage.cn/features/#️️-自动重试连接 "✅️️ 自动重试连接的直接链接")
在访问网站时，由于网络不稳定可能导致连接异常。本库设置了连接自动重试功能，当网页连接异常，会默认重试 3 次。当然也可以手动设置次数和间隔。
```
tab.get('****', retry=5, interval=3)# 出错时重试 5 次，每次间隔 3 秒
```

## ✅️️ 更多便捷的功能[​](https://www.drissionpage.cn/features/#️️-更多便捷的功能 "✅️️ 更多便捷的功能的直接链接")
  * 可对整个网页截图，包括视口外的部分
  * 每次运行程序可以反复使用已经打开的浏览器，无需每次从头运行
  * s 模式访问网页时会自动纠正编码，无需手动设置
  * s 模式在连接时会自动根据当前域名自动填写`Host`和`Referer`属性
  * 下载工具支持多种方式处理文件名冲突、自动创建目标路径、断链重试等
  * 支持直接获取`after`和`before`伪元素的内容
  * 上传文件可直接拦截文件选择框并输入路径，无需依靠 GUI 或查找`<input>`元素输入


[上一页💥 3.2 功能介绍](https://www.drissionpage.cn/features/3)[下一页⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)
  * [✅️️ 强大的自研内核](https://www.drissionpage.cn/features/#️️-强大的自研内核)
  * [✅️️ 无处不在的等待](https://www.drissionpage.cn/features/#️️-无处不在的等待)
  * [✅️️ 极简的定位语法](https://www.drissionpage.cn/features/#️️-极简的定位语法)
  * [✅️️ 无需切入切出的使用方式](https://www.drissionpage.cn/features/#️️-无需切入切出的使用方式)
  * [✅️️ 高度集成的便利功能](https://www.drissionpage.cn/features/#️️-高度集成的便利功能)
  * [✅️️ 强大的下载功能](https://www.drissionpage.cn/features/#️️-强大的下载功��能)
  * [✅️️ 自动重试连接](https://www.drissionpage.cn/features/#️️-自动重试连接)
  * [✅️️ 更多便捷的功能](https://www.drissionpage.cn/features/#️️-更多便捷的功能)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/)
  * [QQ群：391178600](https://www.drissionpage.cn/features/)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
