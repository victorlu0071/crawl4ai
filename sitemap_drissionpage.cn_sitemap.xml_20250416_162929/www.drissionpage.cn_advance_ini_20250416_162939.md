# Content from: https://www.drissionpage.cn/advance/ini

[跳到主要内容](https://www.drissionpage.cn/advance/ini#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/ini)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/ini)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)
    * [⬇️ 下载文件](https://www.drissionpage.cn/download/intro)
    * [⚙️ 配置文件的使用](https://www.drissionpage.cn/advance/ini)
    * [⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)
    * [⚙️ 命令行的使用](https://www.drissionpage.cn/advance/commands)
    * [⚙️ 异常的使用](https://www.drissionpage.cn/advance/errors)
    * [⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)
    * [⚙️ 打包程序](https://www.drissionpage.cn/advance/packaging)
    * [⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
    * [⚙️ 与其它项目对接](https://www.drissionpage.cn/advance/docking)


  * [](https://www.drissionpage.cn/)
  * 🧰 进阶使用
  * ⚙️ 配置文件的使用


本页总览
# ⚙️ 配置文件的使用
本库使用 ini 文件记录浏览器或`Session`对象的启动配置。便于配置复用，免于在代码中加入繁琐的配置信息。 默认情况下，页面对象启动时自动加载文件中的配置信息。 也可以在默认配置基础上用简单的方法再次修改，再保存到 ini 文件。 也可以保存多个 ini 文件，按不同项目需要调用。
注意
  * ini 文件仅用于管理启动配置，页面对象创建后再修改 ini 文件是没用的。
  * 如果是接管已打开的浏览器，这些设置也没有用。
  * 每次升级本库，ini 文件都会被重置，可另存到其它路径以免重置。


## ✅️️ ini 文件内容[​](https://www.drissionpage.cn/advance/ini#️️-ini-文件内容 "✅️️ ini 文件内容的直接链接")
ini 文件初始内容如下。
```
[paths]download_path = tmp_path = [chromium_options]address = 127.0.0.1:9222browser_path = chromearguments = ['--no-default-browser-check', '--disable-suggestions-ui', '--no-first-run', '--disable-infobars', '--disable-popup-blocking', '--hide-crash-restore-bubble', '--disable-features=PrivacySandboxSettings4']extensions = []prefs = {'profile.default_content_settings.popups': 0, 'profile.default_content_setting_values': {'notifications': 2}}flags = {}load_mode = normaluser = Defaultauto_port = Falsesystem_user_path = Falseexisting_only = Falsenew_env = False[session_options]headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'connection': 'keep-alive', 'accept-charset': 'GB2312,utf-8;q=0.7,*;q=0.7'}[timeouts]base = 10page_load = 30script = 30[proxies]http =https = [others]retry_times = 3retry_interval = 2
```

## ✅️️ 文件位置[​](https://www.drissionpage.cn/advance/ini#️️-文件位置 "✅️️ 文件位置的直接链接")
默认配置文件存放在 DrissionPage 库 `'_configs'` 文件夹下，文件名为 configs.ini。 用户可另存其它配置文件，或从另存的文件读取配置，但默认文件的位置和名称不会改变。
## ✅️️ 使用默认配置文件启动[​](https://www.drissionpage.cn/advance/ini#️️-使用默认配置文件启动 "✅️️ 使用默认配置文件启动的直接链接")
### 📌 使用页面对象自动加载[​](https://www.drissionpage.cn/advance/ini#-使用页面对象自动加载 "📌 使用页面对象自动加载的直接链接")
这是默认启动方式。
```
from DrissionPage import Chromiumbrowser = Chromium()
```

### 📌 使用配置对象加载[​](https://www.drissionpage.cn/advance/ini#-使用配置对象加载 "📌 使用配置对象加载的直接链接")
这种方式一般用于加载配置后需要进一步修改。
```
from DrissionPage import ChromiumOptions, SessionOptions, Chromiumco = ChromiumOptions(ini_path=r'D:\setting.ini')so = SessionOptions(ini_path=r'D:\setting.ini')browser = Chromium(addr_or_opts=co, session_options=so)
```

## ✅️️ 保存/另存 ini 文件[​](https://www.drissionpage.cn/advance/ini#️️-保存另存-ini-文件 "✅️️ 保存/另存 ini 文件的直接链接")
```
from DrissionPage import ChromiumOptionsco = ChromiumOptions()# 修改一些设置co.no_imgs()# 保存到当前打开的ini文件co.save()# 保存到指定位置的配置文件co.save(r'D:\config1.ini')# 保存到默认配置文件co.save_to_default()
```

## ✅️️ 在项目路径使用 ini 文件[​](https://www.drissionpage.cn/advance/ini#️️-在项目路径使用-ini-文件 "✅️️ 在项目路径使用 ini 文件的直接链接")
默认 ini 文件存放在 DrissionPage 安装目录下，修改要通过代码进行，给调试带来不便。
因此，提供了一个便捷的方法把默认 ini 文件复制到当前项目文件夹，并且程序会优先使用项目文件夹下的 ini 文件进行初始化配置。
这样开发者可方便地手动更改配置。项目打包也可以直接打包而不会造成找不到文件问题。
复制到项目下的 ini 文件名为`'dp_configs.ini'`，程序会默认读取这个文件的配置。
### 📌 `configs_to_here()`[​](https://www.drissionpage.cn/advance/ini#-configs_to_here "-configs_to_here的直接链接")
此方法放在 `DrissionPage.common` 路径中，用于把默认 ini 文件复制到当前路径，并命名为`'dp_configs.ini'`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_name`| `str`| `None`| 指定文件名，为`None`则命名为`'dp_configs.ini'`  
**返回：**`None`
**示例：**
在项目新建一个 py 文件，输入以下内容并运行
```
from DrissionPage.common import configs_to_hereconfigs_to_here()
```

之后，项目文件夹会多出一个`'dp_configs.ini'`文件。页面对象初始化时会优先读取这个文件。
### 📌 用命令行复制[​](https://www.drissionpage.cn/advance/ini#-用命令行复制 "📌 用命令行复制的直接链接")
除了用`configs_to_here()`方法复制 ini 文件到项目文件夹，还可以用命令行方式复制。
在项目文件夹路径下运行以下命令即可：
```
dp --configs-to-here
```

效果和`configs_to_here()`一致，只是不能指定文件名。
[上一页⤵️ 浏览器下载](https://www.drissionpage.cn/download/browser)[下一页⚙️ 全局设置](https://www.drissionpage.cn/advance/settings)
  * [✅️️ ini 文件内容](https://www.drissionpage.cn/advance/ini#️️-ini-文件内容)
  * [✅️️ 文件位置](https://www.drissionpage.cn/advance/ini#️️-文件位置)
  * [✅️️ 使用默认配置文件启动](https://www.drissionpage.cn/advance/ini#️️-使用默认配置文件启动)
    * [📌 使用页面对象自动加载](https://www.drissionpage.cn/advance/ini#-使用页面对象自动加载)
    * [📌 使用配置对象加载](https://www.drissionpage.cn/advance/ini#-使用配置对象加载)
  * [✅️️ 保存/另存 ini 文件](https://www.drissionpage.cn/advance/ini#️️-保存另存-ini-文件)
  * [✅️️ 在项目路径使用 ini 文件](https://www.drissionpage.cn/advance/ini#️️-在项目路径使用-ini-文件)
    * [📌 `configs_to_here()`](https://www.drissionpage.cn/advance/ini#-configs_to_here)
    * [📌 用命令行复制](https://www.drissionpage.cn/advance/ini#-用命令行复制)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/ini)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/ini)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
