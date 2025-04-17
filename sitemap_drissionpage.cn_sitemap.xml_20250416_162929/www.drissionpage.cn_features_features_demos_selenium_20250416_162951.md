# Content from: https://www.drissionpage.cn/features/features_demos/selenium

[跳到主要内容](https://www.drissionpage.cn/features/features_demos/selenium#__docusaurus_skipToContent_fallback)
支持开源作者，请关闭广告屏蔽功能。当前文档适用于：DrissionPage **4.1.0.18**
[![DrissionPage](https://www.drissionpage.cn/img/color_logo.png)**DrissionPage**](https://www.drissionpage.cn/)[特性](https://www.drissionpage.cn/features/4.1)[入门](https://www.drissionpage.cn/get_start/installation)[文档](https://www.drissionpage.cn/browser_control/intro)[教程](https://www.drissionpage.cn/tutorials/xingqiu)[进度](https://www.drissionpage.cn/versions/4.1.x)[支持](https://www.drissionpage.cn/support)
[更多作品](https://www.drissionpage.cn/features/features_demos/selenium)
  * [DataRecorder](https://drissionpage.cn/DataRecorderDocs)
  * [DownloadKit](https://drissionpage.cn/DownloadKitDocs)
  * [TimePinner](https://drissionpage.cn/TimePinnerDocs)
  * [MixPage](https://drissionpage.cn/MixPageDocs)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)


[项目地址](https://www.drissionpage.cn/features/features_demos/selenium)
  * [Gitee](https://gitee.com/g1879/DrissionPage)
  * [GitHub](https://github.com/g1879/DrissionPage)
  * [GitCode](https://gitcode.com/g1879/DrissionPage)


搜索`K`
  * [🔥 新版本介绍](https://www.drissionpage.cn/features/features_demos/selenium)
  * [💖 特性](https://www.drissionpage.cn/features/)
  * [🌟 特性演示](https://www.drissionpage.cn/features/features_demos/selenium)
    * [⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)
    * [⭐ 与 selenium 对比](https://www.drissionpage.cn/features/features_demos/selenium)
    * [⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)
    * [⭐ 获取元素属性](https://www.drissionpage.cn/features/features_demos/get_ele_attr)
    * [⭐ 下载文件](https://www.drissionpage.cn/features/features_demos/download)


  * [](https://www.drissionpage.cn/)
  * 🌟 特性演示
  * ⭐ 与 selenium 对比


# ⭐ 与 selenium 对比
以下代码实现一模一样的功能，对比两者的代码量：
🔸 用显性等待方式查找第一个文本包含 some text 的元素。
```
# 使用 selenium：element = WebDriverWait(driver).until(ec.presence_of_element_located((By.XPATH,'//*[contains(text(), "some text")]')))# 使用 DrissionPage：element = tab('some text')
```

🔸 跳转到一个标签页
```
# 使用 selenium：driver.switch_to.window(driver.window_handles[0])# 使用 DrissionPage：tab = browser.latest_tab
```

🔸 按文本选择下拉列表
```
# 使用 selenium：from selenium.webdriver.support.select import Selectselect_element = Select(element)select_element.select_by_visible_text('text')# 使用 DrissionPage：element.select('text')
```

🔸 拖拽一个元素
```
# 使用 selenium：ActionChains(driver).drag_and_drop(ele1, ele2).perform()# 使用 DrissionPage：ele1.drag_to(ele2)
```

🔸 滚动窗口到底部（保持水平滚动条不变）
```
# 使用 selenium：driver.execute_script("window.scrollTo(document.documentElement.scrollLeft, document.body.scrollHeight);")# 使用 DrissionPage：tab.scroll.to_bottom()
```

🔸 设置 headless 模式
```
# 使用 selenium：options = webdriver.ChromeOptions()options.add_argument("--headless")# 使用 DrissionPage：options = ChromiumOptions().headless()
```

🔸 获取伪元素内容
```
# 使用 selenium：text = webdriver.execute_script('return window.getComputedStyle(arguments[0], "::after").getPropertyValue("content");', element)# 使用 DrissionPage：text = element.pseudo.after
```

🔸 获取 shadow-root
新版 selenium 已可直接获取 shadow-root，但生成的 ShadowRoot 对象功能实在是太少了。
```
# 使用 selenium：shadow_element = webdriver.execute_script('return arguments[0].shadowRoot', element)# 使用 DrissionPage：shadow_element = element.sr
```

🔸 用 xpath 直接获取属性或文本节点（返回文本）
```
# 使用 selenium：相当复杂# 使用 DrissionPage：class_name = element('xpath://div[@id="div_id"]/@class')text = element('xpath://div[@id="div_id"]/text()[2]')
```

[上一页⭐ 与 requests 对比](https://www.drissionpage.cn/features/features_demos/requests)[下一页⭐ 模式切换](https://www.drissionpage.cn/features/features_demos/change_mode)
作者
  * [g1879](https://gitee.com/g1879)


交流
  * [联系邮箱：g1879@qq.com](https://www.drissionpage.cn/features/features_demos/selenium)
  * [QQ群：391178600](https://www.drissionpage.cn/features/features_demos/selenium)


旧版地址
  * [4.0 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12020073&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [3.2 版文档](https://mall.bilibili.com/neul-next/detailuniversal/detail.html?isMerchant=1&page=detailuniversal_detail&saleType=10&itemsId=12019346&loadingShow=1&noTitleBar=1&msource=merchant_share)
  * [MixPage](https://DrissionPage.cn/mixpagedocs)


本文档禁止商用 [DrissionPageDocs](https://drissionpage.cn) by g1879 is licensed under [CC BY-NC 4.0](http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1)
DrissionPage®为作者已注册的商标 [粤ICP备2024179482号-1](https://beian.miit.gov.cn/).
