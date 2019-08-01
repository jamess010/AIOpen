FROM python:3.6

# Set up code directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install Linux dependencies
RUN apt-get update && apt-get install -y libssl-dev

# git clone https://github.com/ethereum/web3.py

COPY ./web3.py/web3 ./web3/
COPY ./web3.py/tests ./tests/
COPY ./web3.py/ens ./ens/
COPY ./web3.py/setup.py .
COPY ./web3.py/README.md .

RUN pip install -e .[dev]

RUN pip3 install jupyter
RUN jupyter notebook --generate-config
COPY jupyter_notebook_config.py /root/.jupyter/.

RUN python -m solc.install v0.4.25

RUN ln -s /root/.py-solc/solc-v0.4.25/bin/solc /usr/local/bin/solc

WORKDIR /code

EXPOSE 8888

ENTRYPOINT ["jupyter","notebook","--allow-root"]
