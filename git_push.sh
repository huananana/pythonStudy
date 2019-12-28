# 使用shell脚本编写自动更新仓库脚本
echo ==============shell脚本自动更新仓库==============
echo 
# 移动到您的本地仓库地址
cd "$(pwd)"
echo 本地仓库地址: $(pwd)

echo 输入提交信息：
read submit_information
# 添加缓存区
git add -A

# 查看git状态和提交日记
echo --->git状态
git status

# 提交本地仓库
git commit -m $submit_information

# 上传到远程仓库master分之
git push
