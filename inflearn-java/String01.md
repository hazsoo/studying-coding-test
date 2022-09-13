# 1. 문자 찾기
설명

한 개의 문자열을 입력받고, 특정 문자를 입력받아 해당 특정문자가 입력받은 문자열에 몇 개 존재하는지 알아내는 프로그램을 작성하세요.

대소문자를 구분하지 않습니다.문자열의 길이는 100을 넘지 않습니다.


입력  
첫 줄에 문자열이 주어지고, 두 번째 줄에 문자가 주어진다.

문자열은 영어 알파벳으로만 구성되어 있습니다.
  

출력  
첫 줄에 해당 문자의 개수를 출력한다.
  

예시 입력 1   
Computercooler  
c
  
예시 출력 1  
2  

```java
import java.util.Scanner;

class Main {
    public int solution(String str, char t){ // 프로그래머스 방식으로 출력
        int answer=0;
        str = str.toUpperCase(); // 대문자로 만든다.
        t = Character.toUpperCase(t); // char는 Character 클래스 활용하여 대문자로 만든다.
        // System.out.println(str + " " + t);
        for(int i = 0; i < str.length(); i++){
            if(str.charAt(i) == t)
                answer++; // String의 인덱스 i의 문자 하나하나 탐색한다.
        }

        return answer;
    }

    public static void main(String[] args){ // 백준 방식으로 입력받고
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        char c = kb.next().charAt(0); // String에서 0번째 인덱스의 문자를 char로 들고온다.
        System.out.print(T.solution(str, c));
    }
}
```
##### *** for 문 for each 구문도 가능
for(type data : 배열이나 리스트){

}
```java
    for(char x : str.toCharArray()){ // String의 문자 하나하나로 새로운 문자배열을 생성한다.
            if(x == t) answer++;
        }
```

<hr/>
  
### 정리
> - `string.toUpperCase()` : string을 대문자로 만든다.
> - `Character.toUpperCase(char)` : char를 대문자로 만든다.
> - `string.toCharArray()` : string의 문자들로 문자 배열을 만든다.
> - `string.charAt(index)` : string의 index번째 문자를 char로 들고온다.
