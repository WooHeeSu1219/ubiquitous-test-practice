# MARK-0105


def schedule(a):  # schedule() 함수 : 각 시간표의 출력을 저장해놓고 변수에 따라서 각 반의 시간표 출력
    if a == '1':
        print("월 : 과 영 수 진 한 국 자")
        print("화 : 체 역 과 음 한 수")
        print("수 : 영 사 실 과 체 한 국")
        print("목 : 사 음 수 역 국 과 한")
        print("금 : 국 역 영 사 동 동")
         
    elif a == '2':
        print("월 : 사 수 영 역 국 한 자")
        print("화 : 사 과 한 영 수 국")
        print("수 : 체 과 사 역 실 국 음")
        print("목 : 체 역 한 과 수 사 영")
        print("금 : 국 한 영 사 동 동")
        
    elif a == '3':
        print("월 : 수 한 과 체 음 사 자")
        print("화 : 사 역 국 한 진 체")
        print("수 : 과 국 한 영 역 사 수")
        print("목 : 실 영 수 국 과 음 역")
        print("금 : 사 영 과 국 동 동")
        
    elif a == '4':
        print("월 : 과 음 실 수 한 역 자")
        print("화 : 한 음 과 역 국 영")
        print("수 : 사 사 체 사 국 영 과")
        print("목 : 역 국 한 영 진 과 수")
        print("금 : 수 체 국 사 동 동")
        
    elif a == '5':
        print("월 : 국 역 음 과 영 체 자")
        print("화 : 국 사 영 수 한 사")
        print("수 : 진 실 영 수 사 국 역")
        print("목 : 음 한 체 국 역 과 과")
        print("금 : 역 사 과 수 동 동")
        
    elif a == '6':
        print("월 : 체 국 한 역 사 수 자")
        print("화 : 음 사 역 한 과 영")
        print("수 : 음 과 국 체 한 영 사")
        print("목 : 역 사 과 국 영 진 수")
        print("금 : 수 실 과 국 동 동")
        
    elif a == '7':
        print("월 : 정 수 체 국 사 사 자")
        print("화 : 수 국 미 과 사 정")
        print("수 : 실 수 진 과 역 국 영")
        print("목 : 국 과 영 정 사 역 체")
        print("금 : 역 과 영 미 동 동")
        
    elif a == '8':
        print("월 : 역 진 정 사 영 국 자")
        print("화 : 과 수 정 영 역 과")
        print("수 : 국 미 수 영 과 사 역")
        print("목 : 국 미 정 사 체 실 국")
        print("금 : 사 과 수 체 동 동")
        
    elif a == '9':
        print("월 : 영 정 사 수 역 과 자")
        print("화 : 과 체 사 국 정 국")
        print("수 : 과 역 사 국 정 미 진")
        print("목 : 실 사 역 국 과 수 영")
        print("금 : 미 영 체 수 동 동")
        
    elif a == '10':
        print("월 : 과 사 영 정 국 국 자")
        print("화 : 미 역 국 과 수 진")
        print("수 : 사 영 과 정 수 사 체")
        print("목 : 영 정 수 체 역 국 미")
        print("금 : 과 역 사 실 동 동")
        
    elif a == '11':
        print("월 : 사 체 국 미 영 정 자")
        print("화 : 사 과 진 수 역 과")
        print("수 : 역 체 국 미 영 사 수")
        print("목 : 사 과 역 수 정 실 국")
        print("금 : 영 국 정 과 동 동")
        
    elif a == '12':
        print("월 : 국 사 영 정 역 진 자")
        print("화 : 영 수 체 미 정 국")
        print("수 : 과 실 수 역 사 체 영")
        print("목 : 사 수 국 미 역 과 정")
        print("금 : 사 과 국 과 동 동")
        
    elif a == '13':
        print("월 : 미 역 국 과 정 수 자")
        print("화 : 역 국 영 사 체 정")
        print("수 : 수 사 정 영 과 진 실")
        print("목 : 과 체 사 영 미 국 사")
        print("금 : 과 수 역 국 동 동")

    return 0

def remain_time_cal(a,b):
    if a =='국어':
        if b <= 0.5:
            print("오늘 공부한 내용과 관련된 사자성어를 외워보세요.\n")
        elif b > 0.5 and b <=2:
            print("국어 지문을 하나 더 학습해보세요.\n")
        elif b > 2:
            print("학습 시간이 많이 부족합니다. 배운 내용의 개념부터 다시 확인해보세요.\n")
                                
    elif a =='영어':
        if b <= 0.5:
            print("오늘 공부한 지문의 영어 단어를 한 번 외워 보세요.\n")
        elif b > 0.5 and b <=2:
            print("영어 모의고사를 1회 실시해보세요.\n")
        elif b > 2:
            print("학습 시간이 많이 부족합니다. 수업 때 배운 영어 문법부터 다시 확인해보세요\n")
                                
    elif a =='수학':
        if b <= 0.5:
            print("오늘 공부한 부분의 중요한 수학 개념과 공식을 다시 짚어보세요.\n")
        elif b > 0.5 and b <=2:
            print("수업 내용과 관련된 수학 문제들을 풀어보세요.\n")
        elif real_time > 2:
            print("수학 모의고사를 1회 실시해보세요.\n") 
                                
    elif a =='사회' or a =='과학':
        if b <= 0.5:
            print("오늘 배운 내용의 탐구 개념을 다시 한 번 짚어보세요.\n")
        elif b > 0.5 and b <=2:
            print("탐구 모의고사를 1회 실시해보세요.\n")
        elif b > 2:
            print("유인물의 내용을 다시 한번 확인하며 내용을 정리해보세요.\n") 
    

print("\n이 어플리케이션은 공부에 집중 할 수 있는 환경을 만들고 공부습관을 관리하기 위한 프로그램입니다. \n") # 기본 프로그램 설명
print("지정된 숫자를 입력해 어플리케이션의 여러 기능들을 이용할 수 있습니다.\n")
print("1번을 입력해 사용자 등록 기능으로 프로그램을 시작해 주세요.\n")
print("해당 기능을 먼저 완료하신 후, 다른 기능을 이용해 주시기 바랍니다.\n \n")


print("0 : 프로그램 종료 및 랭킹 확인\n") #기능 코드 설명
print("1 : 사용자 등록 및 목표 설정\n")
print("2 : 사용자 정보 확인 및 시간표 확인\n")
print("3 : 사용자별 공부 시간 피드백\n")


user_all = [] #전체 배열
user_personal =[] #사용자별 배열

perfect = [] #완료한 사람들의 배열

non_perfect = [] #완료하지 못한 사람들/ 실공시간 모르는 사람들의 배열

input_stack = 0#input stack 설정
check = str
user_num = 0  # 등록된 사용자의 수

perfect_stack = 0 #완료한 사람의 수

non_perfect_stack = 0 #완료하지 못한/ 실공시간 모르는 사람의 수




while 1:
    if input_stack==0:
        print("기능 코드를 입력해주세요...\n")
        
    input_stack = 0 #input stack 초기화
    
    n = str(input()) # 기능 코드 입력받기
    
    #-------------------------------------------------------------------------------------

    if n=='0':
        
        if user_all==[]: #등록된 사람 없을 때
            print("\n등록된 사용자가 없습니다.\n")
            print("프로그램을 종료합니다...\n")
            
        else:
            for i in range(0,user_num,1): #등록된 사람 있을 때
                if len(user_all[i])==7 and user_all[i][7] == '학습 완료': #완료한 사람은
                    perfect.append(user_all[i]) #완료배열에 추가
                    perfect_stack += 1 #완료한 사람 + 1
                else: #미완인 사람
                    non_perfect.append(user_all[i]) #미완배열에 추가
                    non_perfect_stack += 1 #미완 사람 + 1
                    
            for i in range(0,perfect_stack,1): #완료인만큼 반복(완료인 사람들 랭킹 정렬)
                for j in range(i,perfect_stack,1): #버블소트 알고리즘
                    if(perfect[i][6] < perfect[j][6]): #앞사람의 실공시간이 작으면 교체
                        tmp = perfect[i][6]
                        perfect[i][6] = perfect[j][6]
                        perfect[j][6] = tmp
                        
            for i in range(0,non_perfect_stack,1): #미완인 만큼 반복(미완료인 사람들 랭킹 정렬)
                for j in range(i,non_perfect_stack,1): #버블소트 알고리즘
                    if(non_perfect[i][6] < non_perfect[j][6]): #앞사람의 실공시간이 작으면 교체
                        tmp = non_perfect[i][6]
                        non_perfect[i][6] = non_perfect[j][6]
                        non_perfect[j][6] = tmp
                        
            print("\n-----공부 목표 완료-----\n")
            for i in range(0,perfect_stack,1):
                print("<%d> %s %s시간 \n" %(i+1, perfect[i][0], perfect[i][6]))
                
            print("\n-----공부 목표 미완료-----\n")
            for i in range(0,non_perfect_stack,1):
                print("<%d> %s %s시간 \n" %(i+1, non_perfect[i][0], non_perfect[i][6]))
        break
    
    #-------------------------------------------------------------------------------------

    elif n=='1':  #사용자 등록하기
        
        while 1:
            print("\n사용자의 이름, 학교명, 학년, 반, 목표 공부 시간, 공부할 과목명을 입력해주세요.\n")
            print("EX)우희수/충남여자고등학교/1/13/3/국어\n") #형식에 맞게 입력
            name, school_name, grade, class_number, study_time, subject = map(str,input().split('/')) 
            if name=='X':
                break
            else:
                user_personal =[name, school_name, grade, class_number, study_time, subject]
                user_all.append(user_personal)
                user_personal=[]  # .split() 함수로 입력한 내용 쪼개서 배열에 저장
                user_num += 1 # 등록된 사용자의 수 + 1
                print("\n등록을 완료했습니다.\n")
        

            
            
    #-------------------------------------------------------------------------------------

    elif n=='2': #사용자 정보 확인 및 시간표 확인 기능
        
        if user_all==[]:
            print("\n등록된 사용자가 없습니다.\n")
            print("사용자 등록 후 다시 시도해주세요.\n")
            print("이전 기능으로 돌아가겠습니다...\n")
            
        else:
            print("\n사용자의 이름을 입력해주세요.\n")
            user_name = str(input())
            for i in range(0,user_num,1):
                if user_all[i][0] == user_name:
                    print("\n사용자 정보 :",user_all[i],"\n")
                    schedule(user_all[i][3])
                    print("\n시간표에 따라 각 수업에 필요한 유인물, 과제, 수행평가 등을 다시 한번 확인하고 미리 준비해주세요.\n")
    
        
            


    #-------------------------------------------------------------------------------------
        
    elif n=='3':
        if user_all==[]:
            print("\n등록된 사용자가 없습니다.\n")
            print("사용자 등록 후 다시 시도해주세요.\n")
            print("이전 기능으로 돌아가겠습니다...\n")
            
        else:
            print("\n사용자의 이름을 입력해주세요.\n")
            user_name = str(input())
            for i in range(0,user_num,1):
                if user_all[i][0] == user_name:
                    print("\n%s 사용자님이 확인되셨습니다. 오늘의 공부 시간을 소수점 아래 두 자리까지 입력해주세요.\n" %user_all[i][0])
                    print("EX) 2시간 30분 > 2.50 / 3시간 15분 > 3.25\n")
                    real_time = float(input())
                    word_real_time = "%.2f" %real_time #실공시간 문자변환
                    user_all[i].append(word_real_time) #실공시간 배열에 추가
                    goal_study_time = float(user_all[i][4]) #목표시간 소수화
                    
                    if real_time >= goal_study_time :
                        print("\n목표 시간을 달성하셨습니다. 축하드립니다.\n")
                        user_all[i].append('학습 완료') #학습완료 배열에 추가
                        
                    else :
                        remain_time = goal_study_time - real_time
                        print("\n오늘의 남은 공부 시간은 %.2f시간입니다.\n" %remain_time)
                        word_remain_time = "%.2f" %remain_time # 남은시간 문자변환
                        user_all[i].append(word_remain_time) #남은시간 배열에 추가
                        
                        remain_time_cal(user_all[i][5],remain_time) #시간/과목에 따른 피드백 적용


    #-------------------------------------------------------------------------------------

    else:
        print("\n잘못 입력하셨습니다. 올바른 기능 코드를 다시 입력해주세요...\n")
        input_stack += 1 #input stack 적립해서 같은말 반복하지 않게 하기
        

        ##   0 이름   1 학교    2 학년   3 반   4 목표시간   5 과목   6 실공시간   7 (남은시간)/학습완료오전 1:01 2026-01-05