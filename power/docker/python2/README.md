#### 使用方法

1) 启动python2

   docker-compose up -d

2) 进入python2
  
   docker-compose exec python2 /bin/sh

3) 安装python其它包

   在Dockerfile中，使用RUN pip install xxx 来安装其它python包
   
    
