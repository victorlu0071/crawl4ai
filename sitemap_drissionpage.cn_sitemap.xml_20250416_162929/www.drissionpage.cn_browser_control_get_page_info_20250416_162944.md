# Content from: https://www.drissionpage.cn/browser_control/get_page_info

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_page_info#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_page_info)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_page_info)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_page_info)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_page_info)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_page_info)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 获取网页信息


本页总览
# 🛰️ 获取网页信息
成功访问网页后，可使用 Tab 对象属性和方法获取页面信息。
## ✅️️ 页面信息[​](https://www.drissionpage.cn/browser_control/get_page_info#️️-页面信息 "✅️️ 页面信息的直接链接")
### 📌 `html`[​](https://www.drissionpage.cn/browser_control/get_page_info#-html "-html的直接链接")
此属性返回当前页面 html 文本。
注意
html 文本不包含`<iframe>`元素内容。
**返回类型：**`str`
### 📌 `json`[​](https://www.drissionpage.cn/browser_control/get_page_info#-json "-json的直接链接")
此属性把请求内容解析成 json。
假如用浏览器访问会返回 `*.json` 文件的 url，浏览器会把 json 数据显示出来，这个参数可以把这些数据转换为`dict`格式。
**返回类型：**`dict`
### 📌 `title`[​](https://www.drissionpage.cn/browser_control/get_page_info#-title "-title的直接链接")
此属性返回当前页面`title`文本。
**返回类型：**`str`
### 📌 `user_agent`[​](https://www.drissionpage.cn/browser_control/get_page_info#-user_agent "-user_agent的直接链接")
此属性返回当前页面 user agent 信息。
**返回类型：**`str`
### 📌 `save()`[​](https://www.drissionpage.cn/browser_control/get_page_info#-save "-save的直接链接")
把当前页面保存为文件，同时返回保存的内容。
如果`path`和`name`参数都为`None`，只返回内容，不保存文件。
Page 对象和 Tab 对象有这个方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| 保存路径，为`None`且`name`不为`None`时保存到当前路径  
`name`| `str`| `None`| 保存的文件名，为`None`且`path`不为`None`时使用 title 值  
`as_pdf`| `bool`| `False`| 为`Ture`保存为 pdf，否则保存为 mhtml 且忽略`kwargs`参数  
`**kwargs`| 多种| 无| pdf 生成参数  
pdf 生成参数包括：`landscape`, `displayHeaderFooter`, `printBackground`, `scale`, `paperWidth`, `paperHeight`, `marginTop`, `marginBottom`, `marginLeft`, `marginRight`, `pageRanges`, `headerTemplate`, `footerTemplate`, `preferCSSPageSize`, `generateTaggedPDF`, `generateDocumentOutline`
返回类型| 说明  
---|---  
`str`| `as_pdf`为`False`时返回 mhtml 文本  
`bytes`| `as_pdf`为`True`时返回文件字节数据  
## ✅️️ 运行状态信息[​](https://www.drissionpage.cn/browser_control/get_page_info#️️-运行状态信息 "✅️️ 运行状态信息的直接链接")
### 📌 `url`[​](https://www.drissionpage.cn/browser_control/get_page_info#-url "-url的直接链接")
此属性返回当前访问的 url。
**返回类型：**`str`
### 📌 `tab_id`[​](https://www.drissionpage.cn/browser_control/get_page_info#-tab_id "-tab_id的直接链接")
**返回类型：**`str`
此属性返回当前标签页的 id。
### 📌 `states.is_loading`[​](https://www.drissionpage.cn/browser_control/get_page_info#-statesis_loading "-statesis_loading的直接链接")
此属性返回页面是否正在加载状态。
**返回类型：**`bool`
### 📌 `states.is_alive`[​](https://www.drissionpage.cn/browser_control/get_page_info#-statesis_alive "-statesis_alive的直接链接")
此属性返回页面是否仍然可用，标签页已关闭则返回`False`。
**返回类型：**`bool`
### 📌 `states.ready_state`[​](https://www.drissionpage.cn/browser_control/get_page_info#-statesready_state "-statesready_state的直接链接")
此属性返回页面当前加载状态，有 4 种：
  * `'connecting'`： 网页连接中
  * `'loading'`：表示文档还在加载中
  * `'interactive'`：DOM 已加载，但资源未加载完成
  * `'complete'`：所有内容已完成加载


**返回类型：**`str`
### 📌 `url_available`[​](https://www.drissionpage.cn/browser_control/get_page_info#-url_available "-url_available的直接链接")
此属性以布尔值返回当前链接是否可用。
**返回类型：**`bool`
### 📌 `states.has_alert`[​](https://www.drissionpage.cn/browser_control/get_page_info#-stateshas_alert "-stateshas_alert的直接链接")
此属性以布尔值返回页面是否存在弹出框。
**返回类型：**`bool`
## ✅️️ 窗口信息[​](https://www.drissionpage.cn/browser_control/get_page_info#️️-窗口信息 "✅️️ 窗口信息的直接链接")
### 📌 `rect.size`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectsize "-rectsize的直接链接")
以`tuple`返回页面大小，格式：(宽, 高)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.window_size`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_size "-rectwindow_size的直接链接")
此属性以`tuple`返回窗口大小，格式：(宽, 高)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.window_location`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_location "-rectwindow_location的直接链接")
此属性以`tuple`返回窗口在屏幕上的坐标，左上角为(0, 0)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.window_state`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_state "-rectwindow_state的直接链接")
此属性以返回窗口当前状态，有`'normal'`、`'fullscreen'`、`'maximized'`、 `'minimized'`几种。
**返回类型：**`str`
### 📌 `rect.viewport_size`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_size "-rectviewport_size的直接链接")
此属性以`tuple`返回视口大小，不含滚动条，格式：(宽, 高)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.viewport_size_with_scrollbar`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_size_with_scrollbar "-rectviewport_size_with_scrollbar的直接链接")
此属性以`tuple`返回浏览器窗口大小，含滚动条，格式：(宽, 高)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.page_location`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectpage_location "-rectpage_location的直接链接")
此属性以`tuple`返回页面左上角在屏幕中坐标，左上角为(0, 0)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.viewport_location`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_location "-rectviewport_location的直接链接")
此属性以`tuple`返回视口在屏幕中坐标，左上角为(0, 0)。
**返回类型：**`Tuple[int, int]`
### 📌 `rect.scroll_position`[​](https://www.drissionpage.cn/browser_control/get_page_info#-rectscroll_position "-rectscroll_position的直接链接")
此属性返回页面滚动条位置，格式：(x, y)。
**类型：**`Tuple[float, float]`
## ✅️️ 配置参数信息[​](https://www.drissionpage.cn/browser_control/get_page_info#️️-配置参数信息 "✅️️ 配置参数信息的直接链接")
### 📌 `timeout`[​](https://www.drissionpage.cn/browser_control/get_page_info#-timeout "-timeout的直接链接")
此属性为整体默认超时时间（秒），包括元素查找、点击、处理提示框、列表选择等需要用到超时设置的地方，都以这个数据为默认值。默认为`10`。
**返回类型：**`int` 、`float`
### 📌 `timeouts`[​](https://www.drissionpage.cn/browser_control/get_page_info#-timeouts "-timeouts的直接链接")
此属性以字典方式返回三种超时时间（秒）。
  * `'base'`：与`timeout`属性是同一个值
  * `'page_load'`：用于等待页面加载
  * `'script'`：用于等待脚本执行


**返回类型：**`dict`
```
print(tab.timeouts)
```

**输出：**
```
{'base': 10, 'page_load': 30.0, 'script': 30.0}
```

### 📌 `retry_times`[​](https://www.drissionpage.cn/browser_control/get_page_info#-retry_times "-retry_times的直接链接")
此属性为网络连接失败时的重试次数，默认为`3`。
**返回类型：**`int`
### 📌 `retry_interval`[​](https://www.drissionpage.cn/browser_control/get_page_info#-retry_interval "-retry_interval的直接链接")
此属性为网络连接失败时的重试等待间隔秒数，默认为`2`。
**返回类型：**`int` 、`float`
### 📌 `load_mode`[​](https://www.drissionpage.cn/browser_control/get_page_info#-load_mode "-load_mode的直接链接")
此属性返回页面加载策略，有 3 种：
  * `'normal'`：等待页面所有资源完成加载
  * `'eager'`：DOM 加载完成即停止
  * `'none'`：页面完成连接即停止


**返回类型：**`str`
## ✅️️ cookies 和缓存信息[​](https://www.drissionpage.cn/browser_control/get_page_info#️️-cookies-和缓存信息 "✅️️ cookies 和缓存信息的直接链接")
### 📌 `cookies()`[​](https://www.drissionpage.cn/browser_control/get_page_info#-cookies "-cookies的直接链接")
此方法以列表方式返回 cookies 信息。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`all_domains`| `bool`| `False`| 是否返回所有 cookies，为`False`只返回当前 url 的  
`all_info`| `bool`| `False`| 返回的 cookies 是否包含所有信息，`False`时只包含`name`、`value`、`domain`信息  
返回类型| 说明  
---|---  
`CookiesList`| cookies 组成的列表  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')for i in tab.cookies():print(i)
```

**输出：**
```
{'domain': '.baidu.com', 'domain_specified': True, ......}......
```

### 📌 指定返回类型[​](https://www.drissionpage.cn/browser_control/get_page_info#-指定返回类型 "📌 指定返回类型的直接链接")
`cookies()`方法返回的列表可转换为其它指定格式。
  * `cookies().as_str()`：`'name1=value1; name2=value2'`格式的字符串
  * `cookies().as_dict()`：`{name1: value1, name2: value2}`格式的字典
  * `cookies().as_json()`：json 格式的字符串


说明
`as_str()`和`as_dict()`都只会保留`'name'`和`'value'`字段。
### 📌 `session_storage()`[​](https://www.drissionpage.cn/browser_control/get_page_info#-session_storage "-session_storage的直接链接")
此方法用于获取 sessionStorage 信息，可获取全部或单个项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`item`| `str`| `None`| 要获取的项目，为`None`则返回全部项目组成的字典  
返回类型| 说明  
---|---  
`dict`| `item`参数为`None`时返回所有项目  
`str`| 指定`item`时返回该项目内容  
### 📌 `local_storage()`[​](https://www.drissionpage.cn/browser_control/get_page_info#-local_storage "-local_storage的直接链接")
此方法用于获取 localStorage 信息，可获取全部或单个项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`item`| `str`| `None`| 要获取的项目，为`None`则返回全部项目组成的字典  
返回类型| 说明  
---|---  
`dict`| `item`参数为`None`时返回所有项目  
`str`| 指定`item`时返回该项目内容  
[上一页🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)[下一页🔦 概述](https://www.drissionpage.cn/browser_control/get_elements/intro)
  * [✅️️ 页面信息](https://www.drissionpage.cn/browser_control/get_page_info#️️-页面信息)
    * [📌 `html`](https://www.drissionpage.cn/browser_control/get_page_info#-html)
    * [📌 `json`](https://www.drissionpage.cn/browser_control/get_page_info#-json)
    * [📌 `title`](https://www.drissionpage.cn/browser_control/get_page_info#-title)
    * [📌 `user_agent`](https://www.drissionpage.cn/browser_control/get_page_info#-user_agent)
    * [📌 `save()`](https://www.drissionpage.cn/browser_control/get_page_info#-save)
  * [✅️️ 运行状态信息](https://www.drissionpage.cn/browser_control/get_page_info#️️-运行状态信息)
    * [📌 `url`](https://www.drissionpage.cn/browser_control/get_page_info#-url)
    * [📌 `tab_id`](https://www.drissionpage.cn/browser_control/get_page_info#-tab_id)
    * [📌 `states.is_loading`](https://www.drissionpage.cn/browser_control/get_page_info#-statesis_loading)
    * [📌 `states.is_alive`](https://www.drissionpage.cn/browser_control/get_page_info#-statesis_alive)
    * [📌 `states.ready_state`](https://www.drissionpage.cn/browser_control/get_page_info#-statesready_state)
    * [📌 `url_available`](https://www.drissionpage.cn/browser_control/get_page_info#-url_available)
    * [📌 `states.has_alert`](https://www.drissionpage.cn/browser_control/get_page_info#-stateshas_alert)
  * [✅️️ 窗口信息](https://www.drissionpage.cn/browser_control/get_page_info#️️-窗口信息)
    * [📌 `rect.size`](https://www.drissionpage.cn/browser_control/get_page_info#-rectsize)
    * [📌 `rect.window_size`](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_size)
    * [📌 `rect.window_location`](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_location)
    * [📌 `rect.window_state`](https://www.drissionpage.cn/browser_control/get_page_info#-rectwindow_state)
    * [📌 `rect.viewport_size`](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_size)
    * [📌 `rect.viewport_size_with_scrollbar`](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_size_with_scrollbar)
    * [📌 `rect.page_location`](https://www.drissionpage.cn/browser_control/get_page_info#-rectpage_location)
    * [📌 `rect.viewport_location`](https://www.drissionpage.cn/browser_control/get_page_info#-rectviewport_location)
    * [📌 `rect.scroll_position`](https://www.drissionpage.cn/browser_control/get_page_info#-rectscroll_position)
  * [✅️️ 配置参数信息](https://www.drissionpage.cn/browser_control/get_page_info#️️-配置参数信息)
    * [📌 `timeout`](https://www.drissionpage.cn/browser_control/get_page_info#-timeout)
    * [📌 `timeouts`](https://www.drissionpage.cn/browser_control/get_page_info#-timeouts)
    * [📌 `retry_times`](https://www.drissionpage.cn/browser_control/get_page_info#-retry_times)
    * [📌 `retry_interval`](https://www.drissionpage.cn/browser_control/get_page_info#-retry_interval)
    * [📌 `load_mode`](https://www.drissionpage.cn/browser_control/get_page_info#-load_mode)
  * [✅️️ cookies 和缓存信息](https://www.drissionpage.cn/browser_control/get_page_info#️️-cookies-和缓存信息)
    * [📌 `cookies()`](https://www.drissionpage.cn/browser_control/get_page_info#-cookies)
    * [📌 指定返回类型](https://www.drissionpage.cn/browser_control/get_page_info#-指定返回类型)
    * [📌 `session_storage()`](https://www.drissionpage.cn/browser_control/get_page_info#-session_storage)
    * [📌 `local_storage()`](https://www.drissionpage.cn/browser_control/get_page_info#-local_storage)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_page_info)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_page_info)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
