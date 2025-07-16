# 🛠️ 2025-07-16 기술 업데이트 요약

## 🔹 Kubernetes - Navigating Failures in Pods With Devices
이 기술 블로그 글은 Kubernetes에서 GPU와 같은 특수 하드웨어를 사용하는 포드의 실패를 관리하는 데 있어 직면하는 도전 과제와 관련된 내용을 다루고 있습니다. AI/ML 워크로드의 증가로 인해 Kubernetes는 이러한 특수 하드웨어를 다루는 데 더 복잡한 상황에 놓이게 되었습니다. 글에서는 하드웨어 실패가 AI/ML 교육에 미치는 영향과 Kubernetes가 이러한 실패를 어떻게 처리하는지 설명합니다. 특히, 기존의 자원 관리 방식이 AI/ML 워크로드에는 적합하지 않으며, Kubernetes가 이러한 문제를 해결하기 위해 필요한 개선 사항들을 제시합니다. 다양한 실패 모드와 DIY 솔루션을 통해 Kubernetes가 직면한 문제들을 설명하고, 이를 해결하기 위한 로드맵을 제시합니다. Kubernetes는 여전히 AI/ML 워크로드를 위한 주요 플랫폼으로 자리 잡고 있으며, 지속적인 개선을 통해 이러한 도전을 극복하고자 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/03/navigating-failures-in-pods-with-devices/)

## 🔹 Spring Boot - This Week in Spring - July 15th, 2025
이번 주 Spring 블로그 글 요약:

- 블로그 작성자는 UBERCONF 소프트웨어 행사 참석을 위해 덴버로 출발 예정이며, 워크숍과 두 개의 발표를 진행할 계획이다.
- Spring gRPC 0.9.0 버전이 출시되었고, Spring Cloud 2024.0.2(Moorgate)도 릴리스되었다.
- 최근 "A Bootiful Podcast"에서는 API 전문가 Arjen Poutsma와의 인터뷰가 있었다.
- Cron 작업의 대안으로 Temporal을 사용하여 Spring Boot 앱을 미래 지향적으로 발전시키는 방법에 대한 기사가 소개되었다.
- Jetbrains의 IntelliJ IDEA 리드 Aleksey Stukalov와 함께 새로운 기능을 다룬 발표가 있었다.
- Phil Webb의 12년간의 Spring Boot 경험을 다룬 발표가 있었다.
- Spring Boot 4 출시 관련 주요 변화에 대한 분석 기사가 있다.
- JDBC 코드 어댑터를 쉽게 생성할 수 있는 datasource-proxy 프로젝트의 새 버전이 출시되었다.
- Akka의 CEO가 새로운 AI 프레임워크의 Spring Boot 통합을 발표했다.
- 빌드 시 음악을 재생해주는 Music Maven Plugin이 개발되었으며, Spotify 음악 재생 기능도 추가되었다.
👉 [자세히 보기](https://spring.io/blog/2025/07/15/this-week-in-spring-july-15-2025)

## 🔹 Docker - AI-Powered Testing: Using Docker Model Runner with Microcks for Dynamic Mock APIs
이 블로그 글은 AI 기술을 활용한 테스트 방법에 대해 설명하고 있습니다. 특히, LLM(대규모 언어 모델)의 비결정적 특성을 활용하여 동적이고 풍부한 테스트 데이터를 생성하는 방법에 중점을 두고 있습니다. 이를 통해 애플리케이션의 동작을 검증하고 일관되며 높은 품질의 사용자 경험을 보장할 수 있습니다. 글에서는 Docker의 Model Runner와 Microcks라는 도구를 사용하여 애플리케이션 테스트를 위한 동적 모의 API를 생성하는 방법을 안내합니다. Microcks는 CNCF의 강력한 도구로 소개됩니다.
👉 [자세히 보기](https://www.docker.com/blog/ai-powered-mock-apis-for-testing-with-docker-and-microcks/)

## 🔹 Java - Java GPGPU Enablement: Are We There Yet?
글은 Java에서 데이터 병렬 문제를 해결하기 위해 개발자들이 Java로 다중 커널 알고리즘을 표현하고, 이러한 커널이 서로 및 JVM과 효율적으로 데이터를 교환할 수 있는 방법에 대해 다루고 있습니다. HAT(Heterogeneous Accelerator Toolkit)를 소개하며, Java의 최근 및 제안된 개선 사항(Panama와 Babylon)을 활용하여 Java 개발자들이 GPU의 잠재력을 활용할 수 있도록 하는 방법을 시연합니다.
👉 [자세히 보기](https://inside.java/2025/07/14/javaone-hat/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호화 모듈

요약: Go 프로그래밍 언어에 이제 FIPS 140-3 표준을 준수하는 내장 암호화 모드가 추가되었습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: Helm @ KubeCon + CloudNativeCon EU '25

요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행될 예정이니, 유지 관리자들과의 대화 세션과 프로젝트 파빌리온의 Helm 부스에서 많은 참여 바랍니다. 행사 주간 동안 Helm과 관련된 모든 활동에 대한 자세한 내용은 블로그를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

