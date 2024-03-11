#include <iostream>
#include <cstring>
#include <stack>
using namespace std;

int main() {
    string str;
    cin>>str;
    stack<char> s;

    int count=0;
    for(int i=0; i<str.length(); i++){
        if(str[i]=='('){ 
            s.push(str[i]);
        }
        
        else{
            //레이저
            if(str[i-1]=='('){
                s.pop();
                count+=s.size();
            }
            //레이저 아닌 닫는괄호
            else{
                s.pop();
                count+=1;
            }
        }
    }
    cout<<count;
    return 0;
}