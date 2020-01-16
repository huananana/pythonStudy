#git指令  

######本地指令

`git init ` - 新建git仓库      
`git add 文件/文件夹` - 将文件添加到缓存区中  
`git add -A` - 添加所有内容到缓存区中
`git status` -  查看git状态  
`git commit -m  ‘提交信息’`  -  将缓存区中的内容全部提交到git本地仓库中  
`git log` - 查看提交日志  
`git reset --hard HEAD`  -  让工作目录中的内容和仓库中的内容保持一致  
`git reset --hard HEAD^` - 回到上一个版本  
`git  reset  -- hard 版本号` - 回到指定的版本  
`git tag v0.1` - 给当前版本添加版本标签
`git checkout  文件名` -  从暂存区中恢复工作目录中的内容(让工作区中的指定文件，回到上次提交的时候的状态)  



######远程指令

`git clone <url> ` - 克隆 

`git remote add origin 地址` - 关联远程仓库

`git push -u origin master` - 上传

`git push`- 将本地仓库的内容提交到远程仓库master分支上

`git push origin 分支名` -  将本地仓库的内容提交到远程仓库对应的分支上, 如果分支不存在会自动创建

`git pull` - 将远程仓库中的内容更新到本地仓库和工作区中



###### 分之管理    
`git branch`  - 查看分之   
`git branch 分之名` - 创建分之   
`git checkout   分支名` -   切换分之      
`git checkout -b 分之名` - 切换并创建新的分之   
`git diff 分之1  分之2` - 查看两个分之之间的差异  
`git merge 分之名	` - 让当前分之和指定分之进行合并     





注意: 切换分之、push、pull，这些操作前要保证工作区是clean 

怎么避免冲突：  不要发生多个分之对同一个文件在同一个版本下进行修改(和同伴确认和商量)



