# 🛠️ 2025-07-24 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 기술 블로그 글은 양자 컴퓨팅의 발전으로 인해 암호화 분야가 큰 변화를 맞이하고 있다는 내용입니다. 현재의 암호화 표준이 양자 컴퓨터에 의해 쉽게 깨질 수 있다는 우려가 있으며, 이를 해결하기 위해 '양자 이후 암호화(Post-Quantum Cryptography, PQC)'가 필요합니다. 이 글은 특히 Kubernetes 생태계 내에서 PQC가 어떤 의미를 가지는지 설명합니다. 

PQC는 양자와 고전 컴퓨터 모두에 안전한 것으로 여겨지는 암호 알고리즘을 말합니다. 이는 RSA와 ECC 같은 널리 사용되는 공개키 암호 시스템이 양자 컴퓨터에 의해 쉽게 깨질 수 있다는 점에서 중요합니다. 산업계는 PQC 알고리즘 표준화와 채택을 적극적으로 진행 중이며, NIST는 'Module-Lattice Key Encapsulation Mechanism(ML-KEM)'을 표준화했습니다.

TLS에서 PQC를 도입할 때, 키 교환과 디지털 서명 두 가지 주요 암호화 작업이 필요합니다. 키 교환은 즉각적인 우선순위로, 하이브리드 키 교환 메커니즘을 통해 점진적으로 PQC로 전환되고 있습니다. Kubernetes v1.33부터는 Go 1.24를 사용하여 기본적으로 하이브리드 PQC를 지원합니다.

그러나 Go 버전 불일치로 인해 PQC 보호가 사라질 수 있고, 패킷 크기 문제로 인해 연결 실패가 발생할 수 있습니다. 디지털 서명에 대한 PQC는 아직 초기 단계이며, 보다 널리 사용되기 위해서는 더 많은 표준화와 채택이 필요합니다. 

결론적으로, Kubernetes는 양자 이후의 보안을 향해 나아가고 있으며, PQC의 도입이 점점 현실화되고 있습니다. 그러나 이러한 전환 과정에서 발생할 수 있는 잠재적인 문제에 대한 인식이 중요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Batch 6.0.0-M1 is out!
Spring Batch 6.0.0-M1이 출시되었습니다. 이번 첫 마일스톤 릴리스는 새로운 기능, 개선 사항, 버그 수정 등을 포함하며, 몇 가지 API 변경 및 사용 중단도 포함하고 있습니다. 주요 변경 사항은 다음과 같습니다:

1. **의존성 업그레이드**: Spring Framework 7.0, Spring Integration 7.0, Spring Data 4.0 등으로 업데이트되었습니다. Java 17 이상과 호환됩니다.
   
2. **배치 인프라 구성 개선**: 새로운 애노테이션 및 클래스 도입으로 배치 인프라 구성이 더 유연해졌습니다. `@EnableBatchProcessing` 애노테이션이 공통 속성 구성을 담당하며, `@EnableJdbcJobRepository`, `@EnableMongoJobRepository`와 같은 새로운 애노테이션이 도입되었습니다.

3. **새로운 명령줄 작업 연산자**: 기존의 `CommandLineJobRunner`의 한계를 보완한 `CommandLineJobOperator`가 도입되어 커스터마이징 및 확장이 용이해졌습니다.

4. **사용 중단 및 정리**: 모듈식 구성과 몇 가지 API가 사용 중단되었습니다. 이전 버전에서 사용 중단된 API 및 기능들이 제거되었습니다.

자세한 변경 사항은 [릴리스 노트](https://github.com/spring-projects/spring-batch/releases/tag/6.0.0-M1)와 [마이그레이션 가이드](https://github.com/spring-projects/spring-batch/wiki/Spring-Batch-6.0-Migration-Guide)를 참고하세요.
👉 [자세히 보기](https://spring.io/blog/2025/07/23/spring-batch-6)

## 🔹 Docker - Docker MCP Catalog: Finding the Right AI Tools for Your Project
이 기술 블로그 글은 "Docker MCP Catalog"에 관해 설명하고 있습니다. LLMs(대형 언어 모델)가 발전하면서 외부 도구와 안전하게 상호 작용할 수 있는 표준화된 방법의 필요성이 증가하고 있습니다. 이를 해결하기 위해 Model Context Protocol(MCP)이 소개되었으며, 이는 기존 API를 AI가 접근할 수 있는 도구로 전환하는 프로토콜입니다. 이 글은 MCP의 역할과 중요성에 대해 설명하고 있습니다.
👉 [자세히 보기](https://www.docker.com/blog/finding-the-right-ai-developer-tools-mcp-catalog/)

## 🔹 Java - A Sneak Peek at the Stable Values API
이 기술 블로그 글은 Stable Values API에 대한 간략한 소개를 제공합니다. JDK의 내부 클래스들은 jdk.internal.vm.annotation.@Stable이라는 애노테이션을 사용하여 값이 최대 한 번만 변경되는 스칼라 및 배열 필드를 표시하는데, 이는 성능, 에너지 효율성, 유연성 측면에서 중요한 이점을 제공합니다. 그러나 이 강력한 @Stable 애노테이션은 Java 애플리케이션에서 직접 사용할 수 없어 그 적용 가능성이 제한되었습니다. StableValue API는 이러한 불균형을 해소하여 @Stable 애노테이션을 안전하게 감쌀 수 있는 방법을 제공함으로써, 일반 Java 개발자와 서드파티 라이브러리 개발자들에게 그 이점을 제공합니다. 이를 통해 요소가 상수 값인 것처럼 같은 성능으로 Lazy Lists와 Maps를 생성하는 방법을 배울 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/22/javaone-stablevalues/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호화 모듈

요약: Go 언어에 이제 기본적으로 FIPS 140-3 표준을 준수하는 모드가 내장되었습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 2025년 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU에 참석합니다. 올해 말 출시 예정인 Helm 4에 대한 논의에 참여하고, 발표 세션과 프로젝트 파빌리온의 Helm 부스에서 유지 관리자들과 소통할 수 있는 기회를 놓치지 마세요. 주간 동안 진행되는 Helm 관련 활동에 대한 자세한 정보는 링크에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

