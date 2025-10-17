# 🛠️ 2025-10-17 기술 업데이트 요약

## 🔹 Kubernetes - Introducing Headlamp Plugin for Karpenter - Scaling and Visibility
이 글은 Karpenter를 위한 Headlamp 플러그인을 소개합니다. Headlamp는 Kubernetes 클러스터 리소스를 탐색하고 관리하며 디버그할 수 있는 오픈 소스 UI 프로젝트입니다. Karpenter는 클러스터가 빠르고 효율적으로 확장할 수 있도록 돕는 자동 스케일링 노드 프로비저닝 프로젝트입니다. 새롭게 추가된 Headlamp Karpenter 플러그인은 Headlamp UI에서 Karpenter의 활동을 실시간으로 모니터링할 수 있게 해줍니다. 이를 통해 Karpenter 리소스와 Kubernetes 객체 간의 관계를 보여주고, 실시간 메트릭을 제공하며, 스케일링 이벤트를 시각화합니다. 사용자는 프로비저닝 중인 대기 중인 파드를 검사하고 스케일링 결정을 검토하며, Karpenter가 관리하는 리소스를 편집할 수 있습니다. 이 플러그인은 Kubernetes 사용자가 클러스터의 자동 스케일링 동작을 이해하고 디버그하며 최적화하는 데 도움을 주기 위해 개발되었습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/10/06/introducing-headlamp-plugin-for-karpenter/)

## 🔹 Spring Boot - Spring Framework 7.0.0-RC1 available now
Spring Framework 7.0의 첫 번째 릴리스 후보 버전이 발표되었습니다. 이번 버전에서는 회복력 기능이 개선되어 예외 원인에 대한 매칭 및 특정 예외 유형 포함/제외가 가능합니다. 또한, 새로운 @ConcurrencyLimit 프로그래매틱 변형이 추가되었습니다. 코틀린 코루틴의 컨텍스트 전파가 개선되어, ContextPropagationElement 연산자가 코틀린 사용자에게 더 적합하게 수정되었습니다. API 버전 관리를 위한 기능도 추가되었습니다. 기본 라이브러리 업그레이드로는 JUnit 6.0과 Jackson 3.0을 지원합니다. 자세한 변경 사항은 릴리스 노트를 참고할 수 있습니다. 이번 RC1은 Spring 저장소와 Maven Central에서 사용할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/10/16/spring-framework-7-0-0-RC1-available-now)

## 🔹 Docker - Debug Docker Builds with Visual Studio Code
이 블로그 글은 Visual Studio Code를 사용하여 Docker 이미지를 디버깅하는 방법에 대해 설명합니다. Docker 이미지는 현대 애플리케이션의 소프트웨어 전달 파이프라인에서 중요한 역할을 하며, 애플리케이션과 서비스를 패키징하여 배포 및 프로덕션 환경에 사용할 수 있도록 합니다. Dockerfile은 컨테이너 이미지를 정의하는 표준이지만, 이를 작성하고 디버깅하는 데 어려움이 있을 수 있습니다. 이 글은 이러한 어려움을 해결하기 위한 방법을 소개합니다.
👉 [자세히 보기](https://www.docker.com/blog/debug-docker-builds-with-visual-studio-code/)

## 🔹 Java - Structured Concurrency in Action
Java 25에서는 구조화된 동시성 API가 다섯 번째 미리보기로 소개되었으며, 이전 버전들에 비해 상당한 변화가 있었습니다. 이 API가 더 이상의 큰 변화 없이 최종 확정될 가능성이 높은 상황에서, 이 글에서는 동시성을 갖춘 코드를 구조화하는 방법, 오류 및 취소를 처리하고 전파하는 방법, 스레드 간의 관계를 관찰하는 방법, 그리고 반응형 접근 방식에서 리팩토링하는 방법을 탐구합니다. 이 발표를 통해 프로젝트에서 구조화된 동시성 API를 활용할 준비를 할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/10/16/devoxxbelgium-structured-concurrency-action/)

## 🔹 Golang - Flight Recorder in Go 1.25
제목: Go 1.25의 비행 기록기  
요약: Go 1.25 버전에서는 진단 도구 모음에 새로운 도구인 비행 기록기가 도입되었습니다. 이 도구는 프로그램 실행 중 발생하는 다양한 이벤트를 기록하여 성능 분석과 디버깅에 도움을 줍니다.  
링크: [Go Blog - Flight Recorder](https://go.dev/blog/flight-recorder)
👉 [자세히 보기](https://go.dev/blog/flight-recorder)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로  
요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어든 만큼, 현재 진행 상황과 커뮤니티가 참여할 수 있는 방법에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

