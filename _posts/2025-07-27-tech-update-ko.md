# 🛠️ 2025-07-27 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 블로그 글은 양자 컴퓨팅의 발전으로 인해 기존 암호 체계가 깨질 가능성에 대비하여 포스트 양자 암호(PQC)를 도입해야 할 필요성에 대해 설명하고 있습니다. 특히 Kubernetes 생태계에 미칠 영향을 중점적으로 다루고 있습니다. PQC는 양자 컴퓨터와 고전 컴퓨터의 공격 모두에 안전한 암호 알고리즘을 의미하며, TLS와 Kubernetes에서의 적용 상황을 분석합니다. 또한, Kubernetes v1.33에서는 기본적으로 하이브리드 PQC 키 교환 메커니즘인 X25519MLKEM768을 지원하여, 양자 컴퓨터에 대비하는 데 있어 중요한 한 걸음을 내딛었습니다. 하지만 Go 버전 불일치로 인한 문제나 Client Hello 패킷 크기 제한과 같은 실질적인 문제에 대한 인식이 필요하다고 강조합니다. 디지털 서명에 대한 PQC의 적용은 아직 초기 단계이며, 앞으로의 발전이 필요하다고 결론짓고 있습니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
Spring Modulith 2.0 M1이 출시되었습니다. 이 새로운 버전은 최신 Spring Boot 4 M1 및 Spring Framework 7.0 M7을 기반으로 하며, 특히 이벤트 발행 레지스트리의 개편이 주요 특징입니다. 새로운 레지스트리는 "발행됨", "처리 중", "실패", "재제출됨"과 같은 상태를 도입하여 이전 모델의 한계를 해결합니다. JDBC 구현이 새로운 이벤트 발행 상태 모델을 지원하도록 변경되었으며, 다른 저장소 모듈은 기존 애플리케이션과의 호환성을 유지합니다. 또한, 이벤트 발행이 특정 상태에 멈추지 않도록 하는 오래된 모니터가 도입되었습니다. 새로운 모델은 멀티 인스턴스 애플리케이션 배포를 지원하며, JPA 프로젝트에서도 JDBC 기반 레지스트리를 사용해볼 것을 권장합니다. 기존 레지스트리 스키마를 계속 사용하려면 특정 설정을 통해 가능합니다. 전체 변경 로그는 GitHub에서 확인할 수 있으며, 사용자 피드백을 환영합니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
이 블로그 글은 Docker의 MCP(Model Context Protocol) 카탈로그를 소개하며, AI 프로젝트에 적합한 도구를 찾는 방법을 다룹니다. 대형 언어 모델(LLM)이 단순한 텍스트 생성기에서 외부 도구와 안전하게 상호작용할 수 있는 동적 에이전트로 발전함에 따라, 이를 표준화된 방식으로 구현할 필요성이 커지고 있습니다. MCP는 기존 API를 AI에서 접근 가능한 도구로 전환하는 데 중점을 둔 프로토콜입니다.
👉 [자세히 보기](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - JEP targeted to JDK 25: 520: JFR Method Timing &amp; Tracing
이 기술 블로그 글은 JDK 25에 포함될 예정인 JEP 520에 대한 내용을 다루고 있습니다. JEP 520은 JFR(Method Timing & Tracing) 기능을 개선하는 것을 목표로 하고 있습니다. 이 기능은 메서드 실행 시간과 추적을 더욱 효율적으로 관리할 수 있도록 도와줍니다. 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/25/jep520-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글은 Go 프로그래밍 언어가 이제 FIPS 140-3 호환 모드를 기본적으로 지원한다는 내용을 다룹니다. FIPS 140-3은 암호 모듈의 보안 요건을 규정하는 표준으로, Go는 이를 준수하는 기능을 내장하여 보안성을 강화했습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀은 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참가합니다. 올해 후반에 출시될 Helm 4에 대한 논의를 위해 팀 유지관리자들과의 대화 세션 및 Helm 부스를 방문할 수 있습니다. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

