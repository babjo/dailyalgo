package algospot.AUTOPRODUCTION;

import java.util.*;

public class Main {

    private static int[][] slots;
    private static int[] needMaterial;
    private static int max = 0;

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for(int i=0; i<T; i++){
            int needMaterialLength = Integer.parseInt(sc.nextLine());
            needMaterial = new int[needMaterialLength];
            slots = new int[needMaterialLength][];
            max = 0;

            for(int j=0; j<needMaterialLength; j++) {
                String[] input = sc.nextLine().split(" ");
                int needMaterialCount = Integer.parseInt(input[0]);
                needMaterial[j] = needMaterialCount;
                int materialSlotCount = Integer.parseInt(input[1]);
                slots[j] = new int[materialSlotCount];

                int k=0;
                for(String n : sc.nextLine().split(" ")){
                    slots[j][k++] = Integer.parseInt(n);
                }
                Arrays.sort(slots[j]);
            }
            int[] lengthList = new int[slots.length];
            for(int j=0; j<slots.length; j++){
                lengthList[j] = slots[j].length;
            }
            max = 0;
            select2(lengthList ,0, new int[lengthList.length], MAX);
            System.out.println(max);
        }
    }


    public static int getMaxSum(int[] numbers, int count){
        if(numbers.length < count)
            throw new RuntimeException("너무 많이 선택하려고해");

        int max = 0;
        for(int i=0; i<count; i++){
            max += numbers[numbers.length -i -1];
        }

        return max;
    }

    private static final int MAX = 10;
    public static void select2(int[] lengthList, int depth, int[] results, int rest){
        if(depth < lengthList.length) {
            for (int i = lengthList[depth]; i>0 ; i--) {
                results[depth] = i;
                if(0 <= rest-i)
                    select2(lengthList, depth+1, results, rest-i);
            }
        }else if(rest >= 0 && depth == lengthList.length){
            int min = Integer.MAX_VALUE;
            for(int k=0; k<lengthList.length; k++){
                int maxSum = getMaxSum(slots[k], results[k]);
                int temp = maxSum/needMaterial[k];
                if(temp < min){
                    min = temp;
                }
            }
            if(max < min){
                max = min;
            }
        }
    }
}
