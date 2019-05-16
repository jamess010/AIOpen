FROM ufoym/deepo:cpu

#RUN apt update
RUN pip3 install --upgrade pip
RUN pip3 install jupyter
RUN jupyter notebook --generate-config
COPY jupyter_notebook_config.py /root/.jupyter/.
RUN pip3 install Flask==0.12.2 requests==2.18.4 lxml bs4
RUN pip3 install scrapy
RUN apt update && \
    apt install -y openssh-server &&\
    apt install -y net-tools &&\
    apt install -y ffmpeg 
RUN echo 'root:test' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo "export VISIBLE=now" >> /etc/profile
ADD run.sh /
RUN mkdir /var/run/sshd
RUN mkdir -p /home/src
RUN apt install -y tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN pip3 install flask_socketio msgpack_numpy socketIO_client jupytext librosa
#CMD ["/run.sh"]
