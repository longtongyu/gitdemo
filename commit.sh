#!/bin/bash

# Django项目代码提交脚本
# 使用方法: ./commit.sh "提交说明"

if [ $# -eq 0 ]; then
    echo "请提供提交说明"
    echo "使用方法: ./commit.sh \"提交说明\""
    exit 1
fi

commit_message="$1"

echo "开始提交代码..."
echo "提交说明: $commit_message"

# 添加所有更改
git add .

# 提交代码
git commit -m "$commit_message"

# 推送到远程仓库
git push origin master

echo "代码提交完成！"
echo "远程仓库: https://github.com/longtongyu/gitdemo.git" 