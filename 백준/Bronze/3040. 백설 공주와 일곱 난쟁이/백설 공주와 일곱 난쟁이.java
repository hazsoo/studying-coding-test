import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> num = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 9; i++) {
            num.add(sc.nextInt());
        }
        
        int MUST = 100;
        int summ = 0;
        for (int n : num) {
            summ += n;
        }
        Loop1:
        for (int i = 0; i < 9; i++) {
            for (int j = i+1; j < 9; j++) {
                if (summ - num.get(i) - num.get(j) == MUST) {
                    int numi = num.get(i);
                    int numj = num.get(j);
                    num.remove(Integer.valueOf(numi));
                    num.remove(Integer.valueOf(numj));
                    break Loop1;
                }
            }
        }
        for (int x : num) {
            System.out.println(x);
        }
    }
}