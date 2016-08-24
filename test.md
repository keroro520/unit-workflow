### 链表操作

对于一个双向链表，以伪代码的形式描述插入/删除一个节点的步骤。

节点结构：
```
{
    *prev_pointer,
    *next_pointer,
    value
}
```

1. 链表 `x <--> y` 里插入一个节点 z
2. 链表 `x <--> y <--> z` 删除节点 y


### 最近的巨人

巨人们很在意自己的身高。现 N 个巨人排成一列，已知第 i 个巨人高度为 H[i]。
要求：对于每一个巨人 i，输出距离第 i 个巨人最近的、且比 H[i] 高的巨人的位置 j，若巨人 i 是最高的，则输出 i 本身。

  * N <= 100000
  * 0 <= H[i] <= 100000000000

  * 示例（序号以 1 起始）：

    Input: N = 6;
           H = [1, 2, 5, 9, 4, 2]
    Output: [2, 3, 4, 4, 4, 5]


### 大文件去重

一个包含 100 亿条 url 的文件（约 400G），这些 url 有可能有重复，要求在有限的硬件资源内将该文件内的 url **去重**。

  * url 长度在 1 至 50 之间
  * 硬件资源：2G 内存、1T 硬盘