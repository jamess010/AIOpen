FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

COPY web3 ./web3/
COPY tests ./tests/
COPY ens ./ens/

COPY setup.py .
COPY README.md .

RUN pip install -e .[dev]

RUN pip3 install jupyter
RUN jupyter notebook --generate-config
COPY jupyter_notebook_config.py /root/.jupyter/.

WORKDIR /code

EXPOSE 8888

ENTRYPOINT ["jupyter","notebook","--allow-root"]
