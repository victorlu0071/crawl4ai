# Content from: https://www.drissionpage.cn/browser_control/ele_operation

[跳到主要内容](https://www.drissionpage.cn/browser_control/ele_operation#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/ele_operation)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/ele_operation)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/ele_operation)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/ele_operation)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/ele_operation)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/ele_operation)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🛰️ 元素交互


本页总览
# 🛰️ 元素交互
本节介绍与浏览器元素的交互。浏览器元素对象为`ChromiumElement`。
## ✅️️ 点击元素[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-点击元素 "✅️️ 点击元素的直接链接")
### 📌 `click()`和`click.left()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-click和clickleft "-click和clickleft的直接链接")
这两个方法作用是一样的，用于左键点击元素。可选择模拟点击或 js 点击。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`by_js`| `bool`| `False`| 指定点击行为方式。为`None`时，如不被遮挡，用模拟点击，否则用 js 点击为`True`时直接用 js 点击；为`False`时强制模拟点击，被遮挡也会进行点击  
`timeout`| `float`| `1.5`| 模拟点击的超时时间（秒），等待元素可见、可用、进入视口  
`wait_stop`| `bool`| `True`| 点击前是否等待元素停止运动  
返回值| 说明  
---|---  
`False`| `by_js`为`False`，且元素不可用、不可见时，返回`False`  
`True`| 除以上情况，其余情况都返回`True`  
**示例：**
```
# 对ele元素进行模拟点击，如判断被遮挡也会点击ele.click()# 用js方式点击ele元素，无视遮罩层ele.click(by_js=True)# 如元素不被遮挡，用模拟点击，否则用js点击ele.click(by_js=None)
```

默认情况下，`by_js`为`None`，优先用模拟方式点击，如遇遮挡、元素不可用、不可见、无法自动进入视口，等待直到超时后自动改用 js 方式点击。
`by_js`为`False`，程序会强制使用模拟点击，即使被遮挡也会点击元素位置。如果元素不可见、不可用，会返回`False`。如元素无法自动滚动到视口，会改用 js 点击。
`by_js`为`True`时，则可无视任何遮挡，只要元素在 DOM 内，就能点击得到，但元素是否响应点击视网页所用架构而定。
可以根据需要灵活地对元素进行操作。
在模拟点击前，程序会先尝试把元素滚动到视口中。
默认情况下，如无法进行模拟点击（元素无法进入视口、不可用、隐藏）时，左键单击会返回`False`。但也可以通过全局设置使其抛出异常：
```
from DrissionPage.common import SettingsSettings.set_raise_click_failed(True)ele.click()# 如无法点击则抛出异常
```

### 📌 `click.right()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickright "-clickright的直接链接")
此方法实现右键单击元素。
**参数：** 无
**返回：**`None`
**示例：**
```
ele.click.right()
```

### 📌 `click.middle()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickmiddle "-clickmiddle的直接链接")
此方法实现中键单击元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`get_tab`| `bool`| `True`| 是否返回新出现的 Tab 对象  
返回类型| 说明  
---|---  
`ChromiumTab`| 如`get_tab`参数为`True`，元素在`ChromiumTab`返回对象  
`MixTab`| 如`get_tab`参数为`True`，元素在`MixTab`里时返回的对象  
`None`| `get_tab`参数为`False`时  
**示例：**
```
tab = ele.click.middle()print(tab.title)
```

### 📌 `click.multi()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickmulti "-clickmulti的直接链接")
此方法实现左键多次点击元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`times`| `int`| `2`| 点击次数  
**返回：**`None`
### 📌 `click.at()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickat "-clickat的直接链接")
此方法用于带偏移量点击元素，偏移量相对于元素左上角坐标。不传入`offset_x`和`offset_y`时点击元素中间点。 点击的目标不一定在元素上，可以传入负值，或大于元素大小的值，点击元素附近的区域。向右和向下为正值，向左和向上为负值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`offset_x`| `float`| `None`| 相对元素左上角坐标的 x 轴偏移量，向下向右为正  
`offset_y`| `float`| `None`| 相对元素左上角坐标的 y 轴偏移量，向下向右为正  
`button`| `str`| `'left'`| 要点击的键，传入`'left'`、`'right'`、`'middle'`、`'back'`、`'forward'`  
`count`| `int`| `1`| 点击次数  
**返回：**`None`
**示例：**
```
# 点击元素右上方 50*50 的位置ele.click.at(50,-50)# 点击元素上中部，x相对左上角向右偏移50，y保持在元素中点ele.click.at(offset_x=50)# 和click()一致，但没有重试功能ele.click.at()
```

### 📌 `click.to_upload()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickto_upload "-clickto_upload的直接链接")
此方法用于点击元素，触发文件选择框并把指定的文件路径添加到网页，详见“文件上传”章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`file_paths`| `str``Path``list``tuple`| 必填| 文件路径，如果上传框支持多文件，可传入列表或字符串，字符串时多个文件用`\n`分隔  
`by_js`| `bool`| `False`| 是否用 js 方式点击，逻辑与`click()`一致  
**返回：**`None`
### 📌 `click.to_download()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickto_download "-clickto_download的直接链接")
此方法用于点击元素触发下载，并返回下载任务对象。用法详见“文件下载”章节。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`save_path`| `str``Path`| 必填| 保存路径，为`None`保存在原来设置的，如未设置保存到当前路径  
`rename`| `str`| `None`| 重命名文件名，为`None`则不修改  
`suffix`| `str`| `'left'`| 指定文件后缀，为`None`则不修改  
`new_tab`| `bool`| `1`| 该下载是否在新 tab 中触发  
`by_js`| `bool`| `False`| 是否用 js 方式点击，逻辑与`click()`一致  
`timeout`| `float`| `None`| 超时时间（秒），为`None`时使用页面对象默认超时时间  
返回类型| 说明  
---|---  
`DownloadMission`| 下载任务对象  
### 📌 `click.for_new_tab()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clickfor_new_tab "-clickfor_new_tab的直接链接")
在预期点击后会出现新 tab 的时候，可用此方法点击，会等待并返回新 tab 对象。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`by_js`| `bool`| `False`| 是否用 js 方式点击，逻辑与`click()`一致  
返回类型| 说明  
---|---  
`ChromiumTab`| 元素在`ChromiumTab`里时返回  
`MixTab`| 元素在`MixTab`里时返回  
## ✅️️ 输入内容[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-输入内容 "✅️️ 输入内容的直接链接")
### 📌 `clear()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-clear "-clear的直接链接")
此方法用于清空元素文本，可选择模拟按键或 js 方式。
模拟按键方式会自动输入`ctrl-a-del`组合键来清除文本框，js 方式则直接把元素`value`属性设置为`''`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`by_js`| `bool`| `False`| 是否用 js 方式清空  
**返回：**`None`
**示例：**
```
ele.clear()
```

### 📌 `input()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-input "-input的直接链接")
此方法用于向元素输入文本或组合键，也可用于输入文件路径到上传控件。可选择输入前是否清空元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`vals`| `Any`| `False`| 文本值或按键组合对文件上传控件时输入路径字符串或其组成的列表  
`clear`| `bool`| `False`| 输入前是否清空文本框  
`by_js`| `bool`| `False`| 是否用 js 方式输入，为`True`时不能输入组合键  
**返回：**`None`
Tips
  * 有些文本框可以接收回车代替点击按钮，可以直接在文本末尾加上`'\n'`。
  * 会自动把非`str`数据转换为`str`。


**示例：**
```
# 输入文本ele.input('Hello world!')# 输入文本并回车ele.input('Hello world!\n')
```

### 📌 输入组合键[​](https://www.drissionpage.cn/browser_control/ele_operation#-输入组合键 "📌 输入组合键的直接链接")
使用组合键或要传入特殊按键前，先要导入按键类`Keys`。
```
from DrissionPage.common import Keys
```

然后将组合键放在一个`tuple`中传入`input()`即可。
```
ele.input((Keys.CTRL,'a', Keys.DEL))# ctrl+a+del
```

`Keys`内置了 5 个常用组合键，分别为`CTRL_A`、`CTRL_C`、`CTRL_X`、`CTRL_V`、`CTRL_Z`、`CTRL_Y`。
```
ele.input(Keys.CTRL_A)# 全选
```

### 📌 `focus()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-focus "-focus的直接链接")
此方法用于使元素获取焦点。
**参数：** 无
**返回：** `None`
## ✅️️ 拖拽和悬停[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-拖拽和悬停 "✅️️ 拖拽和悬停的直接链接")
Tips
除了以下方法，本库还提供更灵活的动作链功能，详见后面章节。
### 📌 `drag()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-drag "-drag的直接链接")
此方法用于拖拽元素到相对于当前的一个新位置，可以设置速度。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`offset_x`| `int`| `0`| x 轴偏移量，向下向右为正  
`offset_y`| `int`| `0`| y 轴偏移量，向下向右为正  
`duration`| `float`| `0.5`| 用时，单位秒，传入`0`即瞬间到达  
**返回：**`None`
**示例：**
```
# 拖动当前元素到距离50*50的位置，用时1秒ele.drag(50,50,1)
```

### 📌 `drag_to()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-drag_to "-drag_to的直接链接")
此方法用于拖拽元素到另一个元素上或一个坐标上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`ele_or_loc`| `ChromiumElement``Tuple[int, int]`| 必填| 另一个元素对象或坐标元组  
`duration`| `float`| `0.5`| 用时，单位秒，传入`0`即瞬间到达  
**返回：**`None`
**示例：**
```
# 把 ele1 拖拽到 ele2 上ele1 = page.ele('#div1')ele2 = page.ele('#div2')ele1.drag_to(ele2)# 把 ele1 拖拽到网页 50, 50 的位置ele1.drag_to((50,50))
```

### 📌 `hover()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-hover "-hover的直接链接")
此方法用于模拟鼠标悬停在元素上，可接受偏移量，偏移量相对于元素左上角坐标。不传入`offset_x`和`offset_y`值时悬停在元素中点。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`offset_x`| `int`| `None`| 相对元素左上角坐标的 x 轴偏移量，向下向右为正  
`offset_y`| `int`| `None`| 相对元素左上角坐标的 y 轴偏移量，向下向右为正  
**返回：**`None`
**示例：**
```
# 悬停在元素右上方 50*50 的位置ele.hover(50,-50)# 悬停在元素上中部，x 相对左上角向右偏移50，y 保持在元素中点ele.hover(offset_x=50)# 悬停在元素中点ele.hover()
```

## ✅️️ 修改元素[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-修改元素 "✅️️ 修改元素的直接链接")
### 📌 `set.innerHTML()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-setinnerhtml "-setinnerhtml的直接链接")
此方法用于设置元素的 innerHTML 内容。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`html`| `str`| 必填| html文本  
**返回：**`None`
### 📌 `set.property()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-setproperty "-setproperty的直接链接")
此方法用于设置元素`property`属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名  
`value`| `str`| 必填| 属性值  
**返回：**`None`
**示例：**
```
ele.set.property('value','Hello world!')
```

### 📌 `set.style()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-setstyle "-setstyle的直接链接")
此方法用于设置元素样式。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名  
`value`| `str`| 必填| 属性值  
**返回：**`None`
### 📌 `set.attr()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-setattr "-setattr的直接链接")
此方法用于设置元素 attribute 属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名  
`value`| `str`| 必填| 属性值  
**返回：**`None`
**示例：**
```
ele.set.attr('href','http://DrissionPage.cn')
```

### 📌 `remove_attr()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-remove_attr "-remove_attr的直接链接")
此方法用于删除元素 attribute 属性。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名  
**返回：**`None`
**示例：**
```
ele.remove_attr('href')
```

### 📌 `set.value()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-setvalue "-setvalue的直接链接")
此方法用于设置元素`value`值。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `str`| 必填| 属性值  
**返回：**`None`
### 📌 `check()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-check "-check的直接链接")
此方法用于选中或取消选中元素。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`uncheck`| `bool`| `False`| 是否取消选中  
`by_js`| `bool`| `False`| 是否用 js 方式选择  
**返回：**`None`
## ✅️️ 执行 js 脚本[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-执行-js-脚本 "✅️️ 执行 js 脚本的直接链接")
### 📌 `run_js()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-run_js "-run_js的直接链接")
此方法用于对元素执行 js 代码，代码中用`this`表示元素自己。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本或脚本文件路径  
`*args`| -| 无| 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`...  
`as_expr`| `bool`| `False`| 是否作为表达式运行，为`True`时`args`参数无效  
`timetout`| `float`| `None`| js 超时时间（秒），为`None`则使用页面`timeouts.script`设置  
返回类型| 说明  
---|---  
`Any`| 脚本执行结果  
注意
要获取 js 结果记得写上`return`。
**示例：**
```
# 用执行 js 的方式点击元素ele.run_js('this.click();')# 用 js 获取元素高度height = ele.run_js('return this.offsetHeight;')
```

### 📌 `run_async_js()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-run_async_js "-run_async_js的直接链接")
此方法用于以异步方式执行 js 代码，代码中用`this`表示元素自己。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本  
`*args`| -| 无| 传入的参数，按顺序在js文本中对应`arguments[0]`、`arguments[1]`...  
`as_expr`| `bool`| `False`| 是否作为表达式运行，为`True`时`args`参数无效  
**返回：**`None`
### 📌 `add_init_js()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-add_init_js "-add_init_js的直接链接")
此方法用于添加初始化脚本，在页面加载任何脚本前执行。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script`| `str`| 必填| js 脚本文本  
返回类型| 说明  
---|---  
`str`| 添加的脚本的 id  
### 📌 `remove_init_js()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-remove_init_js "-remove_init_js的直接链接")
此方法用于删除初始化脚本，`script_id`传入`None`时删除所有。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`script_id`| `str`| `None`| 脚本的id，传入`None`时删除所有  
**返回：**`None`
## ✅️️ 元素滚动[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-元素滚动 "✅️️ 元素滚动的直接链接")
元素滚动功能藏在`scroll`属性中。用于使可滚动的容器元素内部进行滚动，或使元素本身滚动到可见。
```
# 滚动到底部ele.scroll.to_bottom()# 滚动到最右边ele.scroll.to_rightmost()# 向下滚动 200 像素ele.scroll.down(200)# 滚动到指定位置ele.scroll.to_location(100,300)# 滚动页面使自己可见ele.scroll.to_see()
```

### 📌 `scroll()`或`scroll.down()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scroll或scrolldown "-scroll或scrolldown的直接链接")
这两个方法效果是一样的，用于使元素向下滚动若干像素，水平位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
```
# 向下滚动30像素ele.scroll(30)ele.scroll.down(30)
```

### 📌 `scroll.up()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollup "-scrollup的直接链接")
此方法用于使元素向上滚动若干像素，水平位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
**示例：**
```
page.scroll.up(30)
```

### 📌 `scroll.right()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollright "-scrollright的直接链接")
此方法用于使元素内滚动条向右滚动若干像素，垂直位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.left()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollleft "-scrollleft的直接链接")
此方法用于使元素内滚动条向左滚动若干像素，垂直位置不变。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 滚动的像素  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_top()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_top "-scrollto_top的直接链接")
此方法用于滚动到元素顶部，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
**示例：**
```
page.scroll.to_top()
```

### 📌 `scroll.to_bottom()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_bottom "-scrollto_bottom的直接链接")
此方法用于滚动到元素底部，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_half()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_half "-scrollto_half的直接链接")
此方法用于滚动到元素垂直中间位置，水平位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_rightmost()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_rightmost "-scrollto_rightmost的直接链接")
此方法用于滚动到元素最右边，垂直位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_leftmost()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_leftmost "-scrollto_leftmost的直接链接")
此方法用于滚动到元素最左边，垂直位置不变。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_location()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_location "-scrollto_location的直接链接")
此方法用于滚动到元素滚动到指定位置。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`x`| `int`| 必填| 水平位置  
`y`| `int`| 必填| 垂直位置  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
**示例：**
```
page.scroll.to_location(300,50)
```

### 📌 `scroll.to_see()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_see "-scrollto_see的直接链接")
此方法用于滚动页面直到元素可见。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`center`| `bool``None`| `None`| 是否尽量滚动到页面正中，为`None`时如果被遮挡，则滚动到页面正中  
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
### 📌 `scroll.to_center()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_center "-scrollto_center的直接链接")
此方法用于尽量把元素滚动到视口正中。
**参数：** 无
返回类型| 说明  
---|---  
`ChromiumElement`| 执行滚动的元素自身  
## ✅️️ 列表选择[​](https://www.drissionpage.cn/browser_control/ele_operation#️️-列表选择 "✅️️ 列表选择的直接链接")
`<select>`下拉列表元素功能在`select`属性中。可自动等待列表项出现再实施选择。
此属性用于对`<select>`元素的操作。非`<select>`元素此属性为`None`。
假设有以下`<select>`元素，下面示例以此为基础：
```
<selectid='s'multiple><optionvalue='value1'>text1</option><optionvalue='value2'>text2</option><optionvalue='value3'>text3</option></select>
```

### 📌 点击列表项元素进行选取[​](https://www.drissionpage.cn/browser_control/ele_operation#-点击列表项元素进行选取 "📌 点击列表项元素进行选取的直接链接")
可以获取`<option>`元素，进行选取或取消选择。
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabele = tab('t:select')('t:option')ele.click()
```

### 📌 `select()`和`select.by_text()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-select和selectby_text "-select和selectby_text的直接链接")
这两个方法功能一样，用于按文本选择列表项。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str``list``tuple`| 必填| 作为选择条件的文本，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.by_value()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_value "-selectby_value的直接链接")
此方法用于按`value`属性选择列表项。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `str``list``tuple`| 必填| 作为选择条件的`value`值，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.by_index()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_index "-selectby_index的直接链接")
此方法用于按序号选择列表项，从`1`开始。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`index`| `int``list``tuple`| 必填| 选择第几项，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.by_locator()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_locator "-selectby_locator的直接链接")
此方法可用定位符筛选选项元素。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``list``tuple`| 必填| 定位符，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.by_option()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_option "-selectby_option的直接链接")
此方法用于选中单个或多个列表项元素。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`option`| `ChromiumElement``List[ChromiumElement]`| 必填| `<option>`元素或它们组成的列表  
**返回：**`None`
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabselect = tab('t:select')option = select('t:option')select.select.by_option(option)
```

### 📌 `select.cancel_by_text()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_text "-selectcancel_by_text的直接链接")
此方法用于按文本取消选择列表项。如为多选列表，可取消多项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str``list``tuple`| 必填| 作为选择条件的文本，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.cancel_by_value()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_value "-selectcancel_by_value的直接链接")
此方法用于按`value`属性取消选择列表项。如为多选列表，可取消多项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`value`| `str``list``tuple`| 必填| 作为选择条件的`value`值，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.cancel_by_index()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_index "-selectcancel_by_index的直接�链接")
此方法用于按序号取消选择列表项，从`1`开始。如为多选列表，可取消多项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`index`| `int``list``tuple`| 必填| 选择第几项，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间（秒），为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.cancel_by_locator()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_locator "-selectcancel_by_locator的直接链接")
此方法可用定位符筛选选项元素。如为多选列表，可取消多项。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`locator`| `str``list``tuple`| 必填| 定位符，传入`list`或`tuple`可选择多项  
`timeout`| `float`| `None`| 超时时间，为`None`默认使用页面超时时间  
返回类型| 说明  
---|---  
`bool`| 是否选择成功  
### 📌 `select.cancel_by_option()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_option "-selectcancel_by_option的直接链接")
此方法用于取消选中单个或多个列表项元素。如为多选列表，可多选。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`option`| `ChromiumElement``List[ChromiumElement]`| 必填| `<option>`元素或它们组成的列表  
**返回：**`None`
### 📌 `select.all()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectall "-selectall的直接链接")
此方法用于全选所有项。多选列表才有效。
**参数：** 无
**返回：**`None`
### 📌 `select.clear()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectclear "-selectclear的直接链接")
此方法用于取消所有项选中状态。多选列表才有效。
**参数：** 无
**返回：**`None`
### 📌 `select.invert()`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectinvert "-selectinvert的直接链接")
此方法用于反选。多选列表才有效。
**参数：** 无
**返回：**`None`
### 📌 `select.is_multi`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectis_multi "-selectis_multi的直接链接")
此属性返回当前元素是否多选列表。
**返回类型：**`bool`
### 📌 `select.options`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectoptions "-selectoptions的直接链接")
此属性返回当前列表元素所有选项元素对象。
**返回类型：**`ChromiumElement`
### 📌 `select.selected_option`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectselected_option "-selectselected_option的直接链接")
此属性返回当前元素选中的选项（单选列表）。
**返回类型：**`ChromiumElement`
### 📌 `select.selected_options`[​](https://www.drissionpage.cn/browser_control/ele_operation#-selectselected_options "-selectselected_options的直接链接")
此属性返回当前元素所有选中的选项（多选列表）。
**返回类型：**`List[ChromiumElement]`
[ 上一页🔦 语法速查表](https://www.drissionpage.cn/browser_control/get_elements/sheet)[下一页🛰️ 获取元素信息](https://www.drissionpage.cn/browser_control/get_ele_info)
  * [✅️️ 点击元素](https://www.drissionpage.cn/browser_control/ele_operation#️️-点击元素)
    * [📌 `click()`和`click.left()`](https://www.drissionpage.cn/browser_control/ele_operation#-click和clickleft)
    * [📌 `click.right()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickright)
    * [📌 `click.middle()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickmiddle)
    * [📌 `click.multi()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickmulti)
    * [📌 `click.at()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickat)
    * [📌 `click.to_upload()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickto_upload)
    * [📌 `click.to_download()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickto_download)
    * [📌 `click.for_new_tab()`](https://www.drissionpage.cn/browser_control/ele_operation#-clickfor_new_tab)
  * [✅️️ 输入内容](https://www.drissionpage.cn/browser_control/ele_operation#️️-输入内容)
    * [📌 `clear()`](https://www.drissionpage.cn/browser_control/ele_operation#-clear)
    * [📌 `input()`](https://www.drissionpage.cn/browser_control/ele_operation#-input)
    * [📌 输入组合键](https://www.drissionpage.cn/browser_control/ele_operation#-输入组合键)
    * [📌 `focus()`](https://www.drissionpage.cn/browser_control/ele_operation#-focus)
  * [✅️️ 拖拽和悬停](https://www.drissionpage.cn/browser_control/ele_operation#️️-拖拽和悬停)
    * [📌 `drag()`](https://www.drissionpage.cn/browser_control/ele_operation#-drag)
    * [📌 `drag_to()`](https://www.drissionpage.cn/browser_control/ele_operation#-drag_to)
    * [📌 `hover()`](https://www.drissionpage.cn/browser_control/ele_operation#-hover)
  * [✅️️ 修改元素](https://www.drissionpage.cn/browser_control/ele_operation#️️-修改元素)
    * [📌 `set.innerHTML()`](https://www.drissionpage.cn/browser_control/ele_operation#-setinnerhtml)
    * [📌 `set.property()`](https://www.drissionpage.cn/browser_control/ele_operation#-setproperty)
    * [📌 `set.style()`](https://www.drissionpage.cn/browser_control/ele_operation#-setstyle)
    * [📌 `set.attr()`](https://www.drissionpage.cn/browser_control/ele_operation#-setattr)
    * [📌 `remove_attr()`](https://www.drissionpage.cn/browser_control/ele_operation#-remove_attr)
    * [📌 `set.value()`](https://www.drissionpage.cn/browser_control/ele_operation#-setvalue)
    * [📌 `check()`](https://www.drissionpage.cn/browser_control/ele_operation#-check)
  * [✅️️ 执行 js 脚本](https://www.drissionpage.cn/browser_control/ele_operation#️️-执行-js-脚本)
    * [📌 `run_js()`](https://www.drissionpage.cn/browser_control/ele_operation#-run_js)
    * [📌 `run_async_js()`](https://www.drissionpage.cn/browser_control/ele_operation#-run_async_js)
    * [📌 `add_init_js()`](https://www.drissionpage.cn/browser_control/ele_operation#-add_init_js)
    * [📌 `remove_init_js()`](https://www.drissionpage.cn/browser_control/ele_operation#-remove_init_js)
  * [✅️️ 元素滚动](https://www.drissionpage.cn/browser_control/ele_operation#️️-元素滚动)
    * [📌 `scroll()`或`scroll.down()`](https://www.drissionpage.cn/browser_control/ele_operation#-scroll或scrolldown)
    * [📌 `scroll.up()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollup)
    * [📌 `scroll.right()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollright)
    * [📌 `scroll.left()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollleft)
    * [📌 `scroll.to_top()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_top)
    * [📌 `scroll.to_bottom()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_bottom)
    * [📌 `scroll.to_half()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_half)
    * [📌 `scroll.to_rightmost()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_rightmost)
    * [📌 `scroll.to_leftmost()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_leftmost)
    * [📌 `scroll.to_location()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_location)
    * [📌 `scroll.to_see()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_see)
    * [📌 `scroll.to_center()`](https://www.drissionpage.cn/browser_control/ele_operation#-scrollto_center)
  * [✅️️ 列表选择](https://www.drissionpage.cn/browser_control/ele_operation#️️-列表选择)
    * [📌 点击列表项元素进行选取](https://www.drissionpage.cn/browser_control/ele_operation#-点击列表项元素进行选取)
    * [📌 `select()`和`select.by_text()`](https://www.drissionpage.cn/browser_control/ele_operation#-select和selectby_text)
    * [📌 `select.by_value()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_value)
    * [📌 `select.by_index()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_index)
    * [📌 `select.by_locator()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_locator)
    * [📌 `select.by_option()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectby_option)
    * [📌 `select.cancel_by_text()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_text)
    * [📌 `select.cancel_by_value()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_value)
    * [📌 `select.cancel_by_index()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_index)
    * [📌 `select.cancel_by_locator()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_locator)
    * [📌 `select.cancel_by_option()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectcancel_by_option)
    * [📌 `select.all()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectall)
    * [📌 `select.clear()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectclear)
    * [📌 `select.invert()`](https://www.drissionpage.cn/browser_control/ele_operation#-selectinvert)
    * [📌 `select.is_multi`](https://www.drissionpage.cn/browser_control/ele_operation#-selectis_multi)
    * [📌 `select.options`](https://www.drissionpage.cn/browser_control/ele_operation#-selectoptions)
    * [📌 `select.selected_option`](https://www.drissionpage.cn/browser_control/ele_operation#-selectselected_option)
    * [📌 `select.selected_options`](https://www.drissionpage.cn/browser_control/ele_operation#-selectselected_options)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/ele_operation)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/ele_operation)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
