# 🛠️ 2025-07-28 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
**요약:**

이 글은 양자 컴퓨팅 시대에 대비한 '양자 이후 암호(Post-Quantum Cryptography, PQC)'가 Kubernetes 생태계에 미치는 영향을 다루고 있습니다. 양자 컴퓨터는 현재의 암호화를 깨뜨릴 수 있는 잠재력을 가지고 있어, 특히 장기적으로 운영되는 시스템에서 큰 우려를 낳고 있습니다. PQC는 이러한 위협에 대응하기 위한 암호 알고리즘을 의미하며, 특히 TLS와 Kubernetes에서의 적용을 설명합니다.

글에서는 PQC의 필요성, 업계의 표준화 노력, 그리고 Kubernetes v1.33에서의 PQC 지원 상태를 살펴봅니다. Kubernetes v1.33은 Go 1.24를 사용하여 기본적으로 하이브리드 양자 이후 암호 교환을 지원합니다. 그러나 Go 버전 불일치로 인한 암호화 강도 저하와 같은 잠재적인 문제점도 존재합니다.

결론적으로, PQC KEM(Key Exchange Mechanisms)은 빠르게 채택되고 있지만, 디지털 서명에 대한 PQC는 도입 초기 단계에 있으며, 완전한 양자 안전성을 확보하기 위해 지속적인 관심이 필요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 2.0 M1 released
Spring Modulith 2.0 M1이 발표되었습니다. 이 버전은 최신 Spring Boot 4 M1과 Spring Framework 7.0 M7을 기반으로 하며, 주요 기능으로는 이벤트 발행 레지스트리의 개편이 있습니다. 새로운 레지스트리는 "발행됨", "처리 중", "실패", "재발행" 등의 새로운 상태를 도입하여 기존 모델의 한계를 극복하고, 여러 인스턴스의 애플리케이션 배포에서도 문제없이 작동할 수 있습니다. JDBC 구현이 새 모델을 지원하도록 변경되었으며, JPA 프로젝트에서도 JDBC 기반 레지스트리를 시도해 볼 것을 권장합니다. 기존 레지스트리 스키마를 사용하려면 `spring.modulith.events.jdbc.use-legacy-structure`를 `true`로 설정할 수 있습니다. 모든 변경 사항은 [릴리스 노트](https://github.com/spring-projects/spring-modulith/releases/tag/2.0.0-M1)에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/26/spring-modulith-2-0-M1-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
Title: Docker MCP Catalog: Finding the Right AI Tools for Your Project

요약: 대형 언어 모델(LLM)이 정적인 텍스트 생성기에서 외부 도구와 안전하게 상호 작용할 수 있는 동적 에이전트로 발전함에 따라, 이러한 상호작용을 표준화할 필요성이 커지고 있습니다. Model Context Protocol(MCP)은 기존 API를 AI가 접근할 수 있는 도구로 변환하기 위해 설계된 프로토콜로, 이러한 필요를 해결합니다.
👉 [자세히 보기](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A New Model for Java Object Initialization
이 기술 블로그 글은 Java 언어, JVM 및 일반적인 코딩 관행을 함께 발전시켜 필드, 배열 및 객체의 초기화를 개선하는 새로운 모델에 대해 설명합니다. 이러한 개선은 객체의 내용에 대한 강력한 보장을 제공하여 버그를 제거하고 런타임 최적화의 새로운 기회를 제공합니다. OpenJDK의 Valhalla 프로젝트는 이러한 최적화를 사용하여 이전에는 달성할 수 없었던 성능 향상을 제공합니다. 이 세션에서는 Java 24의 Flexible Constructor Bodies 미리보기 기능을 다루고, 미래에 계획된 추가적인 언어 개선 사항을 설명합니다.
👉 [자세히 보기](https://inside.java/2025/07/27/javaone-object-initialization/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호화 모듈  
요약: Go 언어에 이제 내장된 FIPS 140-3 준수 모드가 추가되었습니다.  
링크: [https://go.dev/blog/fips140](https://go.dev/blog/fips140)
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 Helm

요약: Helm 팀이 오는 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의를 위해 유지보수자들과의 토크 세션 및 Project Pavilion의 Helm 부스에서 대화에 참여하세요. 주간 동안 진행되는 모든 Helm 관련 활동에 대한 자세한 사항은 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

