#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>
#include <ctime>

using namespace std;

bool compare(int* A, int* B, int* AEnd, int* BEnd);
int* move(int* first, int* end);
string getKeyword(int* targetEnd, int* start, int* mid, int* startToMid, int* loop);

int main(){

    int T;
    cin >> T;

    int A[1000];
    int B[1000];

    for(int i=0; i<T; i++){

        string a, b;
        cin >> a;
        cin >> b;

        int num=0;
        int AStringSize=0;
        int BStringSize=0;
        int ALength = 0;
        int BLength = 0;
        bool inner = false;
        int innerSize = 0;

        for(string::size_type i = 0; i < a.size(); ++i) {
            if(a[i] >= '0' && a[i] <= '9'){
                if(num == 0) num = a[i] - '0';
                else {
                    num = num * 10 + a[i] - '0';
                }

                if(i+1 == a.size() || !isdigit(a[i+1])){
                    AStringSize += (innerSize * num);
                    A[ALength++] = num;

                    inner = false;
                    innerSize = 0;
                    num = 0;
                }
            }
            else{
                if(a[i] == 40) {
                    inner = true;
                }else if(a[i] == 41){
                    inner = false;
                }else if(a[i] != 94){
                    if(inner){
                        innerSize ++;
                    }else{
                        AStringSize ++;
                    }
                }

                A[ALength++] = a[i];
            }
        }

        num = 0;
        innerSize = 0;
        inner = false;
        for(string::size_type i = 0; i < b.size(); ++i) {
            if(b[i] >= '0' && b[i] <= '9'){
                if(num == 0) num = b[i] - '0';
                else {
                    num = num * 10 + b[i] - '0';
                }

                if(i+1 == b.size() || !isdigit(b[i+1])){
                    BStringSize += (innerSize * num);
                    B[BLength++] = num;

                    inner = false;
                    innerSize = 0;
                    num = 0;
                }
            }
            else{
                if(b[i] == 40) {
                    inner = true;
                }else if(b[i] == 41){
                    inner = false;
                }else if(b[i] != 94){
                    if(inner){
                        innerSize++;
                    }else{
                        BStringSize++;
                    }
                }

                B[BLength++] = b[i];
            }
        }

        if(AStringSize == BStringSize){
            bool result = compare(A, B, A + ALength, B + BLength);
            if(result) cout << "YES" << endl;
            else cout<< "NO" <<endl;
        } else{
            cout<< "NO" <<endl;
        }
    }
    return 0;
}

bool compare(int* A, int* B, int* AEnd, int* BEnd){

    int* it1 = A;
    int* it2 = B;
    int* previousIt1;
    int* previousIt2;

    bool inA = false;
    bool inB = false;

    while(it1 != AEnd && it2 != BEnd){
        if(*it1 == 41){
            it1 = move(previousIt1, it1);
            inA = false;
        }

        if(*it1 == 40){
            previousIt1 = it1;
            it1++;
            inA = true;
        }

        if(*it2 == 41){
            it2 = move(previousIt2, it2);
            inB = false;
        }

        if(*it2 == 40){
            previousIt2 = it2;
            it2++;
            inB = true;
        }

        if(inA && inB){
            int it1Loop;
            int it2Loop;
            int it1StartToMid;
            int it2StartToMid;
            string it1Keyword = getKeyword(AEnd, previousIt1+1, it1, &it1StartToMid, &it1Loop);
            string it2Keyword = getKeyword(BEnd, previousIt2+1, it2, &it2StartToMid, &it2Loop);

            if(it1Keyword == it2Keyword){
                int* it1KeywordNum = find(it1, AEnd, '^') + 1;
                int* it2KeywordNum = find(it2, BEnd, '^') + 1;
                if(*it1KeywordNum < *it2KeywordNum){
                    *it2KeywordNum = *it2KeywordNum - *it1KeywordNum + 1;
                    *it1KeywordNum = 1;
                }else if(*it1KeywordNum > *it2KeywordNum){
                    *it1KeywordNum = *it1KeywordNum - *it2KeywordNum + 1;
                    *it2KeywordNum = 1;
                }else {
                    *it1KeywordNum = 1;
                    *it2KeywordNum = 1;
                }
            }else if(it1Loop != -1 && it2Loop != -1 && it1Loop == it2Loop){
                int it1KeywordSize = it1Keyword.size();
                int it2KeywordSize = it2Keyword.size();

                int* it1KeywordNum = find(it1, AEnd, '^') + 1;
                int* it2KeywordNum = find(it2, BEnd, '^') + 1;
                *it1KeywordNum = (*it1KeywordNum) * it1KeywordSize - it1StartToMid;
                *it2KeywordNum = (*it2KeywordNum) * it2KeywordSize - it2StartToMid;

                it1 = it1KeywordNum - 4;
                it2 = it2KeywordNum - 4;
                *(it1) = 40;
                *(it2) = 40;

                previousIt1 = it1;
                it1++;
                previousIt2 = it2;
                it2++;
            }else{
                inA = false;
                inB = false;
            }
        }

        if(it1 == AEnd && it2 == BEnd){
            return true;
        }
        else if(*it1 != *it2){
            return false;
        }

        it1++;
        it2++;
    }

    return true;
}

int* move(int* first, int* end){
    int* number = end;
    number++;
    number++;

    if(*(number) == 1){
        number++;
        return number;
    }else{
        (*number)--;
        return first;
    }
}

string getKeyword(int* targetEnd, int* start, int* mid, int* startToMid, int* loop){
    string keyword = "";
    int* end = find(mid, targetEnd, ')');

    int* it = mid;
    *loop = *it;
    while(it!=end){
        keyword += (char)(*it);
        it++;
    }

    *startToMid = 0;
    while(start != mid){
        keyword += (char)(*start);
        (*startToMid)++;
        start++;
    }

    int i=0;
    while(i<keyword.size()){
        if(keyword[i] != *loop){
            *loop = -1;
            break;
        }
        i++;
    }

    return keyword;
}