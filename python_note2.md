### 拼接
- pd.contact([a,b],axis=1,join='inner') -> axis=1：横向拼接 ab，inner 表示取交集，即按最小的表来拼接。outer 表示并集，即按最大的表来，小的表缺省值为 NaN。
- pd.contact([a,b],axis=0,ignore_index=True) -> axis=0：纵向拼接 ab，表示横向拼接，ignore_index=True 表示索引重排序，false 表示索引按各表原先索引。
- pd.merge(left,right,how='left(right,outer,inner)',on=['key1','key2']) -> 拼接 left 和 right 两个 datafram 对象，拼接方法是对列标签 key1 和 key2 的匹配，有四种操纵方法：1. left 保留 left 全部，匹配 right。2. right同理。 3. inner 取 key1 和 key2 标签下的值的交集。3. outer 取并集。[link](https://blog.csdn.net/brucewong0516/article/details/82707492)
### 双层索引
- 单层索引的 DataFrame 对象变双层索引 -> x.set_index(['key1','key2'])，将 key1 列和 key2 变为索引。
### 统计缺失值
- np.sum(x.isnull()) -> pandas 中 isnull 可以给出 DataFrame 对象每个元素是否为缺失值，再用 numpy 的 sum 统计。
### 排序
- x.sort_values('key',ascending=True,inplace=True) -> 将 key 列进行升序排列，并作用在元数据上。
- x.reset_index(drop=True,inplace=True) -> 将索引重排。
### 分组聚合
- x.groupby('key').mean() -> 按 key 的值进行分组。分组后可以调用方法 mean。
- x.groupby('key').agg([np.mean,np.max]) -> 按 key 的值进行分组。分组后可以调用方法 mean 和 max。