### 读取csv，excel到dataframe
```
pd.read_csv(r''文件路径',encoding='utf-8')
pd.read_excel(r''文件路径',encoding='utf-8',sheet_name='哪张表')
```

### dataframe保存到csv，excel
```
实例.to_csv(r''文件路径',encoding='utf-8',index=False(不写入索引))
实例.to_excel(r''文件路径',encoding='utf-8',index=False(不写入索引))
```


### DataFrame 数据筛选
#### loc 方法 （传递的index和column是索引和列的标签）
- DataFram.loc[index,column] -> 取出索引是index，列是colum的元素。
- DataFram.loc[index,:] -> 取出索引是index行的所用元素。
- DataFram.loc[:,column] -> 取出列是colum行的所用元素。
- DataFram.loc[:,column1:column2]-> 取出列是colum1到colum2的所用元素。
- DataFram.loc[index1:index2,:]-> 取出索引是index1到index2的所用元素。
- DataFram.loc[:,[column1,column2]]-> 取出列是colum1和colum2的所用元素。
- DataFram.loc[[index1,index2],:]-> 取出索引是index1和index2的所用元素。
#### iloc 方法 （传递的index和column是索引和列的值，用法与 loc 相同）
- 