# Content from: https://www.drissionpage.cn/get_start/before_start

[跳到主要内容](https://www.drissionpage.cn/get_start/before_start#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/get_start/before_start)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/get_start/before_start)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🌏 安装](https://www.drissionpage.cn/get_start/installation)
  * [🌏 导入](https://www.drissionpage.cn/get_start/import)
  * [🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)
  * [🌏 准备工作](https://www.drissionpage.cn/get_start/before_start)
  * [🌏 上手示例](https://www.drissionpage.cn/get_start/before_start)
  * [☀️ 基本概念](https://www.drissionpage.cn/get_start/concept)


  * [](https://www.drissionpage.cn/)
  * 🌏 准备工作


本页总览
# 🌏 准备工作
开始前，我们先设置一下浏览器路径。
如果只使用收发数据包功能，无需任何准备工作。
程序默认控制 Chrome，所以下面用 Chrome 演示。 如果要使用 Edge 或其它 Chromium 内核浏览器，设置方法是一样的。
注意
尽量使用版本号在 100 以上的浏览器，旧版有些功能不支持。
## 1️⃣ 尝试启动浏览器[​](https://www.drissionpage.cn/get_start/before_start#1️⃣-尝试启动浏览器 "1️⃣ 尝试启动浏览器的直接链接")
默认状态下，程序会自动在系统内查找 Chrome 路径。
执行以下代码，浏览器启动并且访问了项目官网，说明可直接使用，跳过后面的步骤即可。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')
```

## 2️⃣ 设置路径[​](https://www.drissionpage.cn/get_start/before_start#2️⃣-设置路径 "2️⃣ 设置路径的直接链接")
如果上面的步骤提示出错，说明程序没在系统里找到 Chrome 浏览器。
可用以下其中一种方法设置，设置会持久化记录到默认配置文件，之后程序会使用该设置启动。
获取浏览器路径的方法
  * 这里的浏览器路径不一定是 Chrome，Edge 等 Chromium 内核的浏览器都可以。
  * 打开浏览器，在地址栏输入`chrome://version`（Edge 输入`edge://version`），回车。 ![](https://www.drissionpage.cn/assets/images/find_browser_path-1b46b5e4ba053115091a598d3b4211ac.png) 如图所示，红框中就是要获取的路径。 此法不限于 Windows，有界面的 Linux 也可使用。


## 📌 方法一[​](https://www.drissionpage.cn/get_start/before_start#-方法一 "📌 方法一的直接链接")
新建一个临时 py 文件，并输入以下代码，填入您电脑里的 Chrome 浏览器可执行文件路径，然后运行。
```
from DrissionPage import ChromiumOptionspath =r'D:\Chrome\Chrome.exe'# 请改为你电脑内Chrome可执行文件路径ChromiumOptions().set_browser_path(path).save()
```

这段代码会把浏览器路径记录到配置文件，今后启动浏览器皆使用该路径。
如果是想临时切换浏览器路径以尝试运行和操作是否正常，可以去掉`.save()`，以如下方式结合第1️⃣步的代码。
```
from DrissionPage import Chromium, ChromiumOptionspath =r'D:\Chrome\Chrome.exe'# 请改为你电脑内Chrome可执行文件路径co = ChromiumOptions().set_browser_path(path)tab = Chromium(co).latest_tabtab.get('http://DrissionPage.cn')
```

## 📌 方法二[​](https://www.drissionpage.cn/get_start/before_start#-方法二 "📌 方法二的直接链接")
在命令行输入以下命令（路径改成自己电脑里的）：
```
dp -p "D:\Chrome\chrome.exe"
```

注意
  * 注意命令行的 python 环境与项目应是同一个
  * 注意要先使用 cd 命令定位到项目路径


## 3️⃣ 重试控制浏览器[​](https://www.drissionpage.cn/get_start/before_start#3️⃣-重试控制浏览器 "3️⃣ 重试控制浏览器的直接链接")
现在，请重新执行第1️⃣步的代码，如果正确访问了项目官网，说明已经设置完成。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')
```

## ✅️️ 说明[​](https://www.drissionpage.cn/get_start/before_start#️️-说明 "✅️️ 说明的直接链接")
当您完成准备工作后，无需关闭浏览器，后面的上手示例可继续接管当前浏览器。
[上一页🌏 设置语言 / Set Language](https://www.drissionpage.cn/get_start/set_lang)[下一页🗺️ 自动登录](https://www.drissionpage.cn/get_start/examples/control_browser)
  * [1️⃣ 尝试启动浏览器](https://www.drissionpage.cn/get_start/before_start#1️⃣-尝试启动浏览器)
  * [2️⃣ 设置路径](https://www.drissionpage.cn/get_start/before_start#2️⃣-设置路径)
  * [📌 方法一](https://www.drissionpage.cn/get_start/before_start#-方法一)
  * [📌 方法二](https://www.drissionpage.cn/get_start/before_start#-方法二)
  * [3️⃣ 重试控制浏览器](https://www.drissionpage.cn/get_start/before_start#3️⃣-重试控制浏览器)
  * [✅️️ 说明](https://www.drissionpage.cn/get_start/before_start#️️-说明)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/get_start/before_start)
  * [QQ群：391178600](https://www.drissionpage.cn/get_start/before_start)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
