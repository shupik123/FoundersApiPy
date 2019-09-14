# FoundersApiPy
A small package for the [Founders API](https://github.com/Xeladarocks/founders-api) access made into a python package!

## Index:
- [Package](https://github.com/shupik123/FoundersApiPy#Package)
- [Sub Packages](https://github.com/shupik123/FoundersApiPy#sub-packages)
  - [user](https://github.com/shupik123/FoundersApiPy#user)
  - [server](https://github.com/shupik123/FoundersApiPy#server)
  - [status](https://github.com/shupik123/FoundersApiPy#status)
- [Classes](https://github.com/shupik123/FoundersApiPy#Classes)
  - [user_info](https://github.com/shupik123/FoundersApiPy#user_info)
  - [server_info](https://github.com/shupik123/FoundersApiPy#server_info)
  - [status_info](https://github.com/shupik123/FoundersApiPy#status_info)

## Package:

`import founders`


## Sub Packages:


### user:

`founders.user.info(id)`: returns a [user_info](https://github.com/shupik123/FoundersApiPy#user_info) class based on user id input.

`founderse.user.all()`: returns a dictionary of all users in the form of `{username: id, username: id...}`.


### server:

`founders.server.info(id)`: returns a [server_info](https://github.com/shupik123/FoundersApiPy#server_info) class based on server id input.

`founders.server.all()`: returns a dictionary of all servers in the form of `{server_name: id, server_name: id...}`.


### status:

`founders.status.stat(id)`: returns a [status_info](https://github.com/shupik123/FoundersApiPy#status_info) class based on server id input.


## Classes:

### user_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!

`self.username`: username of user.

`self.rank`: rank of user.

`self.servers`: servers user has access to.

`self.lastSeen`: time when user was last on in unix epoch time

`self.created`: time when user account was created in unix epoch time

### server_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!

`self.domain`: The domain name of the server; Ex: *hypixel.net*.

`self.ip`: The ip adress of the server, Ex: 172.65.128.70

`self.port`: The port of the server (by default and usually 25565).

`self.name`: The name of the server in the [Founders Server Board](http://m.founders.gg/); Ex: Hypixel

`self.mRam`: Minimum [ram allocated](https://minecraft.gamepedia.com/Tutorials/Setting_up_a_server) to the server.

`self.xRam`: Maximum [ram allocated](https://minecraft.gamepedia.com/Tutorials/Setting_up_a_server) to the server.

`self.serverJar`: Type of Minecraft [server jar](https://mcversions.net/) often pertaining to the Minecraft version, Ex: spigot-1.14.4.

### status_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!

`self.status`: True/False - whether the server is running or not.

`self.ip`: The ip adress of the server, Ex: 172.65.128.70

`self.port`: The port of the server (by default and usually 25565).