window._feInjection = JSON.parse(decodeURIComponent("{"code":200,"currentTemplate":"ProblemSolution","currentData":{"solutions":{"result":[{"content":"## 思路
本题涉及到的操作为”横向交换“与”纵向交换“。

实际上，”横向交换“即改变某张卡牌的列号，而”纵向交换“即改变某张卡牌的行号。

容易想到，既然连续进行同种交换不产生额外花费，我们应当试着先统一改变列号，再统一改变行号（或者反过来）。

可是，从第一个样例中我们就可以发现，这样的操作中可能会有冲突。例如，两张卡牌原先所处的行相同而目标列相同，这会使得按列归位时两张卡牌无法同时被移动到目标列。当两张卡牌原先所处的列相同而目标行相同时，也会产生类似的冲突。

通过手动模拟，可以发现，在出现冲突时，我们可以先正常地横向与纵向移动其它卡牌使其归位，再用一次额外的横向或纵向（注意，两种操作中有一种即可，另一种操作可以在之前提前进行）使冲突的卡牌归位。

还需要注意的是，我们需要尽可能减少冲突从而使花费尽可能小。这意味着当同种类型的卡牌有两张出现时，除非两张都会与某张卡牌产生冲突，否则我们就不将其视为冲突；另外，如果只有一个方向的冲突（如只有横向或纵向交换导致冲突），我们完全可以先进行另一个方向的交换，此时也不视为冲突。

最终的代码模拟上述过程即可。

## 代码
```c++
#include 
using namespace std;

#define CARDID 100003
#define N 303
int cxpos[CARDID],cypos[CARDID],cx2pos[CARDID],cy2pos[CARDID];	\/\/ 注意：x 纵向，y 横向。
int oxpos[CARDID],oypos[CARDID],ox2pos[CARDID],oy2pos[CARDID],targets[N][N];	\/\/ 卡牌的原先位置
int exist[CARDID] = {}, rexist[CARDID] = {};	\/\/ 有几张卡牌
bool counter[CARDID] = {};
bool failure = false;
bool cpx = false, cpy = false;		\/\/ 是否有冲突
int xmove = 0, ymove = 0;			\/\/ 是否需要进行该方向的交换

inline int mini(int x, int y) {
	return x>n>>a>>b;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin>>tmp;
			targets[i][j] = tmp;
			if (!exist[tmp]) {
				oxpos[tmp] = i;
				oypos[tmp] = j;
			} else {
				ox2pos[tmp] = i;
				oy2pos[tmp] = j;
			}
			exist[tmp]++;
			rexist[tmp]++;
		}
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin>>tmp;
			if (!exist[tmp]) {
				failure = true;
			} else {
				exist[tmp]--;
				if (oxpos[tmp] != i && ox2pos[tmp] != i) {
					xmove = 1;
				}
				if (oypos[tmp] != j && oy2pos[tmp] != j) {
					ymove = 1;
				}
				if (counter[tmp]) {
					cx2pos[tmp] = i;
					cy2pos[tmp] = j;
				} else {
					cxpos[tmp] = i;
					cypos[tmp] = j;
				}
				counter[tmp] = true;
			}
		}
	}
	if (failure) {
		cout<<"Fail"<<endl;
		return 0;
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			for (int k = 0; k < i; k++) {
				if (judge(i,j,k,j)) {
					cpx = true;
				}
			}
			for (int k = 0; k < j; k++) {
				if (judge(i,j,i,k)) {
					cpy = true;
				}
			}
		}
	}
	int result = xmove * b + ymove * a;
	if (cpx && cpy) {
		result += mini(a,b);
	}
	cout<<result<<endl;

	return 0;
}
```","type":"题解","status":2,"postTime":1693290624,"author":{"uid":589961,"name":"steambird","slogan":"风生水起，无限可能","badge":null,"isAdmin":false,"isBanned":false,"color":"Red","ccfLevel":0,"background":""},"thumbUp":5,"commentCount":4,"currentUserVoteType":0,"contentDescription":"思路
本题涉及到的操作为”横向交换“与”纵向交换“。
实际上，”横向交换“即改变某张卡牌的列号，而”纵向交换“即改变某张卡牌的行号。
容易想到，既然连续进行同种交换不产生额外花费，我们应当试着先...","id":627264,"identifier":"p2200-ti-jie","title":"P2200 题解"}],"perPage":10,"count":1},"problem":{"pid":"P2200","title":"炉石collection","difficulty":0,"fullScore":100,"type":"P"},"acceptSolution":true},"currentTitle":"题解","currentTheme":{"id":559,"header":{"imagePath":"https:\/\/s2.ax1x.com\/2019\/08\/01\/ea5j4H.jpg","color":[[225,75,120,1],[23,208,180,1]],"blur":0,"brightness":-63,"degree":244,"repeat":0,"position":[50,17],"size":[1,1],"type":1,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\HeaderFooterConfig"},"sideNav":{"logoBackgroundColor":[23,208,180,1],"color":[255,64,122,1],"invertColor":false,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\SideNavConfig"},"footer":{"imagePath":"https:\/\/s2.ax1x.com\/2019\/08\/01\/ea5j4H.jpg","color":[[225,75,120,1],[23,208,180,1]],"blur":0,"brightness":-2,"degree":0,"repeat":0,"position":[38,73],"size":[0,0],"type":1,"__CLASS_NAME":"Luogu\DataClass\User\ThemeConfig\HeaderFooterConfig"}},"currentTime":1694599182,"currentUser":{"followingCount":0,"followerCount":0,"ranking":null,"eloValue":null,"blogAddress":null,"unreadMessageCount":0,"unreadNoticeCount":0,"uid":570994,"name":"kkRookie","slogan":"","badge":null,"isAdmin":false,"isBanned":false,"color":"Gray","ccfLevel":0,"background":"","verified":true}}"));window._feConfigVersion=1694162564;window._tagVersion=1694594997;