# Content from: https://www.drissionpage.cn/browser_control/tabs

[跳到主要内容](https://www.drissionpage.cn/browser_control/tabs#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/tabs)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/tabs)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/tabs)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/tabs)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/tabs)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 标签页管理


本页总览
# 🛰️ 标签页管理
浏览器的标签页由 Tab 对象（`ChromiumTab`和`MixTab`）控制。
与网页的交互都由标签页对象进行。
默认情况下，一个标签页由一个 Tab 对象控制。
多个 Tab 对象可以同时操作，不需要切换焦点，也不需要激活到前台。
提醒
当禁用单例模式后，一个标签页也可以被多个 Tab 对象同时控制。
## ✅️️ 获取标签页对象[​](https://www.drissionpage.cn/browser_control/tabs#️️-获取标签页对象 "✅️️ 获取标签页对象的直接链接")
### 📌 获取最后激活的标签页[​](https://www.drissionpage.cn/browser_control/tabs#-获取最后激活的标签页 "📌 获取最后激活的标签页的直接链接")
`Chromium`对象的`latest_tab`属性返回最后激活的标签页对象。
说明
如`Settings.singleton_tab_obj`为`True`，此属性返回标签页对象的 tab id。
```
from DrissionPage import Chromiumbrowser = Chromium()tab = browser.latest_tab # 获取最新标签页对象
```

### 📌 获取指定标签页[​](https://www.drissionpage.cn/browser_control/tabs#-获取指定标签页 "📌 获取指定标签页的直接链接")
`Chromium`对象的`get_tab()`和`get_tabs()`方法用于获取指定的标签页对象。
可指定标签页序号、id、标题、url、类型等条件用于检索。api 详见 “浏览器对象” 章节。
说明
  * 当`id_or_num`不为`None`时，其它参数无效
  * `title`、`url`和`tab_type`三个参数是与关系
  * 如传入序号，序号与标签页视觉排序不一定一致，而是按照激活顺序排列。


```
from DrissionPage import Chromiumbrowser = Chromium()tab1 = browser.get_tab(1)# 获取列表中第一个标签页的对象tab2 = browser.get_tab('5399F4ADFE3A27503FFAA56390344EE5')# 获取指定id的标签页对象tab3 = browser.get_tab(url='DrissionPage.cn')# 获取第一个url中带 'DrissionPage.cn' 的标签页对象tabs = browser.get_tabs(url='DrissionPage.cn')# 获取所有url中带 'DrissionPage.cn' 的标签页对象
```

注意
Tab 对象默认为单例，即一个实体标签页只有一个`MixTab`对象。`get_tab()`返回的标签页可能是同一个。
### 📌 新建标签页并获取对象[​](https://www.drissionpage.cn/browser_control/tabs#-新建标签页并获取对��象 "📌 新建标签页并获取对象的直接链接")
`Chromium`对象的`new_tab()`方法用于新建一个标签页，返回其对象。
```
from DrissionPage import Chromiumbrowser = Chromium()browser.new_tab(url='http://DrissionPage.cn')
```

说明
当传入`url`参数时，程序会根据`load_mode`设置访问页面，除了`none`模式，都将等待页面加载完毕。 如果新建多个标签页不想等待，可批量新建不传入`url`参数的标签页，再遍历使用`get()`。
### 📌 获取点击后出现的标签页[​](https://www.drissionpage.cn/browser_control/tabs#-获取点击后出现的标签页 "📌 获取点击后出现的标签页的直接链接")
在预期点击元素会出现新标签页时，可用元素的`click.for_new_tab()`方法实行点击，点击后会返回新标签页对象。
具体参数见元素交互章节。
可直接运行以下示例：
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://DrissionPage.cn')ele = tab.ele('.wwads-cn wwads-horizontal').ele('tag:img')if ele:  tab2 = ele.click.for_new_tab()# 点击并获取新tab对象  tab2.set.activate()  ele2 = tab2.ele('确认访问', timeout=5)if ele2:    ele2.wait(.5).click()else:print('支持开源作者，请关闭广告屏蔽功能，谢谢。')
```

元素对象的`click.middle()`方法可用中键点击`<a>`元素，可强制在新标签页打开链接，并返回新标签页对象。
可直接运行以下示例：
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://DrissionPage.cn')ele = tab.ele('.wwads-cn wwads-horizontal').ele('tag:img')if ele:  tab2 = ele.click.middle()# 中键点击元素，并获取新tab对象  tab2.set.activate()  ele2 = tab2.ele('确认访问', timeout=5)if ele2:    ele2.wait(.5).click()else:print('支持开源作者，请关闭广告屏蔽功能，谢谢。')
```

## ✅️️ 多标签页协同[​](https://www.drissionpage.cn/browser_control/tabs#️️-多标签页协同 "✅️️ 多标签页协同的直接链接")
这个示例在一个标签页中遍历列表元素，点击打开新标签页，获取信息后关闭。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://gitee.com/explore/all')links = tab.eles('t:h3')for link in links[:-1]:# 点击链接并获取新标签页对象  new_tab = link.click.for_new_tab()# 等待新标签页加载  new_tab.wait.load_start()# 打印标签页标题print(new_tab.title)# 关闭新打开的标签页  new_tab.close()
```

## ✅️️ 使用多例[​](https://www.drissionpage.cn/browser_control/tabs#️️-使用多例 "✅️️ 使用多例的直接链接")
默认情况下，Tab 对象是单例的，即一个标签页只有一个对象，即使重复使用`get_tab()`，获取的都是同一个对象。
这主要是防止新手不理解机制，反复创建多个连接导致资源耗费。
实际上允许多个 Tab 对象同时操作一个标签页，每个负责不同的工作。比如一个执行主逻辑流程，另外的监视页面，处理各种弹窗。
要允许多例，可用`Settings`设置：
```
from DrissionPage.common import SettingsSettings.set_singleton_tab_obj(False)
```

**示例**
```
from DrissionPage import Chromiumfrom DrissionPage.common import Settingsbrowser = Chromium()browser.new_tab()browser.new_tab()# 未启用多例：tab1 = browser.get_tab(1)tab2 = browser.get_tab(1)print(id(tab1),id(tab2))# 启用多例：Settings.set_singleton_tab_obj(False)tab1 = browser.get_tab(1)tab2 = browser.get_tab(1)print(id(tab1),id(tab2))
```

**输出：**
```
2347582903056 23475829030562347588741840 2347588877712
```

可见第一次输出两个 Tab 对象是同一个，第二次输出是独立的。
[上一页🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)[下一页🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
  * [✅️️ 获取标签页对象](https://www.drissionpage.cn/browser_control/tabs#️️-获取标签页对象)
    * [📌 获取最后激活的标签页](https://www.drissionpage.cn/browser_control/tabs#-获取最后激活的标签页)
    * [📌 获取指定标签页](https://www.drissionpage.cn/browser_control/tabs#-获取指定标签页)
    * [📌 新建标签页并获取对象](https://www.drissionpage.cn/browser_control/tabs#-新建标签页并获取对象)
    * [📌 获取点击后出现的标签页](https://www.drissionpage.cn/browser_control/tabs#-获取点击后出现的标签页)
  * [✅️️ 多标签页协同](https://www.drissionpage.cn/browser_control/tabs#️️-多标签页协同)
  * [✅️️ 使用多例](https://www.drissionpage.cn/browser_control/tabs#️️-使用多例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/tabs)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/tabs)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
