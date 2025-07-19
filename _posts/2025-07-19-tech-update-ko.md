# 🛠️ 2025-07-19 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 블로그 글은 양자 컴퓨팅의 발전으로 인해 암호학의 큰 변화를 앞두고 있는 상황에서, 기존 암호 표준이 깨질 가능성에 대비하는 포스트-양자 암호학(PQC)의 중요성을 다루고 있습니다. 특히 Kubernetes 생태계에서 PQC의 역할과 그 상태에 대해 설명합니다. 

포스트-양자 암호학은 양자 컴퓨터의 공격에도 안전한 것으로 여겨지는 암호 알고리즘을 의미합니다. 현재 널리 사용되는 RSA와 ECC 같은 공개키 암호 시스템이 양자 알고리즘에 의해 깨질 수 있는 가능성 때문에, 산업계는 PQC 알고리즘을 표준화하고 채택하는 데 힘쓰고 있습니다. NIST는 이미 ML-KEM(모듈-격자 키 캡슐화 메커니즘)을 표준화했습니다. 

TLS(전송 계층 보안)에서는 키 교환과 디지털 서명이 중요한데, PQC를 통해 이들을 보호하는 것이 필요합니다. 특히, 하이브리드 키 교환 메커니즘은 이 둘을 결합하여 보안을 강화하는 방법으로, Kubernetes v1.33에서는 Go 1.24를 사용하여 기본적으로 지원됩니다. 

반면, PQC 디지털 서명은 아직 널리 통합되지 않았으며, 큰 키와 서명 크기, 성능 문제로 인해 도입이 더디고 도구 체인에서도 성숙된 지원이 부족합니다. 

결론적으로, Kubernetes에서 포스트-양자 보안으로의 전환이 진행 중이며, 특히 KEM에 대한 하이브리드 지원이 기본 설정으로 제공됩니다. 그러나 개발자들은 Go 버전 불일치와 같은 문제에 주의해야 하며, PQC 서명과 인증서 계층은 아직 초기 단계에 머물러 있어 장기적인 보안을 위해 지속적인 관심이 필요합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.0.2 and 2024.1.8 released
Spring Data 팀은 2025.0.2와 2024.1.8 서비스 릴리스를 발표했습니다. 이번 릴리스는 의존성 업그레이드, 회귀 문제 수정 및 선택된 개선 사항을 포함하고 있습니다. 다음 주에 예정된 Spring Boot 릴리스에서 이 릴리스를 채택할 예정입니다. 2025.0.2 릴리스는 Spring Data Commons, JPA, MongoDB, KeyValue, Apache Cassandra, Neo4j, LDAP, REST, Redis, Elasticsearch, Couchbase, Relational의 업데이트를 포함하고 있으며, 각 업데이트에 대한 Javadoc, 문서 및 변경 로그 링크가 제공됩니다. 2024.1.8 릴리스도 유사한 구성 요소의 업데이트를 포함하고 있습니다. 더 자세한 사항은 블로그 글에서 확인할 수 있습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/18/spring-data-2025-0-2-and-2024-1-8-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
이 블로그 글은 GoFiber v3와 Testcontainers를 활용하여 로컬 개발 환경을 실제 운영 환경과 비슷하게 구성하는 방법에 대해 설명합니다. 외부 서비스(예: 데이터베이스, 큐) 의존성이 있는 앱을 개발할 때 생길 수 있는 불안정한 스크립트와 일관성 없는 환경 문제를 해결하기 위해 Fiber v3와 Testcontainers를 사용합니다. 이들은 앱의 수명 주기에서 실제 서비스 의존성을 완전히 관리, 재현할 수 있게 하여 개발자 친화적인 환경을 제공합니다. 곧 출시될 Fiber v3는 이러한 기능을 더욱 강화할 예정입니다.
👉 [자세히 보기](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - JEP targeted to JDK 25: 515: Ahead-of-Time Method Profiling
블로그 글은 JDK 25에 목표로 하고 있는 JEP 515에 관한 내용입니다. 이 JEP는 "사전 메서드 프로파일링"을 다루고 있으며, 이는 프로그램 실행 전에 메서드의 성능을 분석하여 최적화하는 기술입니다. 이를 통해 프로그램의 실행 속도를 향상시키고 효율성을 높이는 것을 목표로 하고 있습니다. 자세한 내용은 제공된 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/18/jep515-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글 요약: Go 언어에 FIPS 140-3을 준수하는 네이티브 모드가 내장되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서 Helm

요약: Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4에 대한 논의가 진행되며, 팀의 유지 보수자들과 함께 대화에 참여할 수 있는 기회가 제공됩니다. 행사 내내 진행되는 Helm 관련 활동에 대한 자세한 내용은 링크를 통해 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

