# Content from: https://www.drissionpage.cn/SessionPage/get_ele

[跳到主要内容](https://www.drissionpage.cn/SessionPage/get_ele#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/get_ele)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/get_ele)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/intro)
  * [🛫 SessionPage](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 概述](https://www.drissionpage.cn/SessionPage/intro)
    * [🛩️ 创建页面对象](https://www.drissionpage.cn/SessionPage/create_obj)
    * [🛩️ 访问网页](https://www.drissionpage.cn/SessionPage/visit)
    * [🛩️ 获取页面信息](https://www.drissionpage.cn/SessionPage/get_page_info)
    * [🛩️ 查找元素](https://www.drissionpage.cn/SessionPage/get_ele)
    * [🛩️ 获取元素信息](https://www.drissionpage.cn/SessionPage/get_ele_info)
    * [🛩️ 页面设置](https://www.drissionpage.cn/SessionPage/settings)
    * [🛩️ 启动配置](https://www.drissionpage.cn/SessionPage/session_opt)
  * [🧰 进阶使用](https://www.drissionpage.cn/download/intro)


  * [](https://www.drissionpage.cn/)
  * 🛫 SessionPage
  * 🛩️ 查找元素


本页总览
# 🛩️ 查找元素
## ✅️️ 页面或元素内查找[​](https://www.drissionpage.cn/SessionPage/get_ele#️️-页面或元素内查找 "✅️️ 页面或元素内查找的直接链接")
页面对象和元素对象都拥有`ele()`和`eles()`方法，用于获取其内部指定子元素。
### 📌 `ele()`[​](https://www.drissionpage.cn/SessionPage/get_ele#-ele "-ele的直接链接")
用于查找其内部第一个条件匹配的元素。
页面对象和元素对象的`ele()`方法参数名称稍有不同，但用法一样。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| 必填| 元素的定位信息。可以是查询字符串，或 loc 元组  
`index`| `int`| `1`| 获取第几个匹配的元素，从`1`开始，可输入负数表示从后面开始数  
`timeout`| `float`| `None`| 此参数在这里没有作用  
返回类型| 说明  
---|---  
`SessionElement`| 找到的第一个元素对象  
`NoneElement`| 未找到符合条件的元素时返回  
### 📌 `eles()`[​](https://www.drissionpage.cn/SessionPage/get_ele#-eles "-eles的直接链接")
此方法与`ele()`相似，但返回的是匹配到的所有元素组成的列表。
页面对象和元素对象都可调用这个方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| 必填| 元素的定位信息，可以是查询字符串，或 loc 元组  
`timeout`| `float`| `None`| 此参数在这里没有作用  
返回类型| 说明  
---|---  
`SessionElementsList`| 元素对象组成的列表  
## ✅️️ 相对定位[​](https://www.drissionpage.cn/SessionPage/get_ele#️️-相对定位 "✅️️ 相对定位的直接链接")
以下方法可以以某元素为基准，在 DOM 中按照条件获取其直接子节点、同级节点、祖先元素、文档前后节点。
这里说的是 “节点”，不是 “元素”。因为相对定位可以获取除元素外的其它节点，包括文本、注释节点。
### 📌 获取父级元素[​](https://www.drissionpage.cn/SessionPage/get_ele#-获取父级元素 "📌 获取父级元素的直接链接")
🔸 `parent()`
此方法获取当前元素某一级父元素，可指定筛选条件或层数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`level_or_loc`| `int``str``Tuple[str, str]`| `1`| 第几级父元素，从`1`开始，或用定位符在祖先元素中进行筛选  
`index`| `int`| `1`| 当`level_or_loc`传入定位符，使用此参数选择第几个结果，从当前元素往上级数；当`level_or_loc`传入数字时，此参数无效  
`timeout`| `float`| `0`| 查找超时时间（秒）  
返回类型| 说明  
---|---  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
### 📌 获取直接子节点[​](https://www.drissionpage.cn/SessionPage/get_ele#-获取直接子节点 "📌 获取直接子节点的直接链接")
🔸 `child()`
此方法返回当前元素的一个直接子节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
🔸 `children()`
此方法返回当前元素全部符合条件的直接子节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`SessionElementsList`| 结果元素对象组成的列表  
### 📌 获取后面的同级节点[​](https://www.drissionpage.cn/SessionPage/get_ele#-获取后面的同级节点 "📌 获取后面的同级节点的直接链接")
🔸 `next()`
此方法返回当前元素后面的某一个同级节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
🔸 `nexts()`
此方法返回当前元素后面全部符合条件的同级节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`SessionElementsList`| 结果元素对象组成的列表  
### 📌 获取前面的同级节点[​](https://www.drissionpage.cn/SessionPage/get_ele#-获取前面的同级节点 "📌 获取前面的同级节点的直接链接")
🔸 `prev()`
此方法返回当前元素前面的某一个同级节点，可指定筛选条件和第几个。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
🔸 `prevs()`
此方法返回当前元素前面全部符合条件的同级节点组成的列表，可用查询语法筛选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`SessionElementsList`| 结果元素对象组成的列表  
### 📌 在后面文档中查找节点[​](https://www.drissionpage.cn/SessionPage/get_ele#-在后面文档中查找节点 "📌 在后面文档中查找节点的直接链接")
🔸 `after()`
此方法返回当前元素后面的某一个节点，可指定筛选条件和第几个。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
🔸 `afters()`
此方法返回当前元素后面符合条件的全部节点组成的列表，可用查询语法筛选。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`SessionElementsList`| 结果元素对象组成的列表  
### 📌 在前面文档中查找节点[​](https://www.drissionpage.cn/SessionPage/get_ele#-在前面文档中查找节点 "📌 在前面文档中查找节点的直接链接")
🔸 `before()`
此方法返回当前元素前面的某一个符合条件的节点，可指定筛选条件和第几个。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]``int`| `''`| 用于筛选节点的查询语法，为`int`类型时`index`参数无效  
`index`| `int`| `1`| 查询结果中的第几个，从`1`开始，可输入负数表示倒数  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`str`| 获取非元素节点时返回字符串  
`SessionElement`| 元素对象  
`NoneElement`| 未获取到结果时  
🔸 `befores()`
此方法返回当前元素前面全部符合条件的节点组成的列表，可用查询语法筛选。查找范围不限同级节点，而是整个 DOM 文档。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `''`| 用于筛选节点的查询语法  
`timeout`| `float`| `None`| 无实际作用  
`ele_only`| `bool`| `True`| 是否只查找元素，为`False`时把文本、注释节点也纳入查找范围  
返回类型| 说明  
---|---  
`SessionElementsList`| 结果元素对象组成的列表  
## ✅️️ 同时匹配多个定位符[​](https://www.drissionpage.cn/SessionPage/get_ele#️️-同时匹配多个定位符 "✅️️ 同时匹配多个定位符的直接链接")
所有页面或元素对象都有`find()`方法，可接收多个定位符，同时查找多个（批）不同定位符的元素。
以`dict`方法返回每个定位符结果。
说明
当`first_ele`为`True`时，如果一个定位符没有被执行过查找，它返回的结果为`None`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locators`| `List[str]``Tuple[str]``str``tuple`| 必填| 定位符组成的列表  
`any_one`| `bool`| `True`| 是否任何一个定位符找到结果即返回  
`first_ele`| `bool`| `True`| 每个定位符获取第一个元素还是所有元素  
`timeout`| `float`| `None`| 超时时间（秒），为`None`使用该对象默认设置  
说明
以下所说的 “定位符”，是`str`或`tuple`类型的。 “元素对象”，是`SessionElement`类型的，没有找到时是`NoneElement`类型的。 “元素对象组成的列表” 是`SessionElementsList`类型的。 `any_one`参数为`True`时，以`tuple`方式返回找到目标的定位符和结果，为`False`时以`dict`方法返回每个定位符结果。
返回类型| `any_one`参数取值| 说明  
---|---|---  
`tuple(定位符, 元素对象)`| `True`| `first_ele`为`True`时，返回第一个有结果的定位符找到的第一个元素对象  
`tuple(定位符, 元素对象组成的列表)`| `True`| `first_ele`为`False`时，返回第一个有结果的定位符找到的所有元素对象  
`tuple(None, None)`| `True`| 所有定位符都没有找到元素，返回`(None, None)`  
`dict{定位符: 元素对象}`| `False`| `first_ele`为`True`时，每个定位符返回第一个元素，找不到时为`NoneElement`  
`dict{定位符: 元素对象组成的列表}`| `False`| `first_ele`为`False`时，每个定位符返回所有结果元素组成的列表  
[上一页🛩️ 获取页面信息](https://www.drissionpage.cn/SessionPage/get_page_info)[下一页🛩️ 获取元素信息](https://www.drissionpage.cn/SessionPage/get_ele_info)
  * [✅️️ 页面或元素内查找](https://www.drissionpage.cn/SessionPage/get_ele#️️-页面或元素内查找)
    * [📌 `ele()`](https://www.drissionpage.cn/SessionPage/get_ele#-ele)
    * [📌 `eles()`](https://www.drissionpage.cn/SessionPage/get_ele#-eles)
  * [✅️️ 相对定位](https://www.drissionpage.cn/SessionPage/get_ele#️️-相对定位)
    * [📌 获取父级元素](https://www.drissionpage.cn/SessionPage/get_ele#-获取父级元素)
    * [📌 获取直接子节点](https://www.drissionpage.cn/SessionPage/get_ele#-获取直接子节点)
    * [📌 获取后面的同级节点](https://www.drissionpage.cn/SessionPage/get_ele#-获取后面的同级节点)
    * [📌 获取前面的同级节点](https://www.drissionpage.cn/SessionPage/get_ele#-获取前面的同级节点)
    * [📌 在后面文档中查找节点](https://www.drissionpage.cn/SessionPage/get_ele#-在后面文档中查找节点)
    * [📌 在前面文档中查找节点](https://www.drissionpage.cn/SessionPage/get_ele#-在前面文档中查找节点)
  * [✅️️ 同时匹配多个定位符](https://www.drissionpage.cn/SessionPage/get_ele#️️-同时匹配多个定位符)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/get_ele)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/get_ele)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
