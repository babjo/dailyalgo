//
// Created by MyMac on 2016. 7. 5..
//

#include <iostream>
#include <string.h>

using namespace std;

int cache[2000][2000];
int main(){

    int T;
    cin >> T;

    for(int testCase=0; testCase<T; testCase++){
        string input;
        cin >> input;

        char temp = input.at(1);
        bool isOneChar = true;
        for(string::size_type i=2; i < input.size()-1; ++i) {
            if(temp != input.at(i)){
                isOneChar = false;
                break;
            }
        }

        if(isOneChar){
            cout << "lonely island" << endl;
        }else {
            string result = "";
            int L = input.size() % 2 == 0 ? (input.size() - 1) / 2 : (input.size() - 1) / 2 - 1;
            for (int k = 1; k <= L; k++) {
                bool next = false;
                int strLength = k * 2 + 1;
                for (int i = 0; i <= input.size() - strLength - 1; i++) {
                    for (int j = i + 1; j <= input.size() - strLength; j++) {
                        if(cache[i+k][j+k] == k-1){
                            if(input.at(i) == input.at(j) && input.at(i+k) != input.at(j+k) && input.at(i+2*k) == input.at(j+2*k)){
                                cache[i+k][j+k] = k;
                                next = true;

                                string source = input.substr(i, strLength);
                                string target = input.substr(j, strLength);
                                string case1 = source + " " + target;
                                string case2 = target + " " + source;
                                string zzak = case1.compare(case2) > 0 ? case2 : case1;

                                if(result.size() < zzak.size() || result.compare(zzak) > 0){
                                    result = zzak;
                                }
                            }
                        }
                    }
                }
                if(!next) break;
            }

            if(result.size() !=0 ){
                cout << result << endl;
            }else{
                cout << "lonely island" << endl;
            }
        }

        memset(cache, 0, sizeof(cache[0][0])*2000*2000);
    }
}
