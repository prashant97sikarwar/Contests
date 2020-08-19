#include <bits/stdc++.h>
#define ll long long
using namespace std;
int binarySearch(int arr[], int l, int r, int x) 
{ 
    if (r >= l) { 
        int mid = l + (r - l) / 2; 

        if (arr[mid] == x) 
            return mid; 

        if (arr[mid] > x) 
            return binarySearch(arr, l, mid - 1, x); 
  
        return binarySearch(arr, mid + 1, r, x); 
    } 

    return -1; 
}
  
void dark()
{
    ll m,k;
    cin>>m >> k;
    ll arr[m+1];
    ll answer =0;
    for(ll i=0;i<m;i++){
        cin>>arr[i];
    }
    map<ll,ll>d;
    ll mycol[m+1][m+1]={0};
    for(ll i=0;i<m;i++){
        for(ll j=0;j<m;j++) {
            mycol[i][j]=0;
        }
    }
    for(ll i=0;i<m;i++){
        d.clear();
        for(ll j=i;j<m;j++){
            mycol[i][j]=(j==0)?0:mycol[i][j-1];
            if(d.count(arr[j])){
                if(d[arr[j]]==1){
                mycol[i][j]++;
            }
            mycol[i][j]++;
            d[arr[j]]++;
            }else{
            d[arr[j]]++;
            }
            }
        }
       answer=1e18;
       ll onemore[101][1001] = {0};
        ll line=100;
        
        for(int i = 0; i <= line; i++){
            for(ll j=0; j<=line; j++){
                onemore[i][j] = 0;
            }
        }
        for(ll i=1;i<m+1;i++){
            onemore[1][i]=mycol[0][i-1];
        }
        for(ll i=2;i<=line;i++){
        onemore[i][1]=0;
        }
        for(ll i=2;i<=line;i++){
            for(ll j=2;j<=m;j++){
                ll value=1e18;
                for(ll p=1;p<j;p++){
                    value = min(value,onemore[i-1][p]+mycol[p][j-1]);
                }
                onemore[i][j]=value;
            }
        }
        for(ll dep=1;dep<=100; dep++){
          answer=min(dep*k+onemore[dep][m],answer);
        }
            cout<<answer<<endl;
    }
    int main()
{
 int test;
 cin>>test;
 while(test--){
     dark();
 }
 return 0;
}

