# Content from: https://www.drissionpage.cn/browser_control/actions

[跳到主要内容](https://www.drissionpage.cn/browser_control/actions#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/actions)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/actions)
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
  * 🛰️ 动作链


本页总览
# 🛰️ 动作链
动作链可以在浏览器上完成一系列交互行为，如鼠标移动、鼠标点击、键盘输入等。
浏览器页面对象都支持使用动作链。
可以链式操作，也可以分开执行，每个动作执行即生效，无需`perform()`。
这些操作皆为模拟，真正的鼠标不会移动，因此可以多个标签页同时操作。
## ✅️ 使用方法[​](https://www.drissionpage.cn/browser_control/actions#️-使用方法 "✅️ 使用方法的直接链接")
可以用上述对象内置的`actions`属性调用动作链，也可以主动创建一个动作链对象，将页面对象传入使用。
这两种方式唯一区别是，前者会等待页面加载完毕再执行，后者不会。
### 📌 使用内置`actions`属性[​](https://www.drissionpage.cn/browser_control/actions#-使用内置actions属性 "-使用内置actions属性的直接链接")
说明
这种方式会等到页面框架文档（不包括 js 数据）加载完成再执行动作。
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')tab.actions.move_to('#kw').click().type('DrissionPage')tab.actions.move_to('#su').click()
```

### 📌 使用新对象[​](https://www.drissionpage.cn/browser_control/actions#-使用新对象 "📌 使用新对象的直接链接")
使用`from DrissionPage.common import Actions`导入动作链。
只要把`WebPage`对象或`ChromiumPage`对象传入即可。动作链只在这个页面上生效。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`page`| `ChromiumPage``WebPage``ChromiumTab`| 必填| 动作链要操作的浏览器页面  
说明
这种方式**不会** 等到页面框架文档（不包括 js 数据）加载完成再执行动作。
**示例：**
```
from DrissionPage import Chromiumfrom DrissionPage.common import Actionstab = Chromium().latest_tabac = Actions(tab)tab.get('https://www.baidu.com')ac.move_to('#kw').click().type('DrissionPage')ac.move_to('#su').click()
```

### 📌 操作方式[​](https://www.drissionpage.cn/browser_control/actions#-操作方式 "📌 操作方式的直接链接")
多个动作可以用链式模式操作：
```
tab.actions.move_to(ele).click().type('some text')
```

也可以多个操作分开执行：
```
tab.actions.move_to(ele)tab.actions.click()tab.actions.type('some text')
```

这两种方式效果是一样的，每个动作总会依次执行。
## ✅️ 移动鼠标[​](https://www.drissionpage.cn/browser_control/actions#️-移动鼠标 "✅️ 移动鼠标的直接链接")
### 📌 `move_to()`[​](https://www.drissionpage.cn/browser_control/actions#-move_to "-move_to的直接链接")
此方法用于移动鼠标到元素中点，或页面上的某个绝对坐标。
当`offset_x`和`offset_y`都为`None`时，移动到元素中间点。
当传入偏移量时，偏移量相对于元素左上角坐标。
初始化参数| 类型| 默认值| 说明  
---|---|---|---  
`ele_or_loc`| `ChrmoiumElement``str``Tuple[int, int]`| 必填| 元素对象、文本定位符或绝对坐标，坐标为`tuple`(int, int) 形式  
`offset_x`| `int`| `None`| x 轴偏移量，向右为正，向左为负  
`offset_y`| `int`| `None`| y 轴偏移量，向下为正，向上为负  
`duration`| `float`| `0.5`| 拖动用时，传入`0`即瞬间到达  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 使鼠标移动到 ele 元素上
```
ele = tab('tag:a')tab.actions.move_to(ele_or_loc=ele)
```

### 📌 `move()`[​](https://www.drissionpage.cn/browser_control/actions#-move "-move的直接链接")
此方法用于使鼠标相对当前位置移动若干距离。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`offset_x`| `int`| `0`| x 轴偏移量，向右为正，向左为负  
`offset_y`| `int`| `0`| y 轴偏移量，向下为正，向上为负  
`duration`| `float`| `0.5`| 拖动用时，传入`0`即瞬间到达  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 鼠标向右移动 300 像素
```
tab.actions.move(300,0)
```

### 📌 `up()`[​](https://www.drissionpage.cn/browser_control/actions#-up "-up的直接链接")
此方法用于使鼠标相对当前位置向上移动若干距离。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 鼠标移动的像素值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 鼠标向上移动 50 像素
```
tab.actions.up(50)
```

### 📌 `down()`[​](https://www.drissionpage.cn/browser_control/actions#-down "-down的直接链接")
此方法用于使鼠标相对当前位置向下移动若干距离。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 鼠标移动的像素值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.down(50)
```

### 📌 `left()`[​](https://www.drissionpage.cn/browser_control/actions#-left "-left的直接链接")
此方法用于使鼠标相对当前位置向左移动若干距离。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 鼠标移动的像素值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.left(50)
```

### 📌 `right()`[​](https://www.drissionpage.cn/browser_control/actions#-right "-right的直接链接")
此方法用于使鼠标相对当前位置向右移动若干距离。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`pixel`| `int`| 必填| 鼠标移动的像素值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.right(50)
```

## ✅️ 鼠标按键[​](https://www.drissionpage.cn/browser_control/actions#️-鼠标按键 "✅️ 鼠标按键的直接链接")
### 📌 `click()`[​](https://www.drissionpage.cn/browser_control/actions#-click "-click的直接链接")
此方法用于单击鼠标左键，单击前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要点击的元素对象或文本定位符  
`times`| `int`| `1`| 点击次数  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.click('#div1')
```

### 📌 `r_click()`[​](https://www.drissionpage.cn/browser_control/actions#-r_click "-r_click的直接链接")
此方法用于单击鼠标右键，单击前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要点击的元素对象或文本定位符  
`times`| `int`| `1`| 点击次数  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.r_click('#div1')
```

### 📌 `m_click()`[​](https://www.drissionpage.cn/browser_control/actions#-m_click "-m_click的直接链接")
此方法用于单击鼠标中键，单击前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要点击的元素对象或文本定位符  
`times`| `int`| `1`| 点击次数  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.m_click('#div1')
```

### 📌 `hold()`[​](https://www.drissionpage.cn/browser_control/actions#-hold "-hold的直接链接")
此方法用于按住鼠标左键不放，按住前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要按住的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
tab.actions.hold('#div1')
```

### 📌 `release()`[​](https://www.drissionpage.cn/browser_control/actions#-release "-release的直接链接")
此方法用于释放鼠标左键，释放前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要释放的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 移动到某元素上然后释放鼠标左键
```
tab.actions.release('#div1')
```

### 📌 `r_hold()`[​](https://www.drissionpage.cn/browser_control/actions#-r_hold "-r_hold的直接链接")
此方法用于按住鼠标右键不放，按住前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要按住的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
### 📌 `r_release()`[​](https://www.drissionpage.cn/browser_control/actions#-r_release "-r_release的直接链接")
此方法用于释放鼠标右键，释放前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要释放的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
### 📌 `m_hold()`[​](https://www.drissionpage.cn/browser_control/actions#-m_hold "-m_hold的直接链接")
此方法用于按住鼠标中键不放，按住前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要按住的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
### 📌 `m_release()`[​](https://www.drissionpage.cn/browser_control/actions#-m_release "-m_release的直接链接")
此方法用于释放鼠标中键，释放前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`on_ele`| `ChromiumElement``str`| `None`| 要释放的元素对象或文本定位符  
类型| 说明  
---|---  
`Actions`| 动作链对象本身  
## ✅️ 滚动滚轮[​](https://www.drissionpage.cn/browser_control/actions#️-滚动滚轮 "✅️ 滚动滚轮的直接链接")
### 📌 `scroll()`[​](https://www.drissionpage.cn/browser_control/actions#-scroll "-scroll的直接链接")
此方法用于滚动鼠标滚轮，滚动前可先移动到元素上。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`delta_y`| `int`| `0`| 滚轮 y 轴变化值，向下为正，向上为负  
`delta_x`| `int`| `0`| 滚轮 x 轴变化值，向右为正，向左为负  
`on_ele`| `ChromiumElement``str`| `None`| 要滚动的元素对象或文本定位符  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
## ✅️ 键盘按键和文本输入[​](https://www.drissionpage.cn/browser_control/actions#️-键盘按键和文本输入 "✅️ 键盘按键和文本输入的直接链接")
### 📌 `key_down()`[​](https://www.drissionpage.cn/browser_control/actions#-key_down "-key_down的直接链接")
此方法用于按下键盘按键。非字符串按键（如 ENTER）可输入其名称，也可以用 Keys 类获取。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`key`| `str`| 必填| 按键名称，或从`Keys`类获取的键值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 按下 ENTER 键
```
from DrissionPage.common import Keystab.actions.key_down('ENTER')# 输入按键名称tab.actions.key_down(Keys.ENTER)# 从Keys获取按键
```

### 📌 `key_up()`[​](https://www.drissionpage.cn/browser_control/actions#-key_up "-key_up的直接链接")
此方法用于提起键盘按键。非字符串按键（如 ENTER）可输入其名称，也可以用 Keys 类获取。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`key`| `str`| 必填| 按键名称，或从`Keys`类获取的键值  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：** 提起 ENTER 键
```
from DrissionPage.common import Keystab.actions.key_up('ENTER')# 输入按键名称tab.actions.key_up(Keys.ENTER)# 从Keys获取按键
```

### 📌 `input()`[​](https://www.drissionpage.cn/browser_control/actions#-input "-input的直接链接")
此方法用于输入一段文本或多段文本，也可输入组合键。
多段文本或组合键用列表传入。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text`| `str``list``tuple`| 必填| 要输入的文本或按键，多段文本或组合键可用`list`或`tuple`传入  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
from DrissionPage import Chromiumtab = Chromium().latest_tabtab.get('https://www.baidu.com')tab.actions.click('#kw').input('DrissionPage')
```

### 📌 `type()`[​](https://www.drissionpage.cn/browser_control/actions#-type "-type的直接链接")
此方法用于以按键盘的方式输入一段或多段文本。也可输入组合键。
`type()`与`input()`区别在于前者模拟按键输入，逐个字符按下和提起，后者直接输入一整段文本。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`keys`| `str``list``tuple`| 必填| 要输入的文本或按键，多段文本或组合键可用`list`或`tuple`传入  
返回类型| 说明  
---|---  
`Actions`| 动作链对象本身  
**示例：**
```
# 键入一段文本tab.actions.type('text')# 键入多段文本tab.actions.type(('ab','cd'))# 光标向左移动一位再键入文本tab.actions.type((Keys.LEFT,'abc'))# 输入快捷键tab.actions.type(Keys.CTRL_A)
```

## ✅️ 等待[​](https://www.drissionpage.cn/browser_control/actions#️-等待 "✅️ 等待的直接链接")
### 📌 `wait()`[​](https://www.drissionpage.cn/browser_control/actions#-wait "-wait的直接链接")
此方法用于等待若干秒。
`scope`为`None`时，效果与`time.sleep()`没有区别，等待指定秒数。
`scope`不为`None`时，获取两个参数之间的一个随机值，等待这个数值的秒数。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`second`| `float`| 必填| 要等待的秒数，`scope`不为`None`时表示随机数范围起始值  
`scope`| `float`| `None`| 随机数范围结束值  
**返回：**`None`
## ✅️ 属性[​](https://www.drissionpage.cn/browser_control/actions#️-属性 "✅️ 属性的直接链接")
### 📌 `owner`[​](https://www.drissionpage.cn/browser_control/actions#-owner "-owner的直接链接")
此属性返回使用此动作链的页面对象。
**类型：**`ChromiumBase`
### 📌 `curr_x`[​](https://www.drissionpage.cn/browser_control/actions#-curr_x "-curr_x的直接链接")
此属性返回当前光标位置的 x 坐标。
**类型：**`int`
### 📌 `curr_y`[​](https://www.drissionpage.cn/browser_control/actions#-curr_y "-curr_y的直接链接")
此属性返回当前光标位置的 y 坐标。
**类型：**`int`
## ✅️ 示例[​](https://www.drissionpage.cn/browser_control/actions#️-示例 "✅️ 示例的直接链接")
### 📌 模拟输入 ctrl+a[​](https://www.drissionpage.cn/browser_control/actions#-模拟输入-ctrla "📌 模拟输入 ctrl+a的直接链接")
```
from DrissionPage import Chromiumfrom DrissionPage.common import Keys# 创建页面对象tab = Chromium().latest_tab# 鼠标移动到<input>元素上tab.actions.move_to('tag:input')# 点击鼠标，使光标落到元素中tab.actions.click()# 按下 ctrl 键tab.actions.key_down(Keys.CTRL)# 输入 atab.actions.type('a')# 提起 ctrl 键tab.actions.key_up(Keys.CTRL)
```

链式写法：
```
tab.actions.click('tag:input').key_down(Keys.CTRL).type('a').key_up(Keys.CTRL)
```

更简单的写法：
```
tab.actions.click('tag:input').type(Keys.CTRL_A)
```

### 📌 拖拽元素[​](https://www.drissionpage.cn/browser_control/actions#-拖拽元素 "📌 拖拽元素的直接链接")
把一个元素向右拖拽 300 像素：
```
from DrissionPage import Chromium# 创建页面tab = Chromium().latest_tab# 左键按住元素tab.actions.hold('#div1')# 向右移动鼠标300像素tab.actions.right(300)# 释放左键tab.actions.release()
```

把一个元素拖拽到另一个元素上：
```
tab.actions.hold('#div1').release('#div2')
```

[上一页🛰️ iframe 操作](https://www.drissionpage.cn/browser_control/iframe)[下一页🛰️ 模式切换](https://www.drissionpage.cn/browser_control/mode_change)
  * [✅️ 使用方法](https://www.drissionpage.cn/browser_control/actions#️-使用方法)
    * [📌 使用内置`actions`属性](https://www.drissionpage.cn/browser_control/actions#-使用内置actions属性)
    * [📌 使用新对象](https://www.drissionpage.cn/browser_control/actions#-使用新对象)
    * [📌 操作方式](https://www.drissionpage.cn/browser_control/actions#-操作方式)
  * [✅️ 移动鼠标](https://www.drissionpage.cn/browser_control/actions#️-移动鼠标)
    * [📌 `move_to()`](https://www.drissionpage.cn/browser_control/actions#-move_to)
    * [📌 `move()`](https://www.drissionpage.cn/browser_control/actions#-move)
    * [📌 `up()`](https://www.drissionpage.cn/browser_control/actions#-up)
    * [📌 `down()`](https://www.drissionpage.cn/browser_control/actions#-down)
    * [📌 `left()`](https://www.drissionpage.cn/browser_control/actions#-left)
    * [📌 `right()`](https://www.drissionpage.cn/browser_control/actions#-right)
  * [✅️ 鼠标按键](https://www.drissionpage.cn/browser_control/actions#️-鼠标按键)
    * [📌 `click()`](https://www.drissionpage.cn/browser_control/actions#-click)
    * [📌 `r_click()`](https://www.drissionpage.cn/browser_control/actions#-r_click)
    * [📌 `m_click()`](https://www.drissionpage.cn/browser_control/actions#-m_click)
    * [📌 `hold()`](https://www.drissionpage.cn/browser_control/actions#-hold)
    * [📌 `release()`](https://www.drissionpage.cn/browser_control/actions#-release)
    * [📌 `r_hold()`](https://www.drissionpage.cn/browser_control/actions#-r_hold)
    * [📌 `r_release()`](https://www.drissionpage.cn/browser_control/actions#-r_release)
    * [📌 `m_hold()`](https://www.drissionpage.cn/browser_control/actions#-m_hold)
    * [📌 `m_release()`](https://www.drissionpage.cn/browser_control/actions#-m_release)
  * [✅️ 滚动滚轮](https://www.drissionpage.cn/browser_control/actions#️-滚动滚轮)
    * [📌 `scroll()`](https://www.drissionpage.cn/browser_control/actions#-scroll)
  * [✅️ 键盘按键和文本输入](https://www.drissionpage.cn/browser_control/actions#️-键盘按键和文本输入)
    * [📌 `key_down()`](https://www.drissionpage.cn/browser_control/actions#-key_down)
    * [📌 `key_up()`](https://www.drissionpage.cn/browser_control/actions#-key_up)
    * [📌 `input()`](https://www.drissionpage.cn/browser_control/actions#-input)
    * [📌 `type()`](https://www.drissionpage.cn/browser_control/actions#-type)
  * [✅️ 等待](https://www.drissionpage.cn/browser_control/actions#️-等待)
    * [📌 `wait()`](https://www.drissionpage.cn/browser_control/actions#-wait)
  * [✅️ 属性](https://www.drissionpage.cn/browser_control/actions#️-属性)
    * [📌 `owner`](https://www.drissionpage.cn/browser_control/actions#-owner)
    * [📌 `curr_x`](https://www.drissionpage.cn/browser_control/actions#-curr_x)
    * [📌 `curr_y`](https://www.drissionpage.cn/browser_control/actions#-curr_y)
  * [✅️ 示例](https://www.drissionpage.cn/browser_control/actions#️-示例)
    * [📌 模拟输入 ctrl+a](https://www.drissionpage.cn/browser_control/actions#-模拟输入-ctrla)
    * [📌 拖拽元素](https://www.drissionpage.cn/browser_control/actions#-拖拽元素)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/actions)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/actions)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
