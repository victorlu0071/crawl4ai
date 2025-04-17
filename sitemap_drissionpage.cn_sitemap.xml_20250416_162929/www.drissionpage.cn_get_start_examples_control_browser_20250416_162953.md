# Content from: https://www.drissionpage.cn/get_start/examples/control_browser

[跳到主要内容](https://www.drissionpage.cn/get_start/examples/control_browser#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/examples/control_browser)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/examples/control_browser)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/examples/control_browser)
    * [🗺️ 自动登录](https://www.drissionpage.cn/get_start/examples/control_browser)
    * [🗺️ 收发数据包](https://www.drissionpage.cn/get_start/examples/data_packets)
    * [🗺️ 模式切换](https://www.drissionpage.cn/get_start/examples/switch_mode)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * 🌏 上手示例
  * 🗺️ 自动登录


本页总览
# 🗺️ 自动登录
本示例演示控制浏览器登录 gitee 网站。
## ✅️️ 页面分析[​](https://www.drissionpage.cn/get_start/examples/control_browser#️️-页面分析 "✅️️ 页面分析的直接链接")
网址：<https://gitee.com/login>
打开网址，按`F12`，我们可以看到页面 html 如下：
![](https://www.drissionpage.cn/assets/images/gitee_1-a0c506a07b80ba8c2713bf306a475c2e.jpg)
用户名输入框`id`为`'user_login'`，密码输入框`id`为`'user_password'`，登录按钮`value`为`'登 录'`。
我们可以用这三个属性定位这三个元素，然后对其输入数据和点击。
## ✅️️ 示例代码[​](https://www.drissionpage.cn/get_start/examples/control_browser#️️-示例代码 "✅️️ 示例代码的直接链接")
您可以把以下代码复制到编辑器，把账号和密码改为您自己的，可直接执行看到运行结果。
```
from DrissionPage import Chromium# 启动或接管浏览器，并获取标签页对象tab = Chromium().latest_tab# 跳转到登录页面tab.get('https://gitee.com/login')# 定位到账号文本框，获取文本框元素ele = tab.ele('#user_login')# 输入对文本框输入账号ele.input('您的账号')# 定位到密码文本框并输入密码tab.ele('#user_password').input('您的密码')# 点击登录按钮tab.ele('@value=登 录').click()
```

## ✅️️ 示例详解[​](https://www.drissionpage.cn/get_start/examples/control_browser#️️-示例详解 "✅️️ 示例详解的直接链接")
我们逐行解读代码：
```
from DrissionPage import Chromium
```

↑ 首先，我们导入用于控制浏览器的类`Chromium`。
```
tab = Chromium().latest_tab
```

↑ 接下来，我们创建一个`Chromium`对象，用于连接浏览器，并用`latest_tab`获取一个标签页对象。
```
tab.get('https://gitee.com/login')
```

↑ `get()`方法用于访问参数中的网址。它会等待页面完全加载，再继续执行后面的代码。 您也可以修改等待策略，如等待 DOM 加载而不等待资源下载，就停止加载，这将在后面的章节说明。
```
ele = tab.ele('#user_login')
```

↑ `ele()`方法用于查找元素，它返回一个`ChromiumElement`对象，用于操作元素。
`'#user_login'`是定位符文本，`#`意思是按`id`属性查找元素。
值得一提的是，`ele()`内置了等待，如果元素未加载，它会执行等待，直到元素出现或到达时限。默认超时时间 10 秒。
```
ele.input('您的账号')
```

↑ `input()`方法用于对元素输入文本。
```
tab.ele('#user_password').input('您的密码')
```

↑ 我们也可以进行链式操作，获取元素后直接输入文本。
```
tab.ele('@value=登 录').click()
```

↑ 输入账号密码后，以相同的方法获取按钮元素，并对其执行点击操作。
不同的是，这次通过其`value`属性作为查找条件。`@`表示按属性名查找。
到这里，我们已完成了自动登录 gitee 网站的操作。
[上一页🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)[下一页🗺️ 收发数据包](https://www.drissionpage.cn/get_start/examples/data_packets)
  * [✅️️ 页面分析](https://www.drissionpage.cn/get_start/examples/control_browser#️️-页面分析)
  * [✅️️ 示例代码](https://www.drissionpage.cn/get_start/examples/control_browser#️️-示例代码)
  * [✅️️ 示例详解](https://www.drissionpage.cn/get_start/examples/control_browser#️️-示例详解)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/examples/control_browser)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/examples/control_browser)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
