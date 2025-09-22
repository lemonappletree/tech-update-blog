# 🛠️ 2025-09-22 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
블로그 글은 Kubernetes v1.34에서 볼륨 확장 실패 시 자동 복구 기능이 GA(일반 공급) 단계에 도달했음을 설명합니다. 이전에는 잘못된 볼륨 확장 요청을 수동으로 복구해야 했고, 이는 번거로웠지만 이제는 Kubernetes가 자동으로 이를 수정할 수 있습니다. 사용자는 잘못된 크기로 확장 요청을 했을 때, 이전 요청이 완료되지 않았다면 요청 크기를 줄여 수정할 수 있으며, 이에 따라 소비된 할당량도 자동으로 반환됩니다. 또한, 볼륨 확장 중 발생하는 오류 처리 및 관찰 가능성이 개선되었으며, 몇 가지 오랜 버그가 해결되었습니다. 이 기능은 다양한 기여자들의 피드백을 통해 발전해왔습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
Spring Modulith 2.0 M3가 출시되었습니다. 이번 릴리스에는 다음과 같은 새로운 기능들이 포함되어 있습니다:

- JPA용 이벤트 발행 저장소 구현 업데이트
- 직렬화된 이벤트 발행 외부화 지원
- 이벤트 발행 직렬화 및 외부화를 위한 Jackson 3 지원
- 육각형 아키텍처에 대한 더 관대한 기본 검증
- Spring Boot 4.0 M3로 업그레이드
- jMolecules 2025 RC5로 업그레이드

자세한 사항은 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
Docker Desktop 4.46 버전부터 도입되는 자동 구성 요소 업데이트와 새롭게 설계된 업데이트 경험에 대해 설명하는 기술 블로그 글입니다. 이 업데이트는 Docker Desktop의 업데이트 방식을 개선하여 개발 도구를 최신 상태로 유지하는 데 중점을 두고 있습니다. 사용자의 생산성을 우선시하며, 업데이트 과정을 간소화하고 자동화하여 사용자 경험을 향상시키고자 하는 목표를 가지고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - Paths to Support Additional Numeric Types on the Java Platform #JVMLS
이 기술 블로그 글은 자바 플랫폼에서 새로운 숫자 타입을 지원하기 위한 다양한 경로와 그에 따른 고려 사항에 대해 설명합니다. 자바 플랫폼의 숫자 타입은 오랜 기간 동안 안정적으로 유지되어 왔으나, 과학 및 공학 계산에서는 선형 대수와 복소수가 중요하고, 머신러닝에서는 16비트 부동 소수점 숫자와 같은 더 작은 숫자 타입이 필요합니다. IEEE SA 작업 그룹 P3109는 머신러닝을 위한 8비트 부동 소수점 형식의 표준화도 연구 중입니다. 이 발표에서는 자바 플랫폼에서 새로운 숫자 타입을 완전히 지원하는 데 필요한 요소와 다양한 지원 경로의 장단점을 논의합니다.
👉 [자세히 보기](https://inside.java/2025/09/21/jvmls-java-additional-numeric-types/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
블로그 글 요약: "Go 언어의 미래를 함께 만들어가요! Go 언어 사용자들의 의견을 듣기 위해 설문 조사가 진행 중입니다. 사용 경험을 공유하여 Go의 발전에 기여할 수 있는 기회를 놓치지 마세요."
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 막바지에 이르렀기 때문에, 우리는 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 정보를 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

