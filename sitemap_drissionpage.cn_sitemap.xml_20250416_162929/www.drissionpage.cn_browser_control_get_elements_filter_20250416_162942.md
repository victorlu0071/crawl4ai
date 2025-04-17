# Content from: https://www.drissionpage.cn/browser_control/get_elements/filter

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/filter#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/filter)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/filter)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/filter)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/filter)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/filter)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/filter)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 在结果列表中筛选


本页总览
# 🔦 在结果列表中筛选
本节介绍在元素列表中按需要进行筛选，获取指定元素。
`eles()`、`nexts()`等能够获取多个元素的方法，返回的列表可进行进一步筛选，以获取指定的元素。
说明
浏览器页面对象和`SessionPage`产生的元素列表均有此功能，前者筛选功能比后者多。
**示例1，筛选并返回元素列表：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')eles = tab('#s-top-left').eles('t:a')# 获取左上角导航栏内所有<a>元素for ele in eles.filter.displayed():# 筛选出显示的元素列表并逐个打印文本print(ele.text, end=' ')
```

**输出：**
```
新闻 hao123 地图 贴吧 视频 图片 网盘 文库 更多 
```

**示例2，筛选并返回第一个元素：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')eles = tab('#s-top-left').eles('t:a')# 获取左上角导航栏内所有<a>元素print(eles.filter_one.displayed().text)# 筛选出显示的元素并返回第一个
```

**输出：**
```
新闻 
```

## ✅️️ 获取单个匹配元素[​](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取单个匹配元素 "✅️️ 获取单个匹配元素的直接链接")
说明
静态元素列表只有`filter_one.attr()`和`filter_one.text()`方法。
### 📌 `filter_one.displayed()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onedisplayed "-filter_onedisplayed的直接链接")
此方法用于在元素列表中以是否显示为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配显示的元素，`False`匹配不显示的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.checked()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onechecked "-filter_onechecked的直接链接")
此方法用于在元素列表中以是否被选中为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配被选中的元素，`False`匹配不被选中的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.selected()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneselected "-filter_oneselected的直接链接")
此方法用于在元素列表中以是否被选择为条件筛选元素，返回第一个结果。用于`<select>`元素项目。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配被选择的元素，`False`匹配不被选择的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.enabled()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneenabled "-filter_oneenabled的直接链接")
此方法用于在元素列表中以是否可用为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配可用的元素，`False`匹配 disabled 状态的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.clickable()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneclickable "-filter_oneclickable的直接链接")
此方法用于在元素列表中以是否可点击为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配可点击的元素，`False`表示匹配不是可点击的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.have_rect()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onehave_rect "-filter_onehave_rect的直接链接")
此方法用于在元素列表中以是否有大小为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配有大小的元素，`False`表示匹配没有大小的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.style()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onestyle "-filter_onestyle的直接链接")
此方法用于在元素列表中以是否拥有某个 style 值为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.property()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneproperty "-filter_oneproperty的直接链接")
此方法用于在元素列表中以是否拥有某个 property 值为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.attr()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneattr "-filter_oneattr的直接链接")
此方法用于在元素列表中以是否拥有某个 attribute 值为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.text()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onetext "-filter_onetext的直接链接")
此方法用于在元素列表中以是否含有指定文本为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str`| 必填| 用于匹配的文本  
`fuzzy`| `bool`| `True`| 是否模糊匹配  
`contain`| `bool`| `True`| 是否包含该字符串，`False`表示不包含  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 `filter_one.tag()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onetag "-filter_onetag的直接链接")
此方法用于在元素列表中以某个类型为条件筛选元素，返回第一个结果。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 元素类型名称  
`equal`| `bool`| `True`| `True`表示匹配该类型元素，`False`表示匹配非该类型元素  
返回类型| 说明  
---|---  
`ChromiumElement`| 匹配成功返回元素对象  
`NoneElement`| 失败返回`NoneElement`  
抛出`ElementNotFoundError`异常| `Settings.raise_when_ele_not_found`为`True`时抛出  
### 📌 选择获取第几个[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-选择获取第几个 "📌 选择获取第几个的直接链接")
`filter_one`可加参数，以选择返回第几个结果。
**示例：**
```
ele = eles.filter_one(2).text('图')# 获取第二个文本带有“图”字的元素
```

说明
`filter_one`在不加序号参数时，可不要后面的`()`。
## ✅️️ 获取全部匹配元素[​](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取全部匹配元素 "✅️️ 获取全部匹配元素的直接链接")
说明
静态元素列表只有`filter.attr()`和`filter.text()`方法。
### 📌 `filter.displayed()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterdisplayed "-filterdisplayed的直接链接")
此方法用于在元素列表中以是否显示为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配显示的元素，`False`匹配不显示的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.checked()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterchecked "-filterchecked的直接链接")
此方法用于在元素列表中以是否被选中为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配被选中的元素，`False`匹配不被选中的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.selected()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterselected "-filterselected的直接链接")
此方法用于在元素列表中以是否被选择为条件筛选元素，返回新的列表。用于`<select>`元素项目。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配被选择的元素，`False`匹配不被选择的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.enabled()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterenabled "-filterenabled的直接链接")
此方法用于在元素列表中以是否可用为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配可用的元素，`False`匹配 disabled 状态的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.clickable()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterclickable "-filterclickable的直接链接")
此方法用于在元素列表中以是否可点击为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配可点击的元素，`False`表示匹配不是可点击的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.have_rect()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterhave_rect "-filterhave_rect的直接链接")
此方法用于在元素列表中以是否有大小为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`equal`| `bool`| `True`| 是否匹配有大小的元素，`False`表示匹配没有大小的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.style()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterstyle "-filterstyle的直接链接")
此方法用于在元素列表中以是否拥有某个 style 值为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.property()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterproperty "-filterproperty的直接链接")
此方法用于在元素列表中以是否拥有某个 property 值为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.tag()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filtertag "-filtertag的直接链接")
此方法用于在元素列表中以某个类型为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 元素类型名称  
`equal`| `bool`| `True`| `True`表示匹配该类型元素，`False`表示匹配非该类型元素  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.attr()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterattr "-filterattr的直接链接")
此方法用于在元素列表中以是否拥有某个 attribute 值为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
`value`| `str`| 必填| 属性值  
`equal`| `bool`| `True`| `True`表示匹配`name`值为`value`值的元素，`False`表示匹配`name`值不为`value`值的  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
### 📌 `filter.text()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-filtertext "-filtertext的直接链接")
此方法用于在元素列表中以是否含有指定文本为条件筛选元素，返回新的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str`| 必填| 用于匹配的文本  
`fuzzy`| `bool`| `True`| 是否模糊匹配  
`contain`| `bool`| `True`| 是否包含该字符串，`False`表示不包含  
返回类型| 说明  
---|---  
`Filter`| 元素对象组成的列表，可继续用于筛选  
## ✅️️ 多条件筛选[​](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-多条件筛选 "✅️️ 多条件筛选的直接链接")
### 📌 与关系筛选[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-与关系筛选 "📌 与关系筛选的直接链接")
筛选支持链式操作，可串连多个条件，每个条件会筛选一层再进入下一层。
可实现多个条件的与关系筛选。
**示例，出导航栏中显示且含有“图”字的元素：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')eles = tab('#s-top-left').eles('t:a')for ele in eles.filter.displayed().text('图'):print(ele.text, end=' ')
```

### 📌 或关系筛选[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-或关系筛选 "📌 或关系筛选的直接链接")
元素列表的`search()`和`search_one()`方法可用于多个条件或筛选元素。
说明
静态元素列表没有这种方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`index`（`search_one()`独有）| `int`| `1`| 结果中的元素序号，`1`开始  
`displayed`| `bool`| `None`| 是否显示，`bool`表示匹配是或否，`None`为忽略该项  
`checked`| `bool`| `None`| 是否被选中，`bool`表示匹配是或否，`None`为忽略该项  
`selected`| `bool`| `None`| 是否被选择，`bool`表示匹配是或否，`None`为忽略该项  
`enabled`| `bool`| `None`| 是否可用，`bool`表示匹配是或否，`None`为忽略该项  
`clickable`| `bool`| `None`| 是否可点击，`bool`表示匹配是或否，`None`为忽略该项  
`have_rect`| `bool`| `None`| 是否拥有大小，`bool`表示匹配是或否，`None`为忽略该项  
`have_text`| `bool`| `None`| 是否含有文本，`bool`表示匹配是或否，`None`为忽略该项  
`tag`| `str`| `None`| 指定标签页类型，`None`为忽略该项  
返回类型| 说明  
---|---  
`Filter`| `search()`返回元素对象组成的列表  
`ChromiumElement`| `search_one()`匹配成功返回元素对象  
`NoneElement`| `search_one()`匹配失败返回`NoneElement`  
### 📌 混合筛选[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-混合筛选 "📌 混合筛选的直接链接")
与关系和或关系可以用链式操作混合使用。
说明
静态元素列表没有这种方法。
```
es = eles.search(displayed=True).enabled()ele = eles.filter.enablde().search_one(displayed=True)
```

## ✅️️ 获取筛选结果的属性集合[​](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取筛选结果的属性集合 "✅️️ 获取筛选结果的属性集合的直接链接")
筛选结果列表可以调用`get()`方法获取指定属性结合。
该集合为遍历列表中所有元素获取的。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')eles = tab('#s-top-left').eles('t:a')print(eles.get.texts())# 获取所有元素的文本print(eles.filter.displayed().get.texts())# 获取的元素的文本
```

**输出：**
```
['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘', '文库', '更多', '翻译', '学术', '百科', '知道', '健康', '营销推广', '直播', '音乐', '橙篇', '查看全部百度产品 >']['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘', '文库', '更多']
```

### 📌 `get.attrs()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-getattrs "-getattrs的直接链接")
此方法用于返回所有元素指定的 attribute 属性组成的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`List[str]`| 属性文本组成的列表  
### 📌 `get.links()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-getlinks "-getlinks的直接链接")
此方法用于返回所有元素的`link`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 链接文本组成的列表  
### 📌 `get.texts()`[​](https://www.drissionpage.cn/browser_control/get_elements/filter#-gettexts "-gettexts的直接链接")
此方法用于返回所有元素的`text`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 元素文本组成的列表  
[上一页🔦 行为模式](https://www.drissionpage.cn/browser_control/get_elements/behavior)[下一页🔦 简化写法](https://www.drissionpage.cn/browser_control/get_elements/simplify)
  * [✅️️ 获取单个匹配元素](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取单个匹配元素)
    * [📌 `filter_one.displayed()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onedisplayed)
    * [📌 `filter_one.checked()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onechecked)
    * [📌 `filter_one.selected()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneselected)
    * [📌 `filter_one.enabled()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneenabled)
    * [📌 `filter_one.clickable()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneclickable)
    * [📌 `filter_one.have_rect()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onehave_rect)
    * [📌 `filter_one.style()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onestyle)
    * [📌 `filter_one.property()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneproperty)
    * [📌 `filter_one.attr()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_oneattr)
    * [📌 `filter_one.text()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onetext)
    * [📌 `filter_one.tag()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filter_onetag)
    * [📌 选择获取第几个](https://www.drissionpage.cn/browser_control/get_elements/filter#-选择获取第几个)
  * [✅️️ 获取全部匹配元素](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取全部匹配元素)
    * [📌 `filter.displayed()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterdisplayed)
    * [📌 `filter.checked()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterchecked)
    * [📌 `filter.selected()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterselected)
    * [📌 `filter.enabled()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterenabled)
    * [📌 `filter.clickable()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterclickable)
    * [📌 `filter.have_rect()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterhave_rect)
    * [📌 `filter.style()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterstyle)
    * [📌 `filter.property()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterproperty)
    * [📌 `filter.tag()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filtertag)
    * [📌 `filter.attr()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filterattr)
    * [📌 `filter.text()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-filtertext)
  * [✅️️ 多条件筛选](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-多条件筛选)
    * [📌 与关系筛选](https://www.drissionpage.cn/browser_control/get_elements/filter#-与关系筛选)
    * [📌 或关系筛选](https://www.drissionpage.cn/browser_control/get_elements/filter#-或关系筛选)
    * [📌 混合筛选](https://www.drissionpage.cn/browser_control/get_elements/filter#-混合筛选)
  * [✅️️ 获取筛选结果的属性集合](https://www.drissionpage.cn/browser_control/get_elements/filter#️️-获取筛选结果的属性集合)
    * [📌 `get.attrs()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-getattrs)
    * [📌 `get.links()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-getlinks)
    * [📌 `get.texts()`](https://www.drissionpage.cn/browser_control/get_elements/filter#-gettexts)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/filter)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/filter)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
