# Content from: https://www.drissionpage.cn/browser_control/connect_browser

[跳到主要内容](https://www.drissionpage.cn/browser_control/connect_browser#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/connect_browser)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/connect_browser)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/connect_browser)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/connect_browser)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/connect_browser)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 连接浏览器


本页总览
# 🛰️ 连接浏览器
`Chromium`对象用于连接和管理浏览器。标签页的开关和获取、整体运行参数配置、浏览器信息获取等都由它进行。
根据不同的配置，可以接管已打开的浏览器，也可以启动新的浏览器。
每个浏览器只能有一个`Chromium`对象（同一进程中）。对同一个浏览器重复使用`Chromium()`获取的都是同一个对象。
Tips
程序结束时，被打开的浏览器不会主动关闭（VSCode 启动的除外），以便下次运行程序时使用。 新手在使用无头模式时需注意，程序关闭后其实浏览器进程还在，只是看不见。
## ✅️ `Chromium`初始化参数[​](https://www.drissionpage.cn/browser_control/connect_browser#️-chromium初始化参数 "️-chromium初始化参数的直接链接")
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`addr_or_opts`| `str``int``ChromiumOptions`| `None`| 浏览器启动配置或接管信息。传入 'ip: port' 字符串、端口数字或`ChromiumOptions`对象时按配置启动或接管浏览器；为`None`时使用配置文件配置启动浏览器  
`session_options`| `SessionOptions``None``False`| `None`| 使用双模 Tab 时使用的默认 Session 配置，为`None`使用 ini 文件配置，为`False`不从 ini 读取  
## ✅️ 直接创建[​](https://www.drissionpage.cn/browser_control/connect_browser#️-直接创建 "✅️ 直接创建的直接链接")
### 📌 默认方式[​](https://www.drissionpage.cn/browser_control/connect_browser#-默认方式 "📌 默认方式的直接链接")
这种方式代码最简洁，程序会使用默认配置，自动生成页面对象。
```
from DrissionPage import Chromiumbrowser = Chromium()
```

创建`Chromium`对象时会在指定端口启动浏览器，或接管该端口已有浏览器。
默认情况下，程序使用 9222 端口，浏览器可执行文件路径为`'chrome'`。
如路径中没找到浏览器可执行文件，Windows 系统下程序会在注册表中查找路径。
如果都没找到，则要用下文介绍的手动配置方法。
直接创建时，程序默认读取 ini 文件配置，如 ini 文件不存在，会使用内置配置。
默认 ini 和内置配置信息详见“进阶使用->配置文件的使用”章节。
Tips
您可以修改配置文件中的配置，实现所有程序都按您的需要进行启动，详见”启动配置“章节。
### 📌 指定端口或地址[​](https://www.drissionpage.cn/browser_control/connect_browser#-指定端口或地址 "📌 指定端口或地址的直接链接")
创建`Chromium`对象时向`addr_or_opts`参数传入端口号或地址，可接管指定端口浏览器，若端口空闲，使用默认配置在该端口启动一个浏览器。
传入端口时用`int`类型，传入地址时用`'address:port'`格式。
```
# 接管9333端口的浏览器，如该端口空闲，启动一个浏览器browser = Chromium(9333)browser = Chromium('127.0.0.1:9333')
```

## ✅️ 通过配置信息创建[​](https://www.drissionpage.cn/browser_control/connect_browser#️-通过配置信息创建 "✅️ 通过配置信息创建的直接链接")
如果需要已指定方式启动浏览器，可使用`ChromiumOptions`。它是专门用于设置浏览器初始状态的类，内置了常用的配置。详细使用方法见“浏览器启动配置”一节。
### 📌 使用方法[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用方法 "📌 使用方法的直接链接")
`ChromiumOptions`用于管理创建浏览器时的配置，内置了常用的配置，并能实现链式操作。详细使用方法见“启动配置”一节。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`read_file`| `bool`| `True`| 是否从 ini 文件中读取配置信息，如果为`False`则用默认配置创建  
`ini_path`| `str`| `None`| 文件路径，为`None`则读取默认 ini 文件  
注意
  * 配置对象只有在启动浏览器时生效。
  * 浏览器创建后再修改这个配置是没有效果的。
  * 接管已打开的浏览器配置也不会生效。


```
# 导入 ChromiumOptionsfrom DrissionPage import Chromium, ChromiumOptions# 创建浏览器配置对象，指定浏览器路径co = ChromiumOptions().set_browser_path(r'D:\chrome.exe')# 用该配置创建页面对象browser = Chromium(addr_or_opts=co)
```

### 📌 使用指定 ini 文件创建[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用指定-ini-文件创建 "📌 使用指定 ini 文件创建的直接链接")
以上方法是使用默认 ini 文件中保存的配置信息创建对象，你可以保存一个 ini 文件到别的地方，并在创建对象时指定使用它。
```
from DrissionPage import Chromium, ChromiumOptions# 创建配置对象时指定要读取的ini文件路径co = ChromiumOptions(ini_path=r'./config1.ini')# 使用该配置对象创建页面browser = Chromium(addr_or_opts=co)
```

## ✅️ 接管已打开的浏览器[​](https://www.drissionpage.cn/browser_control/connect_browser#️-接管已打开的浏览器 "✅️ 接管已打开的浏览器的直接链接")
页面对象创建时，只要指定的地址（ip:port）已有浏览器在运行，就会直接接管。无论浏览器是下面哪种方式启动的。
### 📌 用程序启动的浏览器[​](https://www.drissionpage.cn/browser_control/connect_browser#-用程序启动的浏览器 "📌 用程序启动的浏览器的直接链接")
默认情况下，创建浏览器页面对象时会自动启动一个浏览器。只要这个浏览器不关闭，下次运行程序时会接管同一个浏览器继续操作（配置的 ip:port 信息不变）。
这种方式极大地方便了程序的调试，使程序不必每次重新开始，可以单独调试某个功能。
```
from DrissionPage import Chromium# 在9333端口启动浏览器同时创建对象，如果浏览器已经存在，则接管它browser = Chromium(9333)
```

### 📌 手动打开的浏览器[​](https://www.drissionpage.cn/browser_control/connect_browser#-手动打开的浏览器 "📌 手动打开的浏览器的直接链接")
如果需要手动打开浏览器再接管，可以这样做：
  1. 右键点击浏览器图标，选择属性
  2. 在“目标”路径后面加上` --remote-debugging-port=端口号`（注意最前面有个空格）
  3. 点击确定
  4. 在程序中的浏览器配置中指定接管该端口浏览器


文件快捷方式的目标路径设置：
```
"D:\chrome.exe" --remote-debugging-port=9333
```

程序代码：
```
from DrissionPage import Chromiumbrowser = Chromium(9333)
```

注意
接管浏览器时只有`local_port`、`address`参数是有效的。
### 📌 bat 文件启动的浏览器[​](https://www.drissionpage.cn/browser_control/connect_browser#-bat-文件启动的浏览器 "📌 bat 文件启动的浏览器的直接链接")
可以把上一种方式的目标路径设置写进 bat 文件（Windows系统），运行 bat 文件来启动浏览器，再用程序接管。
新建一个文本文件，在里面输入以下内容（路径改为自己电脑的）：
```
"D:\chrome.exe" --remote-debugging-port=9333
```

保存后把后缀改成 bat，然后双击运行就能在 9333 端口启动一个浏览器。程序代码则和上一个方法一致。
## ✅️ 多浏览器共存[​](https://www.drissionpage.cn/browser_control/connect_browser#️-多浏览器共存 "✅️ 多浏览器共存的直接链接")
如果想要同时操作多个浏览器，或者自己在使用其中一个上网，同时控制另外几个跑自动化，就需要给这些被程序控制的浏览器设置单独的 **端口** 和 **用户文件夹** ，否则会造成冲突。
### 📌 指定独立端口和数据文件夹[​](https://www.drissionpage.cn/browser_control/connect_browser#-指定独立端口和数据文件夹 "📌 指定独立端口和数据文件夹的直接链接")
每个要启动的浏览器使用一个独立的`ChromiumOptions`对象进行设置：
```
from DrissionPage import Chromium, ChromiumOptions# 创建多个配置对象，每个指定不同的端口号和用户文件夹路径co1 = ChromiumOptions().set_paths(local_port=9111, user_data_path=r'D:\data1')co2 = ChromiumOptions().set_paths(local_port=9222, user_data_path=r'D:\data2')# 创建多个页面对象tab1 = Chromium(addr_or_opts=co1).latest_tabtab2 = Chromium(addr_or_opts=co2).latest_tab# 每个页面对象控制一个浏览器tab1.get('http://DrissionPage.cn')tab2.get('https://www.baidu.com')
```

注意
每个浏览器都要设置独立的端口号和用户文件夹，二者缺一不可。
### 📌 `auto_port()`方法[​](https://www.drissionpage.cn/browser_control/connect_browser#-auto_port方法 "-auto_port方法的直接链接")
`ChromiumOptions`对象的`auto_port()`方法，可以指定程序每次使用空闲的端口和临时用户文件夹创建浏览器。
使用`auto_port()`的配置对象可由多个`Chromium`对象共用，不会出现冲突。
这种方式创建的浏览器是全新不带任何数据的，并且运行数据会自动清除。
Tips
`auto_port()`支持多线程，多进程使用时由小概率出现端口冲突。 多进程使用时，可用`scope`参数指定每个进程使用的端口范围，以免发生冲突。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().auto_port()tab1 = Chromium(addr_or_opts=co).latest_tabtab2 = Chromium(addr_or_opts=co).latest_tabtab2.get('http://DrissionPage.cn')tab1.get('https://www.baidu.com')
```

### 📌 在 ini 文件设置自动分配[​](https://www.drissionpage.cn/browser_control/connect_browser#-在-ini-文件设置自动分配 "📌 在 ini 文件设置自动分配的直接链接")
可以把自动分配的配置记录到 ini 文件，这样无需创建`ChromiumOptions`，每次启动的浏览器都是独立的，不会冲突。但和`auto_port()`一样，这些浏览器也不能复用。
```
from DrissionPage import ChromiumOptionsChromiumOptions().auto_port(True).save()
```

这段代码把该配置记录到 ini 文件，只需运行一次，要关闭的话把参数换成`False`再执行一次即可。
```
from DrissionPage import Chromiumtab1 = Chromium().latest_tabtab2 = Chromium().latest_tabtab1.get('http://DrissionPage.cn')tab2.get('https://www.baidu.com')
```

## ✅️ 使用系统浏览器用户目录[​](https://www.drissionpage.cn/browser_control/connect_browser#️-使用系统浏览器用户目录 "✅️ 使用系统浏览器用户目录的直接链接")
初始默认配置下，程序会为每个使用的端口创建空的用户目录，并且每次接管都使用，这样可以有效避免浏览器冲突。
有些时候我们希望使用系统安装的浏览器的默认用户文件夹。以便复用用户信息和插件等。
我们可以这样设置：
### 📌 使用`ChromiumOptions`[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用chromiumoptions "-使用chromiumoptions的直接链接")
用`ChromiumOptions`在每次启动时配置。
注意
使用这种方法时，需关闭已启动的系统浏览器，否则会连接失败。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().use_system_user_path()browser = Chromium(co)
```

### 📌 使用 ini 文件[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用-ini-文件 "📌 使用 ini 文件的直接链接")
把这个配置记录到 ini 文件，就不用每次使用都配置。
注意
使用这种方法时，需关闭已启动的系统浏览器，否则会连接失败。
```
from DrissionPage import ChromiumOptionsChromiumOptions().use_system_user_path().save()
```

### 📌 手动打开再接管[​](https://www.drissionpage.cn/browser_control/connect_browser#-手动打开再接管 "📌 手动打开再接管的直接链接")
参考上文 “接管已打开浏览器” 的方法，手动为浏览器设置端口启动，再用 DrissionPage 接管。
```
from DrissionPage import Chromiumbrowser = Chromium(9333)# 已手动在9333端口启动浏览器
```

## ✅️ 创建全新的浏览器[​](https://www.drissionpage.cn/browser_control/connect_browser#️-创建全新的浏览器 "✅️ 创建全新的浏览器的直接链接")
默认情况下，程序会复用之前用过的浏览器用户数据，因此可能带有登录数据、历史记录等。
如果想打开全新的浏览器，可用以下方法：
### 📌 使用`auto_port()`[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用auto_port "-使用auto_port的直接链接")
上文提过的`auto_port()`方法，会自动查找一个空闲的端口启动全新的浏览器。
示例见上文。
### 📌 使用`new_env()`[​](https://www.drissionpage.cn/browser_control/connect_browser#-使用new_env "-使用new_env的直接链接")
`ChromiumOptions`对象的`new_env()`方法，可指定启动全新的浏览器。
如果指定端口已有浏览器，会自动关闭再启动新的。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().new_env()browser = Chromium(co)
```

### 📌 手动指定端口和路径[​](https://www.drissionpage.cn/browser_control/connect_browser#-手动指定端口和路径 "📌 手动指定端口和路径的直接链接")
给浏览器用户文件夹路径指定空的路径，以及指定一个空闲的端口，即可打开全新浏览器。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().set_local_port(9333).set_user_data_path(r'C:\tmp')browser = Chromium(co)
```

## ✅️ 用户文件夹位置[​](https://www.drissionpage.cn/browser_control/connect_browser#️-用户文件夹位置 "✅️ 用户文件夹位置的直接链接")
复用用户文件夹可使用已登录的状态、已安装的插件、已设置好的配置等。
以下不同配置下用户文件夹的存放位置。
### 📌 默认配置[​](https://www.drissionpage.cn/browser_control/connect_browser#-默认配置 "📌 默认配置的直接链接")
默认配置下，由 DrissionPage 创建的浏览器，用户文件夹在系统临时文件夹的`DrissionPage\userData`文件夹内，以端口命名。
假如用 DrissionPage 默认配置在 9222 端口创建一个浏览器，那么用户数据就存放在`C:\Users\用户名\AppData\Local\Temp\DrissionPage\userData\9222`路径。
这个用户文件夹不会主动清除，下次再使用 9222 端口时，会继续使用。
如果使用`auto_port()`，会存放在系统临时文件夹的`DrissionPage\autoPortData`文件夹内，以端口命名。
如`C:\Users\用户名\AppData\Local\Temp\DrissionPage\autoPortData\21489`。
这个用户文件夹是临时的，用完会被主动清除。
### 📌 自定义位置[​](https://www.drissionpage.cn/browser_control/connect_browser#-自定义位置 "📌 自定义位置的直接链接")
如果要指定用户文件夹存放位置，可用`ChromiumOptions`对象的`set_tmp_path()`方法。
也可以保持到 ini 文件，可省略每次设置。
示例：
```
from DrissionPage import ChromiumOptionsChromiumOptions().set_tmp_path(r'D:\tmp').save()# 保存到ini文件
```

### 📌 单独指定某个用户文件夹[​](https://www.drissionpage.cn/browser_control/connect_browser#-单独指定某个用户文件夹 "📌 单独指定某个用户文件夹的直接链接")
指定用户文件夹路径，或使用系统文件夹路径，请查看上文。
```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().set_user_data_path(r'D:\tmp')browser = Chromium(co)
```

```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions().use_system_user_path()browser = Chromium(co)
```

[上一页🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)[下一页🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
  * [✅️ `Chromium`初始化参数](https://www.drissionpage.cn/browser_control/connect_browser#️-chromium初始化参数)
  * [✅️ 直接创建](https://www.drissionpage.cn/browser_control/connect_browser#️-直接创建)
    * [📌 默认方式](https://www.drissionpage.cn/browser_control/connect_browser#-默认方式)
    * [📌 指定端口或地址](https://www.drissionpage.cn/browser_control/connect_browser#-指定端口或地址)
  * [✅️ 通过配置信息创建](https://www.drissionpage.cn/browser_control/connect_browser#️-通过配置信息创建)
    * [📌 使用方法](https://www.drissionpage.cn/browser_control/connect_browser#-使用方法)
    * [📌 使用指定 ini 文件创建](https://www.drissionpage.cn/browser_control/connect_browser#-使用指定-ini-文件创建)
  * [✅️ 接管已打开的浏览器](https://www.drissionpage.cn/browser_control/connect_browser#️-接管已打开的浏览器)
    * [📌 用程序启动的浏览器](https://www.drissionpage.cn/browser_control/connect_browser#-用程序启动的浏览器)
    * [📌 手动打开的浏览器](https://www.drissionpage.cn/browser_control/connect_browser#-手动打开的浏览器)
    * [📌 bat 文件启动的浏览器](https://www.drissionpage.cn/browser_control/connect_browser#-bat-文件启动的浏览器)
  * [✅️ 多浏览器共存](https://www.drissionpage.cn/browser_control/connect_browser#️-多浏览器共存)
    * [📌 指定独立端口和数据文件夹](https://www.drissionpage.cn/browser_control/connect_browser#-指定独立端口和数据文件夹)
    * [📌 `auto_port()`方法](https://www.drissionpage.cn/browser_control/connect_browser#-auto_port方法)
    * [📌 在 ini 文件设置自动分配](https://www.drissionpage.cn/browser_control/connect_browser#-在-ini-文件设置自动分配)
  * [✅️ 使用系统浏览器用户目录](https://www.drissionpage.cn/browser_control/connect_browser#️-使用系统浏览器用户目录)
    * [📌 使用`ChromiumOptions`](https://www.drissionpage.cn/browser_control/connect_browser#-使用chromiumoptions)
    * [📌 使用 ini 文件](https://www.drissionpage.cn/browser_control/connect_browser#-使用-ini-文件)
    * [📌 手动打开再接管](https://www.drissionpage.cn/browser_control/connect_browser#-手动打开再接管)
  * [✅️ 创建全新的浏览器](https://www.drissionpage.cn/browser_control/connect_browser#️-创建全新的浏览器)
    * [📌 使用`auto_port()`](https://www.drissionpage.cn/browser_control/connect_browser#-使用auto_port)
    * [📌 使用`new_env()`](https://www.drissionpage.cn/browser_control/connect_browser#-使用new_env)
    * [📌 手动指定端口和路径](https://www.drissionpage.cn/browser_control/connect_browser#-手动指定端口和路径)
  * [✅️ 用户文件夹位置](https://www.drissionpage.cn/browser_control/connect_browser#️-用户文件夹位置)
    * [📌 默认配置](https://www.drissionpage.cn/browser_control/connect_browser#-默认配置)
    * [📌 自定义位置](https://www.drissionpage.cn/browser_control/connect_browser#-自定义位置)
    * [📌 单独指定某个用户文件夹](https://www.drissionpage.cn/browser_control/connect_browser#-单独指定某个用户文件夹)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/connect_browser)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/connect_browser)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
