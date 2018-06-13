#### 使用方法

1) 启动python3

   docker-compose up -d

2) 进入python3
  
   docker-compose exec python3 /bin/sh

3) 安装python其它包

   编辑Dockerfile，使用RUN pip install xxx 来安装其它python包
   
    
