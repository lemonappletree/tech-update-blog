# 🛠️ 2025-09-21 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
이 기술 블로그 글은 Kubernetes v1.34 버전에서 영구 볼륨 확장 실패 시 복구 기능이 일반 사용으로 제공되었음을 설명합니다. 이전에는 볼륨 확장 실패 시 수동으로 복구해야 했으며, 이는 클러스터 관리자 권한이 필요하고 번거로웠습니다. 새로운 버전에서는 사용자가 잘못된 용량을 요청한 경우, 확장이 완료되지 않았다면 즉시 크기를 수정할 수 있습니다. Kubernetes는 자동으로 이를 처리하며, 실패한 확장으로 소모된 할당량은 반환됩니다. 이 기능은 관리자의 개입 없이 작동하며, 볼륨 확장 중 에러 처리와 관찰 가능성이 향상되었습니다. Kubernetes는 실패한 볼륨 확장을 느린 속도로 재시도하고, 에러는 PVC 객체에 조건으로 보고됩니다. 이 기능은 오랜 버그를 수정하는 데에도 기여했습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
제목: Spring Modulith 2.0 M3 출시

요약: Spring Modulith 2.0 M3 버전이 출시되었습니다. 이번 릴리스에는 다음과 같은 새로운 기능이 포함되어 있습니다:

- JPA를 위한 이벤트 발행 저장소 구현 업데이트
- 직렬화된 이벤트 발행 외부화 지원
- Jackson 3를 이용한 이벤트 발행 직렬화 및 외부화 지원
- 헥사고날 아키텍처에 대한 더 관대한 기본 검증 제공
- Spring Boot 4.0 M3로 업그레이드
- jMolecules 2025 RC5로 업그레이드

자세한 사항은 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
블로그 글 요약: Docker는 Docker Desktop 4.46 버전부터 자동 구성 요소 업데이트와 완전히 새로워진 업데이트 경험을 도입하여 개발 도구를 최신 상태로 유지하는 방법을 개선했습니다. 이 업데이트는 사용자의 생산성을 우선시하여 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - JEP targeted to JDK 26: 504: Remove the Applet API
이 기술 블로그 글은 JDK 26에 목표로 한 JEP 504에 대해 다루고 있습니다. JEP 504는 Applet API를 제거하는 것을 목표로 하고 있습니다. 이는 Java 플랫폼에서 더 이상 필요하지 않기 때문에 API를 정리하는 과정의 일환입니다.
👉 [자세히 보기](https://inside.java/2025/09/19/jep504-target-jdk26/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
제목: 설문 조사 시간입니다! Go 언어는 어떻게 사용되고 있나요?  
요약: Go 언어의 미래를 함께 만들어가세요.  
링크: https://go.dev/blog/survey2025-announce

이 블로그 글은 Go 언어 사용자들을 대상으로 한 설문 조사를 안내하며, 설문 조사를 통해 Go 언어의 발전 방향을 결정하는 데 기여할 수 있음을 강조하고 있습니다. 독자들에게 설문 조사에 참여하여 자신의 경험과 의견을 공유함으로써 Go 언어의 미래를 만들어가는 과정에 동참할 것을 요청하고 있습니다.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어들면서, 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

