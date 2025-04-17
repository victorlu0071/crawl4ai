# Content from: https://www.drissionpage.cn/browser_control/iframe

[跳到主要内容](https://www.drissionpage.cn/browser_control/iframe#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/iframe)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/iframe)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/iframe)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/iframe)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/iframe)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/iframe)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ iframe 操作


本页总览
# 🛰️ iframe 操作
`<iframe>`元素是一种特殊的元素，它既是元素，也是页面。
DrissionPage 无需切入切出即可处理`<iframe>`元素。 可实现跨级元素查找、元素内部单独跳转、同时操作`<iframe>`内外元素、多线程控制多个`<iframe>`等操作。
## ✅️ 获取`<iframe>`对象[​](https://www.drissionpage.cn/browser_control/iframe#️-获取iframe对象 "️-获取iframe对象的直接链接")
获取`<iframe>`对象的方法有两种，可用获取普通元素的方式获取，或者用`get_frame()`方法获取。
推荐优先使用`get_frame()`方法，因为当作普通元素获取时，IDE 无法正确识别获取到的是`<iframe>`元素。
### 📌 `get_frame()`[​](https://www.drissionpage.cn/browser_control/iframe#-get_frame "-get_frame的直接链接")
此方法用于获取页面中一个`<frame>`或`<iframe>`对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_ind_ele`| `str``int``ChromiumFrame`| 必填| 定位符`<iframe>`元素序号（从`1`开始，负数表示倒数）`ChromiumFrame对象``id`属性内容`name`属性内容  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面超时时间  
返回类型| 说明  
---|---  
`ChromiumFrame`| `<frame>`或`<iframe>`元素对象  
`NoneElement`| 找不到时返回`NoneElement`  
注意
需要特别注意的是，如果页面中有嵌套的`<iframe>`，用序号获取的方式会存在不准确。 比如，用`get_frames()`可获取到 6 个元素，但用`get_frame(6)`却获取不到最后一个。 这是因为有两个`<iframe>`是嵌套关系，导致获取不准确。
**示例：**
```
# 使用定位符获取iframe = tab.get_frame('t:iframe')# 获取第1个iframeiframe = tab.get_frame(1)
```

### 📌 `get_frames()`[​](https://www.drissionpage.cn/browser_control/iframe#-get_frames "-get_frames的直接链接")
此方法用于获取页面中多个符合条件的`<frame>`或`<iframe>`对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `None`| 定位符，为`None`时返回所有  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面超时时间  
返回类型| 说明  
---|---  
`List[ChromiumFrame]`| `<frame>`或`<iframe>`元素对象组成的列表  
提醒
获取所有`<iframe>`会很慢，而且浪费资源，一般使用获取需要用到的就好。
### 📌 普通元素方式[​](https://www.drissionpage.cn/browser_control/iframe#-普通元素方式 "📌 普通元素方式的直接链接")
可以用获取普通元素的方式获取`<iframe>`对象：
```
iframe = tab('t:iframe')
```

这个`ChromiumFrame`对象既是页面也是元素。由于 IDE 不会提示`<iframe>` 元素对象相关的属性和方法，因此用这种方式获取时建议再用`get_frame()`包装一下：
```
iframe = tab('t:iframe')iframe = tab.get_frame(iframe)
```

## ✅️ 查找`<iframe>`内元素[​](https://www.drissionpage.cn/browser_control/iframe#️-查找iframe内元素 "️-查找iframe内元素的直接链接")
当`<iframe>`与标签页是同域的，我们并不需要先切入`<iframe>`，就可以获取到里面的元素。
如果是异域的，则先要获取这个标签页的`ChromiumFrame`对象，再用这个对象在自己内部搜索。
### 📌 页面跨`<iframe>`查找[​](https://www.drissionpage.cn/browser_control/iframe#-页面跨iframe查找 "-页面跨iframe查找的直接链接")
如果`<iframe>`元素的网址和主页面是同域的，我们可以直接用页面对象查找`<iframe>`内部元素，而无需先获取`ChromiumFrame`对象。
以下示例页面中有一个`<iframe>`元素，和标签页是同域的，可直接通过 Tab 对象查找它内部的元素。
只要是同域名的，无论跨多少层`<iframe>`都能用页面对象直接获取。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn/demos/iframe_same_domain.html')ele = tab('概述')print(ele)
```

**输出：**
```
<ChromiumElement h2 class='anchor anchorWithStickyNavbar_LWe7' id='️-概述'>
```

### 📌 在`<iframe>`内查找[​](https://www.drissionpage.cn/browser_control/iframe#-在iframe内查找 "-在iframe内查找的直接链接")
如果`<iframe>`跟当前标签页是不同域名的，不能使用页面对象直接查找其中元素，只能先获取其`ChromiumFrame`元素对象，再在这个对象中查找。
即使是同域的，也可以通过这种方法查找。
但创建`ChromiumFrame`对象会增加系统资源的使用，一般建议异域的才创建对象。
以下示例页面中有一个`<iframe>`元素，和标签页是不同域的，需要先获取`ChromiumFrame`对象，再在里面找元素。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn/demos/iframe_diff_domain.html')iframe = tab.get_frame('t:iframe')ele = iframe('网易首页')print(ele)
```

**输出：**
```
<ChromiumElement a class='ntes-nav-index-title ntes-nav-entry-wide c-fl' href='https://www.163.com/' title='网易首页'>
```

## ✅️ 方法和属性[​](https://www.drissionpage.cn/browser_control/iframe#️-方法和属性 "✅️ 方法和属性的直接链接")
正如上面所说，`ChromiumFrame`既是元素也是页面，它可以获取自身元素方面的属性或执行操作。
详见相关章节。
```
iframe.tagiframe.htmliframe.remove_attr()iframe.states.is_aliveiframe.get()iframe.get_screenshot()# 等等
```

[上一页🛰️ 获取元素信息](https://www.drissionpage.cn/browser_control/get_ele_info)[下一页🛰️ 动作链](https://www.drissionpage.cn/browser_control/actions)
  * [✅️ 获取`<iframe>`对象](https://www.drissionpage.cn/browser_control/iframe#️-获取iframe对象)
    * [📌 `get_frame()`](https://www.drissionpage.cn/browser_control/iframe#-get_frame)
    * [📌 `get_frames()`](https://www.drissionpage.cn/browser_control/iframe#-get_frames)
    * [📌 普通元素方式](https://www.drissionpage.cn/browser_control/iframe#-普通元素方式)
  * [✅️ 查找`<iframe>`内元素](https://www.drissionpage.cn/browser_control/iframe#️-查找iframe内元素)
    * [📌 页面跨`<iframe>`查找](https://www.drissionpage.cn/browser_control/iframe#-页面跨iframe查找)
    * [📌 在`<iframe>`内查找](https://www.drissionpage.cn/browser_control/iframe#-在iframe内查找)
  * [✅️ 方法和属性](https://www.drissionpage.cn/browser_control/iframe#️-方法和属性)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/iframe)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/iframe)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
