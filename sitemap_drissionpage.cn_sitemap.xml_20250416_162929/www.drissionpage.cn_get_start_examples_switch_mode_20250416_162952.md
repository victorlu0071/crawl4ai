# Content from: https://www.drissionpage.cn/get_start/examples/switch_mode

[跳到主要内容](https://www.drissionpage.cn/get_start/examples/switch_mode#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/examples/switch_mode)
    * [🗺️ 自动登录](https://www.drissionpage.cn/get_start/examples/control_browser)
    * [🗺️ 收发数据包](https://www.drissionpage.cn/get_start/examples/data_packets)
    * [🗺️ 模式切换](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * 🌏 上手示例
  * 🗺️ 模式切换


本页总览
# 🗺️ 模式切换
这个示例演示标签页对象如何切换控制浏览器和收发数据包两种模式。
通常，切换模式是用来应付登录检查很严格的网站，可以用浏览器处理登录，再转换模式用收发数据包的形式来采集数据。 但是这种场景需要有对应的账号，不便于演示。演示使用浏览器在 gitee 搜索，然后转换到收发数据包的模式来读取数据。 虽然此示例现实使用意义不大，但可以了解其工作模式。
## ✅️️ 页面分析[​](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-页面分析 "✅️️ 页面分析的直接链接")
网址：<https://gitee.com/explore>
打开网址，按`F12`，我们可以看到页面 html 如下：
![](https://www.drissionpage.cn/assets/images/change1-bac86dfcdb35ce852aaa00390c5100f1.png)
输入框`<input>`元素`id`属性为`'q'`，搜索按钮`<button>`元素`文本`包含`'搜索'`文本，可用来作条件查找元素。
输入关键词搜索后，再查看页面 html：
![](https://www.drissionpage.cn/assets/images/change2-5177047ea61c4c245d44736eeb34d8fd.png)
通过分析 html 代码，我们可以看出，每个结果的标题都存在`id`为`'hits-list'`里面，`class`为`'item'`的元素中。因此，我们可以获取页面中所有这些元素，再遍历获取其信息。
## ✅️️ 示例代码[​](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-示例代码 "✅️️ 示例代码的直接链接")
您可以直接运行以下代码：
```
from DrissionPage import Chromium# 连接浏览器并获取一个MixTab对象tab = Chromium().latest_tab# 访问网址tab.get('https://gitee.com/explore/all')# 切换到收发数据包模式tab.change_mode()# 获取所有行元素items = tab.ele('.ui relaxed divided items explore-repo__list').eles('.item')# 遍历获取到的元素for item in items:# 打印元素文本print(item('t:h3').text)print(item('.project-desc mb-1').text)print()
```

**输出：**
```
dromara/Sa-Token一个轻量级 Java 权限认证框...lengleng/pig基于Spring Boot 3.3......
```

## ✅️️ 示例详解[​](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-示例详解 "✅️️ 示例详解的直接链接")
我们逐行解读代码：
```
from DrissionPage import Chromium
```

↑ 首先，我们导入用于控制浏览器的类`Chromium`。
```
tab = Chromium().latest_tab
```

↑ 接下来，们创建一个`Chromium`对象，用于连接浏览器，并用`latest_tab`获取一个可切换模式的标签页对象。
```
tab.get('https://gitee.com/explore')
```

↑ 然后控制浏览器访问 gitee。
```
tab.change_mode()
```

↑ `change_mode()`方法用于切换工作模式，从当前控制浏览器的模式切换到收发数据包模式。
切换的时候程序会在新模式重新访问当前 url。
```
items = tab('#hits-list').eles('.item')
```

↑ 切换后，我们可以用与控制浏览器一致的语法，获取页面元素，这获取页面中所有结果行素，它返回这些元素对象组成的列表。
```
for item in items:print(item('.title').text)print(item('.desc').text)print()
```

↑ 最后，我们遍历这些元素，并逐个打印它们包含的文本。
[上一页🗺️ 收发数据包](https://www.drissionpage.cn/get_start/examples/data_packets)[下一页☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)
  * [✅️️ 页面分析](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-页面分析)
  * [✅️️ 示例代码](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-示例代码)
  * [✅️️ 示例详解](https://www.drissionpage.cn/get_start/examples/switch_mode#️️-示例详解)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/examples/switch_mode)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
