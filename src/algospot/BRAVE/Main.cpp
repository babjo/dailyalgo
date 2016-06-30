#include <string.h>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int>* sets[10 * 10000 + 1];
long maxSize;
void marge(int x, int y);

int main() {

    int T;
    cin >> T;

    for(int i=0; i<T; i++){
        int N, M;
        cin >> N;
        cin >> M;

        for(int j=0; j<M; j++) {
            int x, y;
            cin >> x;
            cin >> y;
            marge(x, y);
        }
        cout << maxSize << endl;

        set<vector<int>*> release;
        maxSize = 0;
        for(int k=0; k<N; k++){
            if(sets[k] != nullptr) {
                release.insert(sets[k]);
            }
        }

        for(set<vector<int>*>::iterator it = release.begin(); it != release.end(); it++){
            delete *it;
        }
        memset(sets, 0, sizeof(vector<int>*) * 10 * 10000 + 1);
    }
}

void marge(int x, int y) {
    if(sets[x] == nullptr && sets[y] == nullptr){
        sets[x] = new vector<int>;
        sets[x]->push_back(x);
        sets[x]->push_back(y);
        sets[y] = sets[x];
    }else if(sets[x] == nullptr && sets[y] != nullptr){
        sets[y]->push_back(x);
        sets[x] = sets[y];
    }else if(sets[x] != nullptr && sets[y] == nullptr){
        sets[x]->push_back(y);
        sets[y] = sets[x];
    }else if(sets[x] != sets[y]){
        vector<int>* temp = sets[y];
        vector<int>::iterator v = temp->begin();
        while(v != temp->end()){
            sets[x]->push_back(*v);
            sets[*v] = sets[x];
            v++;
        }
        delete temp;
    }
    long size = sets[x]->size();
    if(maxSize < size) {
        maxSize = size;
    }
}