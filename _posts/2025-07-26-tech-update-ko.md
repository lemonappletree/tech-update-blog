# 🛠️ 2025-07-26 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 기술 블로그 글은 양자 컴퓨팅의 발전으로 인해 암호학이 큰 변화를 맞이할 준비가 되어 있음을 설명합니다. 양자 컴퓨터는 현재의 암호 표준을 깰 수 있는 잠재력을 가지고 있으며, 이는 특히 장기적으로 사용되는 시스템에 큰 우려를 낳고 있습니다. 이 문제를 해결하기 위해 '포스트 양자 암호학'(PQC)이 도입되고 있으며, 이 글에서는 PQC가 TLS 및 Kubernetes 생태계에 미치는 영향을 설명합니다. 

주요 내용은 다음과 같습니다:
1. **포스트 양자 암호학(PQC)**: PQC는 양자 컴퓨터의 공격에도 안전할 것으로 예상되는 암호 알고리즘을 의미합니다. 현재 산업계에서는 이러한 PQC 알고리즘의 표준화 및 채택이 활발히 진행 중입니다.
2. **TLS와의 관계**: TLS에서 PQC의 채택은 키 교환과 디지털 서명에 대한 서로 다른 요구와 일정으로 인해 복잡합니다. 특히, 키 교환의 경우 즉각적인 PQC 채택이 필요합니다.
3. **Kubernetes에서의 PQC**: Kubernetes v1.33에서는 Go 1.24를 사용하여 TLS 연결에 하이브리드 포스트 양자 키 교환을 기본적으로 지원합니다.
4. **현재 상태와 과제**: PQC KEMs는 점차 널리 채택되고 있지만, 디지털 서명의 경우 아직 초기 단계에 있습니다. 또한, Go 버전 불일치와 패킷 크기와 관련된 문제도 존재합니다.

이 글은 Kubernetes가 포스트 양자 보안을 향해 나아가고 있음을 강조하며, 관련된 잠재적 문제를 이해하는 것이 중요하다고 설명합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Modulith 1.4.2 and 1.3.8 released
Spring Modulith 1.4.2와 1.3.8 버전이 출시되었습니다. 이번 릴리스에서는 최신 Spring Boot 및 Framework 버전으로의 종속성 업그레이드가 포함되어 있습니다. 1.4.2 버전은 `application-modules.json`에 더욱 상세한 애플리케이션 모듈 메타데이터를 생성하는 기능을 제공합니다. 이는 Sonargraph와 같은 도구가 Spring Modulith 애플리케이션과의 통합을 구축하는 데 도움을 주며, 애플리케이션의 구조를 가져와 아키텍처 정의를 지원합니다. 자세한 변경 사항은 각 버전의 전체 변경 로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/25/spring-modulith-1-4-2-and-1-3-8-released)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
이 블로그 글은 Docker MCP 카탈로그를 소개하며, AI 프로젝트에 적합한 도구를 찾는 방법에 대해 다룹니다. 대형 언어 모델(LLM)이 발전하면서 외부 도구와 안전하게 상호작용할 수 있는 표준화된 방법의 필요성이 커지고 있습니다. 이러한 요구를 충족시키기 위해 Model Context Protocol(MCP)이 개발되었으며, 기존 API를 AI가 접근 가능한 도구로 전환할 수 있도록 설계되었습니다.
👉 [자세히 보기](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - JEP targeted to JDK 25: 520: JFR Method Timing &amp; Tracing
이 기술 블로그 글은 JDK 25에 목표로 하는 JEP 520에 대해 다루고 있습니다. JEP 520은 JFR(Method Timing & Tracing)을 개선하여 메서드의 실행 시간과 추적을 보다 효율적으로 관리할 수 있는 기능을 제공합니다. 이로 인해 개발자들은 애플리케이션의 성능을 더 잘 분석하고 최적화할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/25/jep520-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글 요약: Go 프로그래밍 언어에 이제 내장된 FIPS 140-3 준수 모드가 제공됩니다. 이는 Go가 기본적으로 FIPS 140-3 표준을 충족하는 암호화 기능을 지원하여, 보안이 중요한 애플리케이션에서 사용할 수 있도록 합니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 Helm  
요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하세요. 팀 유지보수자들과의 대화 세션 및 Helm 부스에서 많은 활동이 예정되어 있습니다. 주간 동안의 Helm 관련 활동에 대한 자세한 내용은 링크를 참조하세요.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

