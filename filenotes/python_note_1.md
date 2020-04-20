**以下 x 是 dataFrame 对象的实例**
### 1. 读取 csv，excel 到 dataframe
pd.read_csv(r''文件路径',encoding='utf-8')
pd.read_excel(r''文件路径',encoding='utf-8',sheet_name='哪张表')
### 2. dataframe保存到csv，excel
实例.to_csv(r''文件路径',encoding='utf-8',index=False(不写入索引))
实例.to_excel(r''文件路径',encoding='utf-8',index=False(不写入索引))
### 3. DataFrame 数据筛选
#### a). loc 方法 （传递的index和column是索引和列的标签）
- x.loc[index,column] -> 取出索引是 index，列是 colum 的元素。
- x.loc[index,:] -> 取出索引是 index 行的所用元素。
- x.loc[:,column] -> 取出列是 colum 行的所用元素。
- x.loc[:,column1:column2] -> 取出列是 colum1 到 colum2 的所用元素。
- x.loc[index1:index2,:] -> 取出索引是 index1 到 index2 的所用元素。
- x.loc[:,[column1,column2]] -> 取出列是 colum1 和 colum2 的所用元素。
- x.loc[[index1,index2],:] -> 取出索引是 index1 和 index2 的所用元素。
#### b). iloc 方法 （传递的 index 和 column 是索引和列的值，用法与 loc 相同）
#### c). 直接对 dataFrame 操作选取数据
- x[a:b] -> 选取从 index a 开始向下的 b 行
- x['column_x'] -> 选取 column 名为 column_x 的那一列
- x[['column_x','column_y','column_z']] -> 选取 column 名为 column_x, column_z, column_z 的那三列
- x[['column_x','column_y','column_z']][a:b] -> 先选 xyz 列，再选 a 到 b 行。（**这里不能对列进行切片，没有[column_x':'column_y]，要切片就用loc 函数**）
#### 4. 条件查询
- x[(x['column_x']==a)&&(x['column_y']>b)] -> 选出 column_x 列为 a，并且 column_y 列大于 b 的所有数据。
- between 方法 -> x['column_x'].between(a,b,inclusive=True)，返回一个由布尔值组成的 series，ab 之间为 True，否则为 False。between 方法给出的判断同样可用来筛选，同上。
- isin 方法 -> x['column_x'].isin([list])，返回一个由布尔值组成的 series，column_x 列的值如果在列表 list 中，值为 True，否则为 False。isin 方法给出的判断同样可用来筛选，同上。
- str.contains 方法 -> x['column_x'].str.contains('m')，返回一个由布尔值组成的 series，column_x 列的值(string 型)如果包含字符 m，值为 True，否则为 False。str.contains 方法给出的判断同样可用来筛选，同上。
#### 5. 增删
- x['new']='new' -> 增加一列标签为new，元素为 new 的列。
- drop 方法 -> x.drop('tag',axis=1,inplace = True)，axis = 1 表示沿行行进遍历列标签，如果找到列标签为 tag 的列，删除。同理，如果 axis = 0 表示沿列行进遍历行标签，如果找到行标签为 tag 的行，删除。inplace = True 表示修改 x，False 则表示不修改。
- insert 方法 -> x.insert(a,'name',series) -> 将 series 插入到第 a 列，列名为 name。
- rename 方法 -> x.rename(index/columns={'bef':'aft'},inplace=True)，把行/列名 bef 改为 aft。