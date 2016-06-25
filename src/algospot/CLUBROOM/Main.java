package algospot.CLUBROOM;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Created by LCH on 2016. 6. 25..
 */
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader bi = new BufferedReader(new InputStreamReader(System.in));
        String line = bi.readLine();
        int T = Integer.parseInt(line.trim());

        for(int m=0; m<T; m++){
            String input = bi.readLine();
            String[] inputs = input.split(" ");
            int welfareCount = Integer.parseInt(inputs[0]);
            int clubCount = Integer.parseInt(inputs[1]);

            Point[] welfareList = new Point[welfareCount];
            int q=0;
            Point[] clubList = new Point[clubCount];
            int p=0;


            for(int i=0; i<welfareCount + clubCount; i++){
                String input2 = bi.readLine();
                String[] input2s = input2.split(" ");
                int x = Integer.parseInt(input2s[0]);
                int y = Integer.parseInt(input2s[1]);
                if(q < welfareCount)
                    welfareList[q++] = new Point(x, y);
                else if(p < clubCount)
                    clubList[p++] = new Point(x, y);
            }

            for(int i=0; i<clubCount; i++){
                if(i == 0) {
                    System.out.print("G ");
                } else{
                    Zone zone = new Zone();
                    for(int j=0; j<welfareCount; j++){
                        zone = zone.intersect(new Zone(welfareList[j], clubList[i]));
                        if(zone == null) break;
                    }
                    String result = contains(clubList, i, zone);
                    if(i == clubCount - 1)
                        System.out.print(result);
                    else
                        System.out.print(result+" ");
                }
            }
            System.out.print("\n");
        }
    }

    private static String contains(Point[] clubList, int length, Zone zone) {
        if(zone == null) return "G";

        for(int k=0; k<length; k++) {
            if(zone.contains(clubList[k])){
                return "B";
            }
        }
        return "G";
    }

    private static class Point {
        public final int x;
        public final int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    private static class Zone {

        private Point tl;
        private Point br;

        public Zone(){}

        public Zone(Point welfare, Point club) {
            int d = Math.max(Math.abs(welfare.x - club.x), Math.abs(welfare.y - club.y));

            tl = new Point(welfare.x - d, welfare.y - d);
            br = new Point(welfare.x + d, welfare.y + d);
        }

        private Zone create(Point tl, Point br){
            Zone zone = new Zone();
            zone.setTl(tl);
            zone.setBr(br);
            return zone;
        }

        public void setTl(Point tl) {
            this.tl = tl;
        }

        public void setBr(Point br) {
            this.br = br;
        }

        public Zone intersect(Zone target) {
            if(tl == null) return target;
            else if((br.x <= target.tl.x || br.y <= target.tl.y) || (target.br.x <= tl.x || target.br.y <= tl.y)) return null;

            return create(new Point(Math.max(tl.x, target.tl.x), Math.max(tl.y, target.tl.y)), new Point(Math.min(br.x, target.br.x), Math.min(br.y, target.br.y)));
        }

        public boolean contains(Point point) {
            return tl.x < point.x && point.x < br.x && tl.y < point.y && point.y < br.y;
        }
    }
}
