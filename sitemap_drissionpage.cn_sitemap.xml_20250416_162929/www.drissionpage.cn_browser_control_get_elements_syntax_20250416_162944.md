# Content from: https://www.drissionpage.cn/browser_control/get_elements/syntax

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/syntax#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/syntax)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/syntax)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/syntax)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/syntax)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/syntax)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/syntax)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 定位语法


本页总览
# 🔦 定位语法
定位语法用于指明以哪种方式去查找指定元素，语法简洁明了，熟练使用可大幅提高程序可读性。
所有涉及获取元素的操作都可以使用定位语法，如`ele()`、`actions.move_to()`、`wait.eles_loaded()`、`get_frame()`等等。
定位语法用于简化代码，提高可读性，但并不覆盖所有复杂场景。很复杂的场景可直接用 xpath 查找。
以下使用这个页面进行讲解。
```
<html><body><divid="one"><pclass="p_cls"id="row1"data="a">第一行</p><pclass="p_cls"id="row2"data="b">第二行</p><pclass="p_cls">第三行</p></div><divid="two">  第二个div</div></body></html>
```

## ✅️️ 基本概念[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-基本概念 "✅️️ 基本概念的直接链接")
几乎所有查找方法都是基于元素属性进行。
元素属性包括以下三种：
写法| 说明| 示例  
---|---|---  
`@tag()`| 标签名| 即`<div id="one">`中的`div`  
`@****`| 标签体中的属性| 如`<div id="one">`中的`id`，写作`'@id'`  
`@text()`| 元素文本| 即`<p class="p_cls">第三行</p>`中的`第三行`  
查找语法就是按需要对这三种属性进行组合，达到查找指定元素的目的。
说明
`@tag()`和`@text()`后面加上`'()'`，是为了避免与普通元素冲突（如`<div text="abc">`）。
### 📌 简单示例[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-简单示例 "📌 简单示例的直接链接")
```
tab.ele('@id=one')# 获取第一个id为one的元素tab.ele('@tag()=div')# 获取第一个div元素tab.ele('@text()=第一行')# 获取第一个文本为“第一行”的元素
```

## ✅️️ 基本逻辑[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-基本逻辑 "✅️️ 基本逻辑的直接链接")
### 📌 单属性匹配符 `@`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-单属性匹配符- "-单属性匹配符-的直接链接")
单个`@`在只以一个属性作为匹配条件时使用，以`'@'`开头，后面跟属性名称。
上面简单示例中就是这种方式：`tab.ele('@id=one')`。
如果`@`后面只有属性名而没有属性值，查找有这个属性的元素，如`tab.ele('@id')`。
注意
如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。
### 📌 多属性与匹配符 `@@`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-多属性与匹配符- "-多属性与匹配符-的直接链接")
当需要多个条件同时确定一个元素时，每个属性用`'@@'`开头。
注意
  * 匹配文本或属性中出现`@@`、`@|`、`@!`时，不能使用多属性匹配，需改用 xpath 的方式。
  * 如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。


**示例：**
```
ele = tab.ele('@@class=p_cls@@text()=第三行')# 查找class为p_cls且文本为“第三行”的元素
```

### 📌 多属性或匹配符 `@|`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-多属性或匹配符- "-多属性或匹配符-的直接链接")
当需要以或关系条件查找元素时，每个属性用`'@|'`开头。
注意
  * 匹配文本或属性中出现`@@`、`@|`、`@!`时，不能使用多属性匹配，需改用 xpath 的方式。
  * 如果属性中包含特殊字符（如包含`@`），用这个方式不能正确匹配到，需使用 css selector 方式查找。且特殊字符要用`\`转义。


**示例：**
```
eles = tab.eles('@|id=row1@|id=row2')# 查找所有id为row1或id为row2的元素
```

### 📌 否定匹配符 `@!`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-否定匹配符- "-否定匹配符-的直接链接")
用于否定某个条件。
如果`@!`后面只有属性名而没有属性值，查找没有这个属性的元素。
**示例：**
```
ele = tab.ele('@!id=one')# 获取第一个id不等于“one”的元素ele = tab.ele('@!class')# 匹配没有class属性的元素
```

### 📌 混合使用[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-混合使用 "📌 混合使用的直接链接")
`@@`和`@|`不能同时出现的查找语句中，即一个查找语句只能是与关系或者或关系。
`@!`则可与两者混合使用。混用时，与还是或关系视`@@`还是`@|`而定。
说明
当语句中有多个`tag()`时，如果全部都没有被`@!`修饰，它们是与关系；如有任一个被`@!`修饰，它们是或关系。 `tag()`与其他属性之间是与关系。
**示例：**
```
# 匹配class等于p_cls且id不等于row1的元素tab.ele('@@class=p_cls@!id=row1')# 匹配class等于p_cls或id不等于row1的元素tab.ele('@|class=p_cls@!id=row1')
```

## ✅️️ 匹配模式[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-匹配模式 "✅️️ 匹配模式的直接链接")
匹配模式指某个查询中匹配条件的方式，有精确匹配、模糊匹配、匹配开头、匹配结尾四种。
说明
`tag()`属性无论用哪种匹配模式，都会视作`=`。
### 📌 精确匹配 `=`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-精确匹配- "-精确匹配-的直接链接")
表示精确匹配，匹配完全符合的文本或属性。
```
ele = tab.ele('@id=row1')# 获取id属性为'row1'的元素
```

### 📌 模糊匹配 `:`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-模糊匹��配- "-模糊匹配-的直接链接")
表示模糊匹配，匹配含有指定字符串的文本或属性。
```
ele = tab.ele('@id:ow')# 获取id属性包含'ow'的元素
```

### 📌 匹配开头 `^`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-匹配开头- "-匹配开头-的直接链接")
表示匹配开头，匹配开头为指定字符串的文本或属性。
```
ele = tab.ele('@id^row')# 获取id属性以'row'开头的元素
```

### 📌 匹配结尾 `$`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-匹配结尾- "-匹配结尾-的直接链接")
表示匹配结尾，匹配结尾为指定字符串的文本或属性。
```
ele = tab.ele('@id$w1')# 获取id属性以'w1'结尾的元素
```

## ✅️️ 常用语法[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-常用语法 "✅️️ 常用语法的直接链接")
基于上述基本逻辑，本库提供了一些更易于使用和阅读的语法。
### 📌 id 匹配符 `#`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-id-匹配符- "-id-匹配符-的直接链接")
用于匹配`id`属性，**只在语句最前面且单独使用时生效** 。相当于单属性查找`@id=****`。
可与匹配模式配合使用。
```
ele = tab.ele('#one')# 查找id为one的元素ele = tab.ele('#=one')# 和上面一行一致ele = tab.ele('#:ne')# 查找id属性包含ne的元素ele = tab.ele('#^on')# 查找id属性以on开头的元素ele = tab.ele('#$ne')# 查找id属性以ne结尾的元素
```

### 📌 class 匹配符 `.`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-class-匹配符- "-class-匹配符-的直接链接")
用于匹配`class`属性，**只在语句最前面且单独使用时生效** ，相当于单属性查找`@class=****`。
可配合匹配模式使用。
说明
在面对多个 class 的元素时，DrissionPage 与 selenium 处理方式不一样，无需将空格替换成`'.'`。 而是将整个 class 视作普通字符串，空格视作普通字符对待，会比较直观。
```
ele = tab.ele('.p_cls')# 查找class属性为p_cls的元素ele = tab.ele('.=p_cls')# 与上一行一致ele = tab.ele('.:_cls')# 查找class属性包含_cls的元素ele = tab.ele('.^p_')# 查找class属性以p_开头的元素ele = tab.ele('.$_cls')# 查找class属性以_cls结尾的元素
```

### 📌 文本匹配符 `text`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-文本匹配符-text "-文本匹配符-text的直接链接")
用于匹配元素文本。**只在语句最前面且单独使用时生效** ，相当于单属性查找`@text()=****`。
可配合匹配模式使用。
如果元素内有多个直接的文本节点，精确查找时可匹配所有文本节点拼成的字符串，模糊查找时可匹配每个文本节点。
如果查找语句没有任何本节介绍的匹配符，默认模糊匹配文本。即`ele('第三行')`相当于`ele('text:第三行')`。
注意
如果要匹配的文本包含特殊字符（如`'&nbsp;'`、`'&gt;'`），需将其转换为十六进制形式，详见《语法速查表》一节。
```
ele = tab.ele('text=第二行')# 查找文本为“第二行”的元素ele = tab.ele('text:第二')# 查找文本包含“第二”的元素ele = tab.ele('第二')# 与上一行一致ele = tab.ele('第\u00A0二')# 匹配包含&nbsp;文本的元素，需将&nbsp;转为\u00A0
```

Tips
若要查找的文本包含`text:` ，可下面这样写，即第一个`text:` 为关键字，第二个是要查找的内容：
```
ele2 = tab.ele('text:text:')
```

### 📌 类型匹配符 `tag`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-类型匹配符-tag "-类型匹配符-tag的直接链接")
用于匹配某类型元素。**只在语句最前面且单独使用时生效** ，相当于单属性查找`@tag()=****`。
可与单属性查找或多属性配合使用。`tag:`与`tag=`效果一致，没有`tag^`和`tag$`语法。
```
ele = tab.ele('tag:div')# 查找第一个div元素ele = tab.ele('tag:p@class=p_cls')# 与单属性查找配合使用ele = tab.ele('tag:p@@class=p_cls@@text()=第二行')# 与多属性查找配合使用
```

注意
`tag:div@text():abc` 和 `tag:div@@text():abc` 是有区别的，前者只在`div`的直接文本节点搜索，后者搜索`div`的整个内部。
### 📌 css selector 匹配符 `css`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-css-selector-匹配符-css "-css-selector-匹配符-css的直接链接")
表示用 css selector 方式查找元素。**只在语句最前面且单独使用时生效** 。
`css:`与`css=`效果一致，没有`css^`和`css$`语法。
```
ele = tab.ele('css:.div')# 查找 div 元素ele = tab.ele('css:>div')# 查找 div 子元素元素，这个写法是本库特有，原生不支持
```

### 📌 xpath 匹配符 `xpath`[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-xpath-匹配符-xpath "-xpath-匹配符-xpath的直接链接")
表示用 xpath 方式查找元素。**只在语句最前面且单独使用时生效** 。
`xpath:`与`xpath=`效果一致，没有`xpath^`和`xpath$`语法。
Tips
**元素对象** 的`ele()`支持完整的 xpath 语法，如能使用 xpath 直接获取元素属性（字符串类型）。
```
ele2 = ele1.ele('xpath:.//div')# 查找后代中第一个 div 元素ele2 = ele1.ele('xpath://div')# 和上面一行一样，查找元素的后代时，// 前面的 . 可以省略ele_class_str = ele1.ele('xpath://div/@class')# 使用xpath获取div元素的class属性（页面元素无此功能）
```

说明
查找元素的后代时，selenium 原生代码要求 xpath 前面必须加`.`，否则会变成在全个页面中查找。 作者觉得这个设计是画蛇添足，既然已经通过元素查找了，自然应该只查找这个元素内部的元素。 所以，用 xpath 在元素下查找时，最前面`//`或`/`前面的`.`可以省略。
### 📌 selenium 的 loc 元组[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#-selenium-的-loc-元组 "📌 selenium 的 loc 元组的直接链接")
查找方法能直接接收 selenium 原生定位元组进行查找，便于项目迁移。
```
from DrissionPage.common import By# 查找id为one的元素loc1 =(By.ID,'one')ele = tab.ele(loc1)# 按 xpath 查找loc2 =(By.XPATH,'//p[@class="p_cls"]')ele = tab.ele(loc2)
```

## ✅️️ `@@text()`的技巧[​](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-text的技巧 "️️-text的技巧的直接链接")
值得一提的是，`text()`配合`@@`或`@|`能实现一种很便利的按查找方式。
网页种经常会出现元素和文本混排的情况，比如：
```
<liclass="explore-categories__item"><ahref="/explore/new-tech"class=""><iclass="explore"></i>    前沿技术</a></li><liclass="explore-categories__item"><ahref="/explore/program-develop"class=""><iclass="explore"></i>    程序开发</a></li>
```

示例中，如果要用文本获取`'前沿技术'`的`<a>`元素，可以这样写：
```
ele = tab.ele('text:前沿技术')# 或ele = tab.ele('@text():前沿技术')
```

这两种写法都能获取到包含直接文本的元素。
但如果要用文本获取`<li>`元素，就获取不到，因为文本不是`<li>`的直接内容。
我们可以这样写：
```
ele = tab.ele('tag:li@@text():前沿技术')
```

`@@text()`与`@text()`不同之处在于，前者可以搜索整个元素内所有文本，而不仅仅是直接文本，因此能实现一些非常灵活的查找。
注意
需要注意的是，使用`@@`或`@|`时，`text()`不要作为唯一的查询条件，否则会定位到整个文档最高层的元素。
❌ 错误做法：
```
ele = tab.ele('@@text():前沿技术')ele = tab.ele('@|text():前沿技术@|text():程序开发')
```

⭕ 正确做法：
```
ele = tab.ele('tag:li@|text():前沿技术@|text():程序开发')
```

[上一页🔦 概述](https://www.drissionpage.cn/browser_control/get_elements/intro)[下一页🔦 页面或元素内查找](https://www.drissionpage.cn/browser_control/get_elements/find_in_object)
  * [✅️️ 基本概念](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-基本概念)
    * [📌 简单示例](https://www.drissionpage.cn/browser_control/get_elements/syntax#-简单示例)
  * [✅️️ 基本逻辑](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-基本逻辑)
    * [📌 单属性匹配符 `@`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-单属性匹配符-)
    * [📌 多属性与匹配符 `@@`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-多属性与匹配符-)
    * [📌 多属性或匹配符 `@|`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-多属性或匹配符-)
    * [📌 否定匹配符 `@!`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-否定匹配符-)
    * [📌 混合使用](https://www.drissionpage.cn/browser_control/get_elements/syntax#-混合使用)
  * [✅️️ 匹配模式](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-匹配模式)
    * [📌 精确匹配 `=`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-精确匹配-)
    * [📌 模糊匹配 `:`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-模糊匹配-)
    * [📌 匹配开头 `^`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-匹配开头-)
    * [📌 匹配结尾 `$`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-匹配结尾-)
  * [✅️️ 常用语法](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-常用语法)
    * [📌 id 匹配符 `#`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-id-匹配符-)
    * [📌 class 匹配符 `.`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-class-匹配符-)
    * [📌 文本匹配符 `text`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-文本匹配符-text)
    * [📌 类型匹配符 `tag`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-类型匹配符-tag)
    * [📌 css selector 匹配符 `css`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-css-selector-匹配符-css)
    * [📌 xpath 匹配符 `xpath`](https://www.drissionpage.cn/browser_control/get_elements/syntax#-xpath-匹配符-xpath)
    * [📌 selenium 的 loc 元组](https://www.drissionpage.cn/browser_control/get_elements/syntax#-selenium-的-loc-元组)
  * [✅️️ `@@text()`的技巧](https://www.drissionpage.cn/browser_control/get_elements/syntax#️️-text的技巧)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/syntax)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/syntax)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
