#include <iostream>
#include <cstring>
#include <stack>
using namespace std;

int main(){
    string sentence;
    cin>>sentence;
    
    int l=0;
    l=sentence.length();
    stack<char> left, right;
    for(int i=0; i<l; i++){
        left.push(sentence[i]);
    }
    
    int m;
    cin>>m;
    
    while(m--){
        char what;
        cin>>what;
        
        if(what == 'L'){
            if(!left.empty()){
                right.push(left.top());
                left.pop();
            }
        }
        else if(what == 'D'){
            if(!right.empty()){
                left.push(right.top());
                right.pop();
            }
        }
        
        else if(what == 'B'){
            if(!left.empty())
                left.pop();
        }
        
        else if(what == 'P'){
            char c;
            cin>>c;
            left.push(c);
        }
    }
    
    while(!left.empty()){
       right.push(left.top());
       left.pop();
    }
    
    while(!right.empty()){
        cout<<right.top();
        right.pop();
    }
    cout<<'\n';
    return 0;
}