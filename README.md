# FoundersApiPy
A small repo of the Founders API access made into a python package!


### Import:

`import founders`


### Sub Packages:


#### founders.user:

`founders.user.info(id)`: returns a [user_info](https://github.com/shupik123/FoundersApiPy/blob/master/README.md#user_info) class based on user id input.

`founderse.user.all()`: returns a dictionary of all users in the form of `{username: id, username: id...}`.


#### founders.server:

`founders.server.info(id)`: returns a [server_info](https://github.com/shupik123/FoundersApiPy/blob/master/README.md#server_info) class based on server id input.

`founders.server.all()`: returns a dictionary of all servers in the form of `{server_name: id, server_name: id...}`.


#### founders.status:

`founders.status.stat(id)`: returns a [status_info](https://github.com/shupik123/FoundersApiPy/blob/master/README.md#status_info) class based on server id input.


### Classes:

#### user_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!

`self.username`: username of user.

`self.rank`: rank of user.

`self.servers`: servers user has access to.

`self.lastSeen`: time when user was last on in unix epoch time

`self.created`: time when user account was created in unix epoch time

#### server_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!

#### status_info:

`self.success`: True/False - whether information was obtained. This should always be checked before using information!
