Recursion & Dynamic Programming

Recursion (재귀호출) - up-bottom
 문제 반복: 큰 문제를 세분화 해서 비슷한 형태의 작은 문제들로 만들겠다.
    ex) !(Factorial) : n과 나머지를 분리 후 해결, n,n-1 과 나머지를 분리 후 해결...
        최대공약수; Euclid's algorithm
        점화식
        피보나치 수열
 나누고 해결: 문제 자체를 쪼개서 해결해 나가는 행 위
함수 내에서 함수를 호출하는 것.
(pseudo code : 간략하게 코딩설계를 해 놓은 코드)
'''
pseudo code
def function(target):
    ...
    functionA(target')
    ...
    if escapeCondition:
        return A;
'''
recursion의 문제: function call이 너무 많다!
    이 문제를 해결하기 위해서는? - Dynamic Programming이용 -bottom-up
    서브 인스턴스가 오버래핑 많이 오버래핑 하는 것을 해결!
    - Memoization
    기존의 함수호출과 결과의 저장을 재활용하기 위한 기법
    - Assembly Line Scheduling
    

재귀함수 호출
 재귀호출 탈출
 재귀호출 종료
Dynamic Programming
 이전 함수 콜 결과를 재활용
 시간 절역을 위한 메모라이징

Merge Sort
 Recursion을 이용한 sorting algorithm의 한 종류

root에서 Leaves 까지 최단 거리(A -> E) :Path to E
Path의 길이 : Depth
Tree의 높이 : Height(Path가 가장 긴 경로 기준)
특정 노의 Child의 수 : Degree
Size of Tree: 트리의 전체 노드 개수

Full Tree: 노드의 넥스트가 모두 차있는 트리.
Complete Tree: Full Tree의 자식 노드들이 왼쪽부터 채워져 나가는 상태.

엣지(간선)의 수: 노드 - 1 
트리의 정의와 다양한 특성

트리의 구조 -(1); Binary Search Tree(BST)
degree = 2 인 트리

트리는 루트에대한 엑세스만 가진다.

Delete operation of Binary search Tree(1)
Deletion Cases
 1. No child Case: Parent Node로 가서 엣지를 끊는다.

 2. one child Case: 제거할 노드를 끊고 Only One Child로 엣지를 잇는다.
  (제거할 노드는 child노드를 가리킬 수 있지만 제거할 노드를 가리킬 수 있는 것이
  없으므로 그 노드는 없다고 볼 수 있다. Python내에서 Garbage Collector가
  나중에 자연스럽게 끊긴 노드를 지운다.)

 3. Two child Case:
 LHS의 최소값을 제거할 노드와 바꾸고 그 최소값의 노드의 엣지를 끊는다.
 RHS의 최대값을 제거할 노드와 바꾸고 그 최대값의 노드의 엣지를 끊는다.

Tree Traversing
 Depth first traverse
  pre-order traverse
  In-order traverse
  Post-order traverse

Performane of binary search tree
 O라는 것은 BST의 성능에 따라 차이가 있다.