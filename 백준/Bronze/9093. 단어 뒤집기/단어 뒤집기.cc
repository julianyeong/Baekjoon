/*
문제
문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 
단, 단어의 순서는 바꿀 수 없다. 
단어는 영어 알파벳으로만 이루어져 있다.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 
단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 
단어와 단어 사이에는 공백이 하나 있다.

출력
각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.
*/

//getline(cin, sentence) .. getline함수
//백준 풀이 봐보자
#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(){
    int N;
    cin>>N;
    string sentence;
    stack <char> st;
    
    cin.ignore(); //버퍼 비우기
    while(N--){
        getline(cin, sentence);
        sentence+=' ';
        
        for(int i=0; i<sentence.size(); i++){
            if(sentence[i]==' '){
                //한 문장이 이미 시작됐고 단어별로 담고있음
                while(!st.empty()){
                    cout << st.top();
                    st.pop();
                }cout <<' ';
                }
            else
                st.push(sentence[i]);
                
            }cout<< '\n';
        }
    }