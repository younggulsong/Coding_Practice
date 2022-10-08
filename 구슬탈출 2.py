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


'''




'''