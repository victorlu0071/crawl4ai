# Content from: https://www.drissionpage.cn/advance/packaging

[跳到主要内容](https://www.drissionpage.cn/advance/packaging#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/advance/packaging)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/advance/packaging)
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
  * ⚙️ 打包程序


本页总览
# ⚙️ 打包程序
本节介绍打包程序需要注意的事项。
## ✅️️ 使用新的虚拟环境！[​](https://www.drissionpage.cn/advance/packaging#️️-使用新的虚拟环境 "✅️️ 使用新的虚拟环境！的直接链接")
养成打包的良好习惯，使用新建的虚拟环境，只安装必要的库去打包，可以使打包出来的 exe 文件体积缩小。 在只安装 DrissionPage 的环境中打包出来的程序，大小约为 14M。
如果您打包出来的程序体积巨大，请尝试这个方法。
## ✅️️ 解决 ini 不存在报错[​](https://www.drissionpage.cn/advance/packaging#️️-解决-ini-不存在报错 "✅️️ 解决 ini 不存在报错的直接链接")
说明
从`v4.0.4.1`开始不存在这个报错，以下是此版本之前打包报错的解决方法。
因为程序用到 ini 文件，而打包时不会自动带上，因此直接打包是会导致运行出错。
解决办法：
  * 手动带上 ini 文件，并在程序中指定路径
  * 把配置信息写在程序中，不带 ini 文件


### 📌 带上 ini 文件[​](https://www.drissionpage.cn/advance/packaging#-带上-ini-文件 "📌 带上 ini 文件的直接链接")
在程序中用相对路径方式指定 ini 文件，把 ini 文件复制到程序文件夹。
```
from DrissionPage import Chromium, ChromiumOptions, SessionOptionsco = ChromiumOptions(ini_path=r'.\configs.ini')so = SessionOptions(ini_path=r'.\configs.ini')browser = Chromium(addr_or_opts=co, session_options=so)
```

可以使用`configs_to_here()`方法自动复制 ini 文件。
在项目新建一个 py 文件，输入以下内容并运行
```
from DrissionPage.common import configs_to_hereconfigs_to_here()
```

之后，项目文件夹会多出一个`'dp_configs.ini'`文件。页面对象初始化时会优先读取这个文件。
把它和打包出来的可执行文件放在一起即可。
### 📌 不使用 ini[​](https://www.drissionpage.cn/advance/packaging#-不使用-ini "📌 不使用 ini的直接链接")
在程序中指定不使用 ini 文件，就不会报错。这种方法需把所有配置信息写到代码里。
```
from DrissionPage import Chromium, ChromiumOptions, SessionOptionsco = ChromiumOptions(read_file=False)# 不读取文件方式新建配置对象co.set_browser_path(r'.\chrome.exe')# 输入配置信息so = SessionOptions(read_file=False)browser = Chromium(addr_or_opts=co, session_options=so)
```

注意，这个时候 driver 和 session 两个参数都要输入内容，如果其中一个不需要设置可以输入`False`：
```
browser = Chromium(addr_or_opts=co, session_or_options=False)
```

## ✅️️ 实用示例[​](https://www.drissionpage.cn/advance/packaging#️️-实用示例 "✅️️ 实用示例的直接链接")
通常，我会把一个绿色浏览器和打包后的 exe 文件放在一起，程序中用相对路径指向该浏览器，这样拿到别的电脑也可以正常使用。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions(read_file=False).set_paths(local_port='9888',                        browser_path=r'.\Chrome\chrome.exe',                        user_data_path=r'.\Chrome\userData')browser = Chromium(addr_or_opts=co, session_options=False)# 注意：session_or_options=Falsetab = browser.latest_tabtab.get('http://DrissionPage.cn')
```

注意以下两点，程序就会跳过读取 ini 文件：
  * `ChromiumOptions()`里要设置`read_file=False`
  * 如果不传入某个模式的配置（示例中为 s 模式），要在页面对象初始化时设置对应参数为`False`


[上一页⚙️ 数据读取加速](https://www.drissionpage.cn/advance/accelerate)[下一页⚙️ 实用工具](https://www.drissionpage.cn/advance/tools)
  * [✅️️ 使用新的虚拟环境！](https://www.drissionpage.cn/advance/packaging#️️-使用新的虚拟环境)
  * [✅️️ 解决 ini 不存在报错](https://www.drissionpage.cn/advance/packaging#️️-解决-ini-不存在报错)
    * [📌 带上 ini 文件](https://www.drissionpage.cn/advance/packaging#-带上-ini-文件)
    * [📌 不使用 ini](https://www.drissionpage.cn/advance/packaging#-不使用-ini)
  * [✅️️ 实用示例](https://www.drissionpage.cn/advance/packaging#️️-实用示例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/advance/packaging)
  * [QQ群：391178600](https://www.drissionpage.cn/advance/packaging)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
