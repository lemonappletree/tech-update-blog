# 🛠️ 2025-07-15 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 기술 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 사용하는 파드의 장애를 처리하는 데 어려움이 있다는 점을 다룹니다. AI/ML 워크로드의 증가로 인해 이러한 특수 장비에 대한 의존도가 높아졌고, 장비 장애는 성능 저하와 작업 중단을 초래할 수 있습니다. 기존의 Kubernetes는 자원 관리가 정적이어서 하드웨어 장애를 효과적으로 처리하지 못합니다. 이 글은 AI/ML 워크로드의 특성과 이를 지원하기 위해 Kubernetes의 확장 가능성과 현재의 DIY 솔루션들을 설명하며, 향후 개선 방향을 제시합니다. Kubernetes는 AI/ML 워크로드에 적합한 플랫폼으로 계속해서 발전하고 있으며, 커뮤니티의 참여를 통해 더 나은 장애 처리 방안을 모색하고자 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - Spring Cloud 2024.0.2 (aka Moorgate) Has Been Released
Spring Cloud 2024.0.2 (Moorgate) 버전이 공식 출시되었다. 이 버전은 주로 버그 수정과 종속성 업데이트를 포함하며, Spring Boot 3.4.x 세대와 호환된다. 업데이트된 모듈로는 Spring Cloud Kubernetes, Spring Cloud Function, Spring Cloud Zookeeper, Spring Cloud Commons, Spring Cloud Task, Spring Cloud Vault, Spring Cloud Openfeign, Spring Cloud Circuitbreaker, Spring Cloud Netflix, Spring Cloud Starter Build, Spring Cloud Stream, Spring Cloud Gateway, Spring Cloud Config, Spring Cloud Consul, Spring Cloud Build, Spring Cloud Contract 등이 있다. 피드백은 GitHub, Gitter, Stack Overflow, Twitter를 통해 받을 수 있으며, Maven과 Gradle을 통해 프로젝트에 통합할 수 있다.
👉 [자세히 보기](https://spring.io/blog/2025/07/14/spring-cloud-2024-0-2-aka-moorgate-has-been-released)

## 🔹 Docker - AI-Powered Testing: Using Docker Model Runner with Microcks for Dynamic Mock APIs
이 기술 블로그 글은 AI를 활용한 테스트 방법에 대해 설명하고 있습니다. 특히, Docker의 Model Runner와 Microcks를 사용하여 동적인 모의 API를 생성하는 방법을 다루고 있습니다. LLM의 비결정적인 특성은 풍부하고 동적인 테스트 데이터를 생성하는 데 이상적이며, 이는 앱의 동작을 검증하고 일관되고 높은 품질의 사용자 경험을 보장하는 데 유용합니다. 이 글에서는 CNCF 도구인 Microcks를 활용하여 애플리케이션 테스트를 위한 모의 API를 생성하는 구체적인 방법을 안내합니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-powered-mock-apis-for-testing-with-docker-and-microcks/)

## 🔹 Java - Java GPGPU Enablement: Are We There Yet?
이 기술 블로그 글에서는 Java에서 데이터 병렬 처리 문제를 해결하기 위해 멀티 커널 알고리즘을 Java로 표현하고, 이러한 커널들이 서로 및 JVM과 효율적으로 데이터를 교환할 수 있도록 하는 방법을 다룹니다. 이를 위해 HAT(Heterogeneous Accelerator Toolkit)를 소개하며, HAT가 최근 Java 개선 사항(Panama 및 Babylon)을 활용하여 Java 개발자가 GPU의 잠재력을 활용할 수 있도록 하는 방법을 시연합니다.
👉 [자세히 보기](https://inside.java/2025/07/14/javaone-hat/)

## 🔹 Golang - Generic interfaces
제목: 제네릭 인터페이스

요약: 인터페이스 타입에 타입 매개변수를 추가하는 것은 매우 강력한 기능입니다. 이 블로그 글에서는 제네릭 인터페이스의 구현 방법과 그로 인해 얻을 수 있는 이점을 설명하고 있습니다. 제네릭을 사용함으로써 코드의 유연성과 재사용성을 높일 수 있으며, 다양한 타입을 안전하고 효율적으로 처리할 수 있는 방법을 제공합니다.
👉 [자세히 보기](https://go.dev/blog/generic-interfaces)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 헬름

요약: 헬름 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 후반에 출시 예정인 헬름 4에 대한 대화에 참여하려면 발표 세션과 프로젝트 파빌리온의 헬름 부스를 방문하세요. 주간 동안의 모든 헬름 관련 활동에 대한 자세한 내용은 아래에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

