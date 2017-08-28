# nginx_cache_clear
clear nginx proxy cache
1.根据proxy_cache_key     proxy_cache_path来计算cache位置，清理cache
2.参数 -p --path          cache 路径
3.参数 -u --url           需清理缓存url 
4.参数 -m --method        请求方法get/head 等 默认GET
5.参数 -s --strategy      缓存策略自定义策略   默认是jfnewclear


