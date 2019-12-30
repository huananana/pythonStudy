# 使用shell脚本编写自动更新仓库脚本
echo ==============shell脚本一键更新仓库==============
echo 
# 移动到您的本地仓库地址
cd "$(pwd)"
echo 本地仓库地址: $(pwd)

echo 输入提交信息：
read submit_information
echo ==============华丽分割线==============
# 添加缓存区
git add -A
echo ==============华丽分割线==============

read a
# 提交本地仓库
git commit -m $submit_information
echo ==============华丽分割线==============
# 上传到远程仓库master分之
git push
