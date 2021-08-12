# 辅助麦课安全网课学习

## 更新日志

2021.8.7 修改刷课延迟速度，避免过快导致服务器不认

## 使用方法

浏览器登录账号之后，F12 打开console，运行

```
userData = JSON.parse(localStorage.user)
console.log(`请在命令行运行： python main.py token_mode ${userData.tenantCode} ${userData.userId} ${userData.preUserProjectId} ${userData.token}`)
```

即可在控制台得出需要运行的python命令，里面包含了您的登录信息，请妥善保管，将它复制到cmd内（记得先CD到本项目目录），运行

## 注意事项

- 运行前需要安装`requests`以及`fire`依赖，可以使用`pip`进行安装
