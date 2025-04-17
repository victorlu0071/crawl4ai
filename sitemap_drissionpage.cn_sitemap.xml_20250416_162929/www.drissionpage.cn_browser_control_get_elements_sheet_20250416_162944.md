# Content from: https://www.drissionpage.cn/browser_control/get_elements/sheet

[跳到主要内容](https://www.drissionpage.cn/browser_control/get_elements/sheet#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/browser_control/get_elements/sheet)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/browser_control/get_elements/sheet)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🚀 控制浏览器](https://www.drissionpage.cn/browser_control/get_elements/sheet)
    * [🛰️ 概述](https://www.drissionpage.cn/browser_control/intro)
    * [🛰️ 连接浏览器](https://www.drissionpage.cn/browser_control/connect_browser)
    * [🛰️ 浏览器启动设置](https://www.drissionpage.cn/browser_control/browser_options)
    * [🛰️ 浏览器对象](https://www.drissionpage.cn/browser_control/browser_object)
    * [🛰️ 标签页管理](https://www.drissionpage.cn/browser_control/tabs)
    * [🛰️ 访问网页](https://www.drissionpage.cn/browser_control/visit)
    * [🛰️ 页面交互](https://www.drissionpage.cn/browser_control/page_operation)
    * [🛰️ 获取网页信息](https://www.drissionpage.cn/browser_control/get_page_info)
    * [🔎 查找元素](https://www.drissionpage.cn/browser_control/get_elements/sheet)
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
  * [🛫 SessionPage](https://www.drissionpage.cn/browser_control/get_elements/sheet)
  * [🧰 进阶使用](https://www.drissionpage.cn/browser_control/get_elements/sheet)


  * [](https://www.drissionpage.cn/)
  * 🚀 控制浏览器
  * 🔎 查找元素
  * 🔦 语法速查表


本页总览
# 🔦 语法速查表
## ✅️ 定位语法[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-定位语法 "✅️ 定位语法的直接链接")
### 📌 基本用法[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#-基本用法 "📌 基本用法的直接链接")
写法| 精确匹配| 模糊匹配| 匹配开头| 匹配结尾| 说明  
---|---|---|---|---|---  
`@属性名`| `@属性名=`| `@属性名:`| `@属性名^`| `@属性名$`| 按某个属性查找  
`@!属性名`| `@!属性名=`| `@!属性名:`| `@!属性名^`| `@!属性名$`| 查找属性不符合指定条件的元素  
`text`| `text=`| `text:`或不写| `text^`| `text$`| 按某个文本查找  
`@text()`| `@text()=`| `@text():`| `text()^`| `text()$`| `text`与`@`或`@@`配合使用时改为`text()`，常用于多条件匹配  
`tag`| `tag=`或`tag:`| 无| 无| 无| 查找某个类型的元素  
`@tag()`| `@tag()=`或`@tag():`| 无| 无| 无| 组合使用时查找某个类型的元素  
`xpath`| `xpath=`或`xpath:`| 无| 无| 无| 用 xpath 方式查找元素  
`css`| `css=`或`css:`| 无| 无| 无| 用 css selector 方式查找元素  
### 📌 组合用法[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#-组合用法 "📌 组合用法的直接链接")
写法| 说明  
---|---  
`@@属性1@@属性2`| 匹配属性同时符合多个条件的元素  
`@@属性1@!属性2`| 多属性匹配与否定匹配同时使用  
`@|属性1@|属性2`| 匹配属性至符合多个条件中一的元素  
`tag:元素名@属性名`| `tag`与属性匹配共同使用  
`tag:元素名@@属性1@@属性2`| `tag`与多属性匹配共同使用  
`tag:元素名@|属性1@|属性2`| `tag`与多属性匹配共同使用  
`tag:元素名@@text()=文本@@属性`| `tag`与文本和属性匹配共同使用  
### 📌 简化写法[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#-简化写法 "📌 简化写法的直接链接")
原写法| 简化写法| 精确匹配| 模糊匹配| 匹配开头| 匹配结尾| 备注  
---|---|---|---|---|---|---  
`@id`| `#`| `#`或`#=`| `#:`| `#^`| `#$`| 简化写法只能单独使用  
`@class`| `.`| `.`或`.=`| `.:`| `.^`| `.$`| 简化写法只能单独使用  
`tag`| `t`| `t:`或`t=`| 无| 无| 无| 只能用在句首  
`@tag()`| `@t()`| `@t():`或`@t()=`| 无| 无| 无| 可作为属性组合使用  
`text`| `tx`| `tx=`| `tx:`或不写| `tx^`| `tx$`| 无标签时使用模糊匹配文本  
`@text()`| `@tx()`| `@tx()=`| `@tx():`| `@tx()^`| `@tx()$`| 可作为属性组合使用  
`xpath`| `x`| `x:`或`x=`| 无| 无| 无| 只能单独使用  
`css`| `c`| `c:`或`c=`| 无| 无| 无| 只能单独使用  
## ✅️ 相对定位[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-相对定位 "✅️ 相对定位的直接链接")
方法| 说明  
---|---  
`parent()`| 查找当前元素某一级父元素  
`child()`| 查找当前元素的一个直接子节点  
`children()`| 查找当前元素全部符合条件的直接子节点  
`next()`| 查找当前元素之后第一个符合条件的兄弟节点  
`nexts()`| 查找当前元素之后所有符合条件的兄弟节点  
`prev()`| 查找当前元素之前第一个符合条件的兄弟节点  
`prevs()`| 查找当前元素之前所有符合条件的兄弟节点  
`after()`| 查找文档中当前元素之后第一个符合条件的节点  
`afters()`| 查找文档中当前元素之后所有符合条件的节点  
`before()`| 查找文档中当前元素之前第一个符合条件的节点  
`befores()`| 查找文档中当前元素之前所有符合条件的节点  
## ✅️ iframe 和 shadow root[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-iframe-和-shadow-root "✅️ iframe 和 shadow root的直接链接")
方法| 简化写法| 说明| 备注  
---|---|---|---  
`get_frame()`| 无| 在页面中查找一个`<iframe>`元素| 只有页面对象有此方法  
`shadow_root`| `sr`| 获取当前元素内的 shadow root 对象| 只有元素对象有此属性  
## ✅️ 特殊字符对照表[​](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-特殊字符对照表 "✅️ 特殊字符对照表的直接链接")
要匹配的文本中如包含特殊字符（如`'&nbsp;'`、`'&gt;'`），需将特殊字符转为十六进制，对照表如下：
特殊符号| 命名实体| 编码| 特殊符号| 命名实体| 编码| 特殊符号| 命名实体| 编码  
---|---|---|---|---|---|---|---|---  
`Α`| `&Alpha;`| \u0391| `Β`| `&Beta;`| \u0392| `Γ`| `&Gamma;`| \u0393  
`Δ`| `&Delta;`| \u0394| `Ε`| `&Epsilon;`| \u0395| `Ζ`| `&Zeta;`| \u0396  
`Η`| `&Eta;`| \u0397| `Θ`| `&Theta;`| \u0398| `Ι`| `&Iota;`| \u0399  
`Κ`| `&Kappa;`| \u039A| `Λ`| `&Lambda;`| \u039B| `Μ`| `&Mu;`| \u039C  
`Ν`| `&Nu;`| \u039D| `Ξ`| `&Xi;`| \u039E| `Ο`| `&Omicron;`| \u039F  
`Π`| `&Pi;`| \u03A0| `Ρ`| `&Rho;`| \u03A1| `Σ`| `&Sigma;`| \u03A3  
`Τ`| `&Tau;`| \u03A4| `Υ`| `&Upsilon;`| \u03A5| `Φ`| `&Phi;`| \u03A6  
`Χ`| `&Chi;`| \u03A7| `Ψ`| `&Psi;`| \u03A8| `Ω`| `&Omega;`| \u03A9  
`α`| `&alpha;`| \u03B1| `β`| `&beta;`| \u03B2| `γ`| `&gamma;`| \u03B3  
`δ`| `&delta;`| \u03B4| `ε`| `&epsilon;`| \u03B5| `ζ`| `&zeta;`| \u03B6  
`η`| `&eta;`| \u03B7| `θ`| `&theta;`| \u03B8| `ι`| `&iota;`| \u03B9  
`κ`| `&kappa;`| \u03BA| `λ`| `&lambda;`| \u03BB| `μ`| `&mu;`| \u03BC  
`ν`| `&nu;`| \u03BD| `ξ`| `&xi;`| \u03BE| `ο`| `&omicron;`| \u03BF  
`π`| `&pi;`| \u03C0| `ρ`| `&rho;`| \u03C1| `ς`| `&sigmaf;`| \u03C2  
`σ`| `&sigma;`| \u03C3| `τ`| `&tau;`| \u03C4| `υ`| `&upsilon;`| \u03C5  
`φ`| `&phi;`| \u03C6| `χ`| `&chi;`| \u03C7| `ψ`| `&psi;`| \u03C8  
`ω`| `&omega;`| \u03C9| `ϑ`| `&thetasym;`| \u03D1| `ϒ`| `&upsih;`| \u03D2  
`ϖ`| `&piv;`| \u03D6| `•`| `&bull;`| \u2022| `…`| `&hellip;`| \u2026  
`′`| `&prime;`| \u2032| `″`| `&Prime;`| \u2033| `‾`| `&oline;`| \u203E  
`⁄`| `&frasl;`| \u2044| `℘`| `&weierp;`| \u2118| `ℑ`| `&image;`| \u2111  
`ℜ`| `&real;`| \u211C| `™`| `&trade;`| \u2122| `ℵ`| `&alefsym;`| \u2135  
`←`| `&larr;`| \u2190| `↑`| `&uarr;`| \u2191| `→`| `&rarr;`| \u2192  
`↓`| `&darr;`| \u2193| `↔`| `&harr;`| \u2194| `↵`| `&crarr;`| \u21B5  
`⇐`| `&lArr;`| \u21D0| `⇑`| `&uArr;`| \u21D1| `⇒`| `&rArr;`| \u21D2  
`⇓`| `&dArr;`| \u21D3| `⇔`| `&hArr;`| \u21D4| `∀`| `&forall;`| \u2200  
`∂`| `&part;`| \u2202| `∃`| `&exist;`| \u2203| `∅`| `&empty;`| \u2205  
`∇`| `&nabla;`| \u2207| `∈`| `&isin;`| \u2208| `∉`| `&notin;`| \u2209  
`∋`| `&ni;`| \u220B| `∏`| `&prod;`| \u220F| `∑`| `&sum;`| \u2212  
`−`| `&minus;`| \u2212| `∗`| `&lowast;`| \u2217| `√`| `&radic;`| \u221A  
`∝`| `&prop;`| \u221D| `∞`| `&infin;`| \u221E| `∠`| `&ang;`| \u2220  
`∧`| `&and;`| \u22A5| `∨`| `&or;`| \u22A6| `∩`| `&cap;`| \u2229  
`∪`| `&cup;`| \u222A| `∫`| `&int;`| \u222B| `∴`| `&there4;`| \u2234  
`∼`| `&sim;`| \u223C| `≅`| `&cong;`| \u2245| `≈`| `&asymp;`| \u2245  
`≠`| `&ne;`| \u2260| `≡`| `&equiv;`| \u2261| `≤`| `&le;`| \u2264  
`≥`| `&ge;`| \u2265| `⊂`| `&sub;`| \u2282| `⊃`| `&sup;`| \u2283  
`⊄`| `&nsub;`| \u2284| `⊆`| `&sube;`| \u2286| `⊇`| `&supe;`| \u2287  
`⊕`| `&oplus;`| \u2295| `⊗`| `&otimes;`| \u2297| `⊥`| `&perp;`| \u22A5  
`⋅`| `&sdot;`| \u22C5| `⌈`| `&lceil;`| \u2308| `⌉`| `&rceil;`| \u2309  
`⌊`| `&lfloor;`| \u230A| `⌋`| `&rfloor;`| \u230B| `◊`| `&loz;`| \u25CA  
`♠`| `&spades;`| \u2660| `♣`| `&clubs;`| \u2663| `♥`| `&hearts;`| \u2665  
`♦`| `&diams;`| \u2666| `&nbsp;`| \u00A0| `¡`| `&iexcl;`| \u00A1  
`¢`| `&cent;`| \u00A2| `£`| `&pound;`| \u00A3| `¤`| `&curren;`| \u00A4  
`¥`| `&yen;`| \u00A5| `¦`| `&brvbar;`| \u00A6| `§`| `&sect;`| \u00A7  
`¨`| `&uml;`| \u00A8| `©`| `&copy;`| \u00A9| `ª`| `&ordf;`| \u00AA  
`«`| `&laquo;`| \u00AB| `¬`| `&not;`| \u00AC| `­`| `&shy;`| \u00AD  
`®`| `&reg;`| \u00AE| `¯`| `&macr;`| \u00AF| `°`| `&deg;`| \u00B0  
`±`| `&plusmn;`| \u00B1| `²`| `&sup2;`| \u00B2| `³`| `&sup3;`| \u00B3  
`´`| `&acute;`| \u00B4| `µ`| `&micro;`| \u0012| `"`| `&quot;`| \u0022  
`<`| `&lt;`| \u003C| `>`| `&gt;`| \u003E| `'`| \u0027  
[上一页🔦 简化写法](https://www.drissionpage.cn/browser_control/get_elements/simplify)[下一页🛰️ 元素交互](https://www.drissionpage.cn/browser_control/ele_operation)
  * [✅️ 定位语法](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-定位语法)
    * [📌 基本用法](https://www.drissionpage.cn/browser_control/get_elements/sheet#-基本用法)
    * [📌 组合用法](https://www.drissionpage.cn/browser_control/get_elements/sheet#-组合用法)
    * [📌 简化写法](https://www.drissionpage.cn/browser_control/get_elements/sheet#-简化写法)
  * [✅️ 相对定位](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-相对定位)
  * [✅️ iframe 和 shadow root](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-iframe-和-shadow-root)
  * [✅️ 特殊字符对照表](https://www.drissionpage.cn/browser_control/get_elements/sheet#️-特殊字符对照表)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/browser_control/get_elements/sheet)
  * [QQ群：391178600](https://www.drissionpage.cn/browser_control/get_elements/sheet)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
