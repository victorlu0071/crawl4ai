# Content from: https://www.drissionpage.cn/SessionPage/get_page_info

[跳到主要内容](https://www.drissionpage.cn/SessionPage/get_page_info#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/SessionPage/get_page_info)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/SessionPage/get_page_info)
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
  * 🛩️ 获取页面信息


本页总览
# 🛩️ 获取页面信息
成功访问网页后，可使用`SessionPage`对象自身属性和方法获取页面信息。
```
from DrissionPage import SessionPagepage = SessionPage()page.get('http://www.baidu.com')# 获取页面标题print(page.title)# 获取页面htmlprint(page.html)
```

**输出：**
```
百度一下，你就知道<!DOCTYPE html><!--STATUS OK--><html> <head><meta http-equi...
```

## ✅️️ 页面信息[​](https://www.drissionpage.cn/SessionPage/get_page_info#️️-页面信息 "✅️️ 页面信息的直接链接")
### 📌 `url`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-url "-url的直接链接")
此属性返回当前访问的 url。
**类型：**`str`
### 📌 `url_available`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-url_available "-url_available的直接链接")
此属性以布尔值返回当前链接是否可用。
**类型：**`bool`
### 📌 `title`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-title "-title的直接链接")
此属性返回当前页面`title`文本。
**类型：**`str`
### 📌 `raw_data`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-raw_data "-raw_data的直接链接")
此属性返回访问到的元素数据，即`Response`对象的`content`属性。
**类型：**`bytes`
### 📌 `html`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-html "-html的直接链接")
此属性返回当前页面 html 文本。
**类型：**`str`
### 📌 `json`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-json "-json的直接链接")
此属性把返回内容解析成 json。 比如请求接口时，若返回内容是 json 格式，用`html`属性获取的话会得到一个字符串，用此属性获取可将其解析成`dict`。 支持访问 `*.json` 文件，也支持 API 返回的json字符串。
**类型：**`dict`
### 📌 `user_agent`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-user_agent "-user_agent的直接链接")
此属性返回当前页面 user_agent 信息。
**类型：**`str`
## ✅️️ 运行参数信息[​](https://www.drissionpage.cn/SessionPage/get_page_info#️️-运行参数信息 "✅️️ 运行参数信息的直接链接")
### 📌 `timeout`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-timeout "-timeout的直接链接")
此属性返回网络请求超时时间，默认为 10 秒。
**类型：**`int` 、`float`
### 📌 `retry_times`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-retry_times "-retry_times的直接链接")
此属性为网络连接失败时的重试次数，默认为`3`。
**类型：**`int`
### 📌 `retry_interval`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-retry_interval "-retry_interval的直接链接")
此属性为网络连接失败时的重试等待间隔秒数，默认为`2`。
**类型：**`int` 、`float`
### 📌 `encoding`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-encoding "-encoding的直接链接")
此属性返回用户主动设置的编码格式。
## ✅️️ cookies 信息[​](https://www.drissionpage.cn/SessionPage/get_page_info#️️-cookies-信息 "✅️️ cookies 信息的直接链接")
### 📌 `cookies()`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-cookies "-cookies的直接链接")
此方法返回 cookies 信息。
**类型：**`dict` 、`list`
参数名称| 类型| 默认值| 说明  
---|---|---|---  
`all_domains`| `bool`| `False`| 是否返回所有 cookies，为`False`只返回当前 url 的  
`all_info`| `bool`| `False`| 返回的 cookies 是否包含所有信息，`False`时只包含`name`、`value`、`domain`信息  
返回类型| 说明  
---|---  
`CookiesList`| cookies 组成的列表  
`cookies()`方法返回的列表可转换为其它指定格式。
  * `cookies().as_str()`：`'name1=value1; name2=value2'`格式的字符串
  * `cookies().as_dict()`：`{name1: value1, name2: value2}`格式的字典
  * `cookies().as_json()`：json 格式的字符串


说明
`as_str()`和`as_dict()`都只会保留`'name'`和`'value'`字段。
**示例：**
```
from DrissionPage import SessionPagepage = SessionPage()page.get('http://www.baidu.com')page.get('http://gitee.com')for i in page.cookies(all_domains=True):print(i)
```

**输出：**
```
{'name': 'BDORZ', 'value': '27875', 'domain': '.baidu.com'}{'name': 'BEC', 'value': '1f1759dfh65j65j5j4feb0357', 'domain': 'gitee.com'}
```

## ✅️️ 内嵌对象[​](https://www.drissionpage.cn/SessionPage/get_page_info#️️-内嵌对象 "✅️️ 内嵌对象的直接链接")
### 📌 `session`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-session "-session的直接链接")
此属性返回当前页面对象使用的`Session`对象。
**类型：**`Session`
### 📌 `response`[​](https://www.drissionpage.cn/SessionPage/get_page_info#-response "-response的直接链接")
此属性为请求网页后生成的`Response`对象，本库没实现的功能可直接获取此属性调用 requests 库的原生功能。
**类型：**`Response`
```
# 打印连接状态r = page.responseprint(r.status_code)
```

[上一页🛩️ 访问网页](https://www.drissionpage.cn/SessionPage/visit)[下一页🛩️ 查找元素](https://www.drissionpage.cn/SessionPage/get_ele)
  * [✅️️ 页面信息](https://www.drissionpage.cn/SessionPage/get_page_info#️️-页面信息)
    * [📌 `url`](https://www.drissionpage.cn/SessionPage/get_page_info#-url)
    * [📌 `url_available`](https://www.drissionpage.cn/SessionPage/get_page_info#-url_available)
    * [📌 `title`](https://www.drissionpage.cn/SessionPage/get_page_info#-title)
    * [📌 `raw_data`](https://www.drissionpage.cn/SessionPage/get_page_info#-raw_data)
    * [📌 `html`](https://www.drissionpage.cn/SessionPage/get_page_info#-html)
    * [📌 `json`](https://www.drissionpage.cn/SessionPage/get_page_info#-json)
    * [📌 `user_agent`](https://www.drissionpage.cn/SessionPage/get_page_info#-user_agent)
  * [✅️️ 运行参数信息](https://www.drissionpage.cn/SessionPage/get_page_info#️️-运行参数信息)
    * [📌 `timeout`](https://www.drissionpage.cn/SessionPage/get_page_info#-timeout)
    * [📌 `retry_times`](https://www.drissionpage.cn/SessionPage/get_page_info#-retry_times)
    * [📌 `retry_interval`](https://www.drissionpage.cn/SessionPage/get_page_info#-retry_interval)
    * [📌 `encoding`](https://www.drissionpage.cn/SessionPage/get_page_info#-encoding)
  * [✅️️ cookies 信息](https://www.drissionpage.cn/SessionPage/get_page_info#️️-cookies-信息)
    * [📌 `cookies()`](https://www.drissionpage.cn/SessionPage/get_page_info#-cookies)
  * [✅️️ 内嵌对象](https://www.drissionpage.cn/SessionPage/get_page_info#️️-内嵌对象)
    * [📌 `session`](https://www.drissionpage.cn/SessionPage/get_page_info#-session)
    * [📌 `response`](https://www.drissionpage.cn/SessionPage/get_page_info#-response)


作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/SessionPage/get_page_info)
  * [QQ群：391178600](https://www.drissionpage.cn/SessionPage/get_page_info)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
