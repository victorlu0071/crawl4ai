# Content from: https://www.drissionpage.cn/get_start/concept

[跳到主要内容](https://www.drissionpage.cn/get_start/concept#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/concept)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/concept)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/concept)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * ☀️ 基本概念


本页总览
# ☀️ 基本概念
本节讲解 DrissionPage 的一些基本概念。了解它大概的构成。
如果您觉得有点懵，可直接跳过本节。
## ✅️️ 网页自动化[​](https://www.drissionpage.cn/get_start/concept#️️-网页自动化 "✅️️ 网页自动化的直接链接")
网页自动化的形式通常有两种，它们各有优劣：
  * 直接向服务器发送数据包，获取需要的数据
  * 控制浏览器跟网页进行交互


前者轻量级，速度快，便于多线程、分布式部署，如 requests 库。但当数据包构成复杂，甚至加入加密技术时，开发过程烧脑程度直线上升。
鉴于此，DrissionPage 以页面为单位将两者整合，对 Chromium 协议 和 requests 进行了重新封装，实现两种模式的互通，并加入常用的页面和元素控制功能，可大幅降低开发难度和代码量。 用于操作浏览器的对象叫 Driver，requests 用于管理连接的对象叫 Session，Drission 就是它们两者的合体。Page 表示以页面为单位使用。
在旧版本，本库是通过对 selenium 和 requests 的重新封装实现的。 从 3.0 版开始，作者另起炉灶，自行实现了 selenium 全部功能，从而摆脱了对 selenium 的依赖，功能更多更强，运行效率更高，开发更灵活。 4.0 则在 3.0 经验的基础上对整个项目底层进行了重构，逻辑更合理。
如果您想了解旧版，请查阅“旧版使用方法”章节。
## ✅️️ 基本使用逻辑[​](https://www.drissionpage.cn/get_start/concept#️️-基本使用逻辑 "✅️️ 基本使用逻辑的直接链接")
无论是控制浏览器，还是收发数据包，其操作逻辑是一致的。
即先创建页面对象，然后从页面对象中获取元素对象，通过对元素对象的读取或操作，实现数据的获取或页面的控制。
因此，最主要的对象就是两种：页面对象，及其生成的元素对象。
## ✅️️ 主要对象[​](https://www.drissionpage.cn/get_start/concept#️️-主要对象 "✅️️ 主要对象的直接链接")
### 📌 浏览器和标签页对象[​](https://www.drissionpage.cn/get_start/concept#-浏览器和标签页对象 "📌 浏览器和标签页对象的直接链接")
  * `Chromium`：浏览器对象，用于连接浏览器、管理标签页及其它和浏览器总体有关的操作
  * `MixTab`：浏览器标签页对象，由`Chromium`对象产生，一个对象控制一个实际的标签页
  * `ChromiumTab`：和`MixTab`一样也是标签页对象，由`ChromiumPage`对象产生，不可切换收发数据包模式


### 📌 元素对象[​](https://www.drissionpage.cn/get_start/concept#-元素对象 "📌 元素对象的直接链接")
  * `ChromiumElement`：浏览器元素对象
  * `SessionElement`：静态元素对象
  * `ChromiumFrame`：`<iframe>`元素对象，兼有标签页对象和元素特性
  * `ShadowRoot`：shadow-root 元素对象


### 📌 Page 对象[​](https://www.drissionpage.cn/get_start/concept#-page-对象 "📌 Page 对象的直接链接")
  * `ChromiumPage`：能管理浏览器本身的标签页对象，可用作程序入口
  * `WebPage`：类似于`ChromiumPage`，整合浏览器控制和收发数据包于一体的页面对象
  * `SessionPage`：单纯用于收发数据包的页面对象，可单独使用


### 📌 称呼[​](https://www.drissionpage.cn/get_start/concept#-称呼 "📌 称呼的直接链接")
文档里经常用到这几个称呼：
  * `MixTab`、`ChromiumTab`统称为 Tab 对象
  * `ChromiumPage`、`WebPage`和`SessionPage`统称为 Page 对象
  * Page 对象、Tab 对象和`ChromiumFrame`统称为页面对象


## ✅️️ 对象关系图[​](https://www.drissionpage.cn/get_start/concept#️️-对象关系图 "✅️️ 对象关系图的直接链接")
下图列出本库中要用到的各种对象的生成关系。
```
├─ SessionPage|   └─ SessionElement|      └─ SessionElement├─ Chrmoium|   └─ MixTab|      ├─ ChromiumElement|      |  ├─ ChromiumElement|      |  ├─ ChromiumFrame|      |  └─ SessionElement|      ├─ SessionElement|      |  └─ SessionElement|      ├─ ChromiumFrame|      |  ├─ ChromiumElement|      |  ├─ ChromiumFrame|      |  └─ SessionElement|      └─ ShadowRoot|        ├─ ChromiumElement|        ├─ ChromiumFrame|        └─ SessionElement├─ SessionOptions└─ ChrmoiumOptions
```

## ✅️️ 工作模式[​](https://www.drissionpage.cn/get_start/concept#️️-工作模式 "✅️️ 工作模式的直接链接")
`MixTab`和`WebPage`既可控制浏览器，也可用数据包方式访问网络数据。 它们有两种工作方式：d 模式和 s 模式。 页面对象可以在这两种模式间切换，两种模式拥有一致的使用方法，但任一时间只能处于其中一种模式。
### 📌 d 模式[​](https://www.drissionpage.cn/get_start/concept#-d-模式 "📌 d 模式的直接链接")
d 模式既表示 Driver，还有 Dynamic 的意思。 d 模式用于控制浏览器，不仅可以读取浏览器获取到的信息，还能对页面进行操作，如点击、填写、开关标签页、改变元素属性、执行 js 脚本等等。 d 模式功能强大，但运行速度受浏览器制约非常缓慢，而且需要占用大量内存。
### 📌 s 模式[​](https://www.drissionpage.cn/get_start/concept#-s-模式 "📌 s 模式的直接链接")
s 模式既表示 Session，还有 speed、silence 的意思。 s 模式的运行速度比 d 模式快几个数量级，但只能基于数据包进行读取或发送，不能对页面进行操作，不能运行 js。 爬取数据时，如网站数据包较为简单，应首选 s 模式。
### 📌 模式切换[​](https://www.drissionpage.cn/get_start/concept#-模式切换 "📌 模式切换的直接链接")
`MixTab`和`WebPage`对象可以在 d 模式和 s 模式之间切换，这通常用于以下情况：
  * 当登录验证很严格，难以解构，如有验证码的时候，用浏览器处理登录，然后转换成 s 模式爬取数据。既避免了处理烧脑的 js，又能享受 s 模式的速度。
  * 页面数据由 js 产生，且页面结构极其复杂，可以用 d 模式读取页面元素，然后把元素转成 s 模式的元素进行分析。可以极大地提高 d 模式的处理速度。


## ✅️️ 配置管理[​](https://www.drissionpage.cn/get_start/concept#️️-配置管理 "✅️️ 配置管理的直接链接")
无论 requests 还是浏览器，都通常需要一些配置信息才能正常工作，如长长的`user_agent`、浏览器 exe 文件路径、浏览器配置等。 这些代码往往是繁琐而重复的，不利于代码的简洁。 因此，DrissionPage 使用配置文件记录常用配置信息，程序会自动读取默认配置文件里的内容。 所以，在示例中，通常看不见配置信息的代码。
这个功能支持用户保存不同的配置文件，按情况调研，也可以支持直接把配置写在代码里面，屏蔽读取配置文件。
Tips
当需要打包程序时，必需把配置写到代码里，或打包后手动复制配置文件到运行路径，否则会报错。详见相关章节。
### 📌 `SessionOptions`[​](https://www.drissionpage.cn/get_start/concept#-sessionoptions "-sessionoptions的直接链接")
用于`SessionPage`和`WebPage` s 模式的配置对象。
### 📌 `ChromiumOptions`[​](https://www.drissionpage.cn/get_start/concept#-chromiumoptions "-chromiumoptions的直接链接")
用于用于浏览器的配置对象。
## ✅️️ 定位符[​](https://www.drissionpage.cn/get_start/concept#️️-定位符 "✅️️ 定位符的直接链接")
定位符用于定位页面中的元素，是本库一大特色，能够用非常简明的方式来获取元素，简洁易用。 可读性和易用性高于 xpath 等其它方式，并且兼容 xpath、css selector、selenium 定位符。
以下是一组对比：
定位文本包含`'abc'`的元素：
```
# DrissionPageele = tab('abc')# seleniumele = driver.find_element(By.XPATH,'//*[contains(text(), "abc"]')
```

定位 class 为`'abc'`的元素：
```
# DrissionPageele = tab('.abc')# seleniumele = driver.find_element(By.CLASS_NAME,'abc')
```

定位 ele 元素的兄弟元素：
```
# DrissionPageele1 = ele.next()# 获取后一个元素ele1 = ele.prev(index=2)# 获取前面第二个元素# seleniumele1 = ele.find_element(By.XPATH,'.//following-sibling::*')# 获取有i一个元素ele1 = ele.find_element(By.XPATH,'.//preceding-sibling::*[2]')# 获取前面第二个元素
```

显然，本库的定位语句更简洁易懂，还有很多灵活好用的方法，详见 “查找元素” 章节。
[上一页🗺️ 模式切换](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [✅️️ 网页自动化](https://www.drissionpage.cn/get_start/concept#️️-网页自动化)
  * [✅️️ 基本使用逻辑](https://www.drissionpage.cn/get_start/concept#️️-基本使用逻辑)
  * [✅️️ 主要对象](https://www.drissionpage.cn/get_start/concept#️️-主要对象)
    * [📌 浏览器和标签页对象](https://www.drissionpage.cn/get_start/concept#-浏览器和标签页对象)
    * [📌 元素对象](https://www.drissionpage.cn/get_start/concept#-元素对象)
    * [📌 Page 对象](https://www.drissionpage.cn/get_start/concept#-page-对象)
    * [📌 称呼](https://www.drissionpage.cn/get_start/concept#-称呼)
  * [✅️️ 对象关系图](https://www.drissionpage.cn/get_start/concept#️️-对象关系图)
  * [✅️️ 工作模式](https://www.drissionpage.cn/get_start/concept#️️-工作模式)
    * [📌 d 模式](https://www.drissionpage.cn/get_start/concept#-d-模式)
    * [📌 s 模式](https://www.drissionpage.cn/get_start/concept#-s-模式)
    * [📌 模式切换](https://www.drissionpage.cn/get_start/concept#-模式切换)
  * [✅️️ 配置管理](https://www.drissionpage.cn/get_start/concept#️️-配置管理)
    * [📌 `SessionOptions`](https://www.drissionpage.cn/get_start/concept#-sessionoptions)
    * [📌 `ChromiumOptions`](https://www.drissionpage.cn/get_start/concept#-chromiumoptions)
  * [✅️️ 定位符](https://www.drissionpage.cn/get_start/concept#️️-定位符)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/concept)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/concept)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
