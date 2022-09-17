# 4. 단어 뒤집기
설명  

N개의 단어가 주어지면 각 단어를 뒤집어 출력하는 프로그램을 작성하세요.
  
  
입력  
첫 줄에 자연수 N(3<=N<=20)이 주어집니다.  

두 번째 줄부터 N개의 단어가 각 줄에 하나씩 주어집니다. 단어는 영어 알파벳으로만 구성되어 있습니다.  


출력  
N개의 단어를 입력된 순서대로 한 줄에 하나씩 뒤집어서 출력합니다.  


예시 입력 1   
3
good
Time
Big  
  
예시 출력 1  
doog
emiT
giB  

### StringBuilder 객체 사용

```java
import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public ArrayList<String> solution(int n, String[] str){
        ArrayList<String> answer = new ArrayList<>(); // 왜 String[] 아니고 ArrayList 쓰는 거지?
        for(String x : str){
            String tmp = new StringBuilder(x).reverse().toString();
            answer.add(tmp);
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        String[] str = new String[n];
        for(int i = 0; i < n; i++){
            str[i] = kb.next();
        }
        for(String x : T.solution(n, str)){
            System.out.println(x);
        }
    }
}

```  

### String.toCharArray() 사용  

> 양 쪽에서 한 칸씩 바꿔 들어가며 진행  
> 
![문자바꾸기](https://user-images.githubusercontent.com/81146582/190859697-d151a58f-083a-4827-ba89-f4aa364d74cf.png)


```java
import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public ArrayList<String> solution(int n, String[] str){
        ArrayList<String> answer = new ArrayList<>();
        for(String x : str){
            char[] s = x.toCharArray();
            int lt = 0, rt = x.length() - 1;
            while(lt < rt){
                char tmp = s[lt];
                s[lt] = s[rt];
                s[rt] = tmp;
                lt++;
                rt--;
            }
            String tmp = String.valueOf(s); // 여기서 잠깐. 아래 '정리' 참고
            answer.add(tmp);
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        String[] str = new String[n];
        for(int i = 0; i < n; i++){
            str[i] = kb.next();
        }
        for(String x : T.solution(n, str)){
            System.out.println(x);
        }
    }
}

```


<hr/>  

### 정리
> - 글자 뒤집는 간단한 방법은 StringBuilder의 reverse()사용
> - String 연산은 다수의 객체가 만들어지는데, 이때 StringBuilder를 쓰면 객체 하나로 연산이 가능하다.
> - String tmp = s.toString(); 이렇게는 안된다.
    null일 가능성 있고, 확실히 String으로 변환하고 싶을 땐
    String.valueOf()를 쓰자
