# 使用shell脚本编写自动更新仓库脚本
echo ==============shell脚本一键更新仓库==============
echo 任意键启动更新
read
echo 

# 移动到您的本地仓库地址
cd "$(pwd)"
echo 本地仓库地址: $(pwd)
echo 请输入提交信息：
read submit_information
echo ==============华丽分割线==============

# 添加缓存区
git add -A
echo ==============华丽分割线==============
echo 完成添加缓存
read

# 提交本地仓库
git commit -m $submit_information
echo ==============华丽分割线==============
echo 完成提交本地仓库
echo 上传到远程仓库master分之

# 上传远程仓库
git push
echo 完成更新，任意键退出
read
