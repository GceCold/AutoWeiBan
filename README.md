# 辅助麦课安全网课学习

## 下载

[点击进入下载页](https://gitee.com/WeiYuanStudio/AutoWeiBan/releases)

## 使用方法

浏览器登录账号之后，F12 打开console，运行

```
userData = JSON.parse(localStorage.user)
console.log(`请在命令行运行： python main.py token_mode ${userData.tenantCode} ${userData.userId} ${userData.preUserProjectId} ${userData.token}`)
```

即可在控制台得出需要运行的python命令，里面包含了您的登录信息，请妥善保管，将它复制到cmd内（记得先CD到项目目录），运行
