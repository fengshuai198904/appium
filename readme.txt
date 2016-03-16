1.data,和case层可以删除，默认是没有的
2.libs下面getcasedata,可以从平台拉数据自动写入data。
也可以不使用这个脚本，手动在data下面添加数据
运行脚本会自动生成data和case层数据
3. 运行libs/readcasedata.py会自动读取data数据 生成具体的case

4. 运行./run.py，会自动跑所有case下面的数据和CI完美结合