# 使用shell脚本编写自动更新仓库脚本

# 移动到您的本地仓库地址
cd /d/studyNote
echo 请输入提示信息：
read submit_information

# 添加缓存区
git add -A

# 查看git状态和提交日记
echo ========git状态=========
git status

# 提交本地仓库
git commit -m $submit_information

# 查看提交日记
echo ========提交日记=========
#git log

# 上传到远程仓库master分之
git push
