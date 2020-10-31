# inkust_proxy



For [NKUST-AP-Flutter](https://github.com/NKUST-ITC/NKUST-AP-Flutter) Web version



這是一個類似Proxy的Proxy 

市面上的Proxy大多沒辦法設定CORS or TLS/SSL(to Public)

Nginx也沒辦法反向代理Proxy(硬要是可以)，不是很方便調整細部設定



折騰在Nginx上在做Proxy ，不如一個小服務轉發我需要的Proxy 



## Docker



```bash
docker build -t inkust_proxy . --no-cache

docker run -d -p 8050:8050 inkust_proxy
```


