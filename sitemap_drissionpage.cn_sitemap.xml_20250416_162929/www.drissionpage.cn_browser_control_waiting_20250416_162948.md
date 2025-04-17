# Content from: https://www.drissionpage.cn/browser_control/waiting

[跳到主要内容](https://www.drissionpage.cn/browser_control/waiting#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/waiting)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/waiting)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/waiting)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/waiting)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/waiting)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/waiting)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 等待


本页总览
# 🛰️ 等待
网络环境不稳定，页面 js 运行时间也难以确定，自动化过程中经常遇到需要等待的情况。
如果总是用`sleep()`，显得不太优雅，等待多了浪费时间，等待不够会导致报错。
因此，程序能够智能等待是非常重要的，DrissionPage 内置了一些等待方法，可以提高程序稳定性和效率。
它们藏在页面对象和元素对象的`wait`属性里。
等待方法均有`timeout`参数，可自行设得超时时间，也可以设置超时后返回`False`还是抛出异常。
## ✅️️ 浏览器对象的等待方法[​](https://www.drissionpage.cn/browser_control/waiting#️️-浏览器对象的等待方法 "✅️️ 浏览器对象的等待方法的直接链接")
### 📌 `wait.new_tab()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitnew_tab "-waitnew_tab的直接链接")
此方法用于等待新标签页出现。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`curr_tab`| `str``ChromiumTab``MixTab`| `None`| 指定当前最新的 Tab 对象或标签页 id，用于判断新标签页出现，为`None`自动获取  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`str`| 等待成返回新标签页 id  
`False`| 等待失败返回`False`  
### 📌 `wait.download_begin()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdownload_begin "-waitdownload_begin的直接链接")
此方法用于等待浏览器一个下载任务开始，详见下载功能章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`cancel_it`| `bool`| `False`| 是否取消该任务  
返回类型| 说明  
---|---  
`DownloadMission`| 等待成功返回下载任务对象  
`False`| 等待失败  
**示例：**
```
tab('#download_btn').click()# 点击按钮触发下载tab.wait.download_begin()# 等待下载开始
```

### 📌 `wait.downloads_done()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdownloads_done "-waitdownloads_done的直接链接")
此方法用于等待浏览器所有下载任务完成，详见下载功能章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时无限等待  
`cancel_if_timeout`| `bool`| `True`| 超时时是否取消剩余任务  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
## ✅️️ 页面对象的等待方法[​](https://www.drissionpage.cn/browser_control/waiting#️️-页面对象的等待方法 "✅️️ 页面对象的等待方法的直接链接")
页面对象指`ChromiumTab`、`MixTab`和`ChromiumFrame`。
**用法：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')tab.wait.ele_displayed('tag:div')
```

### 📌 `wait.load_start()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitload_start "-waitload_start的直接链接")
此方法用于等待页面进入加载状态。 我们经常会通过点击元素进入下一个网页，并立刻获取新页面的元素。 但若跳转前的页面拥有和跳转后页面相同定位符的元素，会导致过早获取元素，跳转后失效的问题。 使用此方法，会阻塞程序，等待页面开始加载后再继续，从而避免上述问题。 我们通常只需等待页面加载开始，程序会自动等待加载结束。
注意
`get()`已内置等待加载开始，后无须跟`wait.load_start()`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None``True`| `None`| 超时时间（秒），为`None`或`Ture`时使用页面`timeout`设置为数字时等待相应时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 等待结束时是否进入加载状态  
**示例：**
```
ele.click()# 点击某个元素tab.wait.load_start()# 等待页面进入加载状态# 执行在新页面的操作print(page.title)
```

### 📌 `wait.doc_loaded()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdoc_loaded "-waitdoc_loaded的直接链接")
此方法用于等待页面文档加载完成。 一般来说都无需开发者使用，程序大部分动作都会自动等待加载完成再执行。
注意
  * 此功能仅用于等待页面主 document 加载，不能用于等待 js 加载的变化。
  * 除非`load_mode`为`None`，`get()`方法已内置等待加载完成，后面无须添加等待。


参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float``None``True`| `None`| 超时时间（秒），为`None`或`Ture`时使用页面`timeout`设置为数字时等待相应时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 等待结束时是否完成加载完成  
### 📌 `wait.eles_loaded()`[​](https://www.drissionpage.cn/browser_control/waiting#-waiteles_loaded "-waiteles_loaded的直接链接")
此方法用于等待元素被加载到 DOM，可等待全部或任意一个加载。 有时一个元素的正常出现是下一步操作的前提，用此方法可以防止一些元素加载速度慢于程序动作速度导致的误操作。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``list`| 必填| 要等待的元素，定位符  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`any_one`| `bool`| `False`| 是否等待到一个就返回  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
**示例：**
```
ele1.click()# 点击某个元素page.wait.eles_loaded('#div1')# 等待 id 为 div1 的元素加载ele2.click()# div1 加载完成后再执行下一步操作
```

### 📌 `wait.ele_displayed()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitele_displayed "-waitele_displayed的直接链接")
此方法用于等待一个元素变成显示状态。 如果当前 DOM 中查找不到指定元素，则会自动等待元素加载，再等待它显示。 元素隐藏是指元素在 DOM 内，但处于隐藏状态（即使在视口内且不被遮挡）。 父元素隐藏时子元素也是隐藏的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_ele`| `str``Tuple[str, str]``ChromiumElement`| 必填| 要等待的元素，可以是元素或定位符  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
**示例：**
```
# 等待 id 为 div1 的元素显示，超时使用页面设置tab.wait.ele_displayed('#div1')# 等待 id 为 div1 的元素显示，设置超时3秒tab.wait.ele_displayed('#div1', timeout=3)# 等待已获取到的元素被显示ele = tab.ele('#div1')tab.wait.ele_displayed(ele)
```

### 📌 `wait.ele_hidden()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitele_hidden "-waitele_hidden的直接链接")
此方法用于等待一个元素变成隐藏状态。 如果当前 DOM 中查找不到指定元素，则会自动等待元素加载，再等待它隐藏。 元素隐藏是指元素在 DOM 内，但处于隐藏状态（即使在视口内且不被遮挡）。 父元素隐藏时子元素也是隐藏的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_ele`| `str``Tuple[str, str]``ChromiumElement`| 必填| 要等待的元素，可以是元素或定位符  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
### 📌 `wait.ele_deleted()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitele_deleted "-waitele_deleted的直接链接")
此方法用于等待一个元素被从 DOM 中删除。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_ele`| `str``Tuple[str, str]``ChromiumElement`| 必填| 要等待的元素，可以是元素或定位符  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
### 📌 `wait.download_begin()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdownload_begin-1 "-waitdownload_begin-1的直接链接")
此方法用于等待下载开始，详见下载功能章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面`timeout`设置  
`cancel_it`| `bool`| `False`| 是否取消该任务  
返回类型| 说明  
---|---  
`DownloadMission`| 等待成功返回下载任务对象  
`False`| 等待失败  
**示例：**
```
tab('#download_btn').click()# 点击按钮触发下载tab.wait.download_begin()# 等待下载开始
```

### 📌 `wait.downloads_done()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdownloads_done-1 "-waitdownloads_done-1的直接链接")
此方法用于等待本标签页所有下载任务完成，详见下载功能章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时无限等待  
`cancel_if_timeout`| `bool`| `True`| 超时时是否取消剩余任务  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`对象等待成功返回自己  
`MixTab`| `MixTab`对象等待成功返回自己  
`False`| 等待失败  
### 📌 `wait.upload_paths_inputted()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitupload_paths_inputted "-waitupload_paths_inputted的直接链接")
此方法用于等待自动填写上传文件路径。详见文件上传章节。
**参数：** 无
**返回：**`None`
**示例：**
```
# 设置要上传的文件路径tab.set.upload_files('demo.txt')# 点击触发文件选择框按钮btn_ele.click()# 等待路径填入tab.wait.upload_paths_inputted()
```

### 📌 `wait.title_change()`[​](https://www.drissionpage.cn/browser_control/waiting#-waittitle_change "-waittitle_change的直接链接")
此方法用于等待 title 变成包含或不包含指定文本。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str`| 必填| 用于识别的文本  
`exclude`| `bool`| `False`| 是否排除，为`True`时当 title 不包含`text`指定文本时返回`True`  
`timeout`| `bool`| `float`| 超时时间（秒）  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumTab`| 等待成功`ChromiumTab`对象返回自身  
`MixTab`| 等待成功`MixTab`对象返回自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.url_change()`[​](https://www.drissionpage.cn/browser_control/waiting#-waiturl_change "-waiturl_change的直接链接")
此方法用于等待 url 变成包含或不包含指定文本。 比如有些网站登录时会进行多重跳转，url 发生多次变化，可用此功能等待到达最终需要的页面。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str`| 必填| 用于识别的文本  
`exclude`| `bool`| `False`| 是否排除，为`True`时当 url 不包含`text`指定文本时返回`True`  
`timeout`| `bool`| `float`| 超时时间（秒）  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumTab`| 等待成功`ChromiumTab`对象返回自身  
`MixTab`| 等待成功`MixTab`对象返回自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
**示例：**
```
# 访问网站tab.get('https://www.*****.cn/login/')# 访问登录页面tab.ele('#username').input('***')# 执行登录逻辑tab.ele('#password').input('***\n')tab.wait.url_change('https://www.*****.cn/center/')# 等待url变成后台url
```

### 📌 `wait.alert_closed()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitalert_closed "-waitalert_closed的直接链接")
此方法用于等待弹出框被关闭。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `bool`| `float`| 超时时间（秒），为`None`无限等待  
返回类型| 说明  
---|---  
`ChromiumTab`| 等待成功`ChromiumTab`对象返回自身  
`MixTab`| 等待成功`MixTab`对象返回自身  
`False`| 等待失败  
## ✅️️ 元素对象的等待方法[​](https://www.drissionpage.cn/browser_control/waiting#️️-元素对象的等待方法 "✅️️ 元素对象的等待方法的直接链接")
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('http://DrissionPage.cn')ele = tab('tag:div')ele.wait.covered()
```

### 📌 `wait.displayed()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdisplayed "-waitdisplayed的直接链接")
此方法用于等待元素从隐藏状态变成显示状态。 元素隐藏是指元素在 DOM 内，但处于隐藏状态（即使在视口内且不被遮挡）。父元素隐藏时子元素也是隐藏的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
**示例：**
```
# 等待元素显示，超时使用ele所在页面设置ele.wait.displayed()
```

### 📌 `wait.hidden()`[​](https://www.drissionpage.cn/browser_control/waiting#-waithidden "-waithidden的直接链接")
此方法用于等待元素从显示状态变成隐藏状态。 元素隐藏是指元素在 DOM 内，但处于隐藏状态（即使在视口内且不被遮挡）。父元素隐藏时子元素也是隐藏的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
**示例：**
```
# 等待元素不显示，超时为3秒ele.wait.hidden(timeout=3)
```

### 📌 `wait.deleted()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdeleted "-waitdeleted的直接链接")
此方法用于等待元素被从 DOM 删除。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
**示例：**
```
# 等待元素显示，超时使用ele所在页面设置ele.wait.deleted()
```

### 📌 `wait.has_rect()`[​](https://www.drissionpage.cn/browser_control/waiting#-waithas_rect "-waithas_rect的直接链接")
此方法用于等待元素被赋予大小。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.covered()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitcovered "-waitcovered的直接链接")
此方法用于等待元素被其它元素覆盖。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.not_covered()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitnot_covered "-waitnot_covered的直接链接")
此方法用于等待元素不被其它元素覆盖。 可用于等待遮挡被操作元素的“加载中”遮罩消失。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.enabled()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitenabled "-waitenabled的直接链接")
此方法用于等待元素变为可用状态。 不可用状态的元素仍然在 DOM 内，`disabled`属性为`False`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.disabled()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdisabled "-waitdisabled的直接链接")
此方法用于等待元素变为不可用状态。 不可用状态的元素仍然在 DOM 内，`disabled`属性为`True`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.stop_moving()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitstop_moving "-waitstop_moving的直接链接")
此方法用于等待元素运动结束。如果元素没有大小和位置信息，会在超时时抛出`NoRectError`异常。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`gap`| `float`| `0.1`| 检测运动的间隔时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
```
# 等待元素稳定tab.ele('#button1').wait.stop_moving()# 点击元素tab.ele('#button1').click()
```

### 📌 `wait.clickable()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitclickable "-waitclickable的直接链接")
此方法用于等待元素可被点击。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`wait_moved`| `bool`| `True`| 是否等待元素运动结束  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`ChromiumElement`| 元素对象自身  
`ChromiumFrame`| `<iframe>`元素的等待返回对象自身  
`False`| 等待失败  
### 📌 `wait.disabled_or_deleted()`[​](https://www.drissionpage.cn/browser_control/waiting#-waitdisabled_or_deleted "-waitdisabled_or_deleted的直接链接")
此方法用于等待元素变为不可用或被删除。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待超时时间（秒），为`None`则使用元素所在页面超时时间  
`raise_err`| `bool`| `None`| 等待失败时是否报错，为`None`时根据`Settings`设置  
返回类型| 说明  
---|---  
`bool`| 是否等待成功  
## ✅️️ 共有的等待方法[​](https://www.drissionpage.cn/browser_control/waiting#️️-共有的等待方法 "✅️️ 共有的等待方法的直接链接")
### 📌 `wait()`[​](https://www.drissionpage.cn/browser_control/waiting#-wait "-wait的直接链接")
此方法用于等待若干秒。所有对象的等待都可使用这个方法。 `scope`为`None`时，效果与`time.sleep()`没有区别，等待指定秒数。 `scope`不为`None`时，获取两个参数之间的一个随机值，等待这个数值的秒数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 要等待的秒数，`scope`不为`None`时表示随机数范围起始值  
`scope`| `float`| `None`| 随机数范围结束值  
**返回：** 调用者自身
**示例：**
```
from DrissionPage import Chromiumbrowser = Chromium()# 强制等待1秒browser.wait(1)# 获取3.5至8.5之间的一个随机数，等待这个数值的秒数browser.wait(3.5,8.5)
```

[上一页🛰️ 模式切换](https://www.drissionpage.cn/browser_control/mode_change)[下一页🛰️ 监听网络数据](https://www.drissionpage.cn/browser_control/listener)
  * [✅️️ 浏览器对象的等待方法](https://www.drissionpage.cn/browser_control/waiting#️️-浏览器对象的等待方法)
    * [📌 `wait.new_tab()`](https://www.drissionpage.cn/browser_control/waiting#-waitnew_tab)
    * [📌 `wait.download_begin()`](https://www.drissionpage.cn/browser_control/waiting#-waitdownload_begin)
    * [📌 `wait.downloads_done()`](https://www.drissionpage.cn/browser_control/waiting#-waitdownloads_done)
  * [✅️️ 页面对象的等待方法](https://www.drissionpage.cn/browser_control/waiting#️️-页面对象的等待方法)
    * [📌 `wait.load_start()`](https://www.drissionpage.cn/browser_control/waiting#-waitload_start)
    * [📌 `wait.doc_loaded()`](https://www.drissionpage.cn/browser_control/waiting#-waitdoc_loaded)
    * [📌 `wait.eles_loaded()`](https://www.drissionpage.cn/browser_control/waiting#-waiteles_loaded)
    * [📌 `wait.ele_displayed()`](https://www.drissionpage.cn/browser_control/waiting#-waitele_displayed)
    * [📌 `wait.ele_hidden()`](https://www.drissionpage.cn/browser_control/waiting#-waitele_hidden)
    * [📌 `wait.ele_deleted()`](https://www.drissionpage.cn/browser_control/waiting#-waitele_deleted)
    * [📌 `wait.download_begin()`](https://www.drissionpage.cn/browser_control/waiting#-waitdownload_begin-1)
    * [📌 `wait.downloads_done()`](https://www.drissionpage.cn/browser_control/waiting#-waitdownloads_done-1)
    * [📌 `wait.upload_paths_inputted()`](https://www.drissionpage.cn/browser_control/waiting#-waitupload_paths_inputted)
    * [📌 `wait.title_change()`](https://www.drissionpage.cn/browser_control/waiting#-waittitle_change)
    * [📌 `wait.url_change()`](https://www.drissionpage.cn/browser_control/waiting#-waiturl_change)
    * [📌 `wait.alert_closed()`](https://www.drissionpage.cn/browser_control/waiting#-waitalert_closed)
  * [✅️️ 元素对象的等待方法](https://www.drissionpage.cn/browser_control/waiting#️️-元素对象的等待方法)
    * [📌 `wait.displayed()`](https://www.drissionpage.cn/browser_control/waiting#-waitdisplayed)
    * [📌 `wait.hidden()`](https://www.drissionpage.cn/browser_control/waiting#-waithidden)
    * [📌 `wait.deleted()`](https://www.drissionpage.cn/browser_control/waiting#-waitdeleted)
    * [📌 `wait.has_rect()`](https://www.drissionpage.cn/browser_control/waiting#-waithas_rect)
    * [📌 `wait.covered()`](https://www.drissionpage.cn/browser_control/waiting#-waitcovered)
    * [📌 `wait.not_covered()`](https://www.drissionpage.cn/browser_control/waiting#-waitnot_covered)
    * [📌 `wait.enabled()`](https://www.drissionpage.cn/browser_control/waiting#-waitenabled)
    * [📌 `wait.disabled()`](https://www.drissionpage.cn/browser_control/waiting#-waitdisabled)
    * [📌 `wait.stop_moving()`](https://www.drissionpage.cn/browser_control/waiting#-waitstop_moving)
    * [📌 `wait.clickable()`](https://www.drissionpage.cn/browser_control/waiting#-waitclickable)
    * [📌 `wait.disabled_or_deleted()`](https://www.drissionpage.cn/browser_control/waiting#-waitdisabled_or_deleted)
  * [✅️️ 共有的等待方法](https://www.drissionpage.cn/browser_control/waiting#️️-共有的等待方法)
    * [📌 `wait()`](https://www.drissionpage.cn/browser_control/waiting#-wait)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/waiting)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/waiting)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
