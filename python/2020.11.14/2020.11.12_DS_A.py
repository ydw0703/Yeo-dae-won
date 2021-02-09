integrated development environment(IDE) : 컴파일,디버깅하고\
콘솔창, 터미널,스크립트창도 보이고 배포(실행파일생성)도 가능하게 해주는
"통합 개발 환경"이라는 뜻의 응용 소프트웨어 프로그램.

절차적 프로그래밍(procedure-oriented_programming)
main() is a function

객체지향 프로그래밍(Object-doriented_programming)
main() is a class

def main():
<-->print()

indentation  

class Helloworld():
    def performance(self,val1,val2)

def main():
    world=Helloworld()
    world.method(score1,score2) #val1=score1,val2=score2,self=world

Naming and Styling
- Camel casing :낙타의 봉우리 처럼 단어의 뜻마다 대문자로 튀어나온 형태
    1. Class name 
    2. Varible name :맨 첫 글자는 소문자가 좋다.
    3. Method name :맨 첫 글자는 소문자가 좋다.
Java,C에서는 변수형을 선언해 주어야 변수의 형이 생기는데 (ex. int x=0)
Python에서는 앞에 따로 선언 해주지 않아도 나중에 선언 가능(ex. x=0)

복소수 표현
complex(3,4)는 3+4j 와 같다.
x= 4+3j 에서, 내부에서는 오브젝트 클래스 형태로 선언되어있고 \
외부로 x로 인스턴스화 되어있는 거다! 
x.real >>>3
x.imag >>>4
(인스턴스 == 추상화 개념,클래스 객체, 컴퓨터 프로세스 등과 같은 템플릿이\
실제 구현된 것) 변수 선언, 만든 함수, 클래스를 executation하는 것도 다 인스턴스!

%d #정수 표현
%f #소수점 아래까지 표현

튜플 언패킹
a,b=b,a
언팩 연산자
*x #x에 저장되는 요소들이 튜플로 변환됨.