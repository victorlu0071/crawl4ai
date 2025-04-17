# Content from: https://www.drissionpage.cn/get_start/import

[跳到主要内容](https://www.drissionpage.cn/get_start/import#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/import)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/import)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/import)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * 🌏 导入


本页总览
# 🌏 导入
DrissionPage 提供的功能放在以下几个路径：
  * `from DrissionPage import ****`：浏览器类、配置类、页面类
  * `from DrissionPage.errors import ****`：异常
  * `from DrissionPage.common import ****`：辅助工具
  * `from DrissionPage.items import ****`：衍生对象，用于类型判断


## ✅️ 浏览器类[​](https://www.drissionpage.cn/get_start/import#️-浏览器类 "✅️ 浏览器类的直接链接")
### 📌 `Chromium`[​](https://www.drissionpage.cn/get_start/import#-chromium "-chromium的直接链接")
浏览器类用于连接浏览器、管理标签页及其它和浏览器总体有关的操作。
浏览器类相当于总管，它可以作为浏览器入口，使用它产生 Tab 对象去操控每个标签页。
```
from DrissionPage import Chromium
```

## ✅️ 页面类[​](https://www.drissionpage.cn/get_start/import#️-页面类 "✅️ 页面类的直接链接")
### 📌 `ChromiumPage`[​](https://www.drissionpage.cn/get_start/import#-chromiumpage "-chromiumpage的直接链接")
`ChromiumPage`是将浏览器对象和第一个标签页对象封装在一起，用于控制浏览器。
`ChromiumPage`只是简化了操作，使用效果和直接使用`Chromium`对象基本一致。
唯一区别是，`ChromiumPage`生成的标签页对象是`ChromiumTab`，不能切换模式。
```
from DrissionPage import ChromiumPage
```

### 📌 `WebPage`[​](https://www.drissionpage.cn/get_start/import#-webpage "-webpage的直接链接")
`WebPage`与`ChromiumPage`相似，不过其自身及其产生的 Tab 对象可切换模式，既可控制浏览器，也可收发数据包。
```
from DrissionPage import WebPage
```

### 📌 `SessionPage`[​](https://www.drissionpage.cn/get_start/import#-sessionpage "-sessionpage的直接链接")
`SessionPage`用于收发数据包，是对 requests 和 lxml 进行封装实现的。
它把网络连接和结果解析封装成页面。操作逻辑和其它页面一致。
```
from DrissionPage import SessionPage
```

## ✅️ 配置工具[​](https://www.drissionpage.cn/get_start/import#️-配置工具 "✅️ 配置工具的直接链接")
### 📌 `ChromiumOptions`[​](https://www.drissionpage.cn/get_start/import#-chromiumoptions "-chromiumoptions的直接链接")
`ChromiumOptions`类用于设置浏览器启动参数。
这些参数只有在启动浏览器时有用，接管已存在的浏览器时是不生效的。
```
from DrissionPage import ChromiumOptions
```

### 📌 `SessionOptions`[​](https://www.drissionpage.cn/get_start/import#-sessionoptions "-sessionoptions的直接链接")
`SessionOptions`类用于设置`Session`对象启动参数。
用于配置`SessionPage`或`WebPage`的 s 模式的连接参数。
```
from DrissionPage import SessionOptions
```

### 📌 `Settings`[​](https://www.drissionpage.cn/get_start/import#-settings "-settings的直接链接")
`Settings`用于设置全局运行配置，如找不到元素时是否抛出异常等。
```
from DrissionPage.common import Settings
```

## ✅️ 辅助工具[​](https://www.drissionpage.cn/get_start/import#️-辅助工具 "✅️ 辅助工具的直接链接")
### 📌 `Keys`[​](https://www.drissionpage.cn/get_start/import#-keys "-keys的直接链接")
键盘按键类，用于键入 ctrl、alt 等按键。
```
from DrissionPage.common import Keys
```

### 📌 `By`[​](https://www.drissionpage.cn/get_start/import#-by "-by的直接链接")
与 selenium 一致的`By`类，便于项目迁移。
```
from DrissionPage.common import By
```

### 📌 其它工具[​](https://www.drissionpage.cn/get_start/import#-其它工具 "📌 其它工具的直接链接")
这些工具都在`DrissionPage.common`路径中。
  * `wait_until`：可等待传入的方法结果为真
  * `make_session_ele`：从 html 文本生成`ChromiumElement`对象
  * `configs_to_here`：把配置文件复制到当前路径
  * `get_blob`：获取指定的 blob 资源
  * `tree`：用于打印页面对象或元素对象结构
  * `from_selenium`：用于对接 selenium 代码
  * `from_playwright`：用于对接 playwright 代码


```
from DrissionPage.common import wait_untilfrom DrissionPage.common import make_session_elefrom DrissionPage.common import configs_to_here
```

## ✅️ 异常[​](https://www.drissionpage.cn/get_start/import#️-异常 "✅️ 异常的直接链接")
异常放在`DrissionPage.errors`路径。
全部异常详见进阶使用章节。
```
from DrissionPage.errors import ElementNotFoundError
```

## ✅️ 衍生对象类型[​](https://www.drissionpage.cn/get_start/import#️-衍生对象类型 "✅️ 衍生对象类型的直接链接")
Tab、Element 等被其它对象生成的对象，开发过程中需要类型判断时需要导入这些类型。
可在`DrissionPage.items`路径导入。
```
from DrissionPage.items import SessionElementfrom DrissionPage.items import ChromiumElementfrom DrissionPage.items import ShadowRootfrom DrissionPage.items import NoneElementfrom DrissionPage.items import ChromiumTabfrom DrissionPage.items import MixTabfrom DrissionPage.items import ChromiumFrame
```

[上一页🌏 安装](https://www.drissionpage.cn/get_start/installation)[下一页🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [✅️ 浏览器类](https://www.drissionpage.cn/get_start/import#️-浏览器类)
    * [📌 `Chromium`](https://www.drissionpage.cn/get_start/import#-chromium)
  * [✅️ 页面类](https://www.drissionpage.cn/get_start/import#️-页面类)
    * [📌 `ChromiumPage`](https://www.drissionpage.cn/get_start/import#-chromiumpage)
    * [📌 `WebPage`](https://www.drissionpage.cn/get_start/import#-webpage)
    * [📌 `SessionPage`](https://www.drissionpage.cn/get_start/import#-sessionpage)
  * [✅️ 配置工具](https://www.drissionpage.cn/get_start/import#️-配置工具)
    * [📌 `ChromiumOptions`](https://www.drissionpage.cn/get_start/import#-chromiumoptions)
    * [📌 `SessionOptions`](https://www.drissionpage.cn/get_start/import#-sessionoptions)
    * [📌 `Settings`](https://www.drissionpage.cn/get_start/import#-settings)
  * [✅️ 辅助工具](https://www.drissionpage.cn/get_start/import#️-辅助工具)
    * [📌 `Keys`](https://www.drissionpage.cn/get_start/import#-keys)
    * [📌 `By`](https://www.drissionpage.cn/get_start/import#-by)
    * [📌 其它工具](https://www.drissionpage.cn/get_start/import#-其它工具)
  * [✅️ 异常](https://www.drissionpage.cn/get_start/import#️-异常)
  * [✅️ 衍生对象类型](https://www.drissionpage.cn/get_start/import#️-衍生对象类型)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/import)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/import)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
