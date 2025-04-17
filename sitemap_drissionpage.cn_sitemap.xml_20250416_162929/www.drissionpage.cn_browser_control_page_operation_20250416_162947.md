# Content from: https://www.drissionpage.cn/browser_control/page_operation

[跳到主要内容](https://www.drissionpage.cn/browser_control/page_operation#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/page_operation)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/page_operation)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/page_operation)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/page_operation)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/page_operation)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 页面交互


本页总览
# 🛰️ 页面交互
本节介绍浏览器页面交互功能。
一个 Tab 对象控制一个浏览器的标签页，是页面控制的主要单位。
## ✅️️ 页面跳转[​](https://www.drissionpage.cn/browser_control/page_operation#️️-页面跳转 "✅️️ 页面跳转的直接链接")
### 📌 `get()`[​](https://www.drissionpage.cn/browser_control/page_operation#-get "-get的直接链接")
详见 “访问网页” 章节。
### 📌 `back()`[​](https://www.drissionpage.cn/browser_control/page_operation#-back "-back的直接链接")
此方法用于在浏览历史中后退若干步。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`steps`| `int`| `1`| 后退步数  
**返回：**`None`
**示例：**
```
tab.back(2)# 后退两个网页
```

### 📌 `forward()`[​](https://www.drissionpage.cn/browser_control/page_operation#-forward "-forward的直接链接")
此方法用于在浏览历史中前进若干步。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`steps`| `int`| `1`| 前进步数  
**返回：**`None`
```
tab.forward(2)# 前进两步
```

### 📌 `refresh()`[​](https://www.drissionpage.cn/browser_control/page_operation#-refresh "-refresh的直接链接")
此方法用于刷新当前页面。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`ignore_cache`| `bool`| `False`| 刷新时是否忽略缓存  
**返回：**`None`
**示例：**
```
tab.refresh()# 刷新页面
```

### 📌 `stop_loading()`[​](https://www.drissionpage.cn/browser_control/page_operation#-stop_loading "-stop_loading的直接链接")
此方法用于强制停止当前页面加载。
**参数：** 无
**返回：**`None`
### 📌 `set.blocked_urls()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setblocked_urls "-setblocked_urls的直接链接")
此方法用于设置忽略的连接。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`urls`| `str``list``tuple``None`| 必填| 要忽略的 url，可传入多个，可用`'*'`通配符，传入`None`时清空已设置的项  
**返回：**`None`
**示例：**
```
tab.set.blocked_urls('*.css*')# 设置不加载css文件
```

## ✅️️ 元素管理[​](https://www.drissionpage.cn/browser_control/page_operation#️️-元素管理 "✅️️ 元素管理的直接链接")
### 📌 `add_ele()`[​](https://www.drissionpage.cn/browser_control/page_operation#-add_ele "-add_ele的直接链接")
此方法用于创建一个元素。可选择是否插入到 DOM。
`html_or_info`传入元素完整 html 文本时，会插入到 DOM。如`insert_to`参数为`None`，插入到`body`元素。
传入元素信息（格式：`(tag, {name: value})`）时，如`insert_to`参数为`None`，不插入到 DOM。此时返回的元素需用 js 方式点击。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`html_or_info`| `str``Tuple[str, dict]`| 必填| 新元素的 html 文本或信息；为`tuple`可新建不加入到 DOM 的元素  
`insert_to`| `str``ChromiumElement``Tuple[str, str]`| `None`| 插入到哪个元素中，可接收元素对象和定位符；如为`None`，`html_or_info`是`str`时添加到 body，否则不添加到 DOM  
`before`| `str``ChromiumElement``Tuple[str, str]`| `None`| 在哪个子节点前面插入，可接收对象和定位符，为`None`插入到父元素末尾  
返回类型| 说明  
---|---  
`ChromiumElement`| 新建的元素对象  
**添加一个可见的元素：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')html ='<a href="http://DrissionPage.cn" target="blank">DrissionPage </a> 'ele = tab.add_ele(html,'#s-top-left','新闻')# 插入到导航栏ele.click()
```

**添加一个不可见的元素：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabinfo =('a',{'innerText':'DrissionPage','href':'http://DrissionPage.cn','target':'blank'})ele = tab.add_ele(info)ele.click('js')# 需用js点击
```

### 📌 `remove_ele()`[​](https://www.drissionpage.cn/browser_control/page_operation#-remove_ele "-remove_ele的直接链接")
此方法用于从页面上删除一个元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_ele`| `str``Tuple[str, str]``ChromiumElement`| 必填| 要删除的元素，可以是元素或定位符  
**返回：**`None`
**示例：**
```
# 删除一个已获得的元素ele = tab('tag:a')tab.remove_ele(ele)# 删除用定位符找到的元素tab.remove_ele('tag:a')
```

## ✅️️ 执行脚本或命令[​](https://www.drissionpage.cn/browser_control/page_operation#️️-执行脚本或命令 "✅️️ 执行脚本或命令的直接链接")
### 📌 `run_js()`[​](https://www.drissionpage.cn/browser_control/page_operation#-run_js "-run_js的直接链接")
此方法用于执行 js 脚本。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本或脚本文件路径  
`*args`| -| 无| 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`...  
`as_expr`| `bool`| `False`| 是否作为表达式运行，为`True`时`args`参数无效  
`timetout`| `float`| `None`| js 超时时间（秒），为`None`则使用页面`timeouts.script`设置  
返回类型| 说明  
---|---  
`Any`| 脚本执行结果  
**示例：**
```
# 用传入参数的方式执行 js 脚本显示弹出框显示 Hello world!tab.run_js('alert(arguments[0]+arguments[1]);','Hello',' world!')
```

注意
  * 如果`as_expr`为`True`，脚本应是返回一个结果的形式，并且不能有`return`
  * 如果`as_expr`不为`True'，脚本应尽量写成一个方法。


### 📌 `run_js_loaded()`[​](https://www.drissionpage.cn/browser_control/page_operation#-run_js_loaded "-run_js_loaded的直接链接")
此方法用于运行 js 脚本，执行前等待页面加载完毕。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本  
`*args`| -| 无| 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`...  
`as_expr`| `bool`| `False`| 是否作为表达式运行，为`True`时`args`参数无效  
`timetout`| `float`| `None`| js 超时时间（秒），为`None`则使用页面`timeouts.script`设置  
返回类型| 说明  
---|---  
`Any`| 脚本执行结果  
### 📌 `run_async_js()`[​](https://www.drissionpage.cn/browser_control/page_operation#-run_async_js "-run_async_js的直接链接")
此方法用于以异步方式执行 js 代码。
**参数：**
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本  
`*args`| -| 无| 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`...  
`as_expr`| `bool`| `False`| 是否作为表达式运行，为`True`时`args`参数无效  
**返回：**`None`
### 📌 `run_cdp()`[​](https://www.drissionpage.cn/browser_control/page_operation#-run_cdp "-run_cdp的直接链接")
此方法用于执行 Chrome DevTools Protocol 语句。
cdp 用法详见 [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/)。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cmd`| `str`| 必填| 协议项目  
`**cmd_args`| -| 无| 项目参数  
返回类型| 说明  
---|---  
`dict`| 执行返回的结果  
**示例：**
```
# 停止页面加载tab.run_cdp('Page.stopLoading')
```

### 📌 `run_cdp_loaded()`[​](https://www.drissionpage.cn/browser_control/page_operation#-run_cdp_loaded "-run_cdp_loaded的直接链接")
此方法用于执行 Chrome DevTools Protocol 语句，执行前先确保页面加载完毕。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cmd`| `str`| 必填| 协议项目  
`**cmd_args`| -| 无| 项目参数  
返回类型| 说明  
---|---  
`dict`| 执行返回的结果  
## ✅️️ cookies 及缓存[​](https://www.drissionpage.cn/browser_control/page_operation#️️-cookies-及缓存 "✅️️ cookies 及缓存的直接链接")
### 📌 `set.cookies()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setcookies "-setcookies的直接链接")
此方法用于设置 cookie。可设置一个或多个。
设置一个 cookie 支持的格式：
  * `Cookie`：单个`Cookie`对象
  * `str`：`'name=value; domain=****; ...'`或`'name=****; value=****; domain=****; ...'`格式，只支持用`';'`分隔
  * `dict`：`{'name': '****', 'value': '****', 'domain': '****', ...}`或`{name: value, 'domain': '****', ...}`格式


设置多个 cookie 支持的格式：
  * `list`或`tuple`：上面几种形式的单个 cookie 放到列表中传入即可
  * `dict`：`{name1: value1, name2: value2, ..., 'domain': '****', ...}`格式
  * `str`：`'name1=value1; name2=value2; ... domain=****; ...'`格式，多个 cookie 之间只能用`';'`分隔
  * `CookieJar`：单个`CookieJar`对象

参数名称| 类型| 默认值| 说明  
---|---|---|---  
`cookies`| `Cookie``CookieJar``list``tuple``str``dict`| 必填| cookies 信息  
**返回：**`None`
**示例：**
```
# 可以接受多种类型的参数cookies1 =['name1=value1','name2=value2']cookies2 ='name1=value1; name2=value2; path=/; domain=.example.com;'cookies3 ={'name1':'value1','name2':'value2','domain':'.example.com'}tab.set.cookies(cookies1)
```

### 📌 `set.cookies.clear()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setcookiesclear "-setcookiesclear的直接链接")
此方法用于清除所有 cookie。
**参数：** 无
**返回：**`None`
### 📌 `set.cookies.remove()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setcookiesremove "-setcookiesremove的直接链接")
此方法用于删除一个 cookie。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| cookie 的 name 字段  
`url`| `str`| `None`| cookie 的 url 字段  
`domain`| `str`| `None`| cookie 的 domain 字段  
`path`| `str`| `None`| cookie 的 path 字段  
**返回：**`None`
### 📌 `set.session_storage()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setsession_storage "-setsession_storage的直接链接")
此方法用于设置或删除某项 sessionStorage 信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`item`| `str`| 必填| 要设置的项  
`value`| `str``False`| 必填| 为`False`时，删除该项  
**返回：**`None`
**示例：**
```
tab.set.session_storage(item='abc', value='123')
```

### 📌 `set.local_storage()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setlocal_storage "-setlocal_storage的直接链接")
此方法用于设置或删除某项 localStorage 信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`item`| `str`| 必填| 要设置的项  
`value`| `str``False`| 必填| 为`False`时，删除该项  
**返回：**`None`
### 📌 `clear_cache()`[​](https://www.drissionpage.cn/browser_control/page_operation#-clear_cache "-clear_cache的直接链接")
此方法用于清除缓存，可选择要清除的项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`session_storage`| `bool`| `True`| 是否清除 sessionstorage  
`local_storage`| `bool`| `True`| 是否清除 localStorage  
`cache`| `bool`| `True`| 是否清除 cache  
`cookies`| `bool`| `True`| 是否清除 cookies  
**返回：**`None`
**示例：**
```
tab.clear_cache(cookies=False)# 除了 cookies，其它都清除
```

## ✅️️ 运行参数设置[​](https://www.drissionpage.cn/browser_control/page_operation#️️-运行参数设置 "✅️️ 运行参数设置的直接链接")
各种设置功能藏在`set`属性中。
### 📌 `set.retry_times()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setretry_times "-setretry_times的直接链接")
此方法用于设置连接失败时重连次数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| 必填| 次数  
**返回：**`None`
### 📌 `set.retry_interval()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setretry_interval "-setretry_interval的直接链接")
此方法用于设置连接失败时重连间隔。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`interval`| `float`| 必填| 秒数  
**返回：**`None`
### 📌 `set.timeouts()`[​](https://www.drissionpage.cn/browser_control/page_operation#-settimeouts "-settimeouts的直接链接")
此方法用于设置三种超时时间，单位为秒。可单独设置，为`None`表示不改变原来设置。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`base`| `float`| `None`| 整体超时时间  
`page_load`| `float`| `None`| 页面加载超时时间  
`script`| `float`| `None`| 脚本运行超时时间  
**返回：**`None`
**示例：**
```
tab.set.timeouts(base=10, page_load=30)
```

### 📌 `set.load_mode`[​](https://www.drissionpage.cn/browser_control/page_operation#-setload_mode "-setload_mode的直接链接")
此属性用于设置页面加载策略，调用其方法选择某种策略。
方法名称| 参数| 说明  
---|---|---  
`normal()`| 无| 等待页面完全加载完成，为默认状态  
`eager()`| 无| 等待文档加载完成就结束，不等待资源加载  
`none()`| 无| 页面连接完成就结束  
**示例：**
```
tab.set.load_mode.normal()tab.set.load_mode.eager()tab.set.load_mode.none()
```

### 📌 `set.user_agent()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setuser_agent "-setuser_agent的直接链接")
此方法用于为浏览器当前标签页设置 user agent。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`ua`| `str`| 必填| user agent 字符串  
`platform`| `str`| `None`| 平台类型，如`'android'`  
**返回：**`None`
### 📌 `set.headers()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setheaders "-setheaders的直接链接")
此方法用于设置额外添加到当前页面请求 headers 的参数。
headers 可以是`dict`格式的，也可以是文本格式。
文本格式不同字段用`\n`分隔，字段 key 和 value 用`': '`分隔，即从浏览器直接复制的格式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`headers`| `dict``str`| 必填| headers 信息  
**返回：**`None`
**示例：**
```
# dict格式h ={'connection':'keep-alive','accept-charset':'GB2312,utf-8;q=0.7,*;q=0.7'}tab.set.headers(headers=h)# 文本格式h ='''connection: keep-aliveaccept-charset: GB2312,utf-8;q=0.7,*;q=0.7'''tab.set.headers(headers=h)
```

## ✅️️ 窗口管理[​](https://www.drissionpage.cn/browser_control/page_operation#️️-窗口管理 "✅️️ 窗口管理的直接链接")
窗口管理功能藏在`set.window`属性中。
### 📌 `set.window.max()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowmax "-setwindowmax的直接链接")
此方法用于使窗口最大化。
**参数：** 无
**返回：**`None`
**示例：**
```
tab.set.window.max()
```

### 📌 `set.window.mini()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowmini "-setwindowmini的直接链接")
此方法用于使窗口最小化。
**参数：** 无
**返回：**`None`
### 📌 `set.window.full()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowfull "-setwindowfull的直接链接")
此方法用于使窗口切换到全屏模式。
**参数：** 无
**返回：**`None`
### 📌 `set.window.normal()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindownormal "-setwindownormal的直接链接")
此方法用于使窗口切换到普通模式。
**参数：** 无
**返回：**`None`
### 📌 `set.window.size()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowsize "-setwindowsize的直接链接")
此方法用于设置窗口大小。只传入一个参数时另一个参数不会变化。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`width`| `int`| `None`| 窗口宽度  
`height`| `int`| `None`| 窗口高度  
**返回：**`None`
**示例：**
```
tab.set.window.size(500,500)
```

### 📌 `set.window.location()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowlocation "-setwindowlocation的直接链接")
此方法用于设置窗口位置。只传入一个参数时另一个参数不会变化。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`x`| `int`| `None`| 距离顶部距离  
`y`| `int`| `None`| 距离左边距离  
**返回：**`None`
**示例：**
```
tab.set.window.location(500,500)
```

### 📌 `set.window.hide()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowhide "-setwindowhide的直接链接")
此方法用于隐藏浏览器窗口。
与 headless 模式不一样，这个方法是直接隐藏浏览器进程。在任务栏上也会消失。只支持 Windows 系统，并且必需已安装 pypiwin32 库才可使用。
不过，窗口隐藏后，如果有新窗口出现，整个浏览器又会显现出来。
**参数：** 无
**返回：**`None`
**示例：**
```
tab.set.window.hide()
```

注意
  * 浏览器隐藏后并没有关闭，下次运行程序还会接管已隐藏的浏览器
  * 浏览器隐藏后，如果有新建标签页，会自行显示出来


### 📌 `set.window.show()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setwindowshow "-setwindowshow的直接链接")
此方法用于显示当前浏览器窗口。
**参数：** 无
**返回：**`None`
## ✅️️ 页面滚动[​](https://www.drissionpage.cn/browser_control/page_operation#️️-页面滚动 "✅️️ 页面滚动的直接链接")
页面滚动的功能藏在`scroll`属性中。
### 📌 `scroll()`或`scroll.down()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scroll或scrolldown "-scroll或scrolldown的直接链接")
这两个方法效果是一样的，用于使页面向下滚动若干像素，水平位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.up()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollup "-scrollup的直接链接")
此方法用于使页面向上滚动若干像素，水平位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
**示例：**
```
tab.scroll.up(30)
```

### 📌 `scroll.right()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollright "-scrollright的直接链接")
此方法用于使页面向右滚动若干像素，垂直位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.left()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollleft "-scrollleft的直接链接")
此方法用于使页面向左滚动若干像素，垂直位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.to_top()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_top "-scrollto_top的直接链接")
此方法用于滚动页面到顶部，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
**示例：**
```
tab.scroll.to_top()
```

### 📌 `scroll.to_bottom()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_bottom "-scrollto_bottom的直接链接")
此方法用于滚动页面到底部，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.to_half()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_half "-scrollto_half的直接链接")
此方法用于滚动页面到垂直中间位置，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.to_rightmost()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_rightmost "-scrollto_rightmost的直接链接")
此方法用于滚动页面到最右边，垂直位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.to_leftmost()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_leftmost "-scrollto_leftmost的直接链接")
此方法用于滚动页面到最左边，垂直位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
### 📌 `scroll.to_location()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_location "-scrollto_location的直接链接")
此方法用于滚动页面到滚动到指定位置。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`x`| `int`| 必填| 水平位置，单位是像素  
`y`| `int`| 必填| 垂直位置，单位是像素  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
**示例：**
```
tab.scroll.to_location(300,50)
```

### 📌 `scroll.to_see()`[​](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_see "-scrollto_see的直接链接")
此方法用于滚动页面直到元素可见。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_ele`| `str``tuple``ChromiumElement`| 必填| 元素的定位信息，可以是元素、定位符  
`center`| `bool``None`| `None`| 是否尽量滚动到页面正中，为`None`时如果被遮挡，则滚动到页面正中  
返回类型| 说明  
---|---  
`ChromiumTab`| `ChromiumTab`执行滚动时返回页面对象自身  
`MixTab`| `MixTab`执行滚动时返回页面对象自身  
`ChromiumFrame`| `ChromiumFrame`执行滚动时返回页面对象自身  
**示例：**
```
# 滚动到某个已获取到的元素ele = tab.ele('tag:div')tab.scroll.to_see(ele)# 滚动到按定位符查找到的元素tab.scroll.to_see('tag:div')
```

## ✅️️ 滚动设置[​](https://www.drissionpage.cn/browser_control/page_operation#️️-滚动设置 "✅️️ 滚动设置的直接链接")
页面滚动有两种方式，一种是滚动时直接跳到目标位置，第二种是平滑滚动，需要一定时间。后者滚动时间难以确定，容易导致程序不稳定，点击不准确的问题。
一些网站会在 css 设置中指定网站使用平滑滚动，这是我们不希望的，但本着让开发者拥有充分选择权利的原则，本库没有强制修改，而是提供两项设置供开发者选择。
### 📌 `set.scroll.smooth()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setscrollsmooth "-setscrollsmooth的直接链接")
此方法设置网站是否开启平滑滚动。建议用此方法为网页关闭平滑滚动。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`None`
**示例：**
```
tab.set.scroll.smooth(on_off=False)
```

### 📌 `set.scroll.wait_complete()`[​](https://www.drissionpage.cn/browser_control/page_operation#-setscrollwait_complete "-setscrollwait_complete的直接链接")
此方法用于设置滚动后是否等待滚动结束。在不想关闭网页平滑滚动功能时，可开启此设置以保障滚动结束后才执行后面的步骤
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| `bool`表示开或关  
**返回：**`None`
**示例：**
```
tab.set.scroll.wait_complete(on_off=True)
```

## ✅️️ 弹出消息处理[​](https://www.drissionpage.cn/browser_control/page_operation#️️-弹出消息处理 "✅️️ 弹出消息处理的直接链接")
### 📌 `handle_alert()`[​](https://www.drissionpage.cn/browser_control/page_operation#-handle_alert "-handle_alert的直接链接")
此方法用于处理提示框。 它能够设置等待时间，等待提示框出现才进行处理，若超时没等到提示框，返回`False`。 也可只获取提示框文本而不处理提示框。 还可以处理下一个出现的提示框，这在处理离开页面时触发的弹窗非常有用。
注意
程序无法接管一个已经弹出了提示框的浏览器或标签页。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`accept`| `bool``None`| `True`| `True`表示确认，`False`表示取消，`None`不会按按钮但依然返回文本值  
`send`| `str`| `None`| 处理 prompt 提示框时可输入文本  
`timeout`| `float`| `None`| 等待提示框出现的超时时间（秒），为`None`时使用页面整体超时时间  
`next_one`| `bool`| `False`| 是否处理下一个出现的弹窗，为`True`时`timeout`参数无效  
返回类型| 说明  
---|---  
`str`| 提示框内容文本  
`False`| 未等到提示框则返回`False`  
**示例：**
```
# 确认提示框并获取提示框文本txt = tab.handle_alert()# 点击取消tab.handle_alert(accept=False)# 给 prompt 提示框输入文本并点击确定tab.handle_alert(accept=True, send='some text')# 不处理提示框，只获取提示框文本txt = tab.handle_alert(accept=None)
```

### 📌 自动处理[​](https://www.drissionpage.cn/browser_control/page_operation#-自动处理 "📌 自动处理的直接链接")
标签页对象可使用`set.auto_handle_alert()`方法设置自动处理该 tab 的提示框，使提示框不会弹窗而直接被处理掉。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_off`| `bool`| `True`| 开或关  
`accept`| `bool`| `True`| 确定还是取消  
**返回：**`None`
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.set.auto_handle_alert()# 这之后出现的弹窗都会自动确认
```

### 📌 全局自动处理[​](https://www.drissionpage.cn/browser_control/page_operation#-全局自动处理 "📌 全局自动处理的直接链接")
如果需要设置所有标签页都自动处理 alert，可用`Chromium`对象进行设置。
```
from DrissionPage import Chromiumbrowser = Chromium()browser.set.auto_handle_alert()
```

或者
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.browser.set.auto_handle_alert()
```

## ✅️️ 关闭及重连[​](https://www.drissionpage.cn/browser_control/page_operation#️️-关闭及重连 "✅️️ 关闭及重连的直接链接")
### 📌 `disconnect()`[​](https://www.drissionpage.cn/browser_control/page_operation#-disconnect "-disconnect的直接链接")
此方法用于页面对象断开与页面的连接，但不关闭标签页。断开后，对象不能对标签页进行操作。
Tab 和`ChromiumFrame`对象都有此方法。
**参数：** 无
**返回：**`None`
### 📌 `reconnect()`[​](https://www.drissionpage.cn/browser_control/page_operation#-reconnect "-reconnect的直接链接")
此方法用于关闭与页面连接，然后重建一个新连接。
这主要用于应付长期运行导致内存占用过高，断开连接可释放内存，然后重连继续控制浏览器。
Tab 和`ChromiumFrame`对象都有此方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`wait`| `float`| `0`| 关闭后等待多少秒再连接  
**返回：**`None`
### 📌 `close()`[​](https://www.drissionpage.cn/browser_control/page_operation#-close "-close的直接链接")
此方法用于关闭标签页。可关闭自己或自己以外的。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`others`| `bool`| `False`| 是否关闭自己以外的标签页  
`session`| `bool`| `False`| 是否同时关闭内置`Session`对象，只对自己有效  
**返回：**`None`
[ 上一页🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)[下一页🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
  * [✅️️ 页面跳转](https://www.drissionpage.cn/browser_control/page_operation#️️-页面跳转)
    * [📌 `get()`](https://www.drissionpage.cn/browser_control/page_operation#-get)
    * [📌 `back()`](https://www.drissionpage.cn/browser_control/page_operation#-back)
    * [📌 `forward()`](https://www.drissionpage.cn/browser_control/page_operation#-forward)
    * [📌 `refresh()`](https://www.drissionpage.cn/browser_control/page_operation#-refresh)
    * [📌 `stop_loading()`](https://www.drissionpage.cn/browser_control/page_operation#-stop_loading)
    * [📌 `set.blocked_urls()`](https://www.drissionpage.cn/browser_control/page_operation#-setblocked_urls)
  * [✅️️ 元素管理](https://www.drissionpage.cn/browser_control/page_operation#️️-元素管理)
    * [📌 `add_ele()`](https://www.drissionpage.cn/browser_control/page_operation#-add_ele)
    * [📌 `remove_ele()`](https://www.drissionpage.cn/browser_control/page_operation#-remove_ele)
  * [✅️️ 执行脚本或命令](https://www.drissionpage.cn/browser_control/page_operation#️️-执行脚本或命令)
    * [📌 `run_js()`](https://www.drissionpage.cn/browser_control/page_operation#-run_js)
    * [📌 `run_js_loaded()`](https://www.drissionpage.cn/browser_control/page_operation#-run_js_loaded)
    * [📌 `run_async_js()`](https://www.drissionpage.cn/browser_control/page_operation#-run_async_js)
    * [📌 `run_cdp()`](https://www.drissionpage.cn/browser_control/page_operation#-run_cdp)
    * [📌 `run_cdp_loaded()`](https://www.drissionpage.cn/browser_control/page_operation#-run_cdp_loaded)
  * [✅️️ cookies 及缓存](https://www.drissionpage.cn/browser_control/page_operation#️️-cookies-及缓存)
    * [📌 `set.cookies()`](https://www.drissionpage.cn/browser_control/page_operation#-setcookies)
    * [📌 `set.cookies.clear()`](https://www.drissionpage.cn/browser_control/page_operation#-setcookiesclear)
    * [📌 `set.cookies.remove()`](https://www.drissionpage.cn/browser_control/page_operation#-setcookiesremove)
    * [📌 `set.session_storage()`](https://www.drissionpage.cn/browser_control/page_operation#-setsession_storage)
    * [📌 `set.local_storage()`](https://www.drissionpage.cn/browser_control/page_operation#-setlocal_storage)
    * [📌 `clear_cache()`](https://www.drissionpage.cn/browser_control/page_operation#-clear_cache)
  * [✅️️ 运行参数设置](https://www.drissionpage.cn/browser_control/page_operation#️️-运行参数设置)
    * [📌 `set.retry_times()`](https://www.drissionpage.cn/browser_control/page_operation#-setretry_times)
    * [📌 `set.retry_interval()`](https://www.drissionpage.cn/browser_control/page_operation#-setretry_interval)
    * [📌 `set.timeouts()`](https://www.drissionpage.cn/browser_control/page_operation#-settimeouts)
    * [📌 `set.load_mode`](https://www.drissionpage.cn/browser_control/page_operation#-setload_mode)
    * [📌 `set.user_agent()`](https://www.drissionpage.cn/browser_control/page_operation#-setuser_agent)
    * [📌 `set.headers()`](https://www.drissionpage.cn/browser_control/page_operation#-setheaders)
  * [✅️️ 窗口管理](https://www.drissionpage.cn/browser_control/page_operation#️️-窗口管理)
    * [📌 `set.window.max()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowmax)
    * [📌 `set.window.mini()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowmini)
    * [📌 `set.window.full()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowfull)
    * [📌 `set.window.normal()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindownormal)
    * [📌 `set.window.size()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowsize)
    * [📌 `set.window.location()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowlocation)
    * [📌 `set.window.hide()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowhide)
    * [📌 `set.window.show()`](https://www.drissionpage.cn/browser_control/page_operation#-setwindowshow)
  * [✅️️ 页面滚动](https://www.drissionpage.cn/browser_control/page_operation#️️-页面滚动)
    * [📌 `scroll()`或`scroll.down()`](https://www.drissionpage.cn/browser_control/page_operation#-scroll或scrolldown)
    * [📌 `scroll.up()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollup)
    * [📌 `scroll.right()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollright)
    * [📌 `scroll.left()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollleft)
    * [📌 `scroll.to_top()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_top)
    * [📌 `scroll.to_bottom()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_bottom)
    * [📌 `scroll.to_half()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_half)
    * [📌 `scroll.to_rightmost()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_rightmost)
    * [📌 `scroll.to_leftmost()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_leftmost)
    * [📌 `scroll.to_location()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_location)
    * [📌 `scroll.to_see()`](https://www.drissionpage.cn/browser_control/page_operation#-scrollto_see)
  * [✅️️ 滚动设置](https://www.drissionpage.cn/browser_control/page_operation#️️-滚动设置)
    * [📌 `set.scroll.smooth()`](https://www.drissionpage.cn/browser_control/page_operation#-setscrollsmooth)
    * [📌 `set.scroll.wait_complete()`](https://www.drissionpage.cn/browser_control/page_operation#-setscrollwait_complete)
  * [✅️️ 弹出消息处理](https://www.drissionpage.cn/browser_control/page_operation#️️-弹出消息处理)
    * [📌 `handle_alert()`](https://www.drissionpage.cn/browser_control/page_operation#-handle_alert)
    * [📌 自动处理](https://www.drissionpage.cn/browser_control/page_operation#-自动处理)
    * [📌 全局自动处理](https://www.drissionpage.cn/browser_control/page_operation#-全局自动处理)
  * [✅️️ 关闭及重连](https://www.drissionpage.cn/browser_control/page_operation#️️-关闭及重连)
    * [📌 `disconnect()`](https://www.drissionpage.cn/browser_control/page_operation#-disconnect)
    * [📌 `reconnect()`](https://www.drissionpage.cn/browser_control/page_operation#-reconnect)
    * [📌 `close()`](https://www.drissionpage.cn/browser_control/page_operation#-close)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/page_operation)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/page_operation)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
