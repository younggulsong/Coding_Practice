'''
'.'은 구슬이 이동할 수 있는 곳. '#' 은 벽, 구슬의 위치는 각각 'R', 'B'로 표시된다. 빨간 구슬이 구멍에 빠지면 게임 끝, 파란 구슬이 구멍에 빠지면 다시 시작해야 함
최소로 구슬을 움직이는 횟수는 몇번인지 구해야 한다.

-initialize
1. 빨간 구슬과 파란 구슬의 위치를 알아야 한다. ball_pos=[r_R, c_R, r_B, c_B, status=0] 이런 식으로 저장한다.
2. 빨간 구슬과 파란 구슬의 위치를 q에 저장한다. 해당 위치에서 기울이는 방향에 따라 분기가 나뉜다.
cnt=0으로 시작
-Game start (while 시작)
3. q를 모두 pop()해서 새로운 위치정보를 모두 저장한다. pos_list
    cnt+=1
3. for pos in pos_list:
    3. 게임판을 네 방향으로 기울여 본다. dr[i],dc[i]로 방향 define 필요
    for i in range(4)
    m!!! move 함수 다시 정해야 겠다! move(pos,i)  pos[0]~pos[3] : rr,rc,br,bc 이렇게 지정.
        move(pos) -> return pos_moved, status     (status:0,1,2) 1: B가 빠짐. iteration다시 2: R빠짐 완료
            rcnt=0, bcnt=0 선언
            Loop 선언(while?)
                pos에서 rr,rc,br,bc 읽어들임
                rr_, rc_, br_, bc_ 는 +dr[i], +dc[i]만큼 한칸씩 앞에를 탐색
                1. board[rr_][rc_]가 '.'이면 rr=rr_, rc=rc_, rcnt+=1
                2. board[br_][bc_]가 '.'이면 br=br_, bc=bc_, bcnt+=1
                3. '#'이면 그냥 넘어감 조건 넣을 필요는 없음.
                4. 'R'과 'B'위치가 같으면 (rr==br, rc==bc)
                    4-1 만약 rcnt>bcnt이면 rr-=dr[i], rc-=dc[i] 하고 break
                    4-2 만약 rcnt<bcnt이면 br-=dr[i], bc-=dc[i] 하고 break
                위치 결정 됬으니, 이쯤에서, pos_moved에 rr,rc,br,bc 입력
                5. 'B'이 'O'이면 status=1 하고 break
                6. 'R'이 'O'이면 status=2 하고 break
                7. pos==pos_moved이면 break
                8. pos!=pos_moved이면 pos=pos_moved
            return pos_moved, status로 완료
    pos_moved = move(pos)
    1. status==2이면 return cnt하고 끝냄
    2. status==1이면 q에 더이상 넣지 않고 status=0하고 continue
    3. pos_moved == pos이면 q에 넣지 않고 continue
    4. pos_moved != pos이면 q.append(pos_moved)하고 loop 재시작
    움직이고 나서 위치가 변하지 않으면, q에 update하지 않는다.



    4. 기울인 방향으로 구슬이 진행한다.
        함수 move(ball_position) 선언: return 값: ball_pos
        copy_board = copy.deepcopy(board)로 복사한다.
        원래 위치를 복사한다. ball_pos_copy = copy.deepcopy(ball_pos)
        4-1. 1-step에 r_ = r+dr[i],c_ = c+dc[i]로 진행 방향을 탐색한다.
        4-2. r_,c_가 '.' 이면, r=r_, c=c_로 update한다.
        4-3. r_,c_가 벽이면, r,c를 업데이트하지 않는다.
        4-4. r_,c_가 다른 구슬이면,
            4-4-1 다른구슬의 r_,c_가 r,c와 다르면 r=r_, c=c_로 update한다.
            4-4-2 다른 구슬의 r_,c_가 r,c와 같으면 update하지 않는다.
        4-5 만약 r_R, c_R이 'O'이면, 완료 signal을 준다. status=1
        4-6 만약 r_B, c_B이 'O'이면, 종료 signal을 준다. status=2
        4-7 만약 r,c가 변하지 않으면, r,c값을 return하여 함수를 마친다.
    5. move 진행 후 status=1이면 함수 cnt 값을 return한다. (최소값이므로)
    6. status = 2이면 다음 턴으로 넘어간다.

#문제가 있는데, R,B의 위치는 어떻게 지정해야 좋을지..
board에서 R,B의 위치만 받은 다음에, board에 있는 R,B를 지운다.
R,B의 pos는 따로 관리한다. board는 변하지 않음. [r,c,r,c,cnt]이렇게 관리하면? 그런데 cnt가 그렇게 되면 BFS에서도 완전 탐색으로 하는 수밖에 없으니 안좋아

'''
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
board = [[ele for ele in input().strip()] for _ in range(N)]
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def get_ball_pos(board):
    ball_pos=[0,0,0,0]
    for r in range(N):
        for c in range(M):
            if board[r][c]=='R':
                board[r][c]='.'
                ball_pos[0]=r
                ball_pos[1]=c
            elif board[r][c]=='B':
                board[r][c]='.'
                ball_pos[2] = r
                ball_pos[3] = c
    return ball_pos

def move(pos, i):
    status=0
    rcnt = 0
    bcnt = 0
    pos_moved = [0,0,0,0]
    while True:
        rr, rc, br, bc = pos
        rr_, rc_, br_, bc_ = rr+dr[i], rc+dc[i],br+dr[i], bc+dc[i]
        if board[rr_][rc_] !='#':
            rr = rr_
            rc = rc_
            rcnt+=1
        if board[br_][bc_] != '#':
            br = br_
            bc = bc_
            bcnt+=1
        pos_moved = [rr,rc,br,bc]
        if rr== br and rc==bc:
            if rcnt>bcnt:
                rr -= dr[i]
                rc -= dc[i]
                pos_moved = [rr, rc, br, bc]
                break
            if rcnt<bcnt:
                br -= dr[i]
                bc -= dc[i]
                pos_moved = [rr, rc, br, bc]
                break
        if board[rr][rc] == 'O':#rr,rc의 처리를 해야하네.
            pos_moved[0]=0
            pos_moved[1]=0
            status=2
        if board[br][bc] == 'O':
            status=1
            return pos_moved, status
        if pos == pos_moved:
            return pos_moved, status
        if pos!=pos_moved:
            pos=pos_moved
    return pos_moved, status

def main():
    #initialize
    ball_pos= get_ball_pos(board)
    q=deque()
    q.append(ball_pos)
    cnt=0
    while cnt<10:
        cnt+=1
        pos_list=[]
        while q:
            pos_list.append(q.pop())
        for pos in pos_list:
            for i in range(4):
                pos_moved,status = move(pos,i)
                if status ==2:
                    return cnt
                if status ==1:
                    continue
                if pos_moved ==pos: #안움직였으므로 그냥 버림
                    continue
                if pos_moved!=pos:
                    q.append(pos_moved)
    return -1

print(main())



