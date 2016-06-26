package algospot.DICT;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * Created by LCH on 2016. 6. 26..
 */
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        String line = bi.readLine().trim();
        int T = Integer.parseInt(line);

        for(int m=0; m<T; m++){
            String input = bi.readLine().trim();
            StringTokenizer st = new StringTokenizer(input);
            String[] inputs = new String[3];
            int i=0;
            while(st.hasMoreTokens()){
                inputs[i++] = st.nextToken();
            }

            int aCount = Integer.parseInt(inputs[0]);
            int bCount = Integer.parseInt(inputs[1]);
            int k = Integer.parseInt(inputs[2]);
            result = "";
            solve("", aCount, bCount, k);
            if(m == T-1)
                System.out.print(result);
            else
                System.out.println(result);
        }
    }

    private static String result = "";
    private static void solve(String prefix, int aCount, int bCount, int k) {
        if(getC(aCount + bCount, bCount) < k || (aCount == 0 && bCount == 0)) {
            result = "NONE";
            return ;
        }

        if((k==1 && aCount == 0 && bCount > 0) || (k==1 && bCount == 0 && aCount > 0)) {
            int length = aCount == 0 ? bCount : aCount;
            String loopChar = aCount == 0 ? "b" : "a";

            String _result = "";
            for (int i = 0; i < length; i++) {
                _result += loopChar;
            }
            result = prefix + _result;
            return;
        }

        int case1Range = getC(aCount + bCount-1, bCount);

        // case 1. a를 뽑았을 때
        if(1<=k && k<= case1Range){
            prefix += "a";
            solve(prefix, aCount-1, bCount, k);
        }
        else{ // case 2. b를 뽑았을 때
            prefix += "b";
            solve(prefix, aCount, bCount-1, k-case1Range);
        }
    }


    private static int[][] C = new int[201][201];
    private static int getC(int n, int m){
        if(C[n][m] == 0) {
            C[0][0] = 1;
            for (int i = 1; i <= 200; i++) {
                C[i][0] = 1;
                C[i][i] = 1;
                for (int j = 1; j < i; j++)
                    C[i][j] = Math.min(C[i - 1][j] + C[i - 1][j - 1], 1000000001);
            }
        }
        return C[n][m];
    }
}
