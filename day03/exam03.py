# 평면 도형으 꼭지점 개수를 입력하면 입체 도형으로 확장했을 때의 꼭지점, 선, 면의 개수를 구하는 프로그램을 작성

a = int(input("꼭지점의 개수를 입력하세요: "))
dot = a *2
line = a * 3
plane = a + 2
print("꼭지점: {}, 선: {}, 면: {}".format(dot,line,plane))
