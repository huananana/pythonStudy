关于启动远程服务器中redis和MySQL服务出现的问题



初学时，很多知识学了结尾忘了开头，今天列出一些关于启动远程服务自己犯的低级错误，

关于服务器上的服务和进程









---

管道操作：杀指定的所有进程

   `ps -ef | grep "redis-server" | grep -v "grep" | awk '{print $2}' | xargs kill`

`ps -ef `- 查看所有进程的部分信息

`grep "redis-server"` - 选择进程名中包含”redis-server“的进程

`grep -v "grep"` - 移除含有grep进程名的进程

`awk '{print $2}'` - 选择输出的第二列

`xargs kill` - 将输出转置，杀死所有输出的进程

---

