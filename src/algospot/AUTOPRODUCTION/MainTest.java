package algospot.AUTOPRODUCTION;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

/**
 * Created by LCH on 2016. 6. 14..
 */
public class MainTest {

    @Test
    public void testGetMaxSum() throws Exception {
        int[] numbers = new int[]{1,2,3,4,5};

        assertEquals(Main.getMaxSum(numbers, 2), 9);
        assertEquals(Main.getMaxSum(numbers, 3), 12);
        assertEquals(Main.getMaxSum(numbers, 1), 5);
    }

    @Test
    public void testSelect() throws Exception {
        int[] lengthList = new int[]{5, 4, 3};
        //int[] lengthList = new int[]{1, 1, 1};
        int[] results = new int[lengthList.length];
        Main.select2(lengthList, 0, results, 0);

        //Main.select(lengthList);
    }

}