import java.util.Scanner;
// 금액 입력을 받기 위한 Scanner

public class taxi { // 클래스 생성
	
	public static void main(String[] args) { // main 함수
		
		int income = 0; // 수입 초기화
		
		do {
			// 금액 입력 받기
			System.out.print("금액을 지불하세요 : ");
			Scanner scan = new Scanner(System.in);
			int coin = scan.nextInt();
			
			income += coin; 
            // 수입 = 현재 수입 + 지불 금액
			
			if(income < 10000) {
				System.out.println("현재 수입은 : " + income + "원");
			}
			else {
				scan.close(); 
                // scanner 사용 완료 후, 사용 종료 (필수X)
			}

		}while (income < 10000); // 50000원이면 퇴근
		
		System.out.println("축하합니다!\n" + "현재 수입은 " + income + "원 입니다.\n");
        System.out.println("오늘 할당량을 채웠으니 퇴근하세요!😊");
	}
}
