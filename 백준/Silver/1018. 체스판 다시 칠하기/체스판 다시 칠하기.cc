#include <iostream>
using namespace std;

int count(int a, int b, char chess[50][50]){
    int cnt1 = 0; // 시작 색깔이 흰색인 경우
    int cnt2 = 0; // 시작 색깔이 검은색인 경우
    for(int i = a; i < a + 8; i++){
        for(int j = b; j < b + 8; j++){
            // 시작 색깔이 흰색인 경우
            if((i-a + j-b) % 2 == 0){ // 현재 위치가 체스판의 검은색 칸이어야 하는 위치인 경우
                if(chess[i][j] != 'W')
                    cnt1++;
            } else { // 현재 위치가 체스판의 흰색 칸이어야 하는 위치인 경우
                if(chess[i][j] != 'B')
                    cnt1++;
            }
            // 시작 색깔이 검은색인 경우
            if((i-a + j-b) % 2 == 0){ // 현재 위치가 체스판의 검은색 칸이어야 하는 위치인 경우
                if(chess[i][j] != 'B')
                    cnt2++;
            } else { // 현재 위치가 체스판의 흰색 칸이어야 하는 위치인 경우
                if(chess[i][j] != 'W')
                    cnt2++;
            }
        }
    }
    return min(cnt1, cnt2); // 두 경우 중에서 최소값을 반환
}

int main(){
    int M, N;
    char arr[50][50];
    cin >> M >> N;
    
    // arr 채우기
    for(int i = 0; i < M; i++){
        for(int j = 0; j < N; j++){
            cin >> arr[i][j];
        }
    }
    
    // 최소한으로 다시 칠
    int min_re = 2500;
    for(int i = 0; i <= M - 8; i++){
        for(int j = 0; j <= N - 8; j++){
            min_re = min(min_re, count(i, j, arr));
        }
    }
    
    // 다시 칠해야 하는 개수
    cout << min_re << '\n';
    return 0;
}
