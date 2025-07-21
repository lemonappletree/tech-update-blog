# 🛠️ 2025-07-21 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 기술 블로그 글은 양자 컴퓨터의 등장으로 인해 암호화 방식에 큰 변화가 예상되는 가운데, Kubernetes에서의 포스트 양자 암호화(PQC)에 대해 설명합니다. PQC는 양자 컴퓨터와 고전 컴퓨터 모두에 안전한 것으로 여겨지는 암호 알고리즘을 의미하며, 현재 널리 사용되는 RSA와 ECC 같은 공개 키 암호 시스템을 대체할 수 있습니다. TLS에서 PQC는 키 교환과 디지털 서명에 적용되며, 특히 키 교환에 대한 PQC 적용이 긴급하다고 강조됩니다. Kubernetes는 Go 언어를 사용하기 때문에 Go 1.24 버전을 사용하는 Kubernetes v1.33부터 기본적으로 하이브리드 PQC 키 교환을 지원합니다. 그러나 Go 버전 차이로 인한 호환성 문제와 패킷 크기 제한 등의 실용적인 문제도 발생할 수 있습니다. 디지털 서명 분야에서는 아직 도입 초기 단계로, 큰 키 및 서명 크기와 성능 문제를 해결해야 합니다. Kubernetes의 장기적 보안을 위해서는 이러한 PQC 발전에 대해 지속적으로 인지하고 있어야 합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.0.2 and 2024.1.8 released
이 블로그 글은 Spring Data의 두 서비스 릴리스인 2025.0.2와 2024.1.8의 출시를 알리는 내용입니다. 이번 릴리스에서는 의존성 업그레이드, 회귀 오류 수정, 선택된 개선 사항들이 포함되어 있습니다. 이 릴리스들은 다음 주까지 예정된 Spring Boot 릴리스에 포함될 예정입니다. 각 릴리스는 Spring Data Commons, JPA, MongoDB, KeyValue, Cassandra, Neo4j, LDAP, REST, Redis, Elasticsearch, Couchbase, Relational 등 여러 모듈의 업데이트와 관련 문서, API 문서, 변경 로그 링크를 제공합니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/18/spring-data-2025-0-2-and-2024-1-8-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
이 기술 블로그 글은 GoFiber v3와 Testcontainers를 사용하여 실제 서비스 의존성을 관리하고 재현 가능한 개발 환경을 구축하는 방법을 소개합니다. 외부 서비스에 의존하는 앱의 로컬 개발은 종종 취약한 스크립트와 불일치한 환경을 초래할 수 있지만, Fiber v3와 Testcontainers를 통해 이러한 문제를 해결할 수 있습니다. 곧 출시될 Fiber v3는 이러한 서비스 의존성을 앱의 라이프사이클에 완전히 통합하여 개발자 친화적인 환경을 제공합니다.
👉 [자세히 보기](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - Java Security Evolution - Out with the Old, In with the New
이 블로그 글은 Java 플랫폼의 보안 진화에 대해 다루고 있습니다. 시간이 지남에 따라 암호화 프로토콜과 알고리즘이 약화되면서 새로운 것들로 대체되는 과정을 설명합니다. 새로운 위협이 등장하면서 보안 위험도 변화하며, 이에 대응하기 위해 Java 플랫폼의 보안을 지속적으로 발전시키고 있습니다. JDK 24에서 보안 관리자를 영구적으로 비활성화한 이유와 이것이 애플리케이션이나 라이브러리에 미칠 수 있는 영향을 설명합니다. 또한, JDK 24에 양자 저항 알고리즘 지원을 추가하여 애플리케이션의 보안을 강화하는 방법을 보여줍니다. 마지막으로, 가까운 미래에 계획된 몇 가지 보안 강화 사항을 설명합니다.
👉 [자세히 보기](https://inside.java/2025/07/20/javaone-security/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
제목: FIPS 140-3 Go 암호화 모듈  
요약: 이제 Go 언어에는 기본적으로 FIPS 140-3을 준수하는 모드가 내장되어 있습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
블로그 글 요약: Helm 팀이 KubeCon + CloudNativeCon EU 2025에 참가하기 위해 런던으로 갑니다. 이번 행사는 4월 1일부터 4일까지 열리며, 올해 말 출시 예정인 Helm 4에 대한 대화에 참여할 수 있는 기회입니다. 행사 기간 동안 Helm 유지보수자들과의 토크 세션 및 프로젝트 파빌리온 내 Helm 부스에서 다양한 활동이 진행됩니다. 자세한 내용은 블로그에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

