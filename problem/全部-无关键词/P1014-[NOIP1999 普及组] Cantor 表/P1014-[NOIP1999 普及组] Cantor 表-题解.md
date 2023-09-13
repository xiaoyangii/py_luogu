window._feInjection = JSON.parse(decodeURIComponent("{"code":200,"currentTemplate":"ProblemSolution","currentData":{"solutions":{"result":[{"content":"###  现在是扯淡时间：
 这是本蒟蒻第一次发题解，那么我这么垃圾为什么还要发题解呢
 
~~其实是我看这道题实在是太简单了，居然出现在BOSS区~~

其实是因为我看题解里的**大佬**实在是太**大佬**了，想找一个简单的办法解决这个问题


$update$ : 我写这篇题解也差不多快一年了，中间有很多评论我都没有回复，现在统一更新一下。首先声明一下，我写这篇题解的时候，刚入门，以为$AK$新手村已经很不错了，所以这话说的特别蠢（逃），而且似乎试炼场会被在不久的将来撤下，那这个话的起源都不知道去哪里了$233$.


------------

### 好了，扯淡扯完了
可以恢复正题了（我觉得我这个程序应该是题解里最短的了（小声BB））

$update$:显然这样的程序并不是最短的，评论已经有很多的$dalao$指出了，而且时间复杂度也并不优秀，但是当时就会有一种~~莫名的自信~~ 至于怎么压行，评论区也说得比较明白了，所以评论不用再提供压行思路了

废话不多说，先上代码
```cpp
#include 
using namespace std; 
int main() {
	int n,k=1;
	cin>>n;
	while (n>k) {
		n=n-k;
		k++;
	}
	if(k%2==0) cout<<n<<"\/"<<(k+1-n);
	else cout<<k+1-n<<"\/"<<n;
	return 0;
} 
```

（从这一行往下全是$update$）

$update$: 首先我们观察到第$i$行，第$j$列的数就是$i\/j$,这是第一个要发现的。

因为题目中要求是以$Z$字型编号

我们看题目中的表是：

$1\/1,1\/2,1\/3$ ……

$2\/1,2\/2,2\/3$ ……

$Z$字型编号以后（把头向左偏45度）：

第一行：$1\/1$  ($1$号)

第二行：$1\/2$ ($2$号)  $2\/1$($3$号)

第三行：$1\/3$ **($6$号)**  $2\/2$ **($5$号)** $3\/1$ **($4$号)**  

$\uparrow$ 观察法易得每一行比上一行多1

代码里那个$while$循环，就是为了通过循环枚举，判断它在编号之后的第几行，第几个位置。



------------
（这个优化有没有都可以$AC$本题，但是评论指出我的时间复杂度不够优秀，因此提一提这个优化，不愿意看的可以直接略过看下一个分割线以后的内容。）

但其实可以直接出结论优化时间复杂度从$O(n)$ 优化到$O(1)$，这样就要考虑到等差数列求和

公式：$S=\frac{n(a_n+a_1)}{2}$

所以，很显然$Z$字型排序之后，第$k$行的数编号$n$满足：

$\frac{k(k-1)}{2} < n \le \frac{k(k+1)}{2}$

这样就可以把那个循环优化掉。代码就不贴了 ~~（因为懒，还怕出错）~~

------------


但当时我才刚学，没想到上面的这个优化（罪恶之源：我太蒻了），只好写了个丑陋的模拟233。

代码当中$k$用来记$Z$字型编号之后的行数，显然第$k$行有$k$个数，因此每次$n$要减去$k$。

最后用$k$判断奇偶，是判断这一行$Z$字型编号是正序（类似第二行）还是倒序（类似第三行）然后用最开始的结论输出原表中的行号除以列号就行了



最后，我只想表达一下自己那么蒟蒻在这里发题解的愧意

还有有问题的话大佬一定要指出！！（害怕）","type":"题解","status":2,"postTime":1544971248,"author":{"uid":121369,"name":"哦哟筷子","slogan":"梦魂惯得无拘检，又踏杨花过谢桥。","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":"https:\/\/cdn.luogu.com.cn\/upload\/image_hosting\/pm7zoiyp.png"},"thumbUp":549,"commentCount":204,"currentUserVoteType":0,"contentDescription":"现在是扯淡时间：
这是本蒟蒻第一次发题解，那么我这么垃圾为什么还要发题解呢
其实是我看这道题实在是太简单了，居然出现在BOSS区
其实是因为我看题解里的大佬实在是太大佬了，想找一个简单的办法解决...","id":96840,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"算法1：模拟，按题意一个个枚举

时间复杂度O(n),可以通过本题n≤10^7


算法2：发现Z字形的每条斜线可以快速枚举，即枚举

1\/1 , 1\/2 , 3\/1 , 1\/4 , 5\/1 , 1\/6……找到要求的第n项所在斜线，再一个个枚举或计算得出答案

时间复杂度O(√n),可以通过n≤10^14

算法2.5：枚举第n项在哪一行，计算得出答案，比算法2好写,

时间复杂度同算法2


算法3：发现第i条斜线（即分子分母之和=i+1的所有项）中包含i\*(i-1)\/2+1至i\*(i+1)中的每一项，所以可以二分分子分母之和，再根据分子分母之和的奇偶性直接计算第n项

时间复杂度O(㏒₂n),可以通过n≤10^18,加上高精可通过n≤10^1000

二分参考代码：

```cpp
    #include
    #include
    using namespace std;
    int main(){
        long long l=1,r,mid,n,a;
        cin>>n;
        r=n;
        while(l<r){
            mid=(l+r)\/2;
            if(mid*(mid+1)\/2<n)l=mid+1;
            else r=mid;
        }
        a=n-l*(l-1)\/2;
        if(l%2==0)cout<<a<<'\/'<<l+1-a;
        else cout<<l+1-a<<'\/'<<a;
        return 0;
}
```","type":"题解","status":2,"postTime":1512875615,"author":{"uid":35406,"name":"「已注销」","slogan":"这个家伙很弱，什么也没有留下","badge":null,"isAdmin":false,"isBanned":false,"color":"Orange","ccfLevel":7,"background":"https:\/\/cdn.luogu.com.cn\/upload\/image_hosting\/8u20dytw.png"},"thumbUp":269,"commentCount":91,"currentUserVoteType":0,"contentDescription":"算法1：模拟，按题意一个个枚举
时间复杂度O(n),可以通过本题n≤10^7
算法2：发现Z字形的每条斜线可以快速枚举，即枚举
1\/1 , 1\/2 , 3\/1 , 1\/4 , 5\/1 , 1\/6...","id":17266,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】的几种做法"},{"content":"#P1014 【Cantor表】

------------

####模拟题

**建议在Excel上打出Cantor表，再找规律(还有一个好处是可以用来测试)**

~~如图~~ 如表：

1\/1    1\/2    1\/3    1\/4    1\/5    1\/6    1\/7    1\/8    1\/9

2\/1    2\/2    2\/3    2\/4    2\/5    2\/6    2\/7    2\/8

3\/1    3\/2    3\/3    3\/4    3\/5    3\/6    3\/7

4\/1    4\/2    4\/3    4\/4    4\/5    4\/6

5\/1    5\/2    5\/3    5\/4    5\/5

6\/1    6\/2    6\/3    6\/4

7\/1    7\/2    7\/3

8\/1    8\/2

9\/1

**（普及）在单元格中输入分数前先输入一个单引号，避免被判断为日期**


```cpp
    #include
    int main() {
        int n, i=0, j=0;\/\/前i条斜线一共j个数
        scanf("%d", &n);
        while(n>j) {\/\/找到最小的i使得j>=n
            i++;
            j+=i;
        }
        if(i%2==1)
            printf("%d\/%d",j-n+1,i+n-j);\/\/i的奇偶决定着斜线上数的顺序,n是第i条斜线上倒数第j-n+1个数
        else
            printf("%d\/%d",i+n-j,j-n+1);\/\/若i是偶数，第i条斜线上倒数第i个元素是(i+1-i)\/i
        return 0;
}
```","type":"题解","status":2,"postTime":1513151726,"author":{"uid":58502,"name":"char32_t","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":""},"thumbUp":256,"commentCount":108,"currentUserVoteType":0,"contentDescription":"P1014 【Cantor表】

模拟题
建议在Excel上打出Cantor表，再找规律(还有一个好处是可以用来测试)
如图 如表：
1\/1    1\/2    1\/3    1\/4    1\/...","id":17978,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"\/\*
找规律

第1层1\/1

第2层1\/2 2\/1

第3层3\/1 2\/2 1\/3

第4层1\/4 2\/3 3\/2 4\/1

第5层5\/1 4\/2 3\/3 2\/4 1\/5

\*\/
```cpp
#include
int main()
{
    int n;scanf("%d",&n);
    int t=1,ans=0;\/\/t是表示下一次跳到下一次的距离，ans是表示第几层
    while(1)
    {
        if(n>t){n-=t;ans++;t++;}\/\/printf("%d\n",ans);
        else if(n==t&&ans%2==0){printf("1\/%d",ans+1);break;}
        \/\/如果在n==t，并且为偶数层，就在第一行 第ans+1个 
        else if(n==t&&ans%2!=0){printf("%d\/1",ans+1);break;}
        \/\/如果在n==t，并且为奇数层，就在第ans+1行 第一个
        else if(n<t&&ans%2!=0){printf("%d\/%d",ans+n-t+1,t-n+1);break;}
        \/\/如果在n<t，并且为奇数层，t-n+1表示该层最后一个往后走n-1步，ans+n-t+1示该层最后一个往上走t-1步 
        else if(n<t&&ans%2==0){printf("%d\/%d",t-n+1,ans+n-t+1);break;}
        \/\/ 如果在n<t，并且为偶数层，t-n+1表示该层最后一个往上走n-1步，ans+n-t+1示该层最后一个往后走t-1步 
    }
    return 0;
}
```","type":"题解","status":2,"postTime":1512020002,"author":{"uid":35290,"name":"royzhu","slogan":"这个家伙菜得很,什么都没有留下","badge":null,"isAdmin":false,"isBanned":false,"color":"Green","ccfLevel":5,"background":""},"thumbUp":101,"commentCount":62,"currentUserVoteType":0,"contentDescription":"\/*
找规律
第1层1\/1
第2层1\/2 2\/1
第3层3\/1 2\/2 1\/3
第4层1\/4 2\/3 3\/2 4\/1
第5层5\/1 4\/2 3\/3 2\/4 1\/5
*\/
","id":1096,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"虽然说这道题是考**模拟**.但是为啥感觉很多人真的都在写模拟....


这道题应该是属于那种给个数据那台计算器都能手打出结论的题哈.


数据小了都不用计算器都能在初中数学范围之内吧。


很明显就是O(1)复杂度(~~这里忽略系统开根的复杂度~~)，求出Z形侧过来的三角形的行数


然后O(1)复杂度(~~又一次忽略系统乘法的复杂度~~)，算出结果。


以下是公式以及简要的解释


已知数据是第![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20n)个。


明显Z形画出来的三角，从左上到右下的行数是从1开始公差为1的**等差数列**。所以利用**求和公式**，设**行数**为![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20a)的话则有：


![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20%5Cfrac%7Ba%5Ctimes%20%28a-1%29%7D%7B2%7D%3C%20n%5Cle%20%5Cfrac%7B%281&plus;a%29%5Ctimes%20a%7D%7B2%7D)


因此我们 设![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20x)使得



![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20%5Cfrac%7B%281+x%29%5Ctimes%20x%7D%7B2%7D%3Dn)


根据建立起的函数的**递增性**，可知![](http:\/\/latex.codecogs.com\/gif.latex?a%3D%5Clceil%20x%5Crceil)


所以通过**求根公式**求出![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20x)然后**向上取整**就可以在O(1)的时间复杂度求出行数了。


## Which is  ![](http:\/\/latex.codecogs.com\/gif.latex?%5CLARGE%20a%3D%5Clceil%5Cfrac%7B-1&plus;%5Csqrt%7B1&plus;8%5Ctimes%20n%7D%7D%7B2%7D%5Crceil)


接下来，还要求出所在当行的具体位置，这个就很容易了，只需要知道 到![](http:\/\/latex.codecogs.com\/gif.latex?a-1)那一行总共有多少个：明显![](http:\/\/latex.codecogs.com\/gif.latex?%5Cfrac%7Ba%5Ctimes%20%28a-1%29%7D%7B2%7D)个


### 所以要求的也就是![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20a)那一行的第![](http:\/\/latex.codecogs.com\/gif.latex?n-%5Cfrac%7Ba%5Ctimes%20%28a-1%29%7D%7B2%7D)个。


接下来是一个对于知道**行数+第几个**的Cantor形式求法：

对于第a行，中所有个体，都有（“\/”左边）+（“\/”右边）![](http:\/\/latex.codecogs.com\/gif.latex?%5Clarge%20=a+1)


同时 ![](http:\/\/latex.codecogs.com\/gif.latex?%5Cforall%20a%5Cin%20N)，![](http:\/\/latex.codecogs.com\/gif.latex?a%5Cequiv0%28mod%5C%202%29)





### 结果是： (\_第几个\_ )\/(a+1- \_第几个\_ )<\/u>

### 而剩下的则“\/”**两边相反**即好。<\/u>

以上就是O(1)（~~其实应该没比二分快多少，相当于让系统做了二分而已~~）解决此题的详解。既然是数学推算，代码就不贴了，没啥意思。
","type":"题解","status":2,"postTime":1516722277,"author":{"uid":2009,"name":"wmxwmx","slogan":"这个家伙很懒，几乎什么都没留下","badge":null,"isAdmin":false,"isBanned":false,"color":"Green","ccfLevel":4,"background":""},"thumbUp":85,"commentCount":53,"currentUserVoteType":0,"contentDescription":"虽然说这道题是考模拟.但是为啥感觉很多人真的都在写模拟....
这道题应该是属于那种给个数据那台计算器都能手打出结论的题哈.
数据小了都不用计算器都能在初中数学范围之内吧。
很明显就是O(1)复...","id":23133,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"**蒟蒻首发**

~~这个题卡了我三天，用了各种脑残方法最后在~~@八重樱飞（十分感谢）~~的帮助下做了出来~~

~~这个方法真的简单~~

先是找规律

1\/1（第一行）

1\/2 2\/1（第二行）

3\/1 2\/2 1\/3（第三行）

1\/4 2\/3 3\/2 4\/1（第四行）

......

顺着看下来就是规律

注意一下每行的第一个数与层数是有关系的

上代码
```c
#include
using namespace std;
int main(){
	int x,y,h=1,N,k;
    \/\/x是分子，y是分母，h是行数，N是个数，k是 第N个数 与##~~~~ 对应行的第一个数 的距离（别卡在这，先往后看） 
	cin>>N；
	while(N>h){\/\/用循环来算出行数 
	    N=N-h;
	    h++;
	}\/\/很巧的是循环完后 N的值就是 第N个数对应行 的第几个（敲黑板）
	k=N-1;\/\/ 第N个数 与对应行的第一个数 的距离
	if(h%2==0)x=1+k,y=h-k;\/\/判断行数是奇数还是偶数
	\/\/ （奇数：分子减k分母加k，偶数反之） 
	else x=h-k,y=1+k;
	cout<<x<<"\/"<<y;\/\/然后就算出来了 
	return 0;
}
```
祝各位早日AC

~~为什么我打一下回车显示出来只有一个空格~~

~~令人窒息的投稿~~
","type":"题解","status":2,"postTime":1542440094,"author":{"uid":97143,"name":"八个月想一等","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":""},"thumbUp":69,"commentCount":38,"currentUserVoteType":0,"contentDescription":"蒟蒻首发
这个题卡了我三天，用了各种脑残方法最后在@八重樱飞（十分感谢）的帮助下做了出来
这个方法真的简单
先是找规律
1\/1（第一行）
1\/2 2\/1（第二行）
3\/1 2\/2 1\/3（第三行...","id":89722,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"## 模拟就好，不要想多
数据太弱，不会卡TLE
先上代码
```cpp
#include
#define osi ((x+y)%2==0) \/\/判断x+y的奇偶性
using namespace std;
void nxt(int &x,int& y){\/\/模拟函数，找出x\/y的下一个数并存储在x\/y中
	if(osi){
		if(x==1)y+=1;
		else x-=1,y+=1;
	}else{
		if(y==1)x+=1;
		else x+=1,y-=1;
	}
}
int main(){
	int n;
	cin>>n;
	int x=1,y=1;\/\/第一个数
	for(int i=2;i<=n;i++)\/\/从第二个数开始模拟，一直到第n个
		nxt(x,y);
	cout<<x<<'\/'<<y;
    return -1;\/\/防抄袭标记
}
```
## 解释
#### 1. 找规律：
|x\/y|1|2|3|4|（y）|
| :----------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|1|1\/1|1\/2|1\/3|1\/4|...|
|2|2\/1|2\/2|2\/3|2\/4|...|
|3|3\/1|3\/2|3\/3|3\/4|...|
|4|4\/1|4\/2|4\/3|4\/4|...|
|（x）|...|...|...|...|...|
不难发现，位于第x行第y列的数正是x\/y。**所以在模拟时，只需移动坐标xy**。
#### 2. 接着找
|x\/y|1|2|3|4|（y）|
| :----------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|1|1\/1（1）|1\/2（2）|1\/3（6）|1\/4（7）|...|
|2|2\/1（3）|2\/2（5）|2\/3（8）|...|...|
|3|3\/1（4）|3\/2（9）|...|...|...|
|4|4\/1（10）|...|...|...|...|
|（x）|...|...|...|...|...|
不难发现，部分情况下，当x==1时，y+=1；y==1时，x+=1。做过八皇后问题的童鞋都知道，“\/”对角线坐标特点是x+y为定值（不信可以试试）。可以看出，**x+y为偶数，x==1→y+=1；x+y为奇数，y==1→x+=1**。
#### 3. 继续找
|x\/y|1|2|3|4|（y）|
| :----------: | :----------: | :----------: | :----------: | :----------: | :----------: |
|1|1\/1（1）|1\/2（2）|1\/3（6）|1\/4（7）|...|
|2|2\/1（3）|2\/2（5）|2\/3（8）|...|...|
|3|3\/1（4）|3\/2（9）|...|...|...|
|4|4\/1（10）|...|...|...|...|
|（x）|...|...|...|...|...|
不难发现，同样按照2的思路，讨论x+y的奇偶，可以得出**x+y为偶数，x-=1,y+=1；x+y为奇数，x+=1,y-=1**（去除2的特殊情况后）。
#### 4. 总结
可以得出如下代码
```cpp
if((x+y)%2==0){
	if(x==1)y+=1;
	else x-=1,y+=1;
}else{
	if(y==1)x+=1;
	else x+=1,y-=1;
}
```
## ~~好像有点啰嗦~~
~~其实本来想打表（没看数据范围）~~
按钮<\/button>","type":"题解","status":2,"postTime":1519108677,"author":{"uid":39122,"name":"water_lift","slogan":"这个家伙确实很懒，什么也没有留下","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":7,"background":""},"thumbUp":52,"commentCount":24,"currentUserVoteType":0,"contentDescription":"模拟就好，不要想多
数据太弱，不会卡TLE
先上代码

解释
1. 找规律：



x\/y
1
2
3
4","id":27255,"identifier":"TJ0003","title":"题解 P1014 【Cantor表】"},{"content":"第一次发题解，内心非常鸡冻-。-

首先，最重要的一点是
要明白这道题的数排列的顺序

#### Z字型！

本蒟蒻就是被这东西卡了半天没过去

弄明白这一点，代码就比较好实现了

还有一个问题

就是每一行的公式 假设是奇数行的话，很明显是从左向右排列的 1\/1,1\/2,1\/3,1\/4,1\/5, …

2\/1,2\/2,2\/3,2\/4, …

3\/1,3\/2,3\/3, …

4\/1,4\/2, …

5\/1, …观察这几行数（如果觉得不够直观，可以在纸上手动把它翻转一下，或者用exal），显然，奇数行的分子满足这样一个规律

分子=本层及以前所有数的数目和-n（即要求的编号）+1

那么也可以推出奇数行分母以及偶数行分子分母的公式

奇数行分母=cs-(tot-n)（tot即本层及以前所有数的数目和）

偶数行分子=cs-(tot-n) 偶数行分母=tot-n+1

下面贴出AC代码
```cpp
#include
using namespace std;
int main(){
    int n,cs=0,tot=0;\/\/cs记录层数，tot记录到这一层总共有多少数 
    cin>>n;
    while(tot<n){
        cs++;
        tot+=cs;
    }
    if(cs%2==1)\/\/当是奇数行时 
    cout<<tot-n+1<<"\/"<<cs-(tot-n);
    else
    cout<<cs-(tot-n)<<"\/"<<tot-n+1;
    return 0;
}
```
### 仅供参考","type":"题解","status":2,"postTime":1548852060,"author":{"uid":131385,"name":"xytd","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":""},"thumbUp":23,"commentCount":5,"currentUserVoteType":0,"contentDescription":"第一次发题解，内心非常鸡冻-。-
首先，最重要的一点是
要明白这道题的数排列的顺序
Z字型！
本蒟蒻就是被这东西卡了半天没过去
弄明白这一点，代码就比较好实现了
还有一个问题
就是每一行的公式 ...","id":108147,"identifier":"solution111-p1014","title":"题解 P1014 【Cantor表】"},{"content":"好像没有人跟我一样用暴力求解法啊……发一个~~，简洁明了~~！
```
#include
int main(){
	long n,a=1,b=1,i=2;\/\/i初始化必须为2，否则出错（当然你如果有解决办法1或0也可以）
	bool judge=true,become=false;\/\/judge不得为false，否则一开始就错了
	std::cin>>n;
	while(i<=n){
		if(judge&&a==1){
			judge=false;
			b++;
			become=true;\/\/这个变量是变换分母分子的关键点
		}
		else if(!judge&&b==1){
			judge=true;
			a++;
			become=true;
		}
		if(become)i++;\/\/因为是替交，所以无需再像下面操作
		else if(judge){\/\/分母增加分子减少
			a--;
			b++;
			i++;
		}
		else{\/\/分子增加分母减少
			a++;
			b--;
			i++;
		}
		become=false;\/\/不要忘，否则上面的if(become)一直为真则出错
	}
	std::cout<<a<<'\/'<<b;
	return 0;
}
```","type":"题解","status":2,"postTime":1538882838,"author":{"uid":117268,"name":"辣鸡光黄照耀","slogan":"这个人勤快得什么也氵","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":"https:\/\/cdn.luogu.com.cn\/upload\/image_hosting\/9ldmhmjr.png"},"thumbUp":18,"commentCount":8,"currentUserVoteType":0,"contentDescription":"好像没有人跟我一样用暴力求解法啊……发一个，简洁明了！
","id":74329,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"},{"content":"面对各位大佬的神仙AC代码我不禁掩面痛哭

~~请忽略我这个垃圾萌新~~

于是我只好手动拆分本数表：

1\/1  》1\/2  》2\/1  》3\/1  》2\/2  》1\/3  》1\/4  》2\/3  》3\/2  》4\/1  》5\/1 ......

然后手动寻找规律：
1\/1  》（0\/2） 》1\/2  》2\/1  》（3\/0）》3\/1  》2\/2  》1\/3  》（0\/4）》1\/4  》2\/3  》3\/2  》4\/1  》（5\/0）》5\/1 ......

说白了，规律也不多：

（我们把本表向左旋转45度，再考虑本问题）

~~（我不管你们的电脑显示器能不能旋转，实在不行扭着脖子看）~~

1.奇行每次向后，分子增1，分母减1，偶行相反。

2.当分子\/分母减为0时，分子\/分母自增为1，奇行换为偶行

按照这个规律写出来的**萌新专属代码**（实在不行在纸上试着模拟这个程序也行，~~只要是知道C++基础语法的人，除了某些**睿智**应该都看得出来~~）如下：

```cpp
#include 
using namespace std;
int main()
{
    int cnt,l=1,y=1,x=1;\/\/输出如下：x\/y
    cin >> cnt;
    for(int i = 1;i<cnt;i++)
    {
        if(l%2 == 1)
        {
            x--;
            y++;
            if(x == 0)
            {
                x++;
                l++;
            }
        }
        else if(l%2 == 0)
        {
            x++;
            y--;
            if(y == 0)
            {
                y++;
                l++;
            }
        }
    }
    cout << x << '\/' << y;
    return 0;
}
```

**~~请原谅我小学奥数般的清奇思路~~**
","type":"题解","status":2,"postTime":1555161039,"author":{"uid":131002,"name":"Orange_JAMGO","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":""},"thumbUp":17,"commentCount":23,"currentUserVoteType":0,"contentDescription":"面对各位大佬的神仙AC代码我不禁掩面痛哭
请忽略我这个垃圾萌新
于是我只好手动拆分本数表：
1\/1  》1\/2  》2\/1  》3\/1  》2\/2  》1\/3  》1\/4  》2\/3  》3\/2...","id":125572,"identifier":"solution-p1014","title":"题解 P1014 【Cantor表】"}],"perPage":10,"count":46},"problem":{"pid":"P1014","title":"[NOIP1999 普及组] Cantor 表","difficulty":2,"fullScore":100,"type":"P"},"acceptSolution":false},"currentTitle":"题解","currentTheme":{"id":559,"header":{"imagePath":"https:\/\/s2.ax1x.com\/2019\/08\/01\/ea5j4H.jpg","color":[[225,75,120,1],[23,208,180,1]],"blur":0,"brightness":-63,"degree":244,"repeat":0,"position":[50,17],"size":[1,1],"type":1,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\HeaderFooterConfig"},"sideNav":{"logoBackgroundColor":[23,208,180,1],"color":[255,64,122,1],"invertColor":false,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\SideNavConfig"},"footer":{"imagePath":"https:\/\/s2.ax1x.com\/2019\/08\/01\/ea5j4H.jpg","color":[[225,75,120,1],[23,208,180,1]],"blur":0,"brightness":-2,"degree":0,"repeat":0,"position":[38,73],"size":[0,0],"type":1,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\HeaderFooterConfig"}},"currentTime":1694589350,"currentUser":{"followingCount":0,"followerCount":0,"ranking":null,"eloValue":null,"blogAddress":null,"unreadMessageCount":0,"unreadNoticeCount":0,"uid":570994,"name":"kkRookie","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":"","verified":true}}"));window._feConfigVersion=1694162564;window._tagVersion=1694586105;