date=$(date)

file_name=Y${date:2:2}-${date:5:2}-${date:8:2}.md
echo file_name $file_name

fileTime=$(ls | grep "Y[0-9]\{2\}-[0-9]\{2\}-[0-9]\{2\}")
fileLen=`expr ${#fileTime} - ${#file_name}`
echo $fileLen

end=${fileTime:$fileLen}
echo end $end

if [ $end = $file_name ]
then
	echo 文件已存在
else
	touch $file_name
fi

