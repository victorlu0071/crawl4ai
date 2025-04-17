# Content from: https://www.drissionpage.cn/browser_control/get_elements/intro

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/intro#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/intro)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/intro)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/intro)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/intro)
      * [🔦 概述](https://www.drissionpage.cn/browser_control/get_elements/intro)
      * [🔦 定位语法](https://www.drissionpage.cn/browser_control/get_elements/syntax)
      * [🔦 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
      * [🔦 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative)
      * [🔦 行为模式](https://www.drissionpage.cn/browser_control/get_elements/behavior)
      * [🔦 在结果列表中筛选](https://www.drissionpage.cn/browser_control/get_elements/filter)
      * [🔦 简化写法](https://www.drissionpage.cn/browser_control/get_elements/simplify)
      * [🔦 语法速查表](https://www.drissionpage.cn/browser_control/get_elements/sheet)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/intro)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 概述


本页总览
# 🔦 概述
定位元素是自动化重中之重的技能。 虽然可在开发者工具直接复制绝对路径，但这样做有几个缺点：
  * 代码冗长，可读性低
  * 动态页面容易导致元素失效
  * 无法使用相对定位
  * 网页稍有改动或者出现临时元素就不能用，容错性低
  * 无法跨`<iframe>`查找元素


因此作者极不建议使用右键复制的元素路径。
本库提供一套简洁易用的语法，用于快速定位元素，并且内置等待功能、支持链式查找，减少了代码的复杂性。 同时也兼容 css selector、xpath 和 selenium 原生的 loc 元组。
## ✅️️ 基本用法[​](https://www.drissionpage.cn/browser_control/get_elements/intro#️️-基本用法 "✅️️ 基本用法的直接链接")
所有页面对象和元素对象（包括`<iframe>`和 shadow-root），都可以在自己内部查找元素。
元素对象还能以自己为基准，相对定位其它元素。
定位元素大致有以下几种方法，将在后续小节中详细说明。
  * 在页面或元素内查找子元素
  * 根据 DOM 结构相对定位
  * 根据视觉位置相对定位


所有的查找元素方法，都可以使用本库自创的查找语法、xpath、css selector和 selenium 的定位符元组，去查找元素。
## ✅️️ 示例[​](https://www.drissionpage.cn/browser_control/get_elements/intro#️️-示例 "✅️️ 示例的直接链接")
### 📌 简单示例[​](https://www.drissionpage.cn/browser_control/get_elements/intro#-简单示例 "📌 简单示例的直接链接")
假设有这样一个页面：
```
<html><body><divid="one"><pclass="p_cls"name="row1">第一行</p><pclass="p_cls"name="row2">第二行</p><pclass="p_cls">第三行</p></div><divid="two">  第二个div</div></body></html>
```

我们可以用页面对象去获取其中的元素：
```
div1 = tab.ele('#one')# 获取 id 为 one 的元素p1 = tab.ele('@name=row1')# 获取 name 属性为 row1 的元素div2 = tab.ele('第二个div')# 获取包含“第二个div”文本的元素div_list = tab.eles('tag:div')# 获取所有div元素
```

也可以获取到一个元素，然后在它里面或周围查找元素：
```
div1 = tab.ele('#one')# 获取到一个元素div1p_list = div1.eles('tag:p')# 在div1内查找所有p元素div2 = div1.next()# 获取div1后面一个元素
```

### 📌 实际示例[​](https://www.drissionpage.cn/browser_control/get_elements/intro#-实际示例 "📌 实际示例的直接链接")
复制此代码可直接运行查看结果。
```
from DrissionPage import SessionPagepage = SessionPage()page.get('https://gitee.com/explore')# 获取包含“全部推荐项目”文本的 ul 元素ul_ele = page.ele('tag:ul@text():全部推荐项目')# 获取该 ul 元素下所有 a 元素titles = ul_ele.eles('tag:a')# 遍历列表，打印每个 a 元素的文本for i in titles:print(i.text)
```

**输出：**
```
全部推荐项目前沿技术智能硬件IOT/物联网/边缘计算车载应用...
```

[上一页🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)[下一页🔦 定位语法](https://www.drissionpage.cn/browser_control/get_elements/syntax)
  * [✅️️ 基本用法](https://www.drissionpage.cn/browser_control/get_elements/intro#️️-基本用法)
  * [✅️️ 示例](https://www.drissionpage.cn/browser_control/get_elements/intro#️️-示例)
    * [📌 简单示例](https://www.drissionpage.cn/browser_control/get_elements/intro#-简单示例)
    * [📌 实际示例](https://www.drissionpage.cn/browser_control/get_elements/intro#-实际示例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/intro)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/intro)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
