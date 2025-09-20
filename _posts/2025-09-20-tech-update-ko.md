# 🛠️ 2025-09-20 기술 업데이트 요약

## 🔹 Kubernetes - Kubernetes v1.34: Recovery From Volume Expansion Failure (GA)
Kubernetes v1.34 버전에서는 영구 볼륨 확장 실패 시 자동 복구 기능이 일반 사용(GA)으로 제공됩니다. 이전에는 클러스터 관리자 권한이 필요하여 수작업으로 복구해야 했지만, 이제는 사용자가 영구 볼륨 클레임(PVC) 크기를 줄여 복구할 수 있으며, Kubernetes가 자동으로 이를 수정합니다. 이 기능은 잘못된 크기로 인해 소모된 할당량을 사용자에게 반환하고, 연관된 영구 볼륨을 최신 크기로 조정합니다. 또한, 볼륨 확장 과정의 오류 처리 및 관찰 기능이 개선되어, 확장 진행 상황을 쉽게 모니터링할 수 있습니다. 이러한 개선 사항은 볼륨 확장 워크플로우의 오랜 버그를 수정하는 데에도 기여했습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/09/19/kubernetes-v1-34-recover-expansion-failure/)

## 🔹 Spring Boot - Spring Modulith 2.0 M3 released
Spring Modulith 2.0 M3 버전이 출시되었습니다. 이번 릴리스에서는 다음과 같은 새로운 기능들이 포함되었습니다: JPA를 위한 이벤트 게시 저장소 구현 업데이트, 직렬화된 이벤트 게시 외부화 지원, 이벤트 게시 직렬화 및 외부화를 위한 Jackson 3 지원, 육각형 아키텍처에 대한 보다 유연한 기본 검증, Spring Boot 4.0 M3 및 jMolecules 2025 RC5로의 업그레이드 등이 있습니다. 자세한 내용은 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/09/19/spring-modulith-2-0-m3-released)

## 🔹 Docker - Silent Component Updates & Redesigned Update Experience
Docker Desktop의 업데이트 방식을 개선하기 위한 이전 이니셔티브에 이어, Docker Desktop 4.46 버전부터 자동 구성 요소 업데이트와 완전히 새로워진 업데이트 경험을 도입하게 되었다는 소식입니다. 이 업데이트는 개발 도구를 최신 상태로 유지하면서 사용자 생산성을 우선시하는 방향으로 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/docker-desktop-silent-component-updates/)

## 🔹 Java - JEP targeted to JDK 26: 504: Remove the Applet API
블로그 글은 JDK 26 버전에서 Applet API를 제거하는 JEP 504에 대한 내용을 다루고 있습니다. 이 JEP는 Applet API의 제거를 목표로 하고 있으며, 이는 최신 자바 개발 환경에서 더 이상 필요하지 않기 때문에 이루어지는 조치입니다.
👉 [자세히 보기](https://inside.java/2025/09/19/jep504-target-jdk26/)

## 🔹 Golang - It's survey time! How has Go has been working out for you?
이 블로그 글은 Go 언어 사용자들을 대상으로 한 설문조사를 소개하고 있습니다. 설문조사를 통해 사용자의 피드백을 수집하여 Go 언어의 미래 발전 방향을 결정하는 데 도움을 주고자 합니다. Go 언어 사용자들은 설문조사에 참여함으로써 언어의 개선과 발전에 기여할 수 있습니다.
👉 [자세히 보기](https://go.dev/blog/survey2025-announce)

## 🔹 Helm - Path To Releasing Helm v4
제목: Helm v4 출시 경로

요약: Helm v4의 첫 번째 알파 버전이 출시되었습니다. Helm v4 개발이 마무리 단계에 접어들면서 현재 진행 상황과 더 넓은 커뮤니티가 어떻게 참여할 수 있는지에 대한 세부 사항을 공유하고자 합니다.
👉 [자세히 보기](https://helm.sh/blog/path-to-helm-v4/)

