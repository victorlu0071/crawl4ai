# Content from: https://www.drissionpage.cn/browser_control/get_elements/relative

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/relative#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/relative)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/relative)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/relative)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/relative)
      * [🔦 概述](https://www.drissionpage.cn/browser_control/get_elements/intro)
      * [🔦 定位语法](https://www.drissionpage.cn/browser_control/get_elements/syntax)
      * [🔦 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
      * [🔦 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative)
      * [🔦 行为模式](https://www.drissionpage.cn/browser_control/get_elements/behavior)
      * [🔦 在结果列表中筛选](https://www.drissionpage.cn/browser_control/get_elements/filter)
      * [🔦 简化写法](https://www.drissionpage.cn/browser_control/get_elements/simplify)
      * [🔦 语法速查表](https://www.drissionpage.cn/browser_control/get_elements/sheet)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/relative)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/relative)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 相对定位


本页总览
# 🔦 相对定位
相对定位的意思是以一个已获取的元素为基准，按需要使用不同方法获取指定的其它元素。
相对定位有基于 DOM 的方式和基于视觉的方式两种
## ✅️️ 基于 DOM 相对定位[​](https://www.drissionpage.cn/browser_control/get_elements/relative#️️-基于-dom-相对定位 "✅️️ 基于 DOM 相对定位的直接链接")
以下方法可以以某元素为基准，在 DOM 中按照条件获取其直接子节点、同级节点、祖先元素、文档前后节点。
这里说的是 “节点”，不是 “元素”。因为相对定位可以获取除元素外的其它节点，包括文本、注释节点。
注意
如果元素在`<iframe>`中，相对定位不能超越`<iframe>`文档。
### 📌 获取父级元素[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取父级元素 "📌 获取父级元素的直接链接")
🔸 `parent()`
此方法获取当前元素某一级父元素，可指定筛选条件或层数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`level_or_loc`| `int``str``Tuple[str, str]`| `1`| 第几级父元素，从`1`开始，或用定位符在祖先元素中进行筛选  
`index`| `int`| `1`| 当`level_or_loc`传入定位符，使用此参数选择第几个结果，从当前元素往上级数；当`level_or_loc`传入数字时，此参数无效  
`timeout`| `float`| `0`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
返回类型| 说明  
---|---  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
**示例：**
```
# 获取 ele1 的第二层父元素ele2 = ele1.parent(2)# 获取 ele1 父元素中 id 为 id1 的元素ele2 = ele1.parent('#id1')
```

### 📌 获取直接子节点[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取直接子节点 "📌 获�取直接子节点的直接链接")
🔸 `child()`
此方法返回当前元素的一个直接子节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
🔸 `children()`
此方法返回当前元素全部符合条件的直接子节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`ChromiumElementsList`| d 模式结果列表  
`SessionElementsList`| s 模式结果列表  
### 📌 获取后面的同级节点[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取后面的同级节点 "📌 获取后面的同级节点的直接链接")
🔸 `next()`
此方法返回当前元素后面的某一个同级节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
**示例：**
```
# 获取 ele1 后面第一个兄弟元素ele2 = ele1.next()# 获取 ele1 后面第 3 个兄弟元素ele2 = ele1.next(3)# 获取 ele1 后面第 3 个 div 兄弟元素ele2 = ele1.next('tag:div',3)# 获取 ele1 后面第一个文本节点的文本txt = ele1.next('xpath:text()',1)
```

🔸 `nexts()`
此方法返回当前元素后面全部符合条件的同级节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`ChromiumElementsList`| d 模式结果列表  
`SessionElementsList`| s 模式结果列表  
**示例：**
```
# 获取 ele1 后面所有兄弟元素eles = ele1.nexts()# 获取 ele1 后面所有 div 兄弟元素divs = ele1.nexts('tag:div')# 获取 ele1 后面的所有文本节点txts = ele1.nexts('xpath:text()')
```

### 📌 获取前面的同级节点[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取前面的同级节点 "📌 获取前面的同级节点的直接链接")
🔸 `prev()`
此方法返回当前元素前面的某一个同级节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
**示例：**
```
# 获取 ele1 前面第一个兄弟元素ele2 = ele1.prev()# 获取 ele1 前面第 3 个兄弟元素ele2 = ele1.prev(3)# 获取 ele1 前面第 3 个 div 兄弟元素ele2 = ele1.prev(3,'tag:div')# 获取 ele1 前面第一个文本节点的文本txt = ele1.prev(1,'xpath:text()')
```

🔸 `prevs()`
此方法返回当前元素前面全部符合条件的同级节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`ChromiumElementsList`| d 模式结果列表  
`SessionElementsList`| s 模式结果列表  
**示例：**
```
# 获取 ele1 前面所有兄弟元素eles = ele1.prevs()# 获取 ele1 前面所有 div 兄弟元素divs = ele1.prevs('tag:div')
```

### 📌 在后面文档中查找节点[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-在后面文档中查找节点 "📌 在后面文档中查找节点的直接链接")
🔸 `after()`
此方法返回当前元素后面的某一个节点，可指定筛选条件和第几个。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
**示例：**
```
# 获取 ele1 后面第 3 个元素ele2 = ele1.after(index=3)# 获取 ele1 后面第 3 个 div 元素ele2 = ele1.after('tag:div',3)# 获取 ele1 后面第一个文本节点的文本txt = ele1.after('xpath:text()',1)
```

🔸 `afters()`
此方法返回当前元素后面符合条件的全部节点组成的列表，可用查询语法筛选。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`ChromiumElementsList`| d 模式结果列表  
`SessionElementsList`| s 模式结果列表  
**示例：**
```
# 获取 ele1 后所有元素eles = ele1.afters()# 获取 ele1 前面所有 div 元素divs = ele1.afters('tag:div')
```

### 📌 在前面文档中查找节点[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-在前面文档中查找节点 "📌 在前面文档中查找节点的直接链接")
🔸 `before()`
此方法返回当前元素前面的某一个符合条件的节点，可指定筛选条件和第几个。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`ChromiumElement`| d 模式下的元素对象  
`SessionElement`| s 模式下的元素对象  
`NoneElement`| 未获取到结果时  
**示例：**
```
# 获取 ele1 前面第 3 个元素ele2 = ele1.before(3)# 获取 ele1 前面第 3 个 div 元素ele2 = ele1.before('tag:div',3)# 获取 ele1 前面第一个文本节点的文本txt = ele1.before('xpath:text()',1)
```

🔸 `befores()`
此方法返回当前元素前面全部符合条件的节点组成的列表，可用查询语法筛选。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 查找超时时间（秒），为`None`时使用页面超时设置，s 模式下无效  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`ChromiumElementsList`| d 模式结果列表  
`SessionElementsList`| s 模式结果列表  
**示例：**
```
# 获取 ele1 前面所有元素eles = ele1.befores()# 获取 ele1 前面所有 div 元素divs = ele1.befores('tag:div')
```

## ✅️️ 基于视觉相对定位[​](https://www.drissionpage.cn/browser_control/get_elements/relative#️️-基于视觉相对定位 "✅️️ 基于视觉相对定位的直接链接")
以下方法可以以某元素为基准，向不同方向或指定偏移量获取元素。
只有浏览器模式支持这类定位方式。
只能获取可见的元素（不论是否在视口内），不能获取被遮挡的。
### 📌 `east()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-east "-east的直接链接")
此方法用于获取一个在当前元素右边的元素。
`loc_or_pixel`参数可用定位符指定筛选条件，定位符只支持`str`格式，且不支持 xpath 和 css 方式。
用`index`参数可指定获取第几个结果。如果`loc_or_pixel`为`None`，获取第若干个元素。
`loc_or_pixel`为`int`格式时，直接获取元素右边这个距离的元素，此时`index`参数无效。距离从右边框开始计算。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_pixel`| `str``int`| `None`| 定位符或距离（像素）  
`index`| `int`| `1`| 第几个，从1开始，`loc_or_pixel`为`int`格式时无效  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
### 📌 `west()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-west "-west的直接链接")
此方法用于获取一个在当前元素左边的元素。
`loc_or_pixel`参数可用定位符指定筛选条件，定位符只支持`str`格式，且不支持 xpath 和 css 方式。
用`index`参数可指定获取第几个结果。如果`loc_or_pixel`为`None`，获取第若干个元素。
`loc_or_pixel`为`int`格式时，直接获取元素左边这个距离的元素，此时`index`参数无效。距离从左边框开始计算。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_pixel`| `str``int`| `None`| 定位符或距离（像素）  
`index`| `int`| `1`| 第几个，从1开始，`loc_or_pixel`为`int`格式时无效  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
### 📌 `south()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-south "-south的直接链接")
此方法用于获取一个在当前元素下边的元素。
`loc_or_pixel`参数可用定位符指定筛选条件，定位符只支持`str`格式，且不支持 xpath 和 css 方式。
用`index`参数可指定获取第几个结果。如果`loc_or_pixel`为`None`，获取第若干个元素。
`loc_or_pixel`为`int`格式时，直接获取元素下边这个距离的元素，此时`index`参数无效。距离从下边框开始计算。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_pixel`| `str``int`| `None`| 定位符或距离（像素）  
`index`| `int`| `1`| 第几个，从1开始，`loc_or_pixel`为`int`格式时无效  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
### 📌 `north()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-north "-north的直接链接")
此方法用于获取一个在当前元素上边的元素。
`loc_or_pixel`参数可用定位符指定筛选条件，定位符只支持`str`格式，且不支持 xpath 和 css 方式。
用`index`参数可指定获取第几个结果。如果`loc_or_pixel`为`None`，获取第若干个元素。
`loc_or_pixel`为`int`格式时，直接获取元素上边这个距离的元素，此时`index`参数无效。距离从上边框开始计算。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_or_pixel`| `str``int`| `None`| 定位符或距离（像素）  
`index`| `int`| `1`| 第几个，从1开始，`loc_or_pixel`为`int`格式时无效  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
### 📌 `offset()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-offset "-offset的直接链接")
此方法用于获取相对于元素左上角指定偏移量的一个元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`offset_x`| `int`| 必填| 横坐标偏移量（像素），向右为正  
`offset_y`| `int`| 必填| 纵坐标偏移量（像素），向下为正  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
### 📌 `over()`[​](https://www.drissionpage.cn/browser_control/get_elements/relative#-over "-over的直接链接")
此方法用于获取覆盖在本元素上最上层的元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`timeout`| `float`| `None`| 等待元素出现的超时时间（秒），为`None`使用页面`timeout`设置值  
返回类型| 说明  
---|---  
`ChromiumElement`| 找到的元素对象  
`NoneElement`| 未获取到结果时  
[上一页🔦 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)[下一页🔦 行为模式](https://www.drissionpage.cn/browser_control/get_elements/behavior)
  * [✅️️ 基于 DOM 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative#️️-基于-dom-相对定位)
    * [📌 获取父级元素](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取父级元素)
    * [📌 获取直接子节点](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取直接子节点)
    * [📌 获取后面的同级节点](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取后面的同级节点)
    * [📌 获取前面的同级节点](https://www.drissionpage.cn/browser_control/get_elements/relative#-获取前面的同级节点)
    * [📌 在后面文档中查找节点](https://www.drissionpage.cn/browser_control/get_elements/relative#-在后面文档中查找节点)
    * [📌 在前面文档中查找节点](https://www.drissionpage.cn/browser_control/get_elements/relative#-在前面文档中查找节点)
  * [✅️️ 基于视觉相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative#️️-基于视觉相对定位)
    * [📌 `east()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-east)
    * [📌 `west()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-west)
    * [📌 `south()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-south)
    * [📌 `north()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-north)
    * [📌 `offset()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-offset)
    * [📌 `over()`](https://www.drissionpage.cn/browser_control/get_elements/relative#-over)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/relative)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/relative)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
