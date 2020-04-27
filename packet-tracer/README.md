## Networks demo ##

### Router: Set ip address ###
```
enable
configure terminal
interface fastethernet0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
```


### Router Security ###
Set password for enable command:
```
enable
configure terminal
hostname R1
enable secret cisco
exit
exit
```

Set username and password:
```
enable # put password above
configure terminal
username cisco privilege 15 password cisco # 15 is the most hight
```

Allow input Telnet
```
enable
configure terminal
line vty 0 4
transport input telnet
?
login local
exit
```

Optional:
```
line console 0
login local
no login local # inverse, to put off
exit
```

Show configuration
```
show run
copy run startup
```

Connect to Router by telnet
```
telnet 192.168.1.1
put credentials
```
