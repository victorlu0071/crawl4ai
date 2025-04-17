# Content from: https://www.drissionpage.cn/browser_control/get_elements/find_in_object

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 页面或元素内查找


本页总览
# 🔦 页面或元素内查找
## ✅️️ 页面或元素内查找[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-页面或元素内查找 "✅️️ 页面或元素内查找的直接链接")
页面对象和元素对象都拥有`ele()`和`eles()`方法，用于获取其内部指定子元素。
### 📌 `ele()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-ele "-ele的直接链接")
用于查找其内部第一个符合条件的元素。
`SessionPage`和`ChromiumPage`获取元素的方法是一致的，但前者返回的元素对象为`SessionElement`，后者是`ChromiumElement`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| 必填| 元素的定位信息。可以是查询字符串，或 loc 元组  
`index`| `int`| `1`| 获取第几个匹配的元素，从`1`开始，可输入负数表示从后面开始数  
`timeout`| `float`| `None`| 等待元素出现的超时时间（秒），为`None`使用页面对象设置  
返回类型| 说明  
---|---  
`SessionElement`| s 模式下返回静态元素对象  
`ChromiumElement`| d 模式下返回找到的第一个符合条件的浏览器元素对象  
`ChromiumFrame`| 当结果是框架元素时  
`NoneElement`| 未找到符合条件的元素时返回  
说明
  * loc 元组是指 selenium 定位符，例：(By.ID, '****')。下同。
  * `ele('****', index=2)`和`eles('****')[1]`结果一样，不过前者会快很多。


**示例：**
```
from DrissionPage import SessionPagepage = SessionPage()# 在页面内查找元素ele1 = page.ele('#one')# 在元素内查找后代元素ele2 = ele1.ele('第二行')
```

### 📌 `eles()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-eles "-eles的直接链接")
此方法与`ele()`相似，但返回的是匹配到的所有元素组成的列表。
页面对象和元素对象都可调用这个方法。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| 必填| 元素的定位信息，可以是查询字符串，或 loc 元组  
`timeout`| `float`| `None`| 等待元素出现的超时时间（秒），为`None`使用页面对象设置  
返回类型| 说明  
---|---  
`SessionElementsList`| s 模式下返回静态元素对象组成的列表  
`ChromiumElementsList`| d 模式下返回浏览器元素对象组成的列表  
**示例：**
```
# 获取页面内的所有p元素p_eles = tab.eles('tag:p')# 获取ele1元素内的所有p元素p_eles = ele1.eles('tag:p')# 打印第一个p元素的文本print(p_eles[0])
```

### 📌 `get_frame()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-get_frame "-get_frame的直接链接")
`<iframe>`和`<frame>`也可以用`ele()`查找到，生成的对象是`ChromiumFrame`而不是`ChromiumElement`。
但不建议用`ele()`获取`<iframe>`元素，因为 IDE 无法正确提示后续操作。
建议用`get_frame()`方法获取，页面对象和元素对象都有这个方法。
使用方法与`ele()`一致，可以用定位符查找。还增加了用序号、id、name 属性定位元素的功能。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`loc_ind_ele`| `str``int``ChromiumFrame`| 必填| 定位符`<iframe>`元素序号（从`1`开始，负数表示倒数）`ChromiumFrame对象``id`属性内容`name`属性内容  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面超时时间  
返回类型| 说明  
---|---  
`ChromiumFrame`| `<frame>`或`<iframe>`元素对象  
`NoneElement`| 找不到时返回`NoneElement`  
**示例：**
```
# 在标签页中获取第一个iframe元素iframe = tab.get_frame(1)# 在元素中获取id为`theFrame`的<iframe>元素对象iframe = ele.get_frame('#theFrame')
```

### 📌 `get_frames()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-get_frames "-get_frames的直接链接")
此方法用于获取页面中多个符合条件的`<frame>`或`<iframe>`对象。
元素对象无此方法。
提醒
获取所有`<iframe>`会很慢，而且浪费资源，非必要别用。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `None`| 定位符，为`None`时返回所有  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面超时时间  
返回类型| 说明  
---|---  
`ChromiumElementsList`| `<frame>`或`<iframe>`元素对象组成的列表  
## ✅️️ 静态方式查找[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-静态方式查找 "✅️️ 静态方式查找的直接链接")
静态元素即 s 模式的`SessionElement`元素对象，是纯文本构造的，因此用它处理速度非常快。 对于复杂的页面，要在成百上千个元素中采集数据时，转换为静态元素可把速度提升几个数量级。 作者曾在实践的时候，用同一套逻辑，仅仅把元素转换为静态，就把一个要 30 秒才完成的页面，加速到零点几秒完成。 我们甚至可以把整个页面转换为静态元素，再在其中提取信息。 当然，这种元素不能进行点击等交互。 用`s_ele()`可在把查找到的动态元素转换为静态元素输出，或者获取元素或页面本身的静态元素副本。
注意
如果需要获取多条数据，不要反复使用`s_ele()`，只要在容器元素调用一次获取其静态副本，再在其中执行获取多个元素。
### 📌 `s_ele()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-s_ele "-s_ele的直接链接")
页面对象和元素对象都拥有此方法，用于查找第一个匹配条件的元素，获取其静态版本。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| `None`| 元素的定位信息，可以是查询字符串，或 loc 元组，为`None`时获取调用者本身的静态版本  
`index`| `int`| `1`| 获取第几个匹配的元素，从`1`开始，可输入负数表示从后面开始数  
`timeout`| `float`| `None`| 查找元素超时时间（秒），为`None`与页面等待时间一致  
返回类型| 说明  
---|---  
`SessionElement`| 返回查找到的第一个符合条件的元素对象的静态版本  
`NoneElement`| 限时内未找到符合条件的元素时返回`NoneElement`对象  
注意
页面对象和元素对象的`s_ele()`方法不能搜索到在`<iframe>`里的元素，页面对象的静态版本也不能搜索`<iframe>`里的元素。 要使用`<iframe>`里元素的静态版本，可先获取该元素，再转换。而使用`ChromiumFrame`对象，则可以直接用`s_ele()`查找元素，这在后面章节再讲述。
Tips
从一个`ChromiumElement`元素获取到的`SessionElement`版本，依然能够使用相对定位方法定位祖先或兄弟元素。
```
from DrissionPage import Chromiumtab = Chromium().latest_tab# 在页面中查找元素，获取其静态版本ele1 = tab.s_ele('search text')# 在动态元素中查找元素，获取其静态版本ele = tab.ele('search text')ele2 = ele.s_ele()# 获取页面元素的静态副本（不传入参数）s_page = tab.s_ele()# 获取动态元素的静态副本s_ele = ele.s_ele()# 在静态副本中查询下级元素（因为已经是静态元素，用ele()查找结果也是静态）ele3 = s_page.ele('search text')ele4 = s_ele.ele('search text')
```

### 📌 `s_eles()`[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-s_eles "-s_eles的直接链接")
此方法与`s_ele()`相似，但返回的是匹配到的所有元素组成的列表，或属性值组成的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``Tuple[str, str]`| 必填| 元素的定位信息，可以是查询字符串，或 loc 元组  
`timeout`| `float`| `None`| 查找元素超时时间（秒），为`None`与页面等待时间一致  
返回类型| 说明  
---|---  
`SessionElementsList`| 返回找到的所有元素的`SessionElement`版本组成的列表  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabfor ele in tab.s_eles('search text'):print(ele.text)
```

## ✅️ 获取页面焦点元素[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️-获取页面焦点元素 "✅️ 获取页面焦点元素的直接链接")
使用页面对象的`active_ele`属性获取页面上焦点所在元素。
```
ele = tab.active_ele
```

## ✅️️ 查找`<iframe>`中的元素[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-查找iframe中的元素 "️️-查找iframe中的元素的直接链接")
### 📌 在页面下跨级查找[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-在页面下跨级查找 "📌 在页面下跨级查找的直接链接")
与 selenium 不同，本库可以直接查找同域`<iframe>`里面的元素。 而且无视层级，可以直接获取到多层`<iframe>`里的元素。无需切入切出，大大简化了程序逻辑，使用更便捷。 但同域的`<iframe>`才能这样查找。
假设在页面中有个两级`<iframe>`，其中有个元素`<div id='abc'></div>`，可以这样获取：
```
tab = Chromium().latest_tabele = tab('#abc')
```

获取前后无需切入切出，也不影响获取页面上其它元素。
如果用 selenium，要这样写：
```
driver = webdriver.Chrome()driver.switch_to.frame(0)driver.switch_to.frame(0)ele = driver.find_element(By.ID,'abc')driver.switch_to.default_content()
```

显然比较繁琐，而且切入到`<iframe>`后无法对`<iframe>`外的元素进行操作。
注意
  * 跨级查找只是页面对象支持，元素对象不能直接查找内部 iframe 里的元素。
  * 跨级查找只能用于与主框架同域名的`<iframe>`，不同域名的请用下面的方法。


### 📌 在 iframe 元素内查找[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-在-iframe-元素内查找 "📌 在 iframe 元素内查找的直接链接")
对于跨域的`<iframe>`，我们无法通过页面直接查找里面的元素，可以先获取到`<iframe>`元素，再在其下查找。
当然，非跨域`<iframe>`也可以这样操作。
假设一个`<iframe>`的 id 为 `'iframe1'`，要在其中查找一个 id 为`'abc'`的元素：
```
tab = Chromium().latest_tabiframe = tab('#iframe1')ele = iframe('#abc')
```

这个`<iframe>`元素是一个页面对象，因此可以继续在其下进行跨`<iframe>`查找（相对这个`<iframe>`不跨域的）。
## ✅️️ `ShadowRoot`内查找[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-shadowroot内查找 "️️-shadowroot内查找的直接链接")
本库把 shadow-root 也作为元素对象看待，是为`ShadowRoot`对象。 该对象可与普通元素一样查找下级元素和 DOM 内相对定位。 对`ShadowRoot`对象进行相对定位时，把它看作其父对象内部的第一个对象，其余定位逻辑与普通对象一致。
用元素对象的`shadow_root`属性可获取`ShadowRoot`对象。
注意
如果`ShadowRoot`元素的下级元素中有其它`ShadowRoot`元素，那这些下级`ShadowRoot` 元素内部是无法直接通过定位语句查找到的，只能先定位到其父元素，再用`shadow-root`属性获取。
```
# 获取一个 shadow-root 元素sr_ele = page.ele('#app').shadow_root# 在该元素下查找下级元素ele1 = sr_ele.ele('tag:div')# 用相对定位获取其它元素ele1 = sr_ele.parent(2)ele1 = sr_ele.next('tag:div',1)ele1 = sr_ele.after('tag:div',1)eles = sr_ele.nexts('tag:div')# 定位下级元素中的 shadow+-root 元素sr_ele2 = sr_ele.ele('tag:div').shadow_root
```

由于 shadow-root 不能跨级查找，链式操作非常常见，所以设计了一个简写：`sr`，功能和`shadow_root` 一样，都是获取元素内部的`ShadowRoot`。
**多级 shadow-root 链式操作示例：**
以下这段代码，可以打印浏览器历史第一页，可见是通过多级 shadow-root 来获取的。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('chrome://history/')items = tab('#history-app').sr('#history').sr.eles('t:history-item')for i in items:print(i.sr('#item-container').text.replace('\n',''))
```

## ✅️️ 同时匹配多个定位符[​](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-同时匹配多个定位符 "✅️️ 同时匹配多个定位符的直接链接")
所有页面或元素对象都有`find()`方法，可接收多个定位符，同时查找多个（批）不同定位符的元素。
以`dict`方法返回每个定位符结果。
说明
当`first_ele`为`True`时，如果一个定位符没有被执行过查找，它返回的结果为`None`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locators`| `List[str]``Tuple[str, str]``str`| 必填| 一个定位符或多个组成的列表  
`any_one`| `bool`| `True`| 是否任何一个定位符找到结果即返回  
`first_ele`| `bool`| `True`| 每个定位符获取第一个元素还是所有元素  
`timeout`| `float`| `None`| 超时时间（秒），为`None`使用该对象默认设置  
说明
以下所说的 “定位符”，是`str`或`tuple`类型的。 “元素对象”，是`ChromiumElement`（d 模式）或`SessionElement`（s 模式）类型的，没有找到时是`NoneElement`类型的。 “元素对象组成的列表” 是`ChromiumElementsList`（d 模式）或`SessionElementsList`（s 模式）类型的。 `any_one`参数为`True`时，以`tuple`方式返回找到目标的定位符和结果，为`False`时以`dict`方法返回每个定位符结果。
返回类型| `any_one`参数取值| 说明  
---|---|---  
`tuple(定位符, 元素对象)`| `True`| `first_ele`为`True`时，返回第一个有结果的定位符找到的第一个元素对象  
`tuple(定位符, 元素对象组成的列表)`| `True`| `first_ele`为`False`时，返回第一个有结果的定位符找到的所有元素对象  
`tuple(None, None)`| `True`| 所有定位符都没有找到元素，返回`(None, None)`  
`dict{定位符: 元素对象}`| `False`| `first_ele`为`True`时，每个定位符返回第一个元素，找不到时为`NoneElement`  
`dict{定位符: 元素对象组成的列表}`| `False`| `first_ele`为`False`时，每个定位符返回所有结果元素组成的列表  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')res = tab.find(['#kw','#su'])print(res)
```

[上一页🔦 定位语法](https://www.drissionpage.cn/browser_control/get_elements/syntax)[下一页🔦 相对定位](https://www.drissionpage.cn/browser_control/get_elements/relative)
  * [✅️️ 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-页面或元素内查找)
    * [📌 `ele()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-ele)
    * [📌 `eles()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-eles)
    * [📌 `get_frame()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-get_frame)
    * [📌 `get_frames()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-get_frames)
  * [✅️️ 静态方式查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-静态方式查找)
    * [📌 `s_ele()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-s_ele)
    * [📌 `s_eles()`](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-s_eles)
  * [✅️ 获取页面焦点元素](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️-获取页面焦点元素)
  * [✅️️ 查找`<iframe>`中的元素](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-查找iframe中的元素)
    * [📌 在页面下跨级查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-在页面下跨级查找)
    * [📌 在 iframe 元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#-在-iframe-元素内查找)
  * [✅️️ `ShadowRoot`内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-shadowroot内查找)
  * [✅️️ 同时匹配多个定位符](https://www.drissionpage.cn/browser_control/get_elements/find_in_object#️️-同时匹配多个定位符)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
