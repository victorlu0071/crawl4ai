# Content from: https://www.drissionpage.cn/browser_control/browser_object

[跳到主要内容](https://www.drissionpage.cn/browser_control/browser_object#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/browser_object)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/browser_object)
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
  * 🛰️ 浏览器对象


本页总览
# 🛰️ 浏览器对象
我们已经了解如何创建浏览器对象，本节介绍浏览器对象的功能。
说明
文中的 “Tab 对象” 是`ChromiumTab`和`MixTab`的统称。
## ✅️️ 获取标签页对象或信息[​](https://www.drissionpage.cn/browser_control/browser_object#️️-获取标签页对象或信息 "✅️️ 获取标签页对象或信息的直接链接")
### 📌 `get_tab()`[​](https://www.drissionpage.cn/browser_control/browser_object#-get_tab "-get_tab的直接链接")
此方法用于获取一个标签页对象或它的 id。
`id_or_num`不为`None`时，获取`id_or_num`指定的标签页。后面几个参数无效。
`id_or_num`为`None`时，根据后面几个参数指定的条件查找标签页（与关系）。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`id_or_num`| `str``int`| `None`| 要获取的标签页 id 或序号，序号从`1`开始，可传入负数获取倒数第几个，不是视觉排列顺序，而是激活顺序  
`title`| `str`| `None`| 要匹配 title 的文本，模糊匹配，为`None`则匹配所有  
`url`| `str`| `None`| 要匹配 url 的文本，模糊匹配，为`None`则匹配所有  
`tab_type`| `str``list``tuple`| `'page'`| 标签页类型，可用列表输入多个，如`'page'`、`'iframe'`等，为`None`则匹配所有  
`as_id`| `bool`| `False`| 是否返回标签页 id 而不是标签页对象  
返回类型| 说明  
---|---  
`MixTab`| `as_id`为`False`时返回获取到的标签页对象  
`str`| `as_id`为`True`时返回获取到的标签页的 id  
```
from DrissionPage import Chromiumbrowser = Chromium()tab = browser.get_tab()
```

### 📌 `get_tabs()`[​](https://www.drissionpage.cn/browser_control/browser_object#-get_tabs "-get_tabs的直接链接")
此方法用于获取多个符合条件的`MixTab`对象或它们的 id组成的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`title`| `str`| `None`| 要匹配 title 的文本，模糊匹配，为`None`则匹配所有  
`url`| `str`| `None`| 要匹配 url 的文本，模糊匹配，为`None`则匹配所有  
`tab_type`| `str``list``tuple`| `'page'`| 标签页类型，可用列表输入多个，如`'page'`、`'iframe'`等，为`None`则匹配所有  
`as_id`| `bool`| `False`| 是否返回标签页 id 而不是标签页对象  
返回类型| 说明  
---|---  
`List[MixTab]`| `as_id`为`False`时返回获取到的标签页对象组成的列表  
`List[str]`| `as_id`为`True`时返回获取到的标签页的 id 组成的列表  
### 📌 `latest_tab`[​](https://www.drissionpage.cn/browser_control/browser_object#-latest_tab "-latest_tab的直接链接")
此属性返回最新的标签页对象或 id，最新标签页指最后创建或最后被激活的。
如果关闭单例模式，即当`Settings.singleton_tab_obj`为`False`时，返回标签页的 id。
返回类型| 说明  
---|---  
`MixTab`| 单例模式时返回标签页对象  
`str`| 非单例模式时返回标签页 id  
### 📌 `tabs_count`[​](https://www.drissionpage.cn/browser_control/browser_object#-tabs_count "-tabs_count的直接链接")
此属性返回标签页数量，只统计普通标签页（即`'page'`、`'webview'`类型）。
**类型：**`int`
### 📌 `tab_ids`[​](https://www.drissionpage.cn/browser_control/browser_object#-tab_ids "-tab_ids的直接链接")
此属性返回所有标签页 id 组成的列表，只统计普通标签页（即`'page'`、`'webview'`类型）。
**类型：**`List[str]`
## ✅️️ 标签页操作[​](https://www.drissionpage.cn/browser_control/browser_object#️️-标签页操作 "✅️️ 标签页操作的直接链接")
### 📌 `new_tab()`[​](https://www.drissionpage.cn/browser_control/browser_object#-new_tab "-new_tab的直接链接")
此方法用于新建标签页，并返回标签页对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`url`| `str`| `None`| 新标签页跳转到的网址，为`None`时新建空标签页  
`new_window`| `bool`| `False`| 是否在新窗口打开标签页，隐身模式下无效  
`background`| `bool`| `False`| 是否不激活新标签页，隐身模式和访客模式及`new_window`为`True`时无效  
`new_context`| `bool`| `False`| 是否创建独立环境，隐身模式和访客模式下无效  
返回类型| 说明  
---|---  
`MixTab`| 标签页对象  
### 📌 `activate_tab()`[​](https://www.drissionpage.cn/browser_control/browser_object#-activate_tab "-activate_tab的直接链接")
此方法用于使一个标签页显示到前端。可传入 Tab 对象、标签页 id、标签页序号。
注意标签页序号不是视觉顺序，而是激活顺序。
说明
标签页没有焦点的概念，多个标签页可以并行操作，这个方法不会对所谓焦点产生什么影响。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`id_ind_tab`| `str``int``ChromiumTab``MixTab`| 必填| 标签页 id（`str`）、Tab 对象或标签页序号（`int`），序号从`1`开始  
**返回：**`None`
### 📌 `close_tabs()`[​](https://www.drissionpage.cn/browser_control/browser_object#-close_tabs "-close_tabs的直接链接")
此方法用于关闭标签页。可指定多个，可关闭指定标签页以外的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`tabs_or_ids`| `str``ChromiumTab``MixTab``List|Tuple[ChromiumTab|MixTab|str]`| 必填| 指定的标签页对象或 id，可用列表或元组传入多个  
`others`| `bool`| `False`| 是否关闭指定标签页之外的  
**返回：**`None`
### 📌 单例模式说明[​](https://www.drissionpage.cn/browser_control/browser_object#-单例模式说明 "📌 单例模式说明的直接链接")
默认设置下，一个标签页只有一个 Tab 对象。
对同一个标签页反复使用`get_tab()`获取到的是同一个对象。
如上文所述，`latest_tab`获取的也是曾经生成过的 Tab 对象。
如果需要多个 Tab 对象共同管理一个标签页，可关闭单例模式：
```
from DrissionPage.common import SettingsSettings.set_singleton_tab_obj(False)
```

关闭后，每次`get_tab()`都会创建新的 Tab 对象，`latest_tab`改成返回 Tab 对象的 id。
```
from DrissionPage import Chromiumfrom DrissionPage.common import SettingsSettings.set_singleton_tab_obj(False)browser = Chromium()tab1 = browser.get_tab()tab2 = browser.get_tab()print(tab1.title,id(tab1))print(tab2.title,id(tab2))
```

**输出：**
```
新标签页 2500121968848新标签页 2500125672272
```

## ✅️️ 浏览器运行参数[​](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器运行参数 "✅️️ 浏览器运行参数的直接链接")
浏览器运行设置是一些总体的运行参数。
新标签页对象会继承浏览器的运行设置，但标签页对象后再修改浏览器设置，已生成的设置也不会改变。
设置优先级：Tab 对象设置 > `Chromium`对象设置 > `Settings`设置
### 📌 `user_data_path`[​](https://www.drissionpage.cn/browser_control/browser_object#-user_data_path "-user_data_path的直接链接")
此参数返回浏览器返回用户文件夹路径。
**类型：**`str`
### 📌 `download_path`[​](https://www.drissionpage.cn/browser_control/browser_object#-download_path "-download_path的直接链接")
此参数返回浏览器返回默认下载路径。
**类型：**`str`
### 📌 几种超时参数[​](https://www.drissionpage.cn/browser_control/browser_object#-几种超时参数 "📌 几种超时参数的直接链接")
此参数返回所有超时设置，单位为秒，有`base`、`page_load`、`script`三种。
  * `timeouts.base`：各种等待的基础超时设置
  * `timeouts.page_load`：页面文档加载的超时设置
  * `timeouts.script`：JavaScript 运行超时设置


**类型：**`float`
### 📌 `timeout`[​](https://www.drissionpage.cn/browser_control/browser_object#-timeout "-timeout的直接链接")
此参数返回基础超时设置，单位为秒，即`timeouts.base`。
**类型：**`float`
### 📌 `load_mode`[​](https://www.drissionpage.cn/browser_control/browser_object#-load_mode "-load_mode的直接链接")
此参数返回页面加载模式，包括`'none'`、`'normal'`、`'eager'`三种。
**类型：**`str`
## ✅️️ 浏览器运行设置[​](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器运行设置 "✅️️ 浏览器运行设置的直接链接")
### 📌 `set.timeouts()`[​](https://www.drissionpage.cn/browser_control/browser_object#-settimeouts "-settimeouts的直接链接")
此方法用于设置运行时的各种超时时间，单位为秒。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`base`| `float`| `None`| 各种等待的默认超时时间，为`None`则不修改  
`page_load`| `float`| `None`| 页面文档加载超时时间，为`None`则不修改  
`script`| `float`| `None`| 脚本运行超时时间，为`None`则不修改  
**返回：**`None`
### 📌 加载模式设置[​](https://www.drissionpage.cn/browser_control/browser_object#-加载模式设置 "📌 加载模式设置的直接链接")
此方法用于设置页面加载模式。具体使用方法详见访问网页章节。
  * `set.load_mode.normal()`：等待所有资源加载完毕的模式
  * `set.load_mode.eager()`：等待文档加载完即停止加载的模式
  * `set.load_mode.none()`：不会主动停止加载的模式


**返回：**`None`
### 📌 `set.retry_times()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setretry_times "-setretry_times的直接链接")
此方法用于设置页面连接失败重连次数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| 必填| 重连次数  
**返回：**`None`
### 📌 `set.retry_interval()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setretry_interval "-setretry_interval的直接链接")
此方法用于设置连接失败重连间隔（秒）。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`interval`| `float`| 必填| 重连间隔  
**返回：**`None`
### 📌 `set.cookies()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setcookies "-setcookies的直接链接")
此方法用于设置一个或多个 cookie。
注意
用这个方法设置 cookies 记得带上`domain`属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cookies`| `CookieJar``Cookie``list``tuple``str``dict`| 必填| 支持多种格式的 cookies 信息，一个或多个都可以  
**返回：**`None`
### 📌 `set.cookies.clear()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setcookiesclear "-setcookiesclear的直接链接")
此方法用于清除浏览器所有 cookies。
**参数：** 无
**返回：**`None`
### 📌 `set.auto_handle_alert()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setauto_handle_alert "-setauto_handle_alert的直接链接")
此方法用于设置是否启用自动处理 alert 弹窗。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关，传入`None`表示使用`Settings`设置  
`accept`| `bool`| `True`| 处理 alert 的方式，确定还是取消  
**返回：**`None`
### 📌 `set.download_path()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setdownload_path "-setdownload_path的直接链接")
此方法用于设置下载文件默认保存路径。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `Path``str``None`| 必填| 文件夹路径，传入`None`表示当前文件夹  
**返回：**`None`
### 📌 `set.download_file_name()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setdownload_file_name "-setdownload_file_name的直接链接")
此方法用于设置下一个被下载文件的名称。
有些下载是从临时闪现的标签页触发的，这种需要由浏览器对象去捕捉和设置下载信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| `None`| 文件名，可不含后缀，会自动使用远程文件后缀，为`None`使用远程文件名  
`suffix`| `str`| `None`| 后缀名，显式设置后缀名，不使用远程文件后缀  
**返回：**`None`
### 📌 `set.when_download_file_exists()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setwhen_download_file_exists "-setwhen_download_file_exists的直接链接")
此方法用于设置当存在同名文件时的处理方式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`mode`| `str`| 必填| 可在`'rename'`、`'overwrite'`、`'skip'`、`'r'`、`'o'`、`'s'`中选择  
  * `'rename'`或`'r'`：自动重命名，在文件名后加序号，如`'_1'`
  * `'overwrit'`或`'o'`：覆盖已有文件
  * `'skip'`或`'s'`：跳过，不下载


**返回：**`None`
### 📌 `set.NoneElement_value()`[​](https://www.drissionpage.cn/browser_control/browser_object#-setnoneelement_value "-setnoneelement_value的直接链接")
此方法用于设置查找元素失败时返回的空元素是否返回设定值。详见元素查找行为章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `Any`| `None`| 设置的设定值  
`on_off`| `bool`| `True`| 是否启用  
**返回：**`None`
## ✅️️ 浏览器信息[​](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器信息 "✅️️ 浏览器信息的直接链接")
### 📌 `cookies()`[​](https://www.drissionpage.cn/browser_control/browser_object#-cookies "-cookies的直接链接")
此方法以列表形式返回浏览器所有域名的 cookies，cookie 是`dict`格式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`all_info`| `bool`| `False`| 是否返回所有内容，`False`则只返回`'name'`、`'value'`、`'domain'`三个属性  
**返回：**`CookiesList`
除列表格式，还能以其它格式返回：
  * `cookies().as_str`：以`str`格式返回，只包含`name`和`value`字段，`'name1=value1; name2=value2'`格式
  * `cookies().as_dict`：以`dict`格式返回，只包含`name`和`value`字段，`{'name1': 'value1', 'name2': 'value1'}`格式
  * `cookies().as_json`：把列表转换为 json 返回


### 📌 `process_id`[​](https://www.drissionpage.cn/browser_control/browser_object#-process_id "-process_id的直接链接")
此属性返回浏览器进程 pid。
**类型：**`int`
### 📌 `states.is_alive`[​](https://www.drissionpage.cn/browser_control/browser_object#-statesis_alive "-statesis_alive的直接链接")
此属性返回浏览器是否仍可用。
**类型：**`bool`
### 📌 `states.is_existed`[​](https://www.drissionpage.cn/browser_control/browser_object#-statesis_existed "-statesis_existed的直接链接")
此属性返回浏览器是否接管的，而非本程序创建的。
**类型：**`bool`
### 📌 `states.is_headless`[​](https://www.drissionpage.cn/browser_control/browser_object#-statesis_headless "-statesis_headless的直接链接")
此属性返回浏览器是否无头模式。
**类型：**`bool`
### 📌 `states.is_incognito`[​](https://www.drissionpage.cn/browser_control/browser_object#-statesis_incognito "-statesis_incognito的直接链接")
此属性返回浏览器是否无痕模式。
**类型：**`bool`
## ✅️️ 其它浏览器行为[​](https://www.drissionpage.cn/browser_control/browser_object#️️-其它浏览器行为 "✅️️ 其它浏览器行为的直接链接")
### 📌 `wait()`[​](https://www.drissionpage.cn/browser_control/browser_object#-wait "-wait的直接链接")
此方法用于等待若干秒。 `scope`为`None`时，效果与`time.sleep()`没有区别，等待指定秒数。 `scope`不为`None`时，获取两个参数之间的一个随机值，等待这个数值的秒数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 要等待的秒数，`scope`不为`None`时表示随机数范围起始值  
`scope`| `float`| `None`| 随机数范围结束值  
返回类型| 说明  
---|---  
`Chromium`| 浏览器对象自身  
### 📌 `wait.new_tab()`[​](https://www.drissionpage.cn/browser_control/browser_object#-waitnew_tab "-waitnew_tab的直接链接")
此方法用于等待新标签页出现。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`则使用对象`timeout`属性  
`curr_tab`| `str``ChromiumTab``MixTab`| `None`| 指定当前最新的 Tab 对象或标签页 id，用于判断新标签页出现，为`None`自动获取  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`str`| 等待成功返回新标签页 id  
`False`| 等待失败返回`False`  
### 📌 `wait.download_begin()`[​](https://www.drissionpage.cn/browser_control/browser_object#-waitdownload_begin "-waitdownload_begin的直接链接")
此方法用于等待浏览器下载开始。
有些下载是从临时闪现的标签页触发的，这种需要由浏览器对象去捕捉。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），`None`使用页面对象超时时间  
`cancel_it`| `bool`| `False`| 是否取消该任务  
返回类型| 说明  
---|---  
`DownloadMission`| 等待成功返回下载任务对象  
`False`| 等待失败返回`False`  
### 📌 `wait.downloads_done()`[​](https://www.drissionpage.cn/browser_control/browser_object#-waitdownloads_done "-waitdownloads_done的直接链接")
此方法用于等待所有浏览器下载任务结束。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时无限等待  
`cancel_if_timeout`| `bool`| `True`| 超时时是否取消剩余任务  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
### 📌 `clear_cache()`[​](https://www.drissionpage.cn/browser_control/browser_object#-clear_cache "-clear_cache的直接链接")
此方法用于清除缓存。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cache`| `bool`| `True`| 是否清除缓存  
`cookies`| `bool`| `True`| 是否清除 cookies  
**返回：**`None`
### 📌 `reconnect()`[​](https://www.drissionpage.cn/browser_control/browser_object#-reconnect "-reconnect的直接链接")
此方法用于关闭与浏览器连接，并重新创建连接。
**参数：** 无
**返回：**`None`
### 📌 `quit()`[​](https://www.drissionpage.cn/browser_control/browser_object#-quit "-quit的直接链接")
此方法用于关闭浏览器。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `5`| 等待浏览器关闭超时时间（秒）  
`force`| `bool`| `False`| 是否立刻强制终止进程  
`del_data`| `bool`| `False`| 是否删除用户文件夹  
**返回：**`None`
[ 上一页🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)[下一页🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
  * [✅️️ 获取标签页对象或信息](https://www.drissionpage.cn/browser_control/browser_object#️️-获取标签页对象或信息)
    * [📌 `get_tab()`](https://www.drissionpage.cn/browser_control/browser_object#-get_tab)
    * [📌 `get_tabs()`](https://www.drissionpage.cn/browser_control/browser_object#-get_tabs)
    * [📌 `latest_tab`](https://www.drissionpage.cn/browser_control/browser_object#-latest_tab)
    * [📌 `tabs_count`](https://www.drissionpage.cn/browser_control/browser_object#-tabs_count)
    * [📌 `tab_ids`](https://www.drissionpage.cn/browser_control/browser_object#-tab_ids)
  * [✅️️ 标签页操作](https://www.drissionpage.cn/browser_control/browser_object#️️-标签页操作)
    * [📌 `new_tab()`](https://www.drissionpage.cn/browser_control/browser_object#-new_tab)
    * [📌 `activate_tab()`](https://www.drissionpage.cn/browser_control/browser_object#-activate_tab)
    * [📌 `close_tabs()`](https://www.drissionpage.cn/browser_control/browser_object#-close_tabs)
    * [📌 单例模式说明](https://www.drissionpage.cn/browser_control/browser_object#-单例模式说明)
  * [✅️️ 浏览器运行参数](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器运行参数)
    * [📌 `user_data_path`](https://www.drissionpage.cn/browser_control/browser_object#-user_data_path)
    * [📌 `download_path`](https://www.drissionpage.cn/browser_control/browser_object#-download_path)
    * [📌 几种超时参数](https://www.drissionpage.cn/browser_control/browser_object#-几种超时参数)
    * [📌 `timeout`](https://www.drissionpage.cn/browser_control/browser_object#-timeout)
    * [📌 `load_mode`](https://www.drissionpage.cn/browser_control/browser_object#-load_mode)
  * [✅️️ 浏览器运行设置](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器运行设置)
    * [📌 `set.timeouts()`](https://www.drissionpage.cn/browser_control/browser_object#-settimeouts)
    * [📌 加载模式设置](https://www.drissionpage.cn/browser_control/browser_object#-加载模式设置)
    * [📌 `set.retry_times()`](https://www.drissionpage.cn/browser_control/browser_object#-setretry_times)
    * [📌 `set.retry_interval()`](https://www.drissionpage.cn/browser_control/browser_object#-setretry_interval)
    * [📌 `set.cookies()`](https://www.drissionpage.cn/browser_control/browser_object#-setcookies)
    * [📌 `set.cookies.clear()`](https://www.drissionpage.cn/browser_control/browser_object#-setcookiesclear)
    * [📌 `set.auto_handle_alert()`](https://www.drissionpage.cn/browser_control/browser_object#-setauto_handle_alert)
    * [📌 `set.download_path()`](https://www.drissionpage.cn/browser_control/browser_object#-setdownload_path)
    * [📌 `set.download_file_name()`](https://www.drissionpage.cn/browser_control/browser_object#-setdownload_file_name)
    * [📌 `set.when_download_file_exists()`](https://www.drissionpage.cn/browser_control/browser_object#-setwhen_download_file_exists)
    * [📌 `set.NoneElement_value()`](https://www.drissionpage.cn/browser_control/browser_object#-setnoneelement_value)
  * [✅️️ 浏览器信息](https://www.drissionpage.cn/browser_control/browser_object#️️-浏览器信息)
    * [📌 `cookies()`](https://www.drissionpage.cn/browser_control/browser_object#-cookies)
    * [📌 `process_id`](https://www.drissionpage.cn/browser_control/browser_object#-process_id)
    * [📌 `states.is_alive`](https://www.drissionpage.cn/browser_control/browser_object#-statesis_alive)
    * [📌 `states.is_existed`](https://www.drissionpage.cn/browser_control/browser_object#-statesis_existed)
    * [📌 `states.is_headless`](https://www.drissionpage.cn/browser_control/browser_object#-statesis_headless)
    * [📌 `states.is_incognito`](https://www.drissionpage.cn/browser_control/browser_object#-statesis_incognito)
  * [✅️️ 其它浏览器行为](https://www.drissionpage.cn/browser_control/browser_object#️️-其它浏览器行为)
    * [📌 `wait()`](https://www.drissionpage.cn/browser_control/browser_object#-wait)
    * [📌 `wait.new_tab()`](https://www.drissionpage.cn/browser_control/browser_object#-waitnew_tab)
    * [📌 `wait.download_begin()`](https://www.drissionpage.cn/browser_control/browser_object#-waitdownload_begin)
    * [📌 `wait.downloads_done()`](https://www.drissionpage.cn/browser_control/browser_object#-waitdownloads_done)
    * [📌 `clear_cache()`](https://www.drissionpage.cn/browser_control/browser_object#-clear_cache)
    * [📌 `reconnect()`](https://www.drissionpage.cn/browser_control/browser_object#-reconnect)
    * [📌 `quit()`](https://www.drissionpage.cn/browser_control/browser_object#-quit)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/browser_object)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/browser_object)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
