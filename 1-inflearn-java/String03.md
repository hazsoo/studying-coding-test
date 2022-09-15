# 3. 문장 속 단어
설명  

한 개의 문장이 주어지면 그 문장 속에서 가장 긴 단어를 출력하는 프로그램을 작성하세요.  

문장속의 각 단어는 공백으로 구분됩니다.  


입력  
첫 줄에 길이가 100을 넘지 않는 한 개의 문장이 주어집니다. 문장은 영어 알파벳으로만 구성되어 있습니다.  


출력  
첫 줄에 가장 긴 단어를 출력한다. 가장 길이가 긴 단어가 여러개일 경우 문장속에서 가장 앞쪽에 위치한 단어를 답으로 합니다.  


예시 입력 1   
it is time to study  

예시 출력 1  
study  
### string.split(string) 사용

```java
import java.util.Scanner;

class Main {
    public String solution(String str){
        String answer = "";
        int max = Integer.MIN_VALUE; // 가장 작은 값으로 초기화
        for(String x : str.split(" ")){
            if(x.length() > max) {
                max = x.length();
                answer = x;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine(); // 한 문장을 입력받는다.
        System.out.print(T.solution(str));
    }
}
```  

### string.indexOf(string) 사용

```java
import java.util.Scanner;

class Main {
    public String solution(String str){
        String answer = "";
        int max = Integer.MIN_VALUE, pos; // 연달아 초기화할 수 있다.
        while((pos = str.indexOf(" ")) != -1){ // 띄어쓰기 위치를 찾는다.
            String tmp = str.substring(0, pos);
            int len = tmp.length();
            if(len > max){
                max = len;
                answer = tmp;
            }
            str = str.substring(pos + 1); // 처리된 띄어쓰기 앞은 자른다.
        }
        if(str.length() > max) answer = str; // 마지막 단어 체크 해준다.
        return answer;
    }

    public static void main(String[] args){
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine(); // 한 문장을 입력받는다.
        System.out.print(T.solution(str));
    }
}
```  

<hr/>

### 정리
> - `Integer.MIN_VALUE` : 가장 작은 값
> - `string.split(a)` : a를 기준으로 토막낸다. return String[]
> - Scanner 객체의 `nextLine()` : 한 단어가 아닌 문장을 입력 받는다.
> - `string.indexOf(a)` : a가 오는 위치의 인덱스. return int
> - `string.substring(a, b)` : 인덱스 [a, b-1] 부분을 뽑아낸다. return String
