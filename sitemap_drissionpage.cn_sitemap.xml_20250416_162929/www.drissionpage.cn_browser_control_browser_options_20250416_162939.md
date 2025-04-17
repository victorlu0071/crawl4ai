# Content from: https://www.drissionpage.cn/browser_control/browser_options

[跳到主要内容](https://www.drissionpage.cn/browser_control/browser_options#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/browser_options)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/browser_options)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/intro)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 浏览器启动设置


本页总览
# 🛰️ 浏览器启动设置
浏览器的启动配置非常繁杂，本库使用`ChromiumOptions`类管理启动配置，并且内置了常用配置的设置接口。
注意
该对象只能用于浏览器的启动，浏览器启动后，再修改该配置没有任何效果。接管已打开的浏览器时，启动配置也是无效的。
## ✅️️ 创建对象[​](https://www.drissionpage.cn/browser_control/browser_options#️️-创建对象 "✅️️ 创建对象的直接链接")
### 📌 导入[​](https://www.drissionpage.cn/browser_control/browser_options#-导入 "📌 导入的直接链接")
```
from DrissionPage import ChromiumOptions
```

### 📌 初始化参数[​](https://www.drissionpage.cn/browser_control/browser_options#-初始化参数 "📌 初始化参数的直接链接")
`ChromiumOptions`对象用于管理浏览器初始化配置。可从配置文件中读取配置来进行初始化。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`read_file`| `bool`| `True`| 是否从 ini 文件中读取配置信息，为`False`则用默认配置创建  
`ini_path`| `Path``str`| `None`| 指定 ini 文件路径，为`None`则读取内置 ini 文件  
创建配置对象：
```
from DrissionPage import ChromiumOptionsco = ChromiumOptions()
```

默认情况下，`ChromiumOptions`对象会从 ini 文件中读取配置信息，当指定`read_file`参数为`False`时，则以默认配置创建。
提醒
对象创建时已带有默认设置，如要清除，可调用`clear_arguments()`、`clear_prefs()`等方法。
## ✅️️ 使用方法[​](https://www.drissionpage.cn/browser_control/browser_options#️️-使用方法 "✅️️ 使用方法的直接链接")
创建配置对象后，可调整配置内容，然后在页面对象创建时以参数形式把配置对象传递进去，页面对象会根据配置对象的内容对浏览器进行初始化。
配置对象支持链式操作。
```
from DrissionPage import Chromium, ChromiumOptions# 创建配置对象（默认从 ini 文件中读取配置）co = ChromiumOptions()# 设置不加载图片、静音co.no_imgs(True).mute(True)# 以该配置创建页面对象page = Chromium(addr_or_opts=co)
```

```
from DrissionPage import Chromium, ChromiumOptionsco = ChromiumOptions()co.incognito()# 匿名模式co.headless()# 无头模式co.set_argument('--no-sandbox')# 无沙盒模式page = Chromium(co)
```

## ✅️️ 命令行参数设置[​](https://www.drissionpage.cn/browser_control/browser_options#️️-命令行参数设置 "✅️️ 命令行参数设置的直接链接")
Chromium 内核浏览器有一系列的启动配置，以`--`开头，可在浏览器创建时传入，控制浏览器行为和初始状态。
启动参数非常多，详见：[List of Chromium Command Line Switches](https://peter.sh/experiments/chromium-command-line-switches/)
### 📌 `set_argument()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_argument "-set_argument的直接链接")
此方法用于设置启动参数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`arg`| `str`| 必填| 启动参数名称  
`value`| `str``None``False`| `None`| 参数的值。带值的参数传入属性值，没有值的传入`None`。如传入`False`，删除该参数。  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：** 无值和有值的参数设置
```
# 设置启动时最大化co.set_argument('--start-maximized')# 设置初始窗口大小co.set_argument('--window-size','800,600')# 使用来宾模式打开浏览器co.set_argument('--guest')
```

### 📌 `remove_argument()`[​](https://www.drissionpage.cn/browser_control/browser_options#-remove_argument "-remove_argument的直接链接")
此方法用于在启动配置中删除一个启动参数，只要传入参数名称即可，不需要传入值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`arg`| `str`| 必填| 参数名称，有值的设置项传入设置名称即可  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象自身  
**示例：** 删除无值和有值的参数设置
```
# 删除--start-maximized参数co.remove_argument('--start-maximized')# 删除--window-size参数co.remove_argument('--window-size')
```

### 📌 `clear_arguments()`[​](https://www.drissionpage.cn/browser_control/browser_options#-clear_arguments "-clear_arguments的直接链接")
此方法用于清空已设置的`arguments`参数。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象自身  
## ✅️️ 运行路径及端口[​](https://www.drissionpage.cn/browser_control/browser_options#️️-运行路径及端口 "✅️️ 运行路径及端口的直接链接")
这部分是浏览器路径、用户文件夹路径和端口的设置。
### 📌 `set_browser_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_browser_path "-set_browser_path的直接链接")
此方法用于设置浏览器可执行文件路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 浏览器文件路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
如果传入的字符串不是浏览器可执行文件路径，则会转为使用默认路径。
### 📌 `set_tmp_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_tmp_path "-set_tmp_path的直接链接")
此方法用于设置临时文件默认路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 用户数据文件夹默认路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `set_local_port()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_local_port "-set_local_port的直接链接")
此方法用于设置本地启动端口。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`port`| `str``int`| 必填| 端口号  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `set_address()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_address "-set_address的直接链接")
此方法用于设置浏览器地址，格式 'ip:port'。
和`set_local_port()`是互相覆盖的关系。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`address`| `str`| 必填| 浏览器地址  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `auto_port()`[​](https://www.drissionpage.cn/browser_control/browser_options#-auto_port "-auto_port的直接链接")
此方法用于设置是否使用自动分配的端口，启动一个全新的浏览器。
如果设置为`True`，程序会自动寻找一个可用端口，并在指定路径或系统临时文件夹创建一个文件夹，用于储存浏览器数据。
由于端口和用户文件夹都是唯一的，所以用这种方式启动的浏览器不会产生冲突，但也无法多次启动程序时重复接管同一个浏览器。
`set_local_port()`、`set_address()`和`set_user_data_path()`方法，会和`auto_port()`互相覆盖，即以后调用的为准。
注意
`auto_port()`支持多线程，但不支持多进程。 多进程使用时，可用`scope`参数指定每个进程使用的端口范围，以免发生冲突。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| 是否开启自动分配端口和用户文件夹  
`scope`| `Tuple[int, int]`| `None`| 指定端口范围，不含最后的数字，为`None`则使用`[9600-19600)`  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.auto_port(True)
```

注意
启用此功能后即会获取端口和新建临时用户数据文件夹，若此时用`save()`方法保存配置到 ini 文件，ini 文件中的设置会被该端口和文件夹路径覆盖。这个覆盖对使用并没有很大影响。
### 📌 `set_user_data_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_user_data_path "-set_user_data_path的直接链接")
此方法用于设置用户文件夹路径。用户文件夹用于存储当前登陆浏览器的账号在使用浏览器时留下的痕迹，包括设置选项等。
一般来说用户文件夹的名称是 `User Data`。对于默认情况下的 Windows 中的 Chrome 浏览器来说，此文件夹位于 `%USERPROFILE%\AppData\Local\Google\Chrome\User Data\`，也就是当前系统登陆的用户目录的 `AppData` 内。实际情况可能有变，实际路径请在浏览器输入 `chrome://version/`，查阅其中的`个人资料路径`或者叫`用户配置路径`。若要使用独立的用户信息，可以将 `User Data` 目录整个复制到自定的其他位置，然后在代码中使用 `set_user_data_path()` 方法，参数填入自定义位置路径，这样便可使用独立的用户文件夹信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 用户文件夹路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `use_system_user_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-use_system_user_path "-use_system_user_path的直接链接")
此方法设置是否使用系统安装的浏览器默认用户文件夹
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `set_cache_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_cache_path "-set_cache_path的直接链接")
此方法用于设置缓存路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 缓存路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `existing_only()`[​](https://www.drissionpage.cn/browser_control/browser_options#-existing_only "-existing_only的直接链接")
此方法设置是否仅使用已启动的浏览器，如连接目标浏览器失败，会抛出异常，不会启动新浏览器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
## ✅️️ 使用插件[​](https://www.drissionpage.cn/browser_control/browser_options#️️-使用插件 "✅️️ 使用插件的直接链接")
`add_extension()`和`remove_extensions()`用于设置浏览器启动时要加载的插件。可以指定数量不限的插件。
### 📌 `add_extension()`[​](https://www.drissionpage.cn/browser_control/browser_options#-add_extension "-add_extension的直接链接")
此方法用于添加一个插件到浏览器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 插件路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
Tips
根据作者的经验，把插件文件解压到一个独立文件夹，然后把插件路径指向这个文件夹，会比较稳定。
**示例：**
```
co.add_extension(r'D:\SwitchyOmega')
```

### 📌 `remove_extensions()`[​](https://www.drissionpage.cn/browser_control/browser_options#-remove_extensions "-remove_extensions的直接链接")
此方法用于移除配置对象中保存的所有插件路径。如需移除部分插件，请移除全部后再重新添加需要的插件。
**参数：** 无
**返回：** 配置对象自身
```
co.remove_extensions()
```

## ✅️️ 用户文件设置[​](https://www.drissionpage.cn/browser_control/browser_options#️️-用户文件设置 "✅️️ 用户文件设置的直接链接")
除了启动参数，还有大量配置信息保存在浏览器的 `preferences` 文件中。
注意
`preferences` 文件是Chromium内核浏览器的配置信息文件，与 DrissionPage 的 `configs.ini` 完全不同。
以下方法用于对浏览器用户文件进行设置。
### 📌 `set_user()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_user "-set_user的直接链接")
Chromium 浏览器支持多用户配置，我们可以选择使用哪一个。默认为`'Default'`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`user`| `str`| `'Default'`| 用户配置文件夹名称  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_user(user='Profile 1')
```

### 📌 `set_pref()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_pref "-set_pref的直接链接")
此方法用于设置用户配置文件里的一个配置项。
在哪里可以查到所有的配置项？作者也没找到，知道的请告知。谢谢。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`arg`| `str`| 必填| 设置项名称  
`value`| `str`| 必填| 设置项值  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
# 禁止所有弹出窗口co.set_pref(arg='profile.default_content_settings.popups', value='0')# 隐藏是否保存密码的提示co.set_pref('credentials_enable_service',False)
```

### 📌 `remove_pref()`[​](https://www.drissionpage.cn/browser_control/browser_options#-remove_pref "-remove_pref的直接链接")
此方法用于在当前配置对象中删除一个`pref`配置项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`arg`| `str`| 必填| 设置项名称  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.remove_pref(arg='profile.default_content_settings.popups')
```

### 📌 `remove_pref_from_file()`[​](https://www.drissionpage.cn/browser_control/browser_options#-remove_pref_from_file "-remove_pref_from_file的直接链接")
此方法用于在用户配置文件删除一个配置项。注意与上一个方法不一样，如果用户配置文件中已经存在某个项，用`remove_pref()` 是不能删除的，只能用`remove_pref_from_file()`删除。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`arg`| `str`| 必填| 设置项名称  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.remove_pref_from_file(arg='profile.default_content_settings.popups')
```

### 📌 `clear_prefs()`[​](https://www.drissionpage.cn/browser_control/browser_options#-clear_prefs "-clear_prefs的直接链接")
此方法用于清空已设置的`prefs`参数。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象自身  
## ✅️️ 运行参数设置[​](https://www.drissionpage.cn/browser_control/browser_options#️️-运行参数设置 "✅️️ 运行参数设置的直接链接")
页面对象运行时需要用到的参数，也可以在`ChromiumOptions`中设置。
### 📌 `set_timeouts()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_timeouts "-set_timeouts的直接链接")
此方法用于设置几种超时时间，单位为秒。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`base`| `float`| `None`| 默认超时时间，用于元素等待、alert 等待、`WebPage`的 s 模式连接等等，除以下两个参数的场景，都使用这个设置  
`page_load`| `float`| `None`| 页面加载超时时间  
`script`| `float`| `None`| JavaScript 运行超时时间  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_timeouts(base=10)
```

### 📌 `set_retry()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_retry "-set_retry的直接链接")
此方法用于设置页面连接超时时的重试次数和间隔。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| `None`| 连接失败重试次数  
`interval`| `float`| `None`| 连接失败重试间隔（秒）  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `set_load_mode()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_load_mode "-set_load_mode的直接链接")
此方法用于设置网页加载策略。
加载策略是指强制页面停止加载的时机，如加载完 DOM 即停止，不加载图片资源等，以提高自动化效率。
无论设置哪种策略，加载时间都不会超过`set_timeouts()`中`page_load`参数设置的时间。
加载策略：
  * `'normal'`：阻塞进程，等待所有资源下载完成（默认）
  * `'eager'`：DOM 就绪即停止加载
  * `'none'`：网页连接成功即停止加载

参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `str`| 必填| 可接收`'normal'`、`'eager'`、`'none'`  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_load_mode('eager')
```

### 📌 `set_proxy()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_proxy "-set_proxy的直接链接")
该方法用于设置浏览器代理。
该设置在浏览器启动时一次性设置，设置后不能修改。且不支持带账号的代理。
如果需要运行时修改代理，或使用带账号的代理，可以用插件自行实现。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`proxy`| `str`| 必填| 格式：协议://ip:port当不指定协议时，默认使用 http 代理  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_proxy('http://localhost:1080')
```

### 📌 `set_download_path()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_download_path "-set_download_path的直接链接")
此方法用于设置下载文件保存路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| 必填| 下载路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
## ✅️️ 其它设置[​](https://www.drissionpage.cn/browser_control/browser_options#️️-其它设置 "✅️️ 其它设置的直接链接")
作者将一些常用的配置封装成方法，可以直接调用。
### 📌 `headless()`[​](https://www.drissionpage.cn/browser_control/browser_options#-headless "-headless的直接链接")
该方法用于设置是否以无界面模式启动浏览器。
如果指定端口已存在运行中的非无头浏览器，会先关闭已有浏览器再启动新的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.headless(True)
```

### 📌 `new_env()`[​](https://www.drissionpage.cn/browser_control/browser_options#-new_env "-new_env的直接链接")
该方法用于设置是否使用全新环境创建浏览器。
如果指定端口已存在运行中的浏览器，会先关闭已有浏览器再启动新的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `set_flag()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_flag "-set_flag的直接链接")
此方法用于设置实验项，即`'chrome://flags'`中的项目。
设置无值的项，无须设置`value`参数，否则在该参数传入要设置的值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`flag`| `str`| 必填| 设置项名称  
`value`| `str`| `None`| 设置项值  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
from DrissionPage import ChromiumOptionsco = ChromiumOptions()co.set_flag('temporary-unexpire-flags-m118','1')# 有值co.set_flag('disable-accelerated-2d-canvas')# 无值 
```

### 📌 `clear_flags_in_file()`[​](https://www.drissionpage.cn/browser_control/browser_options#-clear_flags_in_file "-clear_flags_in_file的直接链接")
此方法用于删除浏览器配置文件中已设置的实验项。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `clear_flags()`[​](https://www.drissionpage.cn/browser_control/browser_options#-clear_flags "-clear_flags的直接链接")
此方法用于清空本对象中已设置的`flags`参数。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象自身  
### 📌 `incognito()`[​](https://www.drissionpage.cn/browser_control/browser_options#-incognito "-incognito的直接链接")
该方法用于设置是否以无痕模式启动浏览器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `ignore_certificate_errors()`[​](https://www.drissionpage.cn/browser_control/browser_options#-ignore_certificate_errors "-ignore_certificate_errors的直接链接")
该方法用于设置是否忽略证书错误。可以解决访问网页时出现的“您的连接不是私密连接”、“你的连接不是专用连接”等问题。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
### 📌 `no_imgs()`[​](https://www.drissionpage.cn/browser_control/browser_options#-no_imgs "-no_imgs的直接链接")
该方法用于设置是否禁止加载图片。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.no_imgs(True)
```

### 📌 `no_js()`[​](https://www.drissionpage.cn/browser_control/browser_options#-no_js "-no_js的直接链接")
该方法用于设置是否禁用 JavaScript。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.no_js(True)
```

### 📌 `mute()`[​](https://www.drissionpage.cn/browser_control/browser_options#-mute "-mute的直接链接")
该方法用于设置是否静音。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `True`和`False`表示开或关  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.mute(True)
```

### 📌 `set_user_agent()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_user_agent "-set_user_agent的直接链接")
该方法用于设置 user agent。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`user_agent`| `str`| 必填| user agent文本  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_user_agent(user_agent='Mozilla/5.0 (Macintos.....')
```

### 📌 `set_paths()`[​](https://www.drissionpage.cn/browser_control/browser_options#-set_paths "-set_paths的直接链接")
此方法用于设置各种路径信息。对有传入值的路径进行设置，为`None`的则无视。
个方法的功能与上面介绍过设置路径的方法是重复的，只是把几个方法集成在一起。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`browser_path`| `str``Path`| `None`| 浏览器可执行文件路径  
`local_port`| `str``int`| `None`| 浏览器要使用的本地端口号  
`address`| `str`| `None`| 浏览器地址，例：127.0.0.1:9222，如与`local_port`一起设置，会覆盖`local_port`的值  
`download_path`| `str``Path`| `None`| 下载文件默认保存路径  
`user_data_path`| `str``Path`| `None`| 用户数据文件夹路径  
`cache_path`| `str``Path`| `None`| 缓存路径  
返回类型| 说明  
---|---  
`ChromiumOptions`| 配置对象本身  
**示例：**
```
co.set_paths(local_port=9333, user_data_path=r'D:\tmp')
```

## ✅️️ 保存设置到文件[​](https://www.drissionpage.cn/browser_control/browser_options#️️-保存设置到文件 "✅️️ 保存设置到文件的直接链接")
ini 文件是 DrissionPage 的配置文件，持久化记载一些配置参数。您可以把不同的配置保存到各自的 ini 文件，以便适应不同的场景。
### 📌 `save()`[​](https://www.drissionpage.cn/browser_control/browser_options#-save "-save的直接链接")
此方法用于保存配置项到一个 ini 文件。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| ini 文件的路径， 传入`None`保存到当前读取的配置文件  
返回类型| 说明  
---|---  
`str`| 保存的 ini 文件绝对路径  
**示例：**
```
# 保存当前读取的ini文件co.save()# 把当前配置保存到指定的路径co.save(path=r'D:\tmp\settings.ini')
```

### 📌 `save_to_default()`[​](https://www.drissionpage.cn/browser_control/browser_options#-save_to_default "-save_to_default的直接链接")
此方法用于保存配置项到固定的默认 ini 文件。默认 ini 文件是指随 DrissionPage 内置的那个。
默认 ini 文件默认的路径是 Python 安装目录中的 `Lib\site-packages\DrissionPage\_configs\configs.ini`。
ini 文件初始内容点[这里](http://DrissionPage.cn/advance/ini)。
**参数：** 无
返回类型| 说明  
---|---  
`str`| 保存的 ini 文件绝对路径  
**示例：**
```
co.save_to_default()
```

## ✅️️ `ChromiumOptions`属性[​](https://www.drissionpage.cn/browser_control/browser_options#️️-chromiumoptions属性 "️️-chromiumoptions属性的直接链接")
### 📌 `address`[​](https://www.drissionpage.cn/browser_control/browser_options#-address "-address的直接链接")
该属性为要控制的浏览器地址，格式为 ip:port，默认为`'127.0.0.1:9222'`。
**类型：**`str`
### 📌 `browser_path`[​](https://www.drissionpage.cn/browser_control/browser_options#-browser_path "-browser_path的直接链接")
该属性返回浏览器可执行文件的路径。
**类型：**`str`
### 📌 `user_data_path`[​](https://www.drissionpage.cn/browser_control/browser_options#-user_data_path "-user_data_path的直接链接")
该属性返回用户数据文件夹路径。
**类型：**`str`
### 📌 `tmp_path`[​](https://www.drissionpage.cn/browser_control/browser_options#-tmp_path "-tmp_path的直接链接")
该属性返回临时文件夹路径，可用于保存自动分配的用户文件夹路径。
**类型：**`str`
### 📌 `download_path`[​](https://www.drissionpage.cn/browser_control/browser_options#-download_path "-download_path的直接链接")
该属性返回默认下载路径文件路径。
**类型：**`str`
### 📌 `user`[​](https://www.drissionpage.cn/browser_control/browser_options#-user "-user的直接链接")
该属性返回用户配置文件夹名称。
**类型：**`str`
### 📌 `load_mode`[​](https://www.drissionpage.cn/browser_control/browser_options#-load_mode "-load_mode的直接链接")
该属性返回页面加载策略。有`'normal'`、`'eager'`、`'none'`三种
**类型：**`str`
### 📌 `timeouts`[​](https://www.drissionpage.cn/browser_control/browser_options#-timeouts "-timeouts的直接链接")
该属性返回超时设置。包括三种：`'base'`、`'page_load'`、`'script'`。
**类型：**`dict`
```
print(co.timeouts)
```

**输出：**
```
{  'base': 10,  'page_load': 30,  'script': 30}
```

### 📌 `retry_times`[​](https://www.drissionpage.cn/browser_control/browser_options#-retry_times "-retry_times的直接链接")
该属性返回连接失败时的重试次数。
**类型：**`int`
### 📌 `retry_interval`[​](https://www.drissionpage.cn/browser_control/browser_options#-retry_interval "-retry_interval的直接链接")
该属性返回连接失败时的重试间隔（秒）。
**类型：**`float`
### 📌 `proxy`[​](https://www.drissionpage.cn/browser_control/browser_options#-proxy "-proxy的直接链接")
该属性返回代理设置。
**类型：**`str`
### 📌 `arguments`[​](https://www.drissionpage.cn/browser_control/browser_options#-arguments "-arguments的直接链接")
该属性以`list`形式返回浏览器启动参数。
**类型：**`list`
### 📌 `extensions`[​](https://www.drissionpage.cn/browser_control/browser_options#-extensions "-extensions的直接链接")
该属性以`list`形式返回要加载的插件路径。
**类型：**`list`
### 📌 `preferences`[​](https://www.drissionpage.cn/browser_control/browser_options#-preferences "-preferences的直接链接")
该属性返回用户首选项配置。
**类型：**`dict`
### 📌 `system_user_path`[​](https://www.drissionpage.cn/browser_control/browser_options#-system_user_path "-system_user_path的直接链接")
该属性返回是否使用系统按照的浏览器的用户文件夹。
**类型：**`bool`
### 📌 `is_existing_only`[​](https://www.drissionpage.cn/browser_control/browser_options#-is_existing_only "-is_existing_only的直接链接")
该属性返回是否仅使用已打开的浏览器。
**类型：**`bool`
### 📌 `is_auto_port`[​](https://www.drissionpage.cn/browser_control/browser_options#-is_auto_port "-is_auto_port的直接链接")
该属性返回是否仅使用自动分配端口和用户文件夹路径。
**类型：**`bool`
### 📌 `is_headless`[​](https://www.drissionpage.cn/browser_control/browser_options#-is_headless "-is_headless的直接链接")
该属性返回是否以无头模式启动浏览器。
**类型：**`bool`
[ 上一页🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)[下一页🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
  * [✅️️ 创建对象](https://www.drissionpage.cn/browser_control/browser_options#️️-创建对象)
    * [📌 导入](https://www.drissionpage.cn/browser_control/browser_options#-导入)
    * [📌 初始化参数](https://www.drissionpage.cn/browser_control/browser_options#-初始化参数)
  * [✅️️ 使用方法](https://www.drissionpage.cn/browser_control/browser_options#️️-使用方法)
  * [✅️️ 命令行参数设置](https://www.drissionpage.cn/browser_control/browser_options#️️-命令行参数设置)
    * [📌 `set_argument()`](https://www.drissionpage.cn/browser_control/browser_options#-set_argument)
    * [📌 `remove_argument()`](https://www.drissionpage.cn/browser_control/browser_options#-remove_argument)
    * [📌 `clear_arguments()`](https://www.drissionpage.cn/browser_control/browser_options#-clear_arguments)
  * [✅️️ 运行路径及端口](https://www.drissionpage.cn/browser_control/browser_options#️️-运行路径及端口)
    * [📌 `set_browser_path()`](https://www.drissionpage.cn/browser_control/browser_options#-set_browser_path)
    * [📌 `set_tmp_path()`](https://www.drissionpage.cn/browser_control/browser_options#-set_tmp_path)
    * [📌 `set_local_port()`](https://www.drissionpage.cn/browser_control/browser_options#-set_local_port)
    * [📌 `set_address()`](https://www.drissionpage.cn/browser_control/browser_options#-set_address)
    * [📌 `auto_port()`](https://www.drissionpage.cn/browser_control/browser_options#-auto_port)
    * [📌 `set_user_data_path()`](https://www.drissionpage.cn/browser_control/browser_options#-set_user_data_path)
    * [📌 `use_system_user_path()`](https://www.drissionpage.cn/browser_control/browser_options#-use_system_user_path)
    * [📌 `set_cache_path()`](https://www.drissionpage.cn/browser_control/browser_options#-set_cache_path)
    * [📌 `existing_only()`](https://www.drissionpage.cn/browser_control/browser_options#-existing_only)
  * [✅️️ 使用插件](https://www.drissionpage.cn/browser_control/browser_options#️️-使用插件)
    * [📌 `add_extension()`](https://www.drissionpage.cn/browser_control/browser_options#-add_extension)
    * [📌 `remove_extensions()`](https://www.drissionpage.cn/browser_control/browser_options#-remove_extensions)
  * [✅️️ 用户文件设置](https://www.drissionpage.cn/browser_control/browser_options#️️-用户文件设置)
    * [📌 `set_user()`](https://www.drissionpage.cn/browser_control/browser_options#-set_user)
    * [📌 `set_pref()`](https://www.drissionpage.cn/browser_control/browser_options#-set_pref)
    * [📌 `remove_pref()`](https://www.drissionpage.cn/browser_control/browser_options#-remove_pref)
    * [📌 `remove_pref_from_file()`](https://www.drissionpage.cn/browser_control/browser_options#-remove_pref_from_file)
    * [📌 `clear_prefs()`](https://www.drissionpage.cn/browser_control/browser_options#-clear_prefs)
  * [✅️️ 运行参数设置](https://www.drissionpage.cn/browser_control/browser_options#️️-运行参数设置)
    * [📌 `set_timeouts()`](https://www.drissionpage.cn/browser_control/browser_options#-set_timeouts)
    * [📌 `set_retry()`](https://www.drissionpage.cn/browser_control/browser_options#-set_retry)
    * [📌 `set_load_mode()`](https://www.drissionpage.cn/browser_control/browser_options#-set_load_mode)
    * [📌 `set_proxy()`](https://www.drissionpage.cn/browser_control/browser_options#-set_proxy)
    * [📌 `set_download_path()`](https://www.drissionpage.cn/browser_control/browser_options#-set_download_path)
  * [✅️️ 其它设置](https://www.drissionpage.cn/browser_control/browser_options#️️-其它设置)
    * [📌 `headless()`](https://www.drissionpage.cn/browser_control/browser_options#-headless)
    * [📌 `new_env()`](https://www.drissionpage.cn/browser_control/browser_options#-new_env)
    * [📌 `set_flag()`](https://www.drissionpage.cn/browser_control/browser_options#-set_flag)
    * [📌 `clear_flags_in_file()`](https://www.drissionpage.cn/browser_control/browser_options#-clear_flags_in_file)
    * [📌 `clear_flags()`](https://www.drissionpage.cn/browser_control/browser_options#-clear_flags)
    * [📌 `incognito()`](https://www.drissionpage.cn/browser_control/browser_options#-incognito)
    * [📌 `ignore_certificate_errors()`](https://www.drissionpage.cn/browser_control/browser_options#-ignore_certificate_errors)
    * [📌 `no_imgs()`](https://www.drissionpage.cn/browser_control/browser_options#-no_imgs)
    * [📌 `no_js()`](https://www.drissionpage.cn/browser_control/browser_options#-no_js)
    * [📌 `mute()`](https://www.drissionpage.cn/browser_control/browser_options#-mute)
    * [📌 `set_user_agent()`](https://www.drissionpage.cn/browser_control/browser_options#-set_user_agent)
    * [📌 `set_paths()`](https://www.drissionpage.cn/browser_control/browser_options#-set_paths)
  * [✅️️ 保存设置到文件](https://www.drissionpage.cn/browser_control/browser_options#️️-保存设置到文件)
    * [📌 `save()`](https://www.drissionpage.cn/browser_control/browser_options#-save)
    * [📌 `save_to_default()`](https://www.drissionpage.cn/browser_control/browser_options#-save_to_default)
  * [✅️️ `ChromiumOptions`属性](https://www.drissionpage.cn/browser_control/browser_options#️️-chromiumoptions属性)
    * [📌 `address`](https://www.drissionpage.cn/browser_control/browser_options#-address)
    * [📌 `browser_path`](https://www.drissionpage.cn/browser_control/browser_options#-browser_path)
    * [📌 `user_data_path`](https://www.drissionpage.cn/browser_control/browser_options#-user_data_path)
    * [📌 `tmp_path`](https://www.drissionpage.cn/browser_control/browser_options#-tmp_path)
    * [📌 `download_path`](https://www.drissionpage.cn/browser_control/browser_options#-download_path)
    * [📌 `user`](https://www.drissionpage.cn/browser_control/browser_options#-user)
    * [📌 `load_mode`](https://www.drissionpage.cn/browser_control/browser_options#-load_mode)
    * [📌 `timeouts`](https://www.drissionpage.cn/browser_control/browser_options#-timeouts)
    * [📌 `retry_times`](https://www.drissionpage.cn/browser_control/browser_options#-retry_times)
    * [📌 `retry_interval`](https://www.drissionpage.cn/browser_control/browser_options#-retry_interval)
    * [📌 `proxy`](https://www.drissionpage.cn/browser_control/browser_options#-proxy)
    * [📌 `arguments`](https://www.drissionpage.cn/browser_control/browser_options#-arguments)
    * [📌 `extensions`](https://www.drissionpage.cn/browser_control/browser_options#-extensions)
    * [📌 `preferences`](https://www.drissionpage.cn/browser_control/browser_options#-preferences)
    * [📌 `system_user_path`](https://www.drissionpage.cn/browser_control/browser_options#-system_user_path)
    * [📌 `is_existing_only`](https://www.drissionpage.cn/browser_control/browser_options#-is_existing_only)
    * [📌 `is_auto_port`](https://www.drissionpage.cn/browser_control/browser_options#-is_auto_port)
    * [📌 `is_headless`](https://www.drissionpage.cn/browser_control/browser_options#-is_headless)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/browser_options)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/browser_options)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
