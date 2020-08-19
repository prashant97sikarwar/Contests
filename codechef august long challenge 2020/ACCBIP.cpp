#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define lk LLONG_MAX
#define mp make_pair
#define db long double
typedef long long ll;
#define all(x) (x).begin(), (x).end()
#define rev(a) reverse(a.begin(),a.en())


const int MOD = 998244353;
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

unsigned countBits(unsigned int number) 
{       
      return (int)log2(number)+1; 
} 

unsigned int countSetBits(unsigned int n) 
{ 
    unsigned int count = 0; 
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    return count; 
} 

ll get_gcd(ll x,ll y) {return (y==0) ? x : get_gcd(y,x%y);}

ll power(const ll & x,const ll & mi)
{
    ll s1=1LL,s2=x,m=mi;
    while (m)
    {
        if (m&1) s1=s1*s2%MOD;
        s2=s2*s2%MOD;
        m>>=1;
    }
    return s1;
}

inline ll get_inv(ll x)
{
    return power(x,MOD - 2);
}



ll my_fun(int colour,ll num,vector<ll> lines_set[]){

    vector<long long int> lines = lines_set[colour];
    long long int sm3 = 0;
    long long int k = lines.size();
    long long int sm1 = 0;
    ll temp[k+1]={0}; 
    ll sm2 = 0;
    
    for(long long int i=0;i<lines.size();i++){
        if(num > 0){

        long long int temp = min(lines[i],num);
        lines[i] -= temp;
        num -= temp;
        }
        else{
            break;
        }
    }
    if(num>0){
        return 0;
    }

    for (int i=1; i<=k; i++)
    {
        sm1 += lines[i-1]; 
    }
     
    for (long long int i=1; i<=k; i++) 
    { 
        temp[i-1] = (sm1-lines[i-1])*lines[i-1]; 
        sm2 += temp[i-1]; 
    } 
    sm2 /= 2; 

     
    for (long long int i=2; i<=k+1; i++) 
        sm3 += lines[i-2]*(sm2-temp[i-2]); 
    
    sm3 /= 3; 

    return sm3;
}

void dark(){
   long long int N,C,K;
   cin>>N>>C>>K;
   unordered_map<long long int,int> hash[C+1];
   vector<long long int> nooflines[C+1];
   long long int V[C+1];

   for(int i=1;i<=N;i++){
       long long int a,b,col_unit;
       cin>>a>>b>>col_unit;
       hash[col_unit][a]++;
   }
   

   
   for(long long int i=1;i<=C;i++){
       cin>>V[i];
   }
   for(long long int i=1;i<=C;i++){
       vector<long long int> lines_set;
       for(auto iter : hash[i]){
           lines_set.pb(iter.second);
       }
       sort(all(lines_set));
       nooflines[i] = lines_set;
   }
   
   long long int memory[K+1][C+1]={0};
   long long int dp[K+1][C+1] = {0};
   for(int i=0;i<=K;i++){
       for(long long int j=0;j<=C;j++){
           dp[i][j] = lk;
           if(j==0){
               dp[i][j]=0;
           }
            memory[i][j] = -1;
       }
   }
    ll remaining_value;
    long long int remaining_lines;
   for(long long int i=0;i<=K;i++){
       
       for(long long int j=1;j<=C;j++){
           
           remaining_lines = i/V[j];
           
           for(ll k=0;k<=remaining_lines;k++){
               
                remaining_value = k*V[j];
               
              if(memory[k][j]==-1){
                   memory[k][j] = my_fun(j,k,nooflines);
              }

               dp[i][j] = min(dp[i-remaining_value][j-1] + memory[k][j],dp[i][j] );
           }
       }
   }

  printf("%llu\n", dp[K][C]);
}

int main() {
    ll t;
    cin>>t;

    while(t){
        dark();
        t -= 1;
    }
    return 0;
}
