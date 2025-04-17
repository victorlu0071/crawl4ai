# Content from: https://www.drissionpage.cn/SessionPage/get_ele_info

[跳到主要内容](https://www.drissionpage.cn/SessionPage/get_ele_info#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/get_ele_info)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/get_ele_info)
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
  * 🛩️ 获取元素信息


本页总览
# 🛩️ 获取元素信息
`SessionPage`对象获取的元素是`SessionElement`，本节介绍其属性。
假设`ele`为以下`div`元素的对象，本节示例均使用该元素：
```
<divid="div1"class="divs">Hello World!<p>行元素</p><!--这是注释--></div>
```

## ✅️️ `html`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-html "️️-html的直接链接")
此属性返回元素的`outerHTML`文本。
**返回类型：**`str`
```
print(ele.html)
```

**输出：**
```
<div id="div1" class="divs">Hello World!  <p>行元素</p>  <!--这是注释--></div>
```

## ✅️️ `inner_html`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-inner_html "️️-inner_html的直接链接")
此属性返回元素的`innerHTML`文本。
**返回类型：**`str`
```
print(ele.inner_html)
```

**输出：**
```
Hello World!  <p>行元素</p>  <!--这是注释-->
```

## ✅️️ `tag`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-tag "️️-tag的直接链接")
此属性返回元素的标签名。
**返回类型：**`str`
```
print(ele.tag)
```

**输出：**
```
div
```

## ✅️️ `text`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-text "️️-text的直接链接")
此属性返回元素内所有文本组合成的字符串。 该字符串已格式化，即已转码，已去除多余换行符，符合人读取习惯，便于直接使用。
**返回类型：**`str`
```
print(ele.text)
```

**输出：**
```
Hello World!行元素
```

## ✅️️ `raw_text`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-raw_text "️️-raw_text的直接链接")
此属性返回元素内原始文本。
**返回类型：**`str`
```
print(ele.raw_text)
```

输出（注意保留了元素间的空格和换行）：
```
Hello World!  行元素
```

## ✅️️ `texts()`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-texts "️️-texts的直接链接")
此方法返回元素内所有**直接** 子节点的文本，包括元素和文本节点。 它有一个参数`text_node_only`，为`True`时则只获取只返回不被包裹的文本节点。这个方法适用于获取文本节点和元素节点混排的情况。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`text_node_only`| `bool`| `False`| 是否只返回文本节点  
返回类型| 说明  
---|---  
`List[str]`| 文本列表  
**示例：**
```
print(e.texts())print(e.texts(text_node_only=True))
```

**输出：**
```
['Hello World!', '行元素']['Hello World!']
```

## ✅️️ `comments`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-comments "️️-comments的直接链接")
此属性以列表形式返回元素内的注释。
**返回类型：**`List[str]`
```
print(ele.comments)
```

**输出：**
```
[<!--这是注释-->]
```

## ✅️️ `attrs`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-attrs "️️-attrs的直接链接")
此属性以字典形式返回元素所有属性及值。
**返回类型：**`dict`
```
print(ele.attrs)
```

**输出：**
```
{'id': 'div1', 'class': 'divs'}
```

## ✅️️ `attr()`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-attr "️️-attr的直接链接")
此方法返回元素某个 attribute 属性值。它接收一个字符串参数，返回该属性值文本，无该属性时返回`None`。 此属性返回的`src`、`href`属性为已补充完整的路径。`text`属性为已格式化文本。 如果要获取未补充完整路径的`src`或`href`属性，可以用`attrs['src']`。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`str`| 属性值文本  
`None`| 没有该属性返回`None`  
**示例：**
```
print(ele.attr('id'))
```

**输出：**
```
div1
```

## ✅️️ `link`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-link "️️-link的直接链接")
此方法返回元素的 href 属性或 src 属性，没有这两个属性则返回`None`。
**返回类型：**`str`
```
<ahref='http://www.baidu.com'>百度</a>
```

假设`a_ele`为以上元素的对象：
```
print(a_ele.link)
```

**输出：**
```
http://www.baidu.com
```

### 📌 `child_count`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#-child_count "-child_count的直接链接")
此属性返回元素内第一级子元素个数。
**类型：**`int`
## ✅️️ `page`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-page "️️-page的直接链接")
此属性返回元素所在的页面对象。由 html 文本直接生成的`SessionElement`的`page`属性为`None`。
**返回类型：**`SessionPage` 、`WebPage`
```
page = ele.page
```

## ✅️️ `xpath`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-xpath "️️-xpath的直接链接")
此属性返回当前元素在页面中 xpath 的绝对路径。
**返回类型：**`str`
```
print(ele.xpath)
```

**输出：**
```
/html/body/div
```

## ✅️️ `css_path`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-css_path "️️-css_path的直接链接")
此属性返回当前元素在页面中 css selector 的绝对路径。
**返回类型：**`str`
```
print(ele.css_path)
```

**输出：**
```
:nth-child(1)>:nth-child(1)>:nth-child(1)
```

## ✅️️ 元素列表中批量获取信息[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-元素列表中批量获取信息 "✅️️ 元素列表中批量获取信息的直接链接")
`eles()`等返回的元素列表，自带`get`属性，可用于获取指定信息。
### 📌 示例[​](https://www.drissionpage.cn/SessionPage/get_ele_info#-示例 "📌 示例的直接链接")
```
from DrissionPage import SessionPagepage = SessionPage()page.get('https://www.baidu.com')eles = page('#s-top-left').eles('t:a')print(eles.get.texts())# 获取所有元素的文本
```

**输出：**
```
['新闻', 'hao123', '地图', '贴吧', '视频', '图片', '网盘', '文库', '更多', '翻译', '学术', '百科', '知道', '健康', '营销推广', '直播', '音乐', '橙篇', '查看全部百度产品 >']
```

### 📌 `get.attrs()`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#-getattrs "-getattrs的直接链接")
此方法用于返回所有元素指定的 attribute 属性组成的列表。
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`name`| `str`| 必填| 属性名称  
返回类型| 说明  
---|---  
`List[str]`| 属性文本组成的列表  
### 📌 `get.links()`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#-getlinks "-getlinks的直接链接")
此方法用于返回所有元素的`link`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 链接文本组成的列表  
### 📌 `get.texts()`[​](https://www.drissionpage.cn/SessionPage/get_ele_info#-gettexts "-gettexts的直接链接")
此方法用于返回所有元素的`text`属性组成的列表。
**参数：** 无
返回类型| 说明  
---|---  
`List[str]`| 元素文本组成的列表  
## ✅️️ 实际示例[​](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-实际示例 "✅️️ 实际示例的直接链接")
以下示例可直接运行查看结果：
```
from DrissionPage import SessionPagepage = SessionPage()page.get('https://gitee.com/explore')# 获取推荐目录下所有 a 元素li_eles = page('tag:ul@text():全部推荐项目').eles('t:a')# 遍历列表for i in li_eles:# 获取并打印标签名、文本、href 属性print(i.tag, i.text, i.attribute('href'))
```

**输出：**
```
a 全部推荐项目 https://gitee.com/explore/alla 前沿技术 https://gitee.com/explore/new-techa 智能硬件 https://gitee.com/explore/hardwarea IOT/物联网/边缘计算 https://gitee.com/explore/iota 车载应用 https://gitee.com/explore/vehicle以下省略……
```

[上一页🛩️ 查找元素](https://www.drissionpage.cn/SessionPage/get_ele)[下一页🛩️ 页面设置](https://www.drissionpage.cn/SessionPage/settings)
  * [✅️️ `html`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-html)
  * [✅️️ `inner_html`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-inner_html)
  * [✅️️ `tag`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-tag)
  * [✅️️ `text`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-text)
  * [✅️️ `raw_text`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-raw_text)
  * [✅️️ `texts()`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-texts)
  * [✅️️ `comments`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-comments)
  * [✅️️ `attrs`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-attrs)
  * [✅️️ `attr()`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-attr)
  * [✅️️ `link`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-link)
    * [📌 `child_count`](https://www.drissionpage.cn/SessionPage/get_ele_info#-child_count)
  * [✅️️ `page`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-page)
  * [✅️️ `xpath`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-xpath)
  * [✅️️ `css_path`](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-css_path)
  * [✅️️ 元素列表中批量获取信息](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-元素列表中批量获取信息)
    * [📌 示例](https://www.drissionpage.cn/SessionPage/get_ele_info#-示例)
    * [📌 `get.attrs()`](https://www.drissionpage.cn/SessionPage/get_ele_info#-getattrs)
    * [📌 `get.links()`](https://www.drissionpage.cn/SessionPage/get_ele_info#-getlinks)
    * [📌 `get.texts()`](https://www.drissionpage.cn/SessionPage/get_ele_info#-gettexts)
  * [✅️️ 实际示例](https://www.drissionpage.cn/SessionPage/get_ele_info#️️-实际示例)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/get_ele_info)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/get_ele_info)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
