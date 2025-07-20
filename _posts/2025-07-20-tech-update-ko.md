# 🛠️ 2025-07-20 기술 업데이트 요약

## 🔹 Kubernetes - Post-Quantum Cryptography in Kubernetes
이 기술 블로그 글에서는 양자 컴퓨팅의 등장으로 인해 암호학의 큰 변화가 예상되며, 이는 특히 장기 시스템에 대한 우려가 크다는 점을 다루고 있습니다. 이러한 문제를 해결하기 위해 포스트 양자 암호학(PQC)이 도입됩니다. 글은 PQC가 TLS와 Kubernetes 생태계에 미치는 영향을 설명하며, Kubernetes에서 PQC의 현재 상태와 그 의미를 논의합니다. 특히, Kubernetes v1.33이 Go 1.24를 사용하여 기본적으로 하이브리드 포스트 양자 키 교환(X25519MLKEM768)을 지원한다는 점을 강조합니다. 또한, Go 버전 불일치로 인한 잠재적 문제 및 패킷 크기 제한과 같은 기술적 도전 과제도 다루고 있습니다. PQC 디지털 서명은 아직 널리 통합되지 않았지만, 도입을 위한 노력이 계속되고 있습니다. 결론적으로, Kubernetes가 양자 안전성을 향해 나아가고 있으며, 관련 이해관계자들이 이러한 발전을 주시하고 장기적인 플랫폼 보안을 보장하는 것이 중요하다고 강조합니다.
👉 [자세히 보기](https://kubernetes.io/blog/2025/07/18/pqc-in-k8s/)

## 🔹 Spring Boot - Spring Data 2025.1.0-M4 released
이번에 발표된 Spring Data 2025.1.0-M4는 새로운 기능과 개선사항을 제공하며, 팀과 기여자들을 대신하여 기쁘게 발표되었습니다. 주요 업데이트는 다음과 같습니다:

1. **레포지토리 사전 최적화**: Spring Boot의 빌드 플러그인을 통해 AOT 최적화를 적용할 때, AOT 생성 레포지토리가 기본적으로 활성화됩니다. 설정을 통해 AOT 레포지토리 생성을 비활성화할 수 있습니다.

2. **MongoDB 업데이트**: `BigDecimal`과 `BigInteger` 값의 기본 표현을 `Decimal128`로 업데이트하였습니다. 기존 값은 읽을 수 있지만 쿼리와 쓰기는 `Decimal128`을 사용합니다.

3. **Spring Data JDBC**: 복합 식별자 지원이 추가되었습니다. 복합 식별자는 이제 복잡한 유형이 될 수 있습니다.

4. **Spring Data Redis**: JSpecify 주석이 추가되었으며, Jackson 3 기반의 직렬화기를 제공합니다.

각 프로젝트의 Javadoc, 문서, 변경 로그에 대한 링크도 제공됩니다. 이번 출시에는 많은 기여자들의 도움이 있었습니다.
👉 [자세히 보기](https://spring.io/blog/2025/07/18/spring-data-2025-1-0-M4-released)

## 🔹 Docker - GoFiber v3 + Testcontainers: Production-like Local Dev with Air
이 블로그 글은 GoFiber v3와 Testcontainers를 사용하여 로컬 개발 환경을 실제 프로덕션과 유사하게 만드는 방법을 설명합니다. 외부 서비스(예: 데이터베이스나 큐)에 의존하는 앱의 로컬 개발은 환경의 불일치와 불안정한 스크립트를 초래할 수 있습니다. Fiber v3와 Testcontainers는 이러한 외부 서비스 종속성을 앱의 라이프사이클에 포함시켜 관리 가능하고 재현 가능한 개발자 친화적인 환경을 제공합니다. 곧 출시될 v3 버전에서는 Fiber가 강력한 새로운 기능을 선보입니다.
👉 [자세히 보기](https://www.docker.com/blog/go-local-dev-fiber-v3-testcontainers/)

## 🔹 Java - JEP targeted to JDK 25: 515: Ahead-of-Time Method Profiling
제목이 "JEP targeted to JDK 25: 515: Ahead-of-Time Method Profiling"인 기술 블로그 글은 JDK 25에 목표한 JEP 515에 관한 내용을 다루고 있습니다. 이 JEP는 사전 메서드 프로파일링(Ahead-of-Time Method Profiling)에 관한 것으로, 성능 최적화를 위해 메서드의 실행 정보를 미리 수집하는 방안을 제안하고 있습니다. 이 글은 JEP 515의 주요 목표와 기대 효과에 대해 설명하고 있습니다.
👉 [자세히 보기](https://inside.java/2025/07/18/jep515-target-jdk25/)

## 🔹 Golang - The FIPS 140-3 Go Cryptographic Module
블로그 글 요약: Go 언어에 FIPS 140-3 인증을 준수하는 기본 암호화 모드가 추가되었습니다. 이를 통해 Go 개발자들은 보안 표준을 더욱 쉽게 충족할 수 있게 되었습니다.
👉 [자세히 보기](https://go.dev/blog/fips140)

## 🔹 Helm - Helm @ KubeCon + CloudNativeCon EU '25
제목: KubeCon + CloudNativeCon EU '25에서의 Helm

Helm 팀이 4월 1일부터 4일까지 영국 런던에서 열리는 KubeCon + CloudNativeCon EU '25에 참가합니다. 올해 말 출시 예정인 Helm 4와 관련하여, 대화 세션 및 Project Pavilion의 Helm 부스에서 유지관리자들과의 대화에 참여할 수 있습니다. 행사 주간 동안 진행될 모든 Helm 관련 활동에 대한 자세한 내용은 블로그 글에서 확인할 수 있습니다.
👉 [자세히 보기](https://helm.sh/blog/helm-at-kubecon-eu-25/)

