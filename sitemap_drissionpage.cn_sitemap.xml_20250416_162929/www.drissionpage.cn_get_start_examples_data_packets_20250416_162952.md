# Content from: https://www.drissionpage.cn/get_start/examples/data_packets

[跳到主要内容](https://www.drissionpage.cn/get_start/examples/data_packets#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/examples/data_packets)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/examples/data_packets)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/examples/data_packets)
    * [🗺️ 自动登录](https://www.drissionpage.cn/get_start/examples/control_browser)
    * [🗺️ 收发数据包](https://www.drissionpage.cn/get_start/examples/data_packets)
    * [🗺️ 模式切换](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * 🌏 上手示例
  * 🗺️ 收发数据包


本页总览
# 🗺️ 收发数据包
本示例演示用`SessionPage`已收发数据包的方式采集 gitee 网站数据。
本示例不使用浏览器。
## ✅️️ 页面分析[​](https://www.drissionpage.cn/get_start/examples/data_packets#️️-页面分析 "✅️️ 页面分析的直接链接")
网址：<https://gitee.com/explore/all>
这个示例的目标，要获取所有库的名称和链接，为避免对网站造成压力，我们只采集 3 页。
打开网址，按`F12`，我们可以看到页面 html 如下：
![](https://www.drissionpage.cn/assets/images/gitee_2-a46709588060c6c79e04dd943765307a.jpg)
从 html 代码中可以看到，所有开源项目的标题都是`class`属性为`'title project-namespace-path'`的`<a>`元素。我们可以遍历这些`<a>`元素，获取它们的信息。
同时，我们观察到，列表页网址是以页数为参数访问的，如第一页 url 为`https://gitee.com/explore/all?page=1`，页数就是`page`参数。因此我们可以通过修改这个参数访问不同的页面。
## ✅️️ 示例代码[​](https://www.drissionpage.cn/get_start/examples/data_packets#️️-示例代码 "✅️️ 示例代码的直接链接")
以下代码可直接运行并查看结果：
```
from DrissionPage import SessionPage# 创建页面对象page = SessionPage()# 爬取3页for i inrange(1,4):# 访问某一页的网页  page.get(f'https://gitee.com/explore/all?page={i}')# 获取所有开源库<a>元素列表  links = page.eles('.title project-namespace-path')# 遍历所有<a>元素for link in links:# 打印链接信息print(link.text, link.link)
```

**输出：**
```
小熊派开源社区/BearPi-HM_Nano https://gitee.com/bearpi/bearpi-hm_nano明月心/PaddleSegSharp https://gitee.com/raoyutian/PaddleSegSharpRockChin/QChatGPT https://gitee.com/RockChin/QChatGPTTopIAM/eiam https://gitee.com/topiam/eiam以下省略。。。
```

## ✅️️ 示例详解[​](https://www.drissionpage.cn/get_start/examples/data_packets#️️-示例详解 "✅️️ 示例详解的直接链接")
我们逐行解读代码：
```
from DrissionPage import SessionPage
```

↑ 首先，我们导入用于收发数据包的页面类`SessionPage`。
```
page = SessionPage()
```

↑ 接下来，我们创建一个`SessionPage`对象。
```
for i in ranage(1,4):  page.get(f'https://gitee.com/explore/all?page={i}')
```

↑ 然后我们循环 3 次，以构造每页的 url，每次都用`get()`方法访问该页网址。
```
  links = page.eles('.title project-namespace-path')
```

↑ 访问网址后，我们用页面对象的`eles()`获取页面中所有`class`属性为`'title project-namespace-path'`的元素对象。
`eles()`方法用于查找多个符合条件的元素，返回由它们组成的`list`。
这里查找的条件是`class`属性，`.`表示按`class`属性查找元素。
```
for link in links:print(link.text, link.link)
```

↑ 最后，我们遍历获取到的元素列表，获取每个元素的属性并打印出来。
`.text`获取元素的文本，`.link`获取元素的`href`或`src`属性。
[上一页🗺️ 自动登录](https://www.drissionpage.cn/get_start/examples/control_browser)[下一页🗺️ 模式切换](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [✅️️ 页面分析](https://www.drissionpage.cn/get_start/examples/data_packets#️️-页面分析)
  * [✅️️ 示例代码](https://www.drissionpage.cn/get_start/examples/data_packets#️️-示例代码)
  * [✅️️ 示例详解](https://www.drissionpage.cn/get_start/examples/data_packets#️️-示例详解)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/examples/data_packets)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/examples/data_packets)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
