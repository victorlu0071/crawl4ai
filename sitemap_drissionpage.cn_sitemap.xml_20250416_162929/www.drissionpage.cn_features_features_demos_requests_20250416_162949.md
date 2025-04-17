# Content from: https://www.drissionpage.cn/features/features_demos/requests

[跳到主要内容](https://www.drissionpage.cn/features/features_demos/requests#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/features_demos/requests)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/features_demos/requests)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/features_demos/requests)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/features_demos/requests)
    * [⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)
    * [⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)
    * [⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)
    * [⭐ 获取元素属性](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
    * [⭐ 下载文件](https://www.drissionpage.cn/features/features_demos/download)


  * [](https://www.drissionpage.cn/)
  * 🌟 特性演示
  * ⭐ 与 requests 对比


# ⭐ 与 requests 对比
以下代码实现一模一样的功能，对比两者的代码量：
🔸 获取元素内容
```
url ='https://baike.baidu.com/item/python'# 使用 requests：import requestsfrom lxml import etreeheaders ={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}response = requests.get(url, headers = headers)html = etree.HTML(response.text)element = html.xpath('//h1')[0]title = element.text# 使用 DrissionPage：from DrissionPage import SessionPagepage = SessionPage()page.get(url)title = page('tag:h1').text
```

Tips
DrissionPage 自带默认 headers
🔸 下载文件
```
url ='https://www.baidu.com/img/flexible/logo/pc/result.png'save_path =r'C:\download'# 使用 requests：import requestsr = requests.get(url)withopen(f'{save_path}\\img.png','wb')as fd:for chunk in r.iter_content():    fd.write(chunk)# 使用 DrissionPage：from DrissionPage import SessionPagepage = SessionPage()page.download(url, save_path,'img')# 支持重命名，处理文件名冲突
```

[上一页💖 特性](https://www.drissionpage.cn/features/)[下一页⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/features_demos/requests)
  * [QQ群：391178600](https://www.drissionpage.cn/features/features_demos/requests)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
