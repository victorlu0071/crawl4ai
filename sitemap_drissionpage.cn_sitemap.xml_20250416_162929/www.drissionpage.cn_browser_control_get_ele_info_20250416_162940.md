# Content from: https://www.drissionpage.cn/browser_control/get_ele_info

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_ele_info#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_ele_info)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_ele_info)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_ele_info)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_ele_info)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_ele_info)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_ele_info)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 获取元素信息


本页总览
# 🛰️ 获取元素信息
浏览器元素对应的对象是`ChromiumElement`和`ShadowRoot`，本节介绍如何获取元素信息。
## ✅️️ 内容和属性[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-内容和属性 "✅️️ 内容和属性的直接链接")
### 📌 `tag`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-tag "-tag的直接链接")
此属性返回元素的标签名。
**返回类型：**`str`
### 📌 `html`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-html "-html的直接链接")
此属性返回元素的`outerHTML`文本。
**返回类型：**`str`
### 📌 `inner_html`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-inner_html "-inner_html的直接链接")
此属性返回元素的`innerHTML`文本。
**返回类型：**`str`
### 📌 `text`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-text "-text的直接链接")
此属性返回元素内所有文本组合成的字符串。 该字符串已格式化，即已转码，已去除多余换行符，符合人读取习惯，便于直接使用。
**返回类型：**`str`
### 📌 `raw_text`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-raw_text "-raw_text的直接链接")
此属性返回元素内未经处理的原始文本。
**返回类型：**`str`
### 📌 `texts()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-texts "-texts的直接链接")
此方法返回元素内所有**直接** 子节点的文本，包括元素和文本节点。 它有一个参数`text_node_only`，为`True`时则只获取只返回不被包裹的文本节点。这个方法适用于获取文本节点和元素节点混排的情况。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text_node_only`| `bool`| `False`| 是否只返回文本节点  
返回类型| 说明  
---|---  
`List[str]`| 文本列表  
### 📌 `comments`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-comments "-comments的直接链接")
此属性以列表形式返回元素内的注释。
**返回类型：**`List[str]`
### 📌 `attrs`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-attrs "-attrs的直接链接")
此属性以字典形式返回元素所有属性及值。
**返回类型：**`dict`
### 📌 `attr()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-attr "-attr的直接链接")
此方法返回元素某个 attribute 属性值。它接收一个字符串参数，返回该属性值文本，无该属性时返回`None`。 此属性返回的`src`、`href`属性为已补充完整的路径。`text`属性为已格式化文本。 如果要获取未补充完整路径的`src`或`href`属性，可以用`attrs['src']`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`str`| 属性值文本  
`None`| 没有该属性返回`None`  
### 📌 `property()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-property "-property的直接链接")
此方法返回`property`属性值。它接收一个字符串参数，返回该参数的属性值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`str`| 属性值  
### 📌 `value`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-value "-value的直接链接")
此方法返回元素的`value`值。
**返回类型：**`str`
### 📌 `link`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-link "-link的直接链接")
此方法返回元素的`href`属性或`src`属性，没有这两个属性则返回`None`。
**返回类型：**`str`
### 📌 `pseudo.before`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-pseudobefore "-pseudobefore的直接链接")
此属性以文本形式返回当前元素的`::before`伪元素内容。
**类型：**`str`
### 📌 `pseudo.after`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-pseudoafter "-pseudoafter的直接链接")
此属性以文本形式返回当前元素的`::after`伪元素内容。
**类型：**`str`
### 📌 `style()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-style "-style的直接链接")
该方法返回元素 css 样式属性值，可获取伪元素的属性。它有两个参数，`style`参数输入样式属性名称，`pseudo_ele` 参数输入伪元素名称，省略则获取普通元素的 css 样式属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`style`| `str`| 必填| 样式名称  
`pseudo_ele`| `str`| `''`| 伪元素名称（如有）  
返回类型| 说明  
---|---  
`str`| 样式属性值  
### 📌 `shadow_root`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-shadow_root "-shadow_root的直接链接")
此属性返回元素内的 shadow-root 对象，没有的返回`None`。
**类型：**`ShadowRoot`
### 📌 `child_count`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-child_count "-child_count的直接链接")
此属性返回元素内第一级子元素个数。
**类型：**`int`
## ✅️️ 大小和位置[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-大小和位置 "✅️️ 大小和位置的直接链接")
### 📌 `rect.size`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectsize "-rectsize的直接链接")
此属性以元组形式返回元素的大小。
**类型：**`Tuple[float, float]`
```
size = ele.rect.size# 返回：(50, 50)
```

### 📌 `rect.location`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectlocation "-rectlocation的直接链接")
此属性以元组形式返回元素**左上角** 在**整个页面** 中的坐标。
**类型：**`Tuple[float, float]`
```
loc = ele.rect.location# 返回：(50, 50)
```

### 📌 `rect.midpoint`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectmidpoint "-rectmidpoint的直接链接")
此属性以元组形式返回元素**中点** 在**整个页面** 中的坐标。
**类型：**`Tuple[float, float]`
```
loc = ele.rect.midpoint# 返回：(55, 55)
```

### 📌 `rect.click_point`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectclick_point "-rectclick_point的直接链接")
此属性以元组形式返回元素**点击点** 在**整个页面** 中的坐标。
点击点是指`click()`方法点击时的位置，位于元素中上部。
**类型：**`Tuple[float, float]`
### 📌 `rect.corners`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectcorners "-rectcorners的直接链接")
此属性以列表形式返回元素四个角在页面中的坐标，顺序：左上、右上、右下、左下。
**类型：**`((float, float), (float, float), (float, float), (float, float),)`
### 📌 `rect.viewport_corners`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_corners "-rectviewport_corners的直接链接")
此属性以列表形式返回元素四个角在视口中的坐标，顺序：左上、右上、右下、左下。
**类型：**`list[(float, float), (float, float), (float, float), (float, float)]`
### 📌 `rect.viewport_location`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_location "-rectviewport_location的直接链接")
此属性以元组形式返回元素**左上角** 在**当前视口** 中的坐标。
**类型：**`Tuple[float, float]`
### 📌 `rect.viewport_midpoint`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_midpoint "-rectviewport_midpoint的直接链接")
此属性以元组形式返回元素**中点** 在**当前视口** 中的坐标。
**类型：**`Tuple[floatt, float]`
### 📌 `rect.viewport_click_point`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_click_point "-rectviewport_click_point的直接链接")
此属性以元组形式返回元素**点击点** 在**当前视口** 中的坐标。
**类型：**`Tuple[float, float]`
### 📌 `rect.screen_location`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_location "-rectscreen_location的直接链接")
此属性以元组形式返回元素**左上角** 在**屏幕** 中的坐标。
**类型：**`Tuple[float, float]`
### 📌 `rect.screen_midpoint`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_midpoint "-rectscreen_midpoint的直接链接")
此属性以元组形式返回元素**中点** 在**屏幕** 中的坐标。
**类型：**`Tuple[float, float]`
### 📌 `rect.screen_click_point`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_click_point "-rectscreen_click_point的直接链接")
此属性以元组形式返回元素**点击点** 在**屏幕** 中的坐标。
**类型：**`Tuple[float, float]`
### 📌 `rect.scroll_position`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscroll_position "-rectscroll_position的直接链接")
此属性返回元素内滚动条位置，格式：(x, y)。
**类型：**`Tuple[float, float]`
### 📌 `xpath`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-xpath "-xpath的直接链接")
此属性返回当前元素在页面中 xpath 的绝对路径。
**返回类型：**`str`
### 📌 `css_path`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-css_path "-css_path的直接链接")
此属性返回当前元素在页面中 css selector 的绝对路径。
**返回类型：**`str`
## ✅️️ 元素列表中批量获取信息[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-元素列表中批量获取信息 "✅️️ 元素列表中批量获取信息的直接链接")
`eles()`等返回的元素列表，自带`get`属性，可用于获取指定信息。
### 📌 示例[​](https://www.drissionpage.cn/browser_control/get_ele_info#-示例 "📌 示例的直接链接")
```
from DrissionPage import SessionPagepage = SessionPage()page.get('https://www.baidu.com')eles = page('#s-top-left').eles('t:a')print(eles.get.texts())# 获取所有元素的文本
```

**输出：**
```
['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘', '文库', '更多', '翻译', '学术', '百科', '知道', '健康', '营销推广', '直播', '音乐', '橙篇', '查看全部百度产品 >']
```

### 📌 `get.attrs()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-getattrs "-getattrs的直接链接")
此方法用于返回所有元素指定的 attribute 属性组成的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`List[str]`| 属性文本组成的列表  
### 📌 `get.links()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-getlinks "-getlinks的直接链接")
此方法用于返回所有元素的`link`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 链接文本组成的列表  
### 📌 `get.texts()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-gettexts "-gettexts的直接链接")
此方法用于返回所有元素的`text`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 元素文本组成的列表  
## ✅️️ 状态信息[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-状态信息 "✅️️ 状态信息的直接链接")
### 📌`timeout`[​](https://www.drissionpage.cn/browser_control/get_ele_info#timeout "timeout的直接链接")
此属性返回获取内部或相对定位元素的超时时间，实际上是元素所在页面的超时设置。
**类型：**`float`
### 📌`states.is_in_viewport`[​](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_in_viewport "statesis_in_viewport的直接链接")
此属性以布尔值方式返回元素是否在视口中，以元素可以接受点击的点为判断。
**类型：**`bool`
### 📌`states.is_whole_in_viewport`[​](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_whole_in_viewport "statesis_whole_in_viewport的直接链接")
此属性以布尔值方式返回元素是否整个在视口中。
**类型：**`bool`
### 📌`states.is_alive`[​](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_alive "statesis_alive的直接链接")
此属性以布尔值形式返回当前元素是否仍可用。用于判断 d 模式下是否因页面刷新而导致元素失效。
**类型：**`bool`
### 📌 `states.is_checked`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_checked "-statesis_checked的直接链接")
此属性以布尔值返回表单单选或多选元素是否选中。
**类型：**`bool`
### 📌 `states.is_selected`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_selected "-statesis_selected的直接链接")
此属性以布尔值返回`<select>`元素中的项是否选中。
**类型：**`bool`
### 📌 `states.is_enabled`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_enabled "-statesis_enabled的直接链接")
此属性以布尔值返回元素是否可用。
**类型：**`bool`
### 📌 `states.is_displayed`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_displayed "-statesis_displayed的直接链接")
此属性以布尔值返回元素是否可见。
**类型：**`bool`
### 📌 `states.is_covered`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_covered "-statesis_covered的直接链接")
此属性返回元素是否被其它元素覆盖。如被覆盖，返回覆盖元素的 id，否则返回`False`
返回类型| 说明  
---|---  
`False`| 未被覆盖，返回`False`  
`int`| 被覆盖时返回覆盖元素的 id  
### 📌 `states.is_clickable`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_clickable "-statesis_clickable的直接链接")
此属性返回元素是否可被模拟点击，从是否有大小、是否可用、是否显示、是否响应点击判断，不判断是否被遮挡。
**类型：**`bool`
### 📌 `states.has_rect`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-stateshas_rect "-stateshas_rect的直接链接")
此属性返回元素是否拥有大小和位置信息，有则返回四个角在页面上的坐标组成的列表，没有则返回`False`。
返回类型| 说明  
---|---  
`list`| 存在大小和位置信息时，以[(int, int), ...] 格式返回元素四个角的坐标，顺序：左上、右上、右下、左下  
`False`| 不存在时返回`False`  
## ✅️️ 保存元素[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-保存元素 "✅️️ 保存元素的直接链接")
保存功能是本库一个特色功能，可以直接读取浏览器缓存，无需依赖另外的 ui 库或重新下载就可以保存页面资源。
作为对比，selenium 无法自身实现图片另存，往往需要通过使用 ui 工具进行辅助，不仅效率和可靠性低，还占用键鼠资源。
### 📌 `src()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-src "-src的直接链接")
此方法用于返回元素`src`属性所使用的资源。base64 的可转为`bytes`返回，其它的以`str`返回。无资源的返回`None`。
例如，可获取页面上图片字节数据，用于识别内容，或保存到文件。`<script>`和`<link>`标签也可获取文件内容。
注意
获取`<script>`或`<link>`文件内容时，视网站情况不一定会成功。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待资源加载超时时间（秒），为`None`时使用元素所在页面`timeout`属性  
`base64_to_bytes`| `bool`| `True`| 为`True`时，如果是 base64 数据，转换为`bytes`格式  
返回类型| 说明  
---|---  
`str`| 资源字符串  
`None`| 无资源的返回`None`  
**示例：**
```
img = page('tag:img')src = img.src()
```

### 📌 `save()`[​](https://www.drissionpage.cn/browser_control/get_ele_info#-save "-save的直接链接")
此方法用于保存`src()`方法获取到的资源到文件。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`path`| `str``Path`| `None`| 文件保存路径，为`None`时保存到当前文件夹  
`name`| `str`| `None`| 文件名称，需包含后缀，为`None`时从资源 url 获取  
`timeout`| `float`| `None`| 等待资源加载超时时间（秒），为`None`时使用元素所在页面`timeout`属性  
`rename`| `bool`| `True`| 遇到重名文件时是否自动重命名  
返回类型| 说明  
---|---  
`str`| 保存路径  
**示例：**
```
img = page('tag:img')img.save('D:\\img.png')
```

## ✅️️ 比较元素[​](https://www.drissionpage.cn/browser_control/get_ele_info#️️-比较元素 "✅️️ 比较元素的直接链接")
两个元素对象可以用`==`来比较，以判断它们是否指向同一个元素。
**示例：**
```
ele1 = page('t:div')ele2 = page('t:div')print(ele1==ele2)# 输出True
```

[上一页🛰️ 元素交互](https://www.drissionpage.cn/browser_control/ele_operation)[下一页🛰️ iframe 操作](https://www.drissionpage.cn/browser_control/iframe)
  * [✅️️ 内容和属性](https://www.drissionpage.cn/browser_control/get_ele_info#️️-内容和属性)
    * [📌 `tag`](https://www.drissionpage.cn/browser_control/get_ele_info#-tag)
    * [📌 `html`](https://www.drissionpage.cn/browser_control/get_ele_info#-html)
    * [📌 `inner_html`](https://www.drissionpage.cn/browser_control/get_ele_info#-inner_html)
    * [📌 `text`](https://www.drissionpage.cn/browser_control/get_ele_info#-text)
    * [📌 `raw_text`](https://www.drissionpage.cn/browser_control/get_ele_info#-raw_text)
    * [📌 `texts()`](https://www.drissionpage.cn/browser_control/get_ele_info#-texts)
    * [📌 `comments`](https://www.drissionpage.cn/browser_control/get_ele_info#-comments)
    * [📌 `attrs`](https://www.drissionpage.cn/browser_control/get_ele_info#-attrs)
    * [📌 `attr()`](https://www.drissionpage.cn/browser_control/get_ele_info#-attr)
    * [📌 `property()`](https://www.drissionpage.cn/browser_control/get_ele_info#-property)
    * [📌 `value`](https://www.drissionpage.cn/browser_control/get_ele_info#-value)
    * [📌 `link`](https://www.drissionpage.cn/browser_control/get_ele_info#-link)
    * [📌 `pseudo.before`](https://www.drissionpage.cn/browser_control/get_ele_info#-pseudobefore)
    * [📌 `pseudo.after`](https://www.drissionpage.cn/browser_control/get_ele_info#-pseudoafter)
    * [📌 `style()`](https://www.drissionpage.cn/browser_control/get_ele_info#-style)
    * [📌 `shadow_root`](https://www.drissionpage.cn/browser_control/get_ele_info#-shadow_root)
    * [📌 `child_count`](https://www.drissionpage.cn/browser_control/get_ele_info#-child_count)
  * [✅️️ 大小和位置](https://www.drissionpage.cn/browser_control/get_ele_info#️️-大小和位置)
    * [📌 `rect.size`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectsize)
    * [📌 `rect.location`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectlocation)
    * [📌 `rect.midpoint`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectmidpoint)
    * [📌 `rect.click_point`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectclick_point)
    * [📌 `rect.corners`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectcorners)
    * [📌 `rect.viewport_corners`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_corners)
    * [📌 `rect.viewport_location`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_location)
    * [📌 `rect.viewport_midpoint`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_midpoint)
    * [📌 `rect.viewport_click_point`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectviewport_click_point)
    * [📌 `rect.screen_location`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_location)
    * [📌 `rect.screen_midpoint`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_midpoint)
    * [📌 `rect.screen_click_point`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscreen_click_point)
    * [📌 `rect.scroll_position`](https://www.drissionpage.cn/browser_control/get_ele_info#-rectscroll_position)
    * [📌 `xpath`](https://www.drissionpage.cn/browser_control/get_ele_info#-xpath)
    * [📌 `css_path`](https://www.drissionpage.cn/browser_control/get_ele_info#-css_path)
  * [✅️️ 元素列表中批量获取信息](https://www.drissionpage.cn/browser_control/get_ele_info#️️-元素列表中批量获取信息)
    * [📌 示例](https://www.drissionpage.cn/browser_control/get_ele_info#-示例)
    * [📌 `get.attrs()`](https://www.drissionpage.cn/browser_control/get_ele_info#-getattrs)
    * [📌 `get.links()`](https://www.drissionpage.cn/browser_control/get_ele_info#-getlinks)
    * [📌 `get.texts()`](https://www.drissionpage.cn/browser_control/get_ele_info#-gettexts)
  * [✅️️ 状态信息](https://www.drissionpage.cn/browser_control/get_ele_info#️️-状态信息)
    * [📌`timeout`](https://www.drissionpage.cn/browser_control/get_ele_info#timeout)
    * [📌`states.is_in_viewport`](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_in_viewport)
    * [📌`states.is_whole_in_viewport`](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_whole_in_viewport)
    * [📌`states.is_alive`](https://www.drissionpage.cn/browser_control/get_ele_info#statesis_alive)
    * [📌 `states.is_checked`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_checked)
    * [📌 `states.is_selected`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_selected)
    * [📌 `states.is_enabled`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_enabled)
    * [📌 `states.is_displayed`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_displayed)
    * [📌 `states.is_covered`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_covered)
    * [📌 `states.is_clickable`](https://www.drissionpage.cn/browser_control/get_ele_info#-statesis_clickable)
    * [📌 `states.has_rect`](https://www.drissionpage.cn/browser_control/get_ele_info#-stateshas_rect)
  * [✅️️ 保存元素](https://www.drissionpage.cn/browser_control/get_ele_info#️️-保存元素)
    * [📌 `src()`](https://www.drissionpage.cn/browser_control/get_ele_info#-src)
    * [📌 `save()`](https://www.drissionpage.cn/browser_control/get_ele_info#-save)
  * [✅️️ 比较元素](https://www.drissionpage.cn/browser_control/get_ele_info#️️-比较元素)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_ele_info)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_ele_info)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
