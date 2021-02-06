Tool `sc-server` is implementation of storage that supports network connections by using [sctp protocol](../net/sctp.md).

## Configuration file

```ini
[storage]
config_path = <Path to sc-storage configuration file>
# sc-machine/bin/extensions
ext_path = <Path to sc-memory extensions>
# Default: `repo`
repo_path = <Path to knowledge base> 
# flag to clear sc-memory on start. Default: `false`
clear = <true|false> 

[server]
# default `localhost`
host = <address of host>
# default `55770`
port = <port number>
# number of threads to process client connections. Default `0` - number of CPU cores
threads = <number>

```