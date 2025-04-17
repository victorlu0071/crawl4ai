# Content from: https://www.drissionpage.cn/browser_control/intro

[跳到主要内容](https://www.drissionpage.cn/browser_control/intro#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/intro)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/intro)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/intro)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/intro)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 概述


本页总览
# 🛰️ 概述
## ✅️️ 基本逻辑[​](https://www.drissionpage.cn/browser_control/intro#️️-基本逻辑 "✅️️ 基本逻辑的直接链接")
操作浏览器的基本逻辑如下：
  1. 创建浏览器对象，用于启动或接管浏览器
  2. 获取一个 Tab 对象
  3. 使用 Tab 对象访问网址
  4. 使用 Tab 对象获取标签页内需要的元素对象
  5. 使用元素对象进行交互


除此以外，还能执行更为复杂的操作，如执行 js 代码、监听网络数据、下载文件等。这些在后面的章节再介绍。
**示例：** 在百度搜索 “Drissionpage”，并打印结果。
```
# 导入from DrissionPage import Chromium# 连接浏览器browser = Chromium()# 获取标签页对象tab = browser.latest_tab # 访问网页tab.get('https://www.baidu.com')# 获取文本框元素对象ele = tab.ele('#kw')# 向文本框元素对象输入文本ele.input('DrissionPage')# 点击按钮，上两行的代码可以缩写成这样tab('#su').click()# 获取所有<h3>元素links = tab.eles('tag:h3')# 遍历并打印结果for link in links:print(link.text)
```

## ✅️️ 浏览器对象[​](https://www.drissionpage.cn/browser_control/intro#️️-浏览器对象 "✅️️ 浏览器对象的直接链接")
即`Chromium`对象，用于管理浏览器整体相关的操作。
如标签页管理、获取浏览器信息、设置整体运行参数等。
```
from DrissionPage import Chromiumbrowser = Chromium()# 创建浏览器对象browser.set.retry_times(10)# 设置整体运行参数tab = browser.latest_tab # 获取Tab对象browser.quit()# 关闭浏览器
```

## ✅️️ 标签页对象[​](https://www.drissionpage.cn/browser_control/intro#️️-标签页对象 "✅️️ 标签页对象的直接链接")
Tab 对象从浏览器对象获取，每个 Tab 对象对应浏览器上一个实际的标签页。
大部分操作都使用 Tab 对象进行，如访问网站、调整窗口大小、监听网络等。
默认情况下每个标签页只有一个 Tab 对象，关闭单例模式后可用多个 Tab 对象同时控制一个标签页。
```
from DrissionPage import Chromiumbrowser = Chromium()tab1 = browser.latest_tab # 获取最后激活的标签页对象tab1.get('http://DrissionPage.cn')# 标签页访问一个网址tab2 = browser.new_tab('https://www.baidu.com')# 新建一个标签页并访问网址tab3 = browser.get_tab(title='DrissionPage')# 按条件获取标签页对象
```

## ✅️️ 元素对象[​](https://www.drissionpage.cn/browser_control/intro#️️-元素对象 "✅️️ 元素对象的直接链接")
元素对象`ChromiumElemet`是交互的执行者，如点击、文本输入、获取元素信息等。
元素对象可从 Tab 对象获取，也可从另一个元素对象通过内部查找或相对定位的方式获取。
### 📌 对象内部查找[​](https://www.drissionpage.cn/browser_control/intro#-对象内部查找 "📌 对象内部查找的直接链接")
Tab 对象和 元素对象都有`ele()`方法，用于在其内部查找指定元素。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')ele = tab.ele('text=文档')# 获取文本为“文档”的元素ele.click()# 点击该元素
```

### 📌 相对位置查找[​](https://www.drissionpage.cn/browser_control/intro#-相对位置查找 "📌 相对位置查找的直接链接")
可先获取一个元素对象，然后以这个元素为基准定位其内部或指定相对关系的元素。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')ele1 = tab.ele('text=文档')# 获取文本为“文档”的元素ele2 = ele1.next()# 获取ele1的后一个元素ele2.click()# 点击该元素
```

[下一页🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
  * [✅️️ 基本逻辑](https://www.drissionpage.cn/browser_control/intro#️️-基本逻辑)
  * [✅️️ 浏览器对象](https://www.drissionpage.cn/browser_control/intro#️️-浏览器对象)
  * [✅️️ 标签页对象](https://www.drissionpage.cn/browser_control/intro#️️-标签页对象)
  * [✅️️ 元素对象](https://www.drissionpage.cn/browser_control/intro#️️-元素对象)
    * [📌 对象内部查找](https://www.drissionpage.cn/browser_control/intro#-对象内部查找)
    * [📌 相对位置查找](https://www.drissionpage.cn/browser_control/intro#-相对位置查找)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/intro)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/intro)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
