# ivideo的在线简单接口版本
## 线路资源路径

```python
vip_json = "https://iodefog.github.io/text/mviplistmm.json"
```
## 框架选型：starlette
没有选用Kenneth Reiz的responder。

## 部署 leancloud
leancloud 只支持wsgi的部署，Python2 的flask框架会方便很多 
参考branch： [lean2](https://github.com/lai-bluejay/vipeo-starlette/tree/lean2)。
参考文档：[lean2-README.md](https://github.com/lai-bluejay/vipeo-starlette/blob/lean2/README.1.md)

